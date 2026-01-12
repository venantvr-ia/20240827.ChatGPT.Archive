#!/usr/bin/env python3
"""
Reformate les fichiers Markdown avec Gemini Batch API.
- Traite chaque fichier .md individuellement
- Découpage intelligent par section (Heading)
- Réécrit les titres ## de façon claire
- Ajoute un tableau de tags sous chaque ##
- Écrase le fichier source avec le nouveau contenu

Usage:
    python rewrite_titles.py fichier.md     # Soumettre un fichier (non bloquant)
    python rewrite_titles.py *.md           # Soumettre plusieurs fichiers
    python rewrite_titles.py --check        # Vérifier les jobs terminés et réécrire
    python rewrite_titles.py --status       # Voir les jobs en attente
    python rewrite_titles.py --wait *.md    # Soumettre et attendre (bloquant)

Workflow:
    1. python rewrite_titles.py .htaccess.md   # Crée .htaccess.md.job + .jsonl
    2. (attendre quelques minutes)
    3. python rewrite_titles.py --check        # Récupère, réécrit, met status=COMPLETED

Fichiers créés (conservés pour analyse):
    .htaccess.md.jsonl  - Requêtes batch envoyées à Gemini
    .htaccess.md.job    - Infos du job (job_id, status, clés des sections)

Status possibles:
    PENDING   - Job soumis, en attente
    COMPLETED - Traitement terminé avec succès
    FAILED    - Échec du traitement
"""

import hashlib
import json
import os
import sys
import time
import unicodedata
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai.types import CreateBatchJobConfig, UploadFileConfig
from marko import Markdown
from marko.block import Heading

# --- CONFIGURATION ---
# Répertoire de travail : ./md (relatif à la racine du projet)
PROJECT_ROOT = Path(__file__).parent
MD_DIR = PROJECT_ROOT / 'md'
load_dotenv(PROJECT_ROOT / '.env')

API_KEY = os.getenv('GOOGLE_API_KEY')
if not API_KEY:
    print("ERREUR: GOOGLE_API_KEY non définie dans .env")
    sys.exit(1)

MODEL_ID = os.getenv('GEMINI_MODEL', 'gemini-2.0-flash-lite')

client = genai.Client(api_key=API_KEY)


# --- GESTION DES FICHIERS DE TRAVAIL ---
def normalize_filename(name):
    """Supprime les accents d'un nom de fichier pour compatibilité ASCII."""
    # Décompose les caractères accentués (é -> e + accent combinant)
    # puis supprime les accents (catégorie 'Mn' = Mark, Nonspacing)
    normalized = unicodedata.normalize('NFD', name)
    return ''.join(c for c in normalized if unicodedata.category(c) != 'Mn')


def get_job_file(source_path):
    """Retourne le chemin du fichier .job pour un fichier source."""
    # .htaccess.md -> .htaccess.md.job
    return Path(str(source_path) + '.job')


def get_jsonl_file(source_path):
    """Retourne le chemin du fichier .jsonl pour un fichier source."""
    # .htaccess.md -> .htaccess.md.jsonl
    return Path(str(source_path) + '.jsonl')


