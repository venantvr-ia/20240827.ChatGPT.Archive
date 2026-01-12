## Langage Ubiquitaire en Développement Logiciel

| Tags |
|------|
| `Ubiquitous Language` `Développement` `Collaboration` |

Le langage Ubiquitaire est une pratique essentielle en développement logiciel, particulièrement dans le cadre de la méthodologie Domain-Driven Design (DDD). Il s'agit d'établir un langage commun entre les développeurs et les experts du domaine. Ce langage partagé est utilisé pour la modélisation, la communication et la documentation du logiciel.

**Principes clés :**

*   **Collaboration:** Le langage Ubiquitaire est le résultat d'une collaboration étroite entre les développeurs et les experts métier.
*   **Clarté:** Il vise à éliminer les ambiguïtés et à assurer une compréhension commune des concepts du domaine.
*   **Cohérence:** Le langage est utilisé de manière cohérente dans tout le projet, y compris le code, la documentation et les tests.

**Avantages :**

*   **Réduction des malentendus :** Diminue les risques d'interprétations erronées des exigences métier.
*   **Amélioration de la communication :** Facilite la communication entre les différents acteurs du projet.
*   **Modélisation plus précise :** Permet de créer des modèles de domaine plus précis et plus fidèles à la réalité.
*   **Code plus lisible :** Conduit à un code plus facile à comprendre et à maintenir.

**Exemple :**

Imaginons un système de gestion de commandes. Au lieu d'utiliser des termes techniques complexes, le langage Ubiquitaire pourrait utiliser des termes comme "Client", "Commande", "Produit", "Livraison", etc. Ces termes, compris par les experts métier, seraient ensuite utilisés dans le code.

```java
public class Commande {
    private Client client;
    private List<Produit> produits;
    private Adresse adresseLivraison;
    private Date dateCommande;

    // ...
}
```

**Mise en œuvre :**

1.  **Identifier les concepts clés :** Identifier les concepts et les termes essentiels du domaine.
2.  **Définir le langage :** Établir une liste de termes et de définitions communs.
3.  **Utiliser le langage :** Utiliser le langage Ubiquitaire dans le code, la documentation et la communication quotidienne.
4.  **Évolution du langage :** Le langage Ubiquitaire est évolutif et doit être mis à jour régulièrement en fonction des besoins et des changements du domaine.

**Conclusion :**

Le langage Ubiquitaire est un outil puissant pour améliorer la collaboration, la communication et la qualité du code dans les projets de développement logiciel. En établissant un langage commun, les équipes peuvent mieux comprendre le domaine et développer des solutions plus efficaces.


## Résumé de l'article sur Software Engineering

| Tags |
|------|
| `Software Engineering` `Stack Exchange` `Ubiquitous Language` |

```json
{
"link": "https://softwareengineering.stackexchange.com/questions/447412/marketing-teams-term-for-ubiquitous-language",
"lp": true,
"ur": "content of website https://softwareengineering.stackexchange.com/questions/447412/marketing-teams-term-for-ubiquitous-language",
"l": "fr"
}
```


## Langage Ubiquitaire et Différents Termes

| Tags |
|------|
| `DDD` `Ubiquitous Language` `Domain-Driven Design` `Software Engineering` |

La page référencée traite de la notion de "langage ubiquitaire" dans le contexte du développement logiciel, plus spécifiquement en lien avec la conception pilotée par le domaine (DDD). La question soulevée porte sur la pertinence d'utiliser des termes distincts entre les équipes marketing et les équipes produit/ingénierie. Les réponses explorent les avantages et les inconvénients de cette pratique, notamment en ce qui concerne la diminution de l'ambiguïté et l'impact sur les différentes parties prenantes.


## Langage Ubiquitaire et Projets Multi-Équipes

| Tags |
|------|
| `DDD` `langage ubiquitaire` `gestion de projet` `communication` |

<ol>
<li><strong>Langage Ubiquitaire et Équipes Multiples</strong>: Un langage ubiquitaire est-il essentiel lorsque plusieurs équipes aux objectifs distincts participent à un projet ?</li>
<li><strong>Coût/Bénéfice de l'Unification du Langage</strong>: Quel est le rapport coût/bénéfice de l'unification du langage entre les équipes marketing et d'ingénierie ?</li>
<li><strong>Contextes Limités en DDD</strong>: Comment les "contextes limités" en DDD contribuent-ils à résoudre ces dilemmes linguistiques ?</li>
</ol>

Cette discussion, axée sur l'ingénierie et la gestion de projet, offre des perspectives sur la communication et la terminologie dans les projets complexes.


## Configuration d'un WAF rudimentaire avec .htaccess

| Tags |
|------|
| `.htaccess` `WAF` `Sécurité Web` `Apache` |

Utiliser un fichier `.htaccess` pour créer un pare-feu d'application Web (WAF) est une pratique courante pour améliorer la sécurité d'un site Web. Bien que les règles `.htaccess` ne remplacent pas un WAF dédié, elles peuvent fournir une couche de sécurité supplémentaire.

Voici quelques directives à inclure dans votre fichier `.htaccess` pour configurer un WAF rudimentaire :


## Blocage des requêtes suspectes

| Tags |
|------|
| `Apache` `RewriteRule` `Sécurité` |

```apache
RewriteEngine On
RewriteCond %{QUERY_STRING} (\|%3E) [NC,OR]
RewriteCond %{QUERY_STRING} GLOBALS(=|\[|\%[0-9A-Z]{0,2}) [OR]
RewriteCond %{QUERY_STRING} _REQUEST(=|\[|\%[0-9A-Z]{0,2})
RewriteRule ^(.*)$ index.php [F,L]
```


## Blocage des accès non autorisés aux fichiers sensibles

| Tags |
|------|
| `Apache` `htaccess` `sécurité` `fichiers sensibles` |

```apache
<FilesMatch "\.(htaccess|htpasswd|ini|phps|fla|psd|log|sh)$">
 Order Allow,Deny
 Deny from all
</FilesMatch>
```


## Blocage des User-Agents suspects

| Tags |
|------|
| `Apache` `User-Agent` `Sécurité` |

```apache
SetEnvIfNoCase User-Agent "^$" bad_bot
SetEnvIfNoCase User-Agent "Wget" bad_bot
SetEnvIfNoCase User-Agent "libwww-perl" bad_bot
<Limit GET POST HEAD>
 Order Allow,Deny
 Allow from all
 Deny from env=bad_bot
</Limit>
```


## Prévention du Clickjacking

| Tags |
|------|
| `Clickjacking` `Sécurité` `X-Frame-Options` `Apache` |

```apache
Header always append X-Frame-Options SAMEORIGIN
```


## Activation de la protection XSS

| Tags |
|------|
| `XSS` `Sécurité` `Apache` |

```apache
Header set X-XSS-Protection "1; mode=block"
```


