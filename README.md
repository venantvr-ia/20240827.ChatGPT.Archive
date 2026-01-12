# Archive ChatGPT - Notes Techniques

Collection de notes et documentation technique issues de diverses sessions ChatGPT.

## Structure du projet

```
.
├── md/                     # Fichiers markdown (300+ documents)
├── scripts/                # Scripts de traitement
│   ├── static/             # Fichiers statiques pour le serveur web
│   └── templates/          # Templates HTML
├── rewrite_titles.py       # Script de réécriture des titres avec Gemini
└── requirements.txt        # Dépendances Python
```

## Scripts de traitement

Pipeline de traitement des exports ChatGPT :

| Script | Description |
|--------|-------------|
| `01_extract_prompts.py` | Extraction des prompts depuis l'export JSON |
| `02_process_prompts_llm.py` | Traitement des prompts via LLM |
| `03_sanitize_html.py` | Nettoyage et échappement du HTML |
| `04_postprocess_prompts.py` | Post-traitement des prompts |
| `05_replace_prompts.py` | Remplacement des prompts dans les fichiers |
| `06_fix_titles.py` | Correction des titres |
| `07_convert_json_to_md.py` | Conversion JSON vers Markdown |
| `08_normalize_filenames.py` | Normalisation des noms de fichiers |

Utilitaires :

| Script | Description |
|--------|-------------|
| `detect_headers_in_code.py` | Détection des headers dans les blocs de code |
| `validate_markdown.py` | Validation de la syntaxe Markdown |
| `serve_chat_flask.py` | Serveur Flask pour visualiser les conversations |
| `functions.py` | Fonctions utilitaires partagées |
| `rewrite_titles.py` | Réécriture des titres avec Gemini AI |

## Contenu des notes

### Développement & Architecture
- Domain-Driven Design (DDD)
- Patterns d'architecture logicielle
- Docker et containerisation
- APIs et intégrations

### Trading & Finance
- Trading algorithmique multi-timeframe
- Analyse de corrélations
- Stratégies quantitatives
- Intégration avec exchanges (Gate.io, etc.)

### Sécurité Informatique
- Analyse de vulnérabilités (XSS, Clickjacking, etc.)
- Sécurité des sessions
- Analyse de fichiers HAR
- Bonnes pratiques de sécurité

### Intelligence Artificielle & LLM
- Fine-tuning de modèles
- RAG (Retrieval-Augmented Generation)
- LangChain et LangSmith
- Hugging Face et GPT-2

### Data Science
- Manipulation de DataFrames avec Pandas
- Prétraitement de données
- Génération de données avec Faker
- Visualisation

### DevOps & Infrastructure
- Configuration Apache/PHP
- Git workflows
- Docker networking
- Certificats et SSL

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Langue

La majorité du contenu est en français, avec quelques documents en anglais.