def save_job_info(source_path, job_id, section_keys, status="PENDING"):
    """Sauvegarde les infos du job dans un fichier .md.job"""
    job_file = get_job_file(source_path)
    with open(job_file, 'w', encoding='utf-8') as f:
        f.write(f"# Job Gemini Batch\n")
        f.write(f"source_file={source_path}\n")
        f.write(f"job_id={job_id}\n")
        f.write(f"submitted_at={time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"sections={len(section_keys)}\n")
        f.write(f"status={status}\n")
        f.write(f"\n# Clés des sections (pour reconstruire l'ordre)\n")
        for key in section_keys:
            f.write(f"key={key}\n")
    print(f"  Job sauvegardé : {job_file.name} ({len(section_keys)} sections, status={status})")


def load_job_info(job_file):
    """Charge les infos depuis un fichier .md.job"""
    info: dict[str, str] = {}
    keys: list[str] = []
    with open(job_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                k, v = line.split('=', 1)
                if k == 'key':
                    keys.append(v)
                else:
                    info[k] = v
    return {'info': info, 'keys': keys}


def update_job_status(job_file, new_status):
    """Met à jour le status dans le fichier .job"""
    if not job_file.exists():
        return

    # Lire le contenu actuel
    data = load_job_info(job_file)
    info = data['info']
    keys = data['keys']

    # Réécrire avec le nouveau status
    with open(job_file, 'w', encoding='utf-8') as f:
        f.write(f"# Job Gemini Batch\n")
        f.write(f"source_file={info.get('source_file', '')}\n")
        f.write(f"job_id={info.get('job_id', '')}\n")
        f.write(f"submitted_at={info.get('submitted_at', '')}\n")
        f.write(f"sections={info.get('sections', len(keys))}\n")
        f.write(f"status={new_status}\n")
        f.write(f"completed_at={time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"\n# Clés des sections (pour reconstruire l'ordre)\n")
        for key in keys:
            f.write(f"key={key}\n")
    print(f"  Status mis à jour : {new_status}")


# Prompt système pour le reformatage
SYSTEM_PROMPT = """Rôle : Rédacteur technique expert.

Tâche : Reformater cette section Markdown.

Règles STRICTES :
1. Réécris le titre ## de façon claire et concise (max 60 caractères)
2. Juste après le titre ##, ajoute OBLIGATOIREMENT un tableau de tags :
   | Tags |
   |------|
   | `tag1` `tag2` `tag3` |

   Les tags = mots-clés pertinents (technologie, langage, concept...)
3. Anonymisation : Remplacer noms/emails/IP par [NOM], [EMAIL], [IP]
4. Code : Garder les blocs de code intacts
5. Style : Professionnel, direct
6. Output : Markdown pur uniquement, AUCUN commentaire"""


# --- 1. DÉCOUPAGE INTELLIGENT DU MARKDOWN ---
def split_markdown(content):
    """Découpe le contenu en sections avec marko (une par Heading)."""
    md = Markdown()
    parsed = md.parse(content)

    sections = []
    current_chunk = ""

    for node in parsed.children:
        if isinstance(node, Heading):
            if current_chunk.strip():
                sections.append(current_chunk)
            current_chunk = ""
        # marko peut rendre des éléments individuels (le type hint est trop restrictif)
        current_chunk += md.render(node)  # type: ignore[arg-type]

    if current_chunk.strip():
        sections.append(current_chunk)

    return sections


def prepare_jsonl_for_file(source_path, sections):
    """Prépare le fichier JSONL pour un fichier source donné."""
    requests = []
    for i, text in enumerate(sections):
        # Clé = fichier:section pour retrouver l'ordre
        req = {
            "key": f"{source_path.stem}:{i:04d}",
            "request": {
                "system_instruction": {"parts": [{"text": SYSTEM_PROMPT}]},
                "contents": [{"parts": [{"text": text}]}]
            }
        }
        requests.append(req)
    return requests


# --- 2. GESTION DU JOB BATCH ---
def submit_batch_job(jsonl_path, source_path, section_keys):
    """Lance le job batch et sauvegarde dans .md.job (non bloquant)."""
    print("  Upload vers Google AI Studio...")
    # Google n'accepte que minuscules, chiffres et tirets pour le name
    # On utilise display_name pour le nom lisible
    file_hash = hashlib.md5(source_path.name.encode('utf-8')).hexdigest()[:16].lower()
    upload_name = f"batch-{file_hash}"
    with open(jsonl_path, 'rb') as f:
        file_metadata = client.files.upload(
            file=f,
            config=UploadFileConfig(
                name=upload_name,
                display_name=source_path.name,
                mime_type='application/jsonl'
            )
        )

    print(f"  Lancement du Job Batch sur {MODEL_ID}...")
    job = client.batches.create(
        model=MODEL_ID,
        src=file_metadata.name,
        config=CreateBatchJobConfig(display_name=f"Reformat_{normalize_filename(source_path.stem)}")
    )

    job_id = job.name
    print(f"  Job soumis : {job_id}")

    # Sauvegarder dans fichier.md.job avec les clés des sections
    save_job_info(source_path, job_id, section_keys)
    return job_id


def check_job_status(job_id):
    """Vérifie le statut d'un job."""
    batch = client.batches.get(name=job_id)
    state_name = batch.state.name if hasattr(batch.state, 'name') else str(batch.state)
    # Le fichier de sortie est dans batch.dest.file_name
    output_file = batch.dest.file_name if state_name == "JOB_STATE_SUCCEEDED" else None
    return state_name, output_file


# --- 3. RÉCUPÉRATION ET RÉÉCRITURE ---
def fetch_batch_results(output_file_name):
    """Récupère les résultats du batch indexés par clé."""
    print("  Récupération des résultats...")
    output_data = client.files.download(file=output_file_name)

    # Indexer par clé
    results_by_key = {}

    for line in output_data.decode('utf-8').strip().split('\n'):
        item = json.loads(line)
        key = item['key']  # format: "filename:0001"
        text = item['response']['candidates'][0]['content']['parts'][0]['text']
        results_by_key[key] = text

    return results_by_key


def rewrite_source_file(source_path, section_keys, results_by_key):
    """Écrase le fichier source avec les sections reformatées dans l'ordre."""
    sections = []
    for key in section_keys:
        if key in results_by_key:
            sections.append(results_by_key[key])
        else:
            print(f"  ATTENTION: Section manquante {key}")

    content = "\n\n".join(sections)
    with open(source_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Fichier réécrit : {source_path.name}")


# --- 4. TRAITEMENT D'UN FICHIER ---
def submit_file_for_processing(source_path):
    """Soumet un fichier pour traitement (non bloquant)."""
    print(f"\n{'='*60}")
    print(f"Fichier : {source_path.name}")
    print(f"{'='*60}")

    # Vérifier si le fichier doit être traité
    should_process, reason = check_file_status(source_path)
    if not should_process:
        print(f"  Ignoré : {reason}")
        return None

    # Lire et découper
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    sections = split_markdown(content)
    if not sections:
        print("  Aucune section trouvée, ignoré")
        return None

    print(f"  {len(sections)} section(s) trouvée(s)")

    # Préparer le JSONL et récupérer les clés
    requests = prepare_jsonl_for_file(source_path, sections)
    section_keys = [req['key'] for req in requests]

    # Fichier JSONL nommé d'après le fichier source
    jsonl_file = get_jsonl_file(source_path)
    with open(jsonl_file, 'w', encoding='utf-8') as f:
        for req in requests:
            f.write(json.dumps(req) + '\n')
    print(f"  JSONL créé : {jsonl_file.name}")

    # Soumettre le batch (non bloquant)
    job_id = submit_batch_job(jsonl_file, source_path, section_keys)
    return job_id


def process_job_file(job_file):
    """Traite un fichier .md.job : vérifie le statut et réécrit si terminé."""
    data = load_job_info(job_file)
    info = data['info']
    section_keys = data['keys']

    job_id = info.get('job_id')
    source_file = info.get('source_file')
    if not source_file:
        print(f"  ERREUR: source_file manquant dans {job_file.name}")
        return False
    source_path = Path(source_file)

    print(f"\n  Job: {job_file.name}")
    print(f"  Fichier: {source_path.name}")
    print(f"  Sections: {len(section_keys)}")
    print(f"  Soumis: {info.get('submitted_at', '?')}")

    status, output_file = check_job_status(job_id)
    print(f"  Statut: {status}")

    if status == "JOB_STATE_SUCCEEDED":
        # Récupérer les résultats par clé
        results_by_key = fetch_batch_results(output_file)

        # Vérifier qu'on a toutes les sections
        missing = [k for k in section_keys if k not in results_by_key]
        if missing:
            print(f"  ATTENTION: {len(missing)} section(s) manquante(s)")

        # Réécrire le fichier dans l'ordre des clés
        rewrite_source_file(source_path, section_keys, results_by_key)
        update_job_status(job_file, "COMPLETED")
        return True

    elif status in ["JOB_STATE_FAILED", "JOB_STATE_CANCELLED"]:
        print(f"  Job échoué")
        update_job_status(job_file, "FAILED")
        return False

    # Encore en cours (PENDING, RUNNING...)
    update_job_status(job_file, status)
    print(f"  En attente...")
    return False


def check_all_pending_jobs():
    """Cherche tous les .md.job non complétés et vérifie leur statut."""
    job_files = list(MD_DIR.glob("*.md.job"))

    if not job_files:
        print("Aucun job (pas de fichier .md.job)")
        return 0

    # Filtrer les jobs non complétés
    pending_jobs = []
    for job_file in job_files:
        data = load_job_info(job_file)
        status = data['info'].get('status', 'PENDING')
        if status not in ["COMPLETED", "FAILED"]:
            pending_jobs.append(job_file)

    if not pending_jobs:
        print(f"{len(job_files)} job(s) trouvé(s), tous déjà traités")
        return 0

    print(f"\n{len(pending_jobs)} job(s) en attente (sur {len(job_files)} total)...")
    completed = 0

    for job_file in pending_jobs:
        try:
            if process_job_file(job_file):
                completed += 1
        except Exception as e:
            print(f"  ERREUR : {e}")

    return completed


# --- MAIN ---
DEFAULT_LIMIT = 10


def get_limit(args):
    """Extrait la limite du nombre de fichiers depuis les arguments."""
    for i, arg in enumerate(args):
        if arg == '--limit' and i + 1 < len(args):
            try:
                return int(args[i + 1])
            except ValueError:
                pass
        elif arg.startswith('--limit='):
            try:
                return int(arg.split('=')[1])
            except ValueError:
                pass
    return DEFAULT_LIMIT


def check_file_status(source_path):
    """Vérifie si un fichier doit être traité. Retourne (doit_traiter, raison)."""
    job_file = get_job_file(source_path)
    if not job_file.exists():
        return True, "nouveau"

    data = load_job_info(job_file)
    info = data['info']
    status = info.get('status', 'PENDING')

    if status == "COMPLETED":
        return False, "COMPLETED"
    elif status == "FAILED":
        return True, "FAILED (retry)"
    elif status in ["PENDING", "JOB_STATE_PENDING", "JOB_STATE_RUNNING"]:
        return False, f"en cours ({status})"
    else:
        return True, f"status inconnu ({status})"


def get_files_to_process(args, limit=None):
    """Détermine les fichiers à traiter selon les arguments."""
    # Filtrer les options --xxx et leurs valeurs
    file_args = []
    skip_next = False
    for arg in args:
        if skip_next:
            skip_next = False
            continue
        if arg == '--limit':
            skip_next = True
            continue
        if arg.startswith('--'):
            continue
        file_args.append(arg)

    # Si aucun fichier spécifié, lister tous les .md du répertoire
    if not file_args:
        all_files = sorted(MD_DIR.glob("*.md"))
        # Exclure ce script s'il a une extension .md
        all_files = [f for f in all_files if f.name != Path(__file__).name]
    else:
        # Traiter les fichiers passés en argument
        all_files = []
        for arg in file_args:
            p = Path(arg)
            if not p.exists():
                p = MD_DIR / arg
            if p.exists() and p.suffix == '.md':
                all_files.append(p)
            else:
                print(f"Ignoré (non trouvé ou pas .md) : {arg}")

    # Filtrer les fichiers selon leur status
    files_to_process = []
    skipped = {"COMPLETED": 0, "en_cours": 0}

    for f in all_files:
        should_process, reason = check_file_status(f)
        if should_process:
            files_to_process.append(f)
            # Appliquer la limite sur les fichiers valides
            if limit and len(files_to_process) >= limit:
                break
        else:
            if "COMPLETED" in reason:
                skipped["COMPLETED"] += 1
            else:
                skipped["en_cours"] += 1

    # Afficher le résumé
    if skipped["COMPLETED"] > 0 or skipped["en_cours"] > 0:
        print(f"Ignorés: {skipped['COMPLETED']} COMPLETED, {skipped['en_cours']} en cours")

    if limit and len(files_to_process) == limit:
        remaining = len(all_files) - len(files_to_process) - skipped["COMPLETED"] - skipped["en_cours"]
        if remaining > 0:
            print(f"Limite de {limit} atteinte ({remaining} fichiers restants)")

    return files_to_process


def print_usage():
    print(f"""
Usage:
    python rewrite_titles.py                    # Tous les .md (limite {DEFAULT_LIMIT})
    python rewrite_titles.py --limit 10         # Tous les .md (limite 10)
    python rewrite_titles.py fichier.md         # Un seul fichier
    python rewrite_titles.py --check            # Vérifier les jobs et réécrire
    python rewrite_titles.py --status           # Afficher tous les jobs
    python rewrite_titles.py --wait             # Soumettre et attendre (bloquant)

Options:
    --limit N   Nombre max de fichiers à traiter (défaut: {DEFAULT_LIMIT})

Fichiers créés (conservés):
    .htaccess.md.jsonl  - Requêtes batch
    .htaccess.md.job    - Infos du job avec status

Un fichier avec status=COMPLETED ne sera pas resoumis.
Pour forcer le retraitement, supprimez le fichier .job
""")


if __name__ == "__main__":
    # Mode --check : vérifier et traiter les jobs terminés
    if "--check" in sys.argv:
        completed = check_all_pending_jobs()
        print(f"\n{completed} fichier(s) réécrit(s)")
        sys.exit(0)

    # Mode --status : afficher tous les jobs
    if "--status" in sys.argv:
        job_files = list(MD_DIR.glob("*.md.job"))
        if not job_files:
            print("Aucun job")
        else:
            print(f"{len(job_files)} job(s) :")
            for job_file in job_files:
                data = load_job_info(job_file)
                info = data['info']
                keys = data['keys']
                source_file = info.get('source_file', '?')
                status = info.get('status', 'PENDING')
                print(f"\n  {job_file.name}")
                print(f"    Source: {Path(source_file).name if source_file != '?' else '?'}")
                print(f"    Sections: {len(keys)}")
                print(f"    Status: {status}")
                print(f"    Job ID: {info.get('job_id', '?')}")
                print(f"    Soumis: {info.get('submitted_at', '?')}")
                if info.get('completed_at'):
                    print(f"    Complété: {info.get('completed_at')}")
        sys.exit(0)

    # Mode normal : soumettre des fichiers
    limit = get_limit(sys.argv[1:])
    files = get_files_to_process(sys.argv[1:], limit=limit)

    if not files:
        print("Aucun fichier .md à traiter")
        sys.exit(0)

    print(f"Modèle : {MODEL_ID}")
    print(f"Fichiers à soumettre : {len(files)}")

    submitted = 0
    for filepath in files:
        try:
            job_id = submit_file_for_processing(filepath)
            if job_id:
                submitted += 1
        except Exception as e:
            print(f"  ERREUR : {e}")

    print(f"\n{'='*60}")
    print(f"Soumis : {submitted}/{len(files)} fichiers")
    print(f"{'='*60}")

    # Mode --wait : attendre la fin de tous les jobs
    if "--wait" in sys.argv:
        print("\nAttente de la fin des jobs...")
        while True:
            time.sleep(30)
            job_files = list(MD_DIR.glob("*.md.job"))
            if not job_files:
                print("Tous les jobs sont terminés")
                break
            completed = check_all_pending_jobs()
            if completed > 0:
                print(f"  {completed} fichier(s) réécrit(s)")
    else:
        print("\nLes jobs tournent en arrière-plan.")
        print("Utilisez --check pour vérifier et réécrire les fichiers terminés.")