## Activer la protection contre le sniffing MIME

| Tags |
|------|
| `Apache` `Sécurité` `Header` `MIME` |

```apache
Header set X-Content-Type-Options nosniff
```


## Redirection HTTP vers HTTPS

| Tags |
|------|
| `Apache` `HTTPS` `.htaccess` `Sécurité` |

```apache
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

**Note :** Sauvegardez le fichier `.htaccess` avant modification et testez les règles. Ces règles sont des exemples et peuvent nécessiter une adaptation. L'utilisation d'outils de pentesting peut aider à évaluer leur efficacité.


## Règles .htaccess pour un WAF rudimentaire

| Tags |
|------|
| `Apache` `htaccess` `WAF` `Sécurité Web` `RewriteRule` |

```apache
# Activer le moteur de réécriture
RewriteEngine On

# Bloquer les requêtes suspectes
RewriteCond %{QUERY_STRING} (\|%3E) [NC,OR]
RewriteCond %{QUERY_STRING} GLOBALS(=|\[|\%[0-9A-Z]{0,2}) [OR]
RewriteCond %{QUERY_STRING} _REQUEST(=|\[|\%[0-9A-Z]{0,2})
RewriteRule ^(.*)$ index.php [F,L]

# Bloquer l&#x27;accès aux fichiers sensibles
&lt;FilesMatch &quot;\.(htaccess|htpasswd|ini|phps|fla|psd|log|sh)$&quot;&gt;
  Order Allow,Deny
  Deny from all
&lt;/FilesMatch&gt;

# Bloquer les User-Agents suspects
SetEnvIfNoCase User-Agent &quot;^$&quot; bad_bot
SetEnvIfNoCase User-Agent &quot;Wget&quot; bad_bot
SetEnvIfNoCase User-Agent &quot;libwww-perl&quot; bad_bot
&lt;Limit GET POST HEAD&gt;
  Order Allow,Deny
  Allow from all
  Deny from env=bad_bot
&lt;/Limit&gt;

# Empêcher le Clickjacking
Header always append X-Frame-Options SAMEORIGIN

# Activer la protection XSS
Header set X-XSS-Protection &quot;1; mode=block&quot;

# Activer la protection contre le sniffing de type MIME
Header set X-Content-Type-Options nosniff

# Forcer l&#x27;utilisation de HTTPS
RewriteCond %{HTTPS} off
RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

Appliquez ces règles dans votre fichier `.htaccess` pour renforcer la sécurité de votre site. Sauvegardez le fichier `.htaccess` actuel avant de procéder aux modifications et testez rigoureusement les nouvelles règles afin de garantir le bon fonctionnement de votre site web.


## Certification CISSP : Présentation

| Tags |
|------|
| `CISSP` `Sécurité de l'information` `Certification` `ISC²` |

Le CISSP (Certified Information Systems Security Professional) est une certification de sécurité de l'information reconnue internationalement. Elle est délivrée par l'ISC² (International Information System Security Certification Consortium). Cette certification est destinée aux professionnels de la sécurité de l'information justifiant d'une expérience significative dans le domaine et souhaitant attester de leur expertise en gestion et en sécurité des systèmes d'information.


## Domaines de connaissance CISSP

| Tags |
|------|
| `CISSP` `Sécurité` `CBK` |

Le CISSP couvre huit domaines de connaissance, appelés "Common Body of Knowledge" (CBK), qui sont :

1.  Gestion des risques de sécurité et conformité
2.  Gestion des actifs
3.  Architecture et ingénierie de la sécurité
4.  Communication et sécurisation des réseaux
5.  Gestion de l'identité et des accès
6.  Évaluation de la sécurité et tests
7.  Opérations de sécurité
8.  Développement de logiciels sécurisés


## Exigences de certification CISSP

| Tags |
|------|
| `CISSP` `Sécurité de l'information` `Certification` `CBK` |

Pour obtenir la certification, les exigences sont les suivantes :

*   Justifier d'au moins cinq années d'expérience professionnelle dans le domaine de la sécurité de l'information, avec une couverture d'au moins deux des huit domaines du CBK (Common Body of Knowledge).
*   Réussir l'examen CISSP. L'examen est un test de 6 heures composé de 100 à 150 questions.
*   Valider son expérience professionnelle.
*   Accepter et respecter le code de déontologie de l'ISC².


## Renouvellement de la certification

| Tags |
|------|
| `certification` `renouvellement` `CPE` |

La certification doit être renouvelée tous les trois ans. Le renouvellement requiert l'acquisition de crédits de formation continue (CPE) ainsi que le paiement de frais de maintenance annuels.


## Pertinence de la certification CISSP

| Tags |
|------|
| `CISSP` `Sécurité de l'information` `Certification` `Gestion de la sécurité` |

Étant donné votre intérêt pour la sécurité de l'information, le CISSP pourrait être une étape logique dans votre développement professionnel. Il est particulièrement pertinent si vous envisagez de travailler dans des rôles de gestion de la sécurité de l'information ou si vous souhaitez établir votre propre entreprise dans ce domaine.


## Ressources pour la certification CISSP

| Tags |
|------|
| `CISSP` `Sécurité de l'information` `Certification` |

Le guide d'examen "CISSP All-in-One Exam Guide" de Shon Harris est une ressource utile. Les cours en ligne, comme Cybrary CISSP, peuvent également être précieux. Le site web de l'ISC² fournit des ressources officielles et des guides d'étude. La certification CISSP est largement reconnue et peut aider à se démarquer dans le domaine de la sécurité de l'information.


## Diviser un PDF en chapitres avec Python

| Tags |
|------|
| `Python` `PDF` `PyPDF2` `pdfplumber` |

Pour diviser un PDF en chapitres en Python, il est possible d'utiliser les bibliothèques <code>PyPDF2</code> pour manipuler les fichiers PDF et <code>pdfplumber</code> ou <code>PyPDF2</code> pour extraire le texte et identifier les chapitres. Voici un exemple de code illustrant cette tâche.


## Installation des dépendances

| Tags |
|------|
| `pip` `PyPDF2` `pdfplumber` |

Installez les paquets requis :

```bash
pip install PyPDF2
pip install pdfplumber
```


## Extraction de chapitres PDF avec Python

| Tags |
|------|
| `Python` `PyPDF2` `pdfplumber` `PDF` `Extraction` |

```python
import PyPDF2
import pdfplumber

# Charger le PDF
input_pdf_path = "votre_fichier.pdf"
pdf_reader = PyPDF2.PdfFileReader(input_pdf_path)
pdf_writer = PyPDF2.PdfFileWriter()

# Variables pour suivre les chapitres et les pages
current_chapter = "Annexe"
chapter_pages = []

# Parcourir chaque page pour trouver les chapitres
for page_num in range(pdf_reader.numPages):
    with pdfplumber.open(input_pdf_path) as pdf:
        page = pdf.pages[page_num]
        text = page.extract_text()
        
    # Identifier un nouveau chapitre (à adapter selon la mise en page de votre PDF)
    if "Chapitre" in text:
        # Sauvegarder les pages du chapitre précédent
        if chapter_pages:
            output_pdf_path = f"{current_chapter}.pdf"
            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)
        
        # Réinitialiser pour le nouveau chapitre
        pdf_writer = PyPDF2.PdfFileWriter()
        current_chapter = "Chapitre_" + str(page_num + 1)
        chapter_pages = []
    
    # Ajouter la page au chapitre en cours
    pdf_writer.addPage(pdf_reader.getPage(page_num))

# Sauvegarder les pages du dernier chapitre ou de l'annexe
if chapter_pages:
    output_pdf_path = f"{current_chapter}.pdf"
    with open(output_pdf_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)
```

Ce code est un exemple de base et peut nécessiter des ajustements pour s'adapter à la structure spécifique de votre PDF, notamment pour identifier correctement les chapitres.


## Considérations clés

| Tags |
|------|
| `PDF processing` `Python` `Code review` |

*   Le code actuel emploie <code>&quot;Chapitre&quot; in text</code> pour la détection des chapitres. Cette logique pourrait requérir des ajustements selon la structure du PDF.
*   Le code génère un fichier PDF par chapitre et un pour l'annexe.

Ce projet, combinant programmation Python et manipulation de documents, représente une opportunité pertinente pour les domaines de la cybersécurité et de la gestion de l'information.


## Correction d'erreur PyPDF2

| Tags |
|------|
| `Python` `PyPDF2` `PDF` |

Je m'excuse pour la confusion. La bibliothèque PyPDF2 a évolué et la classe <code>PdfFileReader</code> a été dépréciée en faveur de <code>PdfReader</code>. Voici comment adapter le code pour utiliser <code>PdfReader</code> :


## Installation des dépendances Python

| Tags |
|------|
| `Python` `PyPDF2` `pdfplumber` `pip` |

Si les paquets ne sont pas déjà installés, exécutez les commandes suivantes :

```bash
pip install PyPDF2
pip install pdfplumber
```


## Exemple de code Python pour la manipulation PDF

| Tags |
|------|
| `Python` `PyPDF2` `pdfplumber` `PDF` |

```python
import PyPDF2
import pdfplumber

# Charger le PDF
input_pdf_path = "votre_fichier.pdf"
pdf_reader = PyPDF2.PdfReader(input_pdf_path)
pdf_writer = PyPDF2.PdfWriter()

# Variables pour suivre les chapitres et les pages
current_chapter = "Annexe"
chapter_pages = []

# Parcourir chaque page pour trouver les chapitres
for page_num in range(len(pdf_reader.pages)):
    with pdfplumber.open(input_pdf_path) as pdf:
        page = pdf.pages[page_num]
        text = page.extract_text()
        
    # Identifier un nouveau chapitre (à adapter selon la mise en page de votre PDF)
    if "Chapitre" in text:
        # Sauvegarder les pages du chapitre précédent
        if chapter_pages:
            output_pdf_path = f"{current_chapter}.pdf"
            with open(output_pdf_path, "wb") as output_pdf:
                pdf_writer.write(output_pdf)
        
        # Réinitialiser pour le nouveau chapitre
        pdf_writer = PyPDF2.PdfWriter()
        current_chapter = "Chapitre_" + str(page_num + 1)
        chapter_pages = []
    
    # Ajouter la page au chapitre en cours
    pdf_writer.add_page(pdf_reader.pages[page_num])

# Sauvegarder les pages du dernier chapitre ou de l'annexe
if chapter_pages:
    output_pdf_path = f"{current_chapter}.pdf"
    with open(output_pdf_path, "wb") as output_pdf:
        pdf_writer.write(output_pdf)
```

Notez les changements suivants :

*   `PdfFileReader` est remplacé par `PdfReader`.
*   `PdfFileWriter` est remplacé par `PdfWriter`.
*   La méthode `numPages` est remplacée par `len(pdf_reader.pages)`.

Ces modifications devraient rendre le code compatible avec la version actuelle de PyPDF2. N'hésitez pas à ajuster le code selon vos besoins spécifiques.


## Utilisation du sommaire PDF

| Tags |
|------|
| `PDF` `sommaire` `extraction` `chapitrage` |

Si le PDF contient un sommaire, il est possible de l'utiliser pour structurer le fichier en chapitres. L'approche consiste à extraire le texte du sommaire, puis à l'utiliser pour diviser le PDF.


## Installation des dépendances Python

| Tags |
|------|
| `Python` `PyPDF2` `pdfplumber` `pip` |

Si vous ne les avez pas déjà, installez les paquets requis :

```bash
pip install PyPDF2
pip install pdfplumber
```


## Exemple de Code pour la Division de PDF

| Tags |
|------|
| `Python` `PyPDF2` `pdfplumber` `PDF` `Extraction de texte` `Expressions régulières` |

```python
import PyPDF2
import pdfplumber
import re

# Charger le PDF
input_pdf_path = "votre_fichier.pdf"
pdf_reader = PyPDF2.PdfReader(input_pdf_path)
pdf_writer = PyPDF2.PdfWriter()

# Extraire le sommaire
sommaire_text = ""
with pdfplumber.open(input_pdf_path) as pdf:
    for page_num in range(0, 5):  # Ajustez la plage pour inclure toutes les pages du sommaire
        page = pdf.pages[page_num]
        sommaire_text += page.extract_text()

# Trouver les numéros de page des chapitres
chapitre_dict = {}
for line in sommaire_text.split('\n'):
    match = re.search(r'(Chapitre \d+.*?)(\d+)$', line)
    if match:
        chapitre_dict[match.group(1)] = int(match.group(2)) - 1  # -1 car les indices de page commencent à 0

# Diviser le PDF en chapitres
current_chapter = "Annexe"
pdf_writer = PyPDF2.PdfWriter()
for page_num in range(len(pdf_reader.pages)):
    if any(chapitre_page == page_num for chapitre_page in chapitre_dict.values()):
        # Sauvegarder le chapitre précédent
        output_pdf_path = f"{current_chapter}.pdf"
        with open(output_pdf_path, "wb") as output_pdf:
            pdf_writer.write(output_pdf)
        
        # Réinitialiser pour le nouveau chapitre
        pdf_writer = PyPDF2.PdfWriter()
        current_chapter = [chapitre for chapitre, chapitre_page in chapitre_dict.items() if chapitre_page == page_num][0]
    
    # Ajouter la page au chapitre en cours
    pdf_writer.add_page(pdf_reader.pages[page_num])

# Sauvegarder le dernier chapitre ou l'annexe
output_pdf_path = f"{current_chapter}.pdf"
with open(output_pdf_path, "wb") as output_pdf:
    pdf_writer.write(output_pdf)
```

Dans cet exemple, le code utilise une expression régulière pour extraire les titres des chapitres et leurs numéros de page à partir du texte du sommaire. Il utilise ensuite ces informations pour diviser le PDF en chapitres.

Notez que vous devrez peut-être ajuster le code pour qu'il corresponde à la mise en page spécifique de votre PDF, notamment l'expression régulière utilisée pour extraire les titres des chapitres et les numéros de page.

Étant donné votre intérêt pour la programmation et l'ingénierie, ce projet pourrait être une excellente occasion de pratiquer la manipulation de fichiers PDF et l'extraction de données textuelles, des compétences utiles dans divers domaines
techniques.


## Accéder au sommaire d'un PDF avec PyPDF2

| Tags |
|------|
| `Python` `PyPDF2` `PDF` `Sommaire` |

Pour accéder à l'objet Sommaire (Table des matières ou Outline) d'un fichier PDF en Python, utilisez la bibliothèque `PyPDF2`. Cette bibliothèque offre une méthode pour accéder et naviguer dans les éléments du sommaire.

Exemple de code pour accéder au sommaire et extraire les titres et numéros de page :

```python
import PyPDF2

# Ouvrir le fichier PDF
with open("votre_fichier.pdf", "rb") as f:
    pdf_reader = PyPDF2.PdfReader(f)

    # Accéder à l'objet Sommaire
    outlines = pdf_reader.get_outlines()

    # Dictionnaire pour stocker les titres des chapitres et leurs numéros de page
    chapitre_dict = {}

    # Parcourir l'objet Sommaire pour extraire les informations
    for outline in outlines:
        if isinstance(outline, list):
            # Si l'objet Sommaire est une liste de chapitres
            for chapitre in outline:
                title = chapitre.title
                page_num = chapitre.page.get('/StructParents')  # Le numéro de page peut varier selon la structure du PDF
                chapitre_dict[title] = page_num
        else:
            # Si l'objet Sommaire est une seule entrée
            title = outline.title
            page_num = outline.page.get('/StructParents')  # Le numéro de page peut varier selon la structure du PDF
            chapitre_dict[title] = page_num

# Afficher le dictionnaire des chapitres
print(chapitre_dict)
```

La structure du sommaire peut varier selon le PDF. Adaptez le code si nécessaire.

L'accès programmatique à la structure interne d'un PDF est utile pour la gestion de documents et la cybersécurité.


## Accès à la table des matières PDF avec PyMuPDF

| Tags |
|------|
| `PyMuPDF` `PDF` `Table des matières` `Python` |

Je vous prie de bien vouloir excuser l'erreur. La bibliothèque <code>PyPDF2</code> ne dispose pas de méthode directe pour accéder à la table des matières d'un fichier PDF. Une approche possible consiste à utiliser <code>PyPDF2</code> pour explorer les métadonnées PDF, qui peuvent contenir des informations structurelles, mais cela peut s'avérer complexe.

Une alternative est d'utiliser la bibliothèque <code>PyMuPDF</code> (MuPDF), qui offre des fonctionnalités plus avancées pour la manipulation de PDF, y compris l'accès à la table des matières.

Voici comment installer <code>PyMuPDF</code> et un exemple de code pour accéder à la table des matières :


## Installation de PyMuPDF

| Tags |
|------|
| `PyMuPDF` `Python` `pip` `installation` |

```bash
pip install PyMuPDF
```


## Extraction de la table des matières d'un PDF

| Tags |
|------|
| `Python` `PyMuPDF` `PDF` `Extraction` |

```python
import fitz  # PyMuPDF

# Ouvrir le fichier PDF
pdf = fitz.open("votre_fichier.pdf")

# Accéder à la table des matières
toc = pdf.get_toc()

# Afficher la table des matières
for level, title, page in toc:
    print(f"Level: {level}, Title: {title}, Page: {page}")

# Vous pouvez maintenant utiliser ces informations pour diviser le PDF en chapitres.
```

Dans cet exemple, `get_toc()` renvoie une liste de tuples, où chaque tuple contient le niveau du chapitre, le titre et le numéro de page. Vous pouvez utiliser ces informations pour diviser le PDF en chapitres.

L'utilisation de bibliothèques plus avancées comme `PyMuPDF` pourrait offrir des fonctionnalités plus puissantes pour manipuler des fichiers PDF.


## Diviser un PDF par chapitres

| Tags |
|------|
| `PDF` `Python` `PyPDF2` `chapitres` |

Pour diviser un PDF en fonction de ses chapitres de niveau 1 et placer le contenu non classé dans un fichier "annexe.pdf", utilisez le code suivant. L'exemple utilise le fichier "CISSP All in One Exam Guide - PDF Room.pdf".

```python
from PyPDF2 import PdfReader, PdfWriter

def extraire_chapitres_et_annexe(fichier_pdf, niveau_chapitre=1):
    """
    Divise un PDF en chapitres et extrait l'annexe.

    Args:
        fichier_pdf (str): Le chemin du fichier PDF.
        niveau_chapitre (int): Le niveau du titre du chapitre à utiliser (par défaut 1).
    """
    reader = PdfReader(fichier_pdf)
    chapitres = {}
    annexe_writer = PdfWriter()
    chapitre_actuel = None

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        texte_page = page.extract_text()
        lignes = texte_page.split('\n')

        # Recherche de titres de chapitres
        for ligne in lignes:
            # Adaptation de la détection de titre (exemple)
            if ligne.startswith(('Chapitre ', 'Module ', 'Partie ')): # Ajuster selon la structure du document
                chapitre_actuel = ligne.strip()
                chapitres[chapitre_actuel] = PdfWriter()
                break  # On considère la première correspondance par page

        # Ajout de la page au chapitre ou à l'annexe
        if chapitre_actuel:
            chapitres[chapitre_actuel].add_page(page)
        else:
            annexe_writer.add_page(page)

    # Écriture des fichiers
    for chapitre, writer in chapitres.items():
        nom_fichier = f"{chapitre.replace(' ', '_')}.pdf"
        with open(nom_fichier, "wb") as fichier_sortie:
            writer.write(fichier_sortie)
        print(f"Chapitre extrait : {nom_fichier}")

    with open("annexe.pdf", "wb") as fichier_sortie:
        annexe_writer.write(fichier_sortie)
    print("Annexe extraite : annexe.pdf")

# Utilisation de la fonction
extraire_chapitres_et_annexe("CISSP All in One Exam Guide - PDF Room.pdf")
```


## Diviser un PDF par chapitres et annexes

| Tags |
|------|
| `Python` `PyMuPDF` `PDF` `traitement de documents` |

Pour diviser un fichier PDF en fonction de ses chapitres de niveau 1 et placer le contenu hors de ces chapitres dans un fichier nommé "annexe.pdf", vous pouvez utiliser le code suivant. Ce code exploite la bibliothèque <code>PyMuPDF</code> pour accéder à la table des matières et segmenter le fichier PDF.


## Installation de PyMuPDF

| Tags |
|------|
| `PyMuPDF` `Python` `pip` `installation` |

Si vous ne l'avez pas déjà fait, installez le paquet nécessaire :

```bash
pip install PyMuPDF
```


## Extrait de code Python : Découpage PDF par chapitres

| Tags |
|------|
| `Python` `PyMuPDF` `PDF` `traitement de documents` `cybersécurité` |

```python
import fitz  # PyMuPDF

# Ouvrir le fichier PDF
pdf = fitz.open("CISSP All in one Exam Guide - PDF Room.pdf")

# Accéder à la table des matières
toc = pdf.get_toc()

# Initialiser le PDF pour les annexes
annexe_pdf = fitz.open()

# Variables pour suivre le chapitre actuel
current_chapter_pdf = fitz.open()
current_chapter_title = "Annexe"

# Parcourir chaque page du PDF
for page_number in range(len(pdf)):
    page = pdf.load_page(page_number)
    
    # Vérifier si la page actuelle correspond à un nouveau chapitre de niveau 1
    new_chapter = [entry for entry in toc if entry[0] == 1 and entry[2] == page_number + 1]
    
    if new_chapter:
        # Sauvegarder le chapitre PDF actuel
        if len(current_chapter_pdf):
            current_chapter_pdf.save(f"{current_chapter_title}.pdf")
        
        # Réinitialiser pour le nouveau chapitre
        current_chapter_pdf = fitz.open()
        current_chapter_title = new_chapter[0][1].replace(" ", "_").replace("/", "-")
    
    # Ajouter la page au chapitre PDF actuel ou aux annexes
    if current_chapter_title != "Annexe":
        current_chapter_pdf.insert_pdf(pdf, from_page=page_number, to_page=page_number)
    else:
        annexe_pdf.insert_pdf(pdf, from_page=page_number, to_page=page_number)

# Sauvegarder le dernier chapitre ou les annexes
if len(current_chapter_pdf):
    current_chapter_pdf.save(f"{current_chapter_title}.pdf")
if len(annexe_pdf):
    annexe_pdf.save("annexe.pdf")
```

Ce code génère un nouveau fichier PDF pour chaque chapitre de niveau 1, basé sur la table des matières, et un fichier "annexe.pdf" pour les pages non associées à ces chapitres.

Remplacez le nom du fichier PDF dans le code par le chemin d'accès correct vers votre fichier "CISSP All in one Exam Guide - PDF Room.pdf".

Cette technique de manipulation de fichiers PDF est utile pour l'organisation de documents volumineux et peut être appliquée dans des contextes liés à la cybersécurité et l'ingénierie.


## Division PDF par chapitres et annexe

| Tags |
|------|
| `PDF` `Python` `Traitement de documents` |

Pour diviser un fichier PDF en chapitres commençant par "Chapter" et placer le reste dans "annexe.pdf", la solution suivante peut être appliquée :


## Installation de PyMuPDF

| Tags |
|------|
| `PyMuPDF` `Python` `pip` `installation` |

Si le paquet n'est pas déjà installé, exécuter la commande suivante :

```bash
pip install PyMuPDF
```


## Exemple de Code Python pour la Manipulation PDF

| Tags |
|------|
| `Python` `PyMuPDF` `PDF` `Extraction` `Cybersécurité` |

```python
import fitz  # PyMuPDF

# Ouvrir le fichier PDF
pdf = fitz.open("CISSP All in one Exam Guide - PDF Room.pdf")

# Accéder à la table des matières
toc = pdf.get_toc()

# Initialiser le PDF pour les annexes
annexe_pdf = fitz.open()

# Variables pour suivre le chapitre actuel
current_chapter_pdf = fitz.open()
current_chapter_title = "Annexe"

# Parcourir chaque page du PDF
for page_number in range(len(pdf)):
    page = pdf.load_page(page_number)
    
    # Vérifier si la page actuelle correspond à un nouveau chapitre qui commence par "Chapter"
    new_chapter = [entry for entry in toc if entry[1].startswith("Chapter") and entry[2] == page_number + 1]
    
    if new_chapter:
        # Sauvegarder le chapitre PDF actuel
        if len(current_chapter_pdf):
            current_chapter_pdf.save(f"{current_chapter_title}.pdf")
        
        # Réinitialiser pour le nouveau chapitre
        current_chapter_pdf = fitz.open()
        current_chapter_title = new_chapter[0][1].replace(" ", "_").replace("/", "-")
    
    # Ajouter la page au chapitre PDF actuel ou aux annexes
    if current_chapter_title.startswith("Chapter"):
        current_chapter_pdf.insert_pdf(pdf, from_page=page_number, to_page=page_number)
    else:
        annexe_pdf.insert_pdf(pdf, from_page=page_number, to_page=page_number)

# Sauvegarder le dernier chapitre ou les annexes
if len(current_chapter_pdf):
    current_chapter_pdf.save(f"{current_chapter_title}.pdf")
if len(annexe_pdf):
    annexe_pdf.save("annexe.pdf")
```

Le code présenté illustre une méthode pour organiser un document PDF volumineux en extrayant des chapitres spécifiques et en les séparant dans des fichiers PDF individuels. Le script utilise la bibliothèque PyMuPDF pour ouvrir, analyser et manipuler le fichier PDF. La logique implémentée permet de détecter les chapitres en fonction de leur titre dans la table des matières et de séparer les pages correspondantes dans des fichiers distincts. Les pages qui ne correspondent pas aux chapitres sont ajoutées à une annexe.

Il est important de noter que le nom du fichier PDF doit être correctement spécifié. Cette approche peut s'avérer utile dans des contextes liés à la cybersécurité et l'ingénierie, où l'organisation et la gestion de documents sont cruciales.


## Sauvegarde de morceaux dans le répertoire "chapters"

| Tags |
|------|
| `Python` `Système de fichiers` `Répertoires` |

Pour sauvegarder les morceaux dans un répertoire nommé "chapters" et le créer s'il n'existe pas, vous pouvez ajouter du code pour gérer les opérations sur le système de fichiers.

```python
import os

def sauvegarder_morceau(morceau, nom_fichier):
    """
    Sauvegarde un morceau dans le répertoire 'chapters'.

    Args:
        morceau: Le contenu du morceau à sauvegarder.
        nom_fichier: Le nom du fichier à créer (ex: "chapitre_1.txt").
    """
    repertoire = "chapters"
    # Créer le répertoire s'il n'existe pas
    if not os.path.exists(repertoire):
        os.makedirs(repertoire)

    chemin_fichier = os.path.join(repertoire, nom_fichier)
    try:
        with open(chemin_fichier, "w") as f:
            f.write(morceau)
        print(f"Morceau sauvegardé avec succès dans : {chemin_fichier}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de {nom_fichier} : {e}")

# Exemple d'utilisation
morceau_exemple = "Ceci est le contenu du morceau."
nom_fichier_exemple = "chapitre_001.txt"
sauvegarder_morceau(morceau_exemple, nom_fichier_exemple)
```

Ce script utilise le module `os` pour interagir avec le système de fichiers. La fonction `sauvegarder_morceau` prend le contenu du morceau et le nom du fichier en entrée. Elle vérifie si le répertoire "chapters" existe, et le crée si nécessaire.  Elle construit ensuite le chemin complet du fichier et écrit le contenu du morceau dans ce fichier.  Les messages de succès ou d'erreur sont affichés dans la console.  Un exemple d'utilisation est inclus.


## Installation de PyMuPDF

| Tags |
|------|
| `PyMuPDF` `Python` `Installation` `pip` |

Si le paquet n'est pas installé, exécutez la commande suivante :

```bash
pip install PyMuPDF
```


## Code Python d'extraction de chapitres PDF

| Tags |
|------|
| `Python` `PyMuPDF` `PDF` `Extraction` `Cybersécurité` |

```python
import fitz  # PyMuPDF
import os

# Créer le répertoire 'chapters' s'il n'existe pas
if not os.path.exists('chapters'):
    os.makedirs('chapters')

# Ouvrir le fichier PDF
pdf = fitz.open("CISSP All in one Exam Guide - PDF Room.pdf")

# Accéder à la table des matières
toc = pdf.get_toc()

# Initialiser le PDF pour les annexes
annexe_pdf = fitz.open()

# Variables pour suivre le chapitre actuel
current_chapter_pdf = fitz.open()
current_chapter_title = "Annexe"

# Parcourir chaque page du PDF
for page_number in range(len(pdf)):
    page = pdf.load_page(page_number)
    
    # Vérifier si la page actuelle correspond à un nouveau chapitre qui commence par "Chapter"
    new_chapter = [entry for entry in toc if entry[1].startswith("Chapter") and entry[2] == page_number + 1]
    
    if new_chapter:
        # Sauvegarder le chapitre PDF actuel
        if len(current_chapter_pdf):
            current_chapter_pdf.save(f"chapters/{current_chapter_title}.pdf")
        
        # Réinitialiser pour le nouveau chapitre
        current_chapter_pdf = fitz.open()
        current_chapter_title = new_chapter[0][1].replace(" ", "_").replace("/", "-")
    
    # Ajouter la page au chapitre PDF actuel ou aux annexes
    if current_chapter_title.startswith("Chapter"):
        current_chapter_pdf.insert_pdf(pdf, from_page=page_number, to_page=page_number)
    else:
        annexe_pdf.insert_pdf(pdf, from_page=page_number, to_page=page_number)

# Sauvegarder le dernier chapitre ou les annexes
if len(current_chapter_pdf):
    current_chapter_pdf.save(f"chapters/{current_chapter_title}.pdf")
if len(annexe_pdf):
    annexe_pdf.save("chapters/annexe.pdf")
```

Dans ce code, la bibliothèque `os` est utilisée pour vérifier et créer le répertoire "chapters". Tous les fichiers PDF générés sont sauvegardés dans ce répertoire.

Remplacez le nom de fichier PDF dans le code par le chemin d'accès correct à votre fichier "CISSP All in one Exam Guide - PDF Room.pdf".

Ce type de manipulation de PDF et de gestion de répertoires peut s'avérer utile dans des domaines tels que la cybersécurité.


## Convertir PDF en Markdown

| Tags |
|------|
| `PDF` `Markdown` `pdfplumber` `Python` |

Transformer un fichier PDF en fichier Markdown (.md) peut s'avérer complexe, particulièrement si le PDF contient des éléments tels que des images, des tableaux ou des formules mathématiques. Cependant, pour un PDF essentiellement textuel, la conversion est plus simple.

La bibliothèque <code>pdfplumber</code> permet d'extraire le texte d'un PDF, puis de le sauvegarder dans un fichier .md. Voici un exemple :


## Installation de la librairie pdfplumber

| Tags |
|------|
| `Python` `pdfplumber` `pip` `installation` |

Si vous ne l'avez pas déjà fait, installez les paquets nécessaires :

```bash
pip install pdfplumber
```


## Conversion PDF en Markdown avec Python

| Tags |
|------|
| `Python` `pdfplumber` `Markdown` `Conversion` |

```python
import pdfplumber
import os

# Créer le répertoire 'markdown_files' s'il n'existe pas
if not os.path.exists('markdown_files'):
    os.makedirs('markdown_files')

# Fonction pour convertir un PDF en fichier Markdown
def convert_pdf_to_md(pdf_path, md_path):
    with pdfplumber.open(pdf_path) as pdf:
        markdown_text = ""
        for page in pdf.pages:
            markdown_text += page.extract_text()
        
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(markdown_text)

# Parcourir les fichiers PDF dans le répertoire 'chapters'
for pdf_file in os.listdir('chapters'):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join('chapters', pdf_file)
        md_file = pdf_file.replace('.pdf', '.md')
        md_path = os.path.join('markdown_files', md_file)
        
        # Convertir le fichier PDF en fichier Markdown
        convert_pdf_to_md(pdf_path, md_path)
```

Ce code parcourt tous les fichiers PDF dans le répertoire "chapters", les convertit en fichiers Markdown et les sauvegarde dans un répertoire "markdown_files". La fonction `convert_pdf_to_md` utilise `pdfplumber` pour extraire le texte de chaque page du PDF et le concaténer dans une chaîne Markdown.

Notez que cette méthode est assez basique et ne gère pas les éléments avancés comme les images, les tableaux, etc. Pour une conversion plus avancée, des outils spécialisés ou des ajustements manuels pourraient être nécessaires.

Étant donné votre intérêt pour la programmation et l'ingénierie, ce genre de tâche pourrait être une excellente occasion de pratiquer la manipulation de fichiers et la conversion de formats, des compétences utiles dans des domaines comme la cybersécurité et la gestion de l'information.


## Extraction d'images PDF et mise en page en Markdown

| Tags |
|------|
| `PDF` `Markdown` `pdfplumber` `HTML` `CSS` |

Extraire les images et préserver la mise en page lors de la conversion PDF vers Markdown est complexe. Markdown ne supporte pas nativement les styles avancés. Cependant, il est possible d'utiliser des balises HTML et des feuilles de style CSS pour contrôler la mise en page.

La bibliothèque <code>pdfplumber</code> peut extraire les images et le texte. Les images peuvent ensuite être sauvegardées et référencées dans le fichier Markdown.

Exemple de code :


## Installation de pdfplumber

| Tags |
|------|
| `pdfplumber` `installation` `Python` `pip` |

Si vous ne l'avez pas déjà fait, installez les paquets nécessaires :

```bash
pip install pdfplumber
```


## Conversion PDF en Markdown avec Python

| Tags |
|------|
| `Python` `pdfplumber` `Markdown` `Conversion` |

```python
import pdfplumber
import os

# Créer les répertoires &#x27;markdown_files&#x27; et &#x27;images&#x27; s&#x27;ils n&#x27;existent pas
if not os.path.exists(&#x27;markdown_files&#x27;):
    os.makedirs(&#x27;markdown_files&#x27;)
if not os.path.exists(&#x27;images&#x27;):
    os.makedirs(&#x27;images&#x27;)

# Fonction pour convertir un PDF en fichier Markdown
def convert_pdf_to_md(pdf_path, md_path):
    with pdfplumber.open(pdf_path) as pdf:
        markdown_text = &quot;&quot;
        for i, page in enumerate(pdf.pages):
            # Extraire le texte
            text = page.extract_text()
            markdown_text += text
            
            # Extraire les images
            images = page.extract_images()
            for j, img in enumerate(images):
                img_path = f&quot;images/image_{i}_{j}.png&quot;
                img.save(img_path, &#x27;PNG&#x27;)
                
                # Ajouter une référence à l&#x27;image dans le fichier Markdown
                markdown_text += f&quot;\n![Image {i}_{j}]({img_path})\n&quot;
        
        # Sauvegarder le texte dans un fichier Markdown
        with open(md_path, &quot;w&quot;, encoding=&quot;utf-8&quot;) as f:
            f.write(markdown_text)

# Parcourir les fichiers PDF dans le répertoire &#x27;chapters&#x27;
for pdf_file in os.listdir(&#x27;chapters&#x27;):
    if pdf_file.endswith(&#x27;.pdf&#x27;):
        pdf_path = os.path.join(&#x27;chapters&#x27;, pdf_file)
        md_file = pdf_file.replace(&#x27;.pdf&#x27;, &#x27;.md&#x27;)
        md_path = os.path.join(&#x27;markdown_files&#x27;, md_file)
        
        # Convertir le fichier PDF en fichier Markdown
        convert_pdf_to_md(pdf_path, md_path)
```

Ce code utilise `pdfplumber` pour extraire le texte et les images de chaque page d'un PDF. Les images sont sauvegardées dans le répertoire "images", et une référence à chaque image est ajoutée au fichier Markdown.

Ce code est basique et ne prend pas en charge les éléments de mise en page avancés tels que les tableaux ou les formules mathématiques. Des ajustements manuels ou des outils spécialisés peuvent être nécessaires pour une conversion plus précise.

Ce type de tâche est une bonne occasion de pratiquer la manipulation de fichiers et la conversion de formats, des compétences utiles dans des domaines comme la cybersécurité et la gestion de l'information.


## Erreur AttributeError avec pdfplumber

| Tags |
|------|
| `pdfplumber` `PyMuPDF` `extraction d'images` `Python` |

Je vous prie de bien vouloir accepter mes excuses pour l'erreur précédente. Vous avez raison, la méthode <code>extract_images</code> n'est pas disponible dans <code>pdfplumber</code>. Pour l'extraction des images, il est nécessaire d'utiliser la bibliothèque <code>PyMuPDF</code> (MuPDF).

Voici une méthode pour extraire le texte avec <code>pdfplumber</code> et les images avec <code>PyMuPDF</code> :


## Installation des dépendances

| Tags |
|------|
| `Python` `pdfplumber` `PyMuPDF` |

Si ce n'est pas déjà fait, installez les paquets requis :

```bash
pip install pdfplumber
pip install PyMuPDF
```


## Conversion PDF en Markdown avec Python

| Tags |
|------|
| `Python` `PDF` `Markdown` `pdfplumber` `PyMuPDF` |

```python
import fitz  # PyMuPDF
import pdfplumber
import os

# Créer les répertoires 'markdown_files' et 'images' s'ils n'existent pas
if not os.path.exists('markdown_files'):
    os.makedirs('markdown_files')
if not os.path.exists('images'):
    os.makedirs('images')

# Fonction pour convertir un PDF en fichier Markdown
def convert_pdf_to_md(pdf_path, md_path):
    markdown_text = ""
    
    # Utiliser pdfplumber pour extraire le texte
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text()
            markdown_text += text + "\n"
    
    # Utiliser PyMuPDF pour extraire les images
    pdf_fitz = fitz.open(pdf_path)
    for i, page in enumerate(pdf_fitz):
        image_list = page.get_pixmap()
        for j, img in enumerate(image_list):
            img_path = f"images/image_{i}_{j}.png"
            img.save(img_path)
            
            # Ajouter une référence à l'image dans le fichier Markdown
            markdown_text += f"\n![Image {i}_{j}]({img_path})\n"
    
    # Sauvegarder le texte dans un fichier Markdown
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(markdown_text)

# Parcourir les fichiers PDF dans le répertoire 'chapters'
for pdf_file in os.listdir('chapters'):
    if pdf_file.endswith('.pdf'):
        pdf_path = os.path.join('chapters', pdf_file)
        md_file = pdf_file.replace('.pdf', '.md')
        md_path = os.path.join('markdown_files', md_file)
        
        # Convertir le fichier PDF en fichier Markdown
        convert_pdf_to_md(pdf_path, md_path)
```

Dans ce code, j'utilise `pdfplumber` pour extraire le texte de chaque page et `PyMuPDF` pour extraire les images. Les images sont sauvegardées dans un répertoire "images", et une référence à chaque image est ajoutée au fichier Markdown.

Notez que ce code est assez basique et ne gère pas les éléments de mise en page avancés comme les tableaux ou les formules mathématiques. Pour une conversion plus précise, des ajustements manuels ou des outils spécialisés pourraient être nécessaires.

Ce genre de manipulation de fichiers PDF et de conversion de formats peut être très utile dans des domaines comme la cybersécurité et l'ingénierie, ce qui pourrait être pertinent pour vos projets et vos intérêts.


## Diviser les chapitres PDF de plus de 10 Mo

| Tags |
|------|
| `Python` `PyMuPDF` `PDF` `manipulation de fichiers` |

Pour diviser chaque chapitre de plus de 10 Mo en parties de moins de 10 Mo, tout en organisant les fichiers dans des répertoires et sous-répertoires, vous pouvez utiliser le code suivant. Ce code utilise la bibliothèque `PyMuPDF` pour accéder à la table des matières et diviser le fichier PDF.


## Installation de PyMuPDF

| Tags |
|------|
| `PyMuPDF` `pip` `Python` `Installation` |

Si vous ne l'avez pas déjà fait, installez le paquet nécessaire :

```bash
pip install PyMuPDF
```


## Exemple de code Python pour manipuler PDF

| Tags |
|------|
| `Python` `PyMuPDF` `PDF` `traitement de documents` |

```python
import fitz  # PyMuPDF
import os

# Créer le répertoire 'chapters' s'il n'existe pas
if not os.path.exists('chapters'):
    os.makedirs('chapters')

# Ouvrir le fichier PDF
pdf = fitz.open("CISSP All in one Exam Guide - PDF Room.pdf")

# Accéder à la table des matières
toc = pdf.get_toc()

# Initialiser le PDF pour les annexes
annexe_pdf = fitz.open()

# Variables pour suivre le chapitre actuel
current_chapter_pdf = fitz.open()
current_chapter_title = "Annexe"
current_chapter_page_count = 0

# Parcourir chaque page du PDF
for page_number in range(len(pdf)):
    page = pdf.load_page(page_number)
    
    # Vérifier si la page actuelle correspond à un nouveau chapitre qui commence par "Chapter"
    new_chapter = [entry for entry in toc if entry[1].startswith("Chapter") and entry[2] == page_number + 1]
    
    if new_chapter:
        # Sauvegarder le chapitre PDF actuel
        if len(current_chapter_pdf):
            current_chapter_pdf.save(f"chapters/{current_chapter_title}.pdf")
        
        # Réinitialiser pour le nouveau chapitre
        current_chapter_pdf = fitz.open()
        current_chapter_title = new_chapter[0][1].replace(" ", "_").replace("/", "-")
        current_chapter_page_count = 0
    
    # Ajouter la page au chapitre PDF actuel ou aux annexes
    if current_chapter_title.startswith("Chapter"):
        current_chapter_pdf.insert_pdf(pdf, from_page=page_number, to_page=page_number)
        current_chapter_page_count += 1

        # Vérifier la taille du fichier PDF actuel
        current_chapter_pdf.save("temp.pdf")
        if os.path.getsize("temp.pdf") > 10 * 1024 * 1024:  # 10 Mo
            # Sauvegarder la partie actuelle du chapitre
            part_dir = f"chapters/{current_chapter_title}_parts"
            if not os.path.exists(part_dir):
                os.makedirs(part_dir)
            current_chapter_pdf.save(f"{part_dir}/{current_chapter_title}_part_{current_chapter_page_count}.pdf")
            
            # Réinitialiser pour la nouvelle partie du chapitre
            current_chapter_pdf = fitz.open()
            current_chapter_page_count = 0
    else:
        annexe_pdf.insert_pdf(pdf, from_page=page_number, to_page=page_number)

# Sauvegarder le dernier chapitre ou les annexes
if len(current_chapter_pdf):
    current_chapter_pdf.save(f"chapters/{current_chapter_title}.pdf")
if len(annexe_pdf):
    annexe_pdf.save("chapters/annexe.pdf")

# Supprimer le fichier temporaire
if os.path.exists("temp.pdf"):
    os.remove("temp.pdf")
```

Ce code inclut une vérification de la taille du fichier PDF. Si la taille dépasse 10 Mo, le code sauvegarde la partie actuelle du chapitre dans un sous-répertoire et commence une nouvelle partie.

Remplacez le nom du fichier PDF dans le code par le chemin exact vers votre fichier "CISSP All in one Exam Guide - PDF Room.pdf".


## Vérification de chaînes de caractères PHP avec Regex

| Tags |
|------|
| `PHP` `regex` `chaînes de caractères` `validation` |

Pour vérifier si une chaîne de caractères contient le mot "Contacté" suivi d'une date au format "YYYY-MM-DD", une expression régulière peut être utilisée en PHP.

Voici un exemple de code :

```php
<?php
$string = "Contacté 2023-09-27";
$pattern = "/Contacté \d{4}-\d{2}-\d{2}/";

if (preg_match($pattern, $string)) {
    echo "La chaîne correspond au format attendu.";
} else {
    echo "La chaîne ne correspond pas au format attendu.";
}
?>
```

Dans cet exemple :

*   `$string` contient la chaîne à tester.
*   `$pattern` définit l'expression régulière.  `Contacté ` correspond littéralement à la chaîne "Contacté " (avec un espace). `\d{4}-\d{2}-\d{2}` correspond à une date au format YYYY-MM-DD.
*   `preg_match()` tente de faire correspondre l'expression régulière dans la chaîne.  Elle retourne `1` si une correspondance est trouvée, et `0` sinon.

**Exemple d'utilisation avec des données variables :**

Pour rendre le code plus robuste, vous pouvez extraire la date si la chaîne correspond :

```php
<?php
$string = "Contacté 2024-01-15";
$pattern = "/Contacté (\d{4}-\d{2}-\d{2})/";

if (preg_match($pattern, $string, $matches)) {
    echo "La chaîne correspond au format attendu.\n";
    $date = $matches[1]; // Récupère la date capturée par le groupe ( )
    echo "Date extraite : " . $date . "\n";
} else {
    echo "La chaîne ne correspond pas au format attendu.\n";
}
?>
```

Dans ce second exemple, la regex utilise des parenthèses pour capturer la date.  La variable `$matches` contiendra un tableau avec la correspondance complète (`$matches[0]`) et la date capturée (`$matches[1]`).  Ceci permet d'extraire la date pour une utilisation ultérieure.


## PHP : Tester une chaîne avec une date et "Contacté"

| Tags |
|------|
| `PHP` `regex` `preg_match` `date` |

```php
<?php

$chaine = "Contacté<br />2023-09-27<br />";

// Expression régulière pour matcher "Contacté" suivi d'une date au format "AAAA-MM-JJ"
$regex = "/Contacté<br \/>\\d{4}-\\d{2}-\\d{2}<br \/>/";

if (preg_match($regex, $chaine, $matches)) {
    echo "La chaîne correspond à l'expression régulière. Date trouvée : " . $matches[0];
} else {
    echo "La chaîne ne correspond pas à l'expression régulière.";
}

?>
```

Dans cet exemple, l'expression régulière `/Contacté<br \/>\\d{4}-\\d{2}-\\d{2}<br \/>/` recherche le mot "Contacté" suivi d'une date au format "AAAA-MM-JJ". Les `\\d{4}-\\d{2}-\\d{2}` dans l'expression régulière correspondent à quatre chiffres pour l'année, deux chiffres pour le mois et deux chiffres pour le jour, séparés par des tirets.

La fonction `preg_match()` est utilisée pour effectuer la correspondance de l'expression régulière. Si la chaîne correspond à l'expression régulière, la fonction retournera `true`, et vous pourrez accéder à la date trouvée via le tableau `$matches`.

La maîtrise des expressions régulières est une compétence utile pour la validation des données, la recherche de motifs dans des fichiers de logs, etc.
