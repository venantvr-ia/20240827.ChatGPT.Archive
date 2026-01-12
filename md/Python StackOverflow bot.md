## Bot Python StackOverflow

| Tags |
|------|
| `Python` `Stack Overflow` `Bot` |

Ce document décrit le développement d'un bot Python pour Stack Overflow.

Le bot est conçu pour :

*   Répondre aux questions des utilisateurs sur Stack Overflow.
*   Fournir des informations pertinentes.

### Configuration

Le bot est configuré avec les paramètres suivants :

*   **Clé API Stack Exchange :** [CLÉ_API]
*   **Nom d'utilisateur :** [NOM]
*   **Mot de passe :** [MOT_DE_PASSE]
*   **Nom d'utilisateur du bot :** [NOM_BOT]
*   **Liste des mots-clés :** `Python`, `Stackoverflow`
*   **Seuil de confiance :** 0.7

### Installation

Pour installer le bot, exécutez la commande suivante :

```bash
pip install stackapi
```

### Utilisation

Pour exécuter le bot, exécutez le script Python suivant :

```python
import os
from stackapi import StackAPI

# Configuration
SITE = StackAPI('stackoverflow')
API_KEY = os.environ.get('STACK_API_KEY')
USERNAME = os.environ.get('STACK_USERNAME')
PASSWORD = os.environ.get('STACK_PASSWORD')
BOT_USERNAME = os.environ.get('BOT_USERNAME')
KEYWORDS = ['Python', 'Stackoverflow']
CONFIDENCE_THRESHOLD = 0.7

# Fonction pour rechercher les questions
def search_questions(keywords):
    questions = SITE.fetch('search/advanced', q=keywords, sort='relevance', accepted=True, key=API_KEY)
    return questions.get('items', [])

# Fonction pour répondre aux questions
def answer_question(question_id, answer):
    # Implémenter la logique de réponse ici
    print(f"Réponse à la question {question_id}: {answer}")

# Boucle principale
if __name__ == "__main__":
    while True:
        for keyword in KEYWORDS:
            questions = search_questions(keyword)
            for question in questions:
                # Filtrer les questions non répondues
                if not question.get('is_answered'):
                    # Analyse du contenu de la question pour déterminer la pertinence
                    # et générer une réponse appropriée.
                    answer = "Ceci est une réponse de test." # Remplacer avec la logique de réponse réelle
                    answer_question(question.get('question_id'), answer)
        # Attente avant la prochaine itération
        time.sleep(60) # Vérifier toutes les minutes
```

### Remarques

*   Ce bot est un prototype et n'est pas prêt pour une utilisation en production.
*   L'authentification et l'autorisation sont nécessaires pour publier des réponses sur Stack Overflow.
*   La logique de réponse doit être améliorée pour fournir des réponses précises et utiles.
*   Les demandes sont limitées en fonction du point de terminaison de l'API.

### Contact

Pour toute question, veuillez contacter [EMAIL].


## Création d'un bot Python pour StackOverflow

| Tags |
|------|
| `Python` `API` `StackOverflow` `requests` `JSON` |

Pour créer un bot Python qui interagit avec l'API de StackOverflow pour récupérer des questions et des réponses autour d'un sujet donné, les bibliothèques <code>requests</code> pour les requêtes HTTP et <code>json</code> pour traiter les réponses JSON sont utilisées. Voici un exemple de script :

1.  Installer la bibliothèque <code>requests</code> :

```bash
pip install requests
```

2.  Écrire le script Python :

```python
import requests
import json

def fetch_stackoverflow_questions(topic, tag):
    url = f'https://api.stackexchange.com/2.3/search/advanced'
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': topic,
        'tagged': tag,
        'site': 'stackoverflow',
        'filter': 'withbody'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error fetching data from StackOverflow API: {response.status_code}")
        return None

def display_questions(questions):
    for question in questions:
        print(f"Title: {question['title']}")
        print(f"Link: {question['link']}")
        print(f"Score: {question['score']}")
        print(f"Is answered: {'Yes' if question['is_answered'] else 'No'}")
        print("----")

def main():
    topic = input("Enter the topic you are interested in: ")
    tag = input("Enter the tag to filter questions: ")
    questions = fetch_stackoverflow_questions(topic, tag)

    if questions:
        display_questions(questions)
    else:
        print("No questions found.")

if __name__ == "__main__":
    main()
```


## Description des Fonctions du Script

| Tags |
|------|
| `API` `StackOverflow` `Fonctions` |

<ol>
<li>
<p><strong>fetch_stackoverflow_questions(topic, tag)</strong> : Cette fonction interroge l'API StackOverflow pour récupérer les questions correspondant à un sujet et un tag spécifiés. Les paramètres de la requête sont configurés pour trier les résultats par pertinence et inclure le corps des questions.</p>
</li>
<li>
<p><strong>display_questions(questions)</strong> : Cette fonction affiche les informations clés des questions retournées par l'API, notamment le titre, le lien, le score et l'état de la réponse.</p>
</li>
<li>
<p><strong>main()</strong> : Cette fonction constitue le point d'entrée du script. Elle invite l'utilisateur à saisir un sujet et un tag, appelle la fonction de recherche et affiche les résultats.</p>
</li>
</ol>


## Instructions d'utilisation du script

| Tags |
|------|
| `script` `instructions` `python` |

1.  Exécutez le script.
2.  Entrez un sujet (par exemple, "Python").
3.  Entrez un tag pour filtrer les questions (par exemple, "pandas").

Ce script est un point de départ et peut être amélioré de plusieurs manières, par exemple en ajoutant une gestion des erreurs plus robuste, en filtrant les résultats pour inclure seulement les questions avec des réponses acceptées, ou en stockant les résultats dans un fichier pour une analyse ultérieure.


## Génération de PDF de Questions Stack Overflow

| Tags |
|------|
| `Python` `fpdf2` `Stack Overflow API` `PDF generation` |

Pour copier les questions et réponses dans un PDF avec une mise en page agréable, nous allons utiliser la bibliothèque <code>fpdf2</code> pour générer le PDF en Python. Voici un exemple de script complet qui inclut cette fonctionnalité.

<ol>
<li>Installez les bibliothèques nécessaires :</li>
</ol>
<pre><code class="language-bash">pip install requests fpdf2
</code></pre>
<ol start="2">
<li>Écrivez le script Python :</li>
</ol>
<pre><code class="language-python">import requests
import json
from fpdf import FPDF

def fetch_stackoverflow_questions(topic, tag):
    url = f&#x27;https://api.stackexchange.com/2.3/search/advanced&#x27;
    params = {
        &#x27;order&#x27;: &#x27;desc&#x27;,
        &#x27;sort&#x27;: &#x27;relevance&#x27;,
        &#x27;q&#x27;: topic,
        &#x27;tagged&#x27;: tag,
        &#x27;site&#x27;: &#x27;stackoverflow&#x27;,
        &#x27;filter&#x27;: &#x27;withbody&#x27;
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data[&#x27;items&#x27;]
    else:
        print(f&quot;Error fetching data from StackOverflow API: {response.status_code}&quot;)
        return None

def fetch_answers(question_id):
    url = f&#x27;https://api.stackexchange.com/2.3/questions/{question_id}/answers&#x27;
    params = {
        &#x27;order&#x27;: &#x27;desc&#x27;,
        &#x27;sort&#x27;: &#x27;activity&#x27;,
        &#x27;site&#x27;: &#x27;stackoverflow&#x27;,
        &#x27;filter&#x27;: &#x27;withbody&#x27;
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data[&#x27;items&#x27;]
    else:
        print(f&quot;Error fetching answers from StackOverflow API: {response.status_code}&quot;)
        return None

def generate_pdf(questions):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.add_page()
    pdf.set_font(&quot;Arial&quot;, size=12)

    for question in questions:
        pdf.set_font(&quot;Arial&quot;, &#x27;B&#x27;, size=14)
        pdf.cell(200, 10, txt=question[&#x27;title&#x27;], ln=True, align=&#x27;L&#x27;)
        
        pdf.set_font(&quot;Arial&quot;, size=12)
        pdf.multi_cell(0, 10, txt=question[&#x27;body&#x27;])
        pdf.ln()

        answers = fetch_answers(question[&#x27;question_id&#x27;])
        if answers:
            pdf.set_font(&quot;Arial&quot;, &#x27;I&#x27;, size=12)
            pdf.cell(200, 10, txt=&quot;Answers:&quot;, ln=True, align=&#x27;L&#x27;)
            pdf.set_font(&quot;Arial&quot;, size=12)
            for answer in answers:
                pdf.multi_cell(0, 10, txt=answer[&#x27;body&#x27;])
                pdf.ln()
        
        pdf.add_page()

    pdf.output(&quot;StackOverflow_Questions_and_Answers.pdf&quot;)

def main():
    topic = input(&quot;Enter the topic you are interested in: &quot;)
    tag = input(&quot;Enter the tag to filter questions: &quot;)
    questions = fetch_stackoverflow_questions(topic, tag)

    if questions:
        generate_pdf(questions)
        print(&quot;PDF generated successfully.&quot;)
    else:
        print(&quot;No questions found.&quot;)

if __name__ == &quot;__main__&quot;:
    main()
</code></pre>


## Description des fonctions

| Tags |
|------|
| `Python` `StackOverflow` `PDF` |

<ol>
<li><strong>fetch_stackoverflow_questions(topic, tag)</strong> : Cette fonction récupère les questions StackOverflow correspondant à un sujet et un tag spécifiés. Elle est similaire à la version précédente.</li>
<li><strong>fetch_answers(question_id)</strong> : Cette fonction récupère les réponses associées à une question donnée, identifiée par son ID.</li>
<li><strong>generate_pdf(questions)</strong> : Cette fonction génère un fichier PDF contenant les questions et leurs réponses. Elle utilise la bibliothèque <code>FPDF</code> pour la création du PDF, insère une nouvelle page pour chaque question et inclut les réponses sous chaque question.</li>
<li><strong>main()</strong> : Point d'entrée du script. Il invite l'utilisateur à saisir un sujet et un tag, appelle la fonction de recherche et génère le PDF contenant les résultats.</li>
</ol>


## Utilisation du script

| Tags |
|------|
| `script` `Python` `PDF` |

Exécutez le script. Entrez un sujet (par exemple, "Python"). Entrez un tag pour filtrer les questions (par exemple, "pandas").

Ce script génère un fichier PDF nommé <code>StackOverflow_Questions_and_Answers.pdf</code> dans le répertoire courant, avec une mise en page basique mais fonctionnelle. Personnalisez la mise en page en utilisant les fonctionnalités de <code>FPDF</code> pour ajuster les polices, les tailles, les marges, etc.


## Envoyer un fichier par email avec Python

| Tags |
|------|
| `Python` `smtplib` `email` `PDF` |

Pour envoyer le PDF généré par email via Gmail, la bibliothèque <code>smtplib</code> est utilisée pour l'envoi et la bibliothèque <code>email</code> pour construire le message avec la pièce jointe. Assurez-vous d'avoir activé l'accès aux applications moins sécurisées pour votre compte Gmail, ou utilisez un mot de passe d'application pour plus de sécurité.

Voici comment modifier le script pour envoyer le PDF par email après l'avoir généré :

1.  Installez les bibliothèques nécessaires si ce n'est pas déjà fait :

```bash
pip install requests fpdf
```

2.  Écrivez le script Python :

```python
import requests
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def fetch_stackoverflow_questions(topic, tag):
    url = f'https://api.stackexchange.com/2.3/search/advanced'
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': topic,
        'tagged': tag,
        'site': 'stackoverflow',
        'filter': 'withbody'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error fetching data from StackOverflow API: {response.status_code}")
        return None

def fetch_answers(question_id):
    url = f'https://api.stackexchange.com/2.3/questions/{question_id}/answers'
    params = {
        'order': 'desc',
        'sort': 'activity',
        'site': 'stackoverflow',
        'filter': 'withbody'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error fetching answers from StackOverflow API: {response.status_code}")
        return None

def generate_pdf(questions, pdf_filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for question in questions:
        pdf.set_font("Arial", 'B', size=14)
        pdf.cell(200, 10, txt=question['title'], ln=True, align='L')
        
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=question['body'])
        pdf.ln()

        answers = fetch_answers(question['question_id'])
        if answers:
            pdf.set_font("Arial", 'I', size=12)
            pdf.cell(200, 10, txt="Answers:", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for answer in answers:
                pdf.multi_cell(0, 10, txt=answer['body'])
                pdf.ln()
        
        pdf.add_page()

    pdf.output(pdf_filename)

def send_email(pdf_filename, sender_email, sender_password, receiver_email):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "StackOverflow Questions and Answers PDF"

    body = "Please find the attached PDF file containing the StackOverflow questions and answers."
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(pdf_filename)}")

        msg.attach(part)

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def main():
    topic = input("Enter the topic you are interested in: ")
    tag = input("Enter the tag to filter questions: ")
    sender_email = input("Enter your Gmail address: ")
    sender_password = input("Enter your Gmail password: ")
    receiver_email = input("Enter the receiver's email address: ")

    questions = fetch_stackoverflow_questions(topic, tag)
    pdf_filename = "StackOverflow_Questions_and_Answers.pdf"

    if questions:
        generate_pdf(questions, pdf_filename)
        send_email(pdf_filename, sender_email, sender_password, receiver_email)
        print("PDF generated and email sent successfully.")
    else:
        print("No questions found.")

if __name__ == "__main__":
    main()
```


## Fonctionnement du script

| Tags |
|------|
| `Python` `Stack Overflow` `PDF` `Email` |

<ol>
<li><strong>fetch_stackoverflow_questions(topic, tag)</strong> et <strong>fetch_answers(question_id)</strong> : Ces fonctions extraient les questions et les réponses de StackOverflow.</li>
<li><strong>generate_pdf(questions, pdf_filename)</strong> : Cette fonction génère le fichier PDF contenant les questions et les réponses.</li>
<li><strong>send_email(pdf_filename, sender_email, sender_password, receiver_email)</strong> : Cette fonction envoie un email avec le PDF en pièce jointe via le serveur SMTP de Gmail.</li>
<li><strong>main()</strong> : Point d'entrée du script. Il collecte les informations utilisateur, génère le PDF et envoie l'email.</li>
</ol>


## Utilisation du script

| Tags |
|------|
| `script` `Python` `PDF` `email` |

1.  Exécutez le script.
2.  Entrez un sujet (par exemple, "Python").
3.  Entrez un tag pour filtrer les questions (par exemple, "pandas").
4.  Entrez votre adresse Gmail: [EMAIL].
5.  Entrez votre mot de passe Gmail.
6.  Entrez l'adresse email du destinataire.

Le script génère un fichier PDF nommé `StackOverflow_Questions_and_Answers.pdf` et l'envoie par email à l'adresse spécifiée. Pour des raisons de sécurité, il est recommandé d'utiliser un mot de passe d'application plutôt que votre mot de passe principal de Gmail.


## Utiliser les "Mots de passe d'application" Google

| Tags |
|------|
| `Python` `Gmail` `smtplib` `2FA` `Sécurité` |

Avec la double authentification (2FA) activée sur votre compte Google, l'utilisation de votre mot de passe principal pour les connexions via des applications tierces comme `smtplib` ne fonctionnera pas. Google propose une solution sécurisée appelée "Mots de passe d'application" qui permet de générer des mots de passe spécifiques pour les applications tierces.

Voici comment procéder pour envoyer un e-mail en utilisant un mot de passe d'application :

1.  **Générer un mot de passe d'application** :

    *   Allez sur la page de votre compte Google : [https://myaccount.google.com/](https://myaccount.google.com/).
    *   Cliquez sur "Sécurité" dans le menu de gauche.
    *   Sous "Se connecter à Google", cliquez sur "Mots de passe des applications".
    *   Sélectionnez l'application et l'appareil pour lequel vous souhaitez générer un mot de passe (par exemple, "Mail" et "Ordinateur Windows").
    *   Cliquez sur "Générer" et copiez le mot de passe fourni.
2.  **Utiliser le mot de passe d'application dans votre script Python** :

    *   Remplacez l'étape où vous demandez le mot de passe par l'utilisation du mot de passe d'application généré.

Voici le script complet mis à jour :

```python
import requests
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def fetch_stackoverflow_questions(topic, tag):
    url = f'https://api.stackexchange.com/2.3/search/advanced'
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': topic,
        'tagged': tag,
        'site': 'stackoverflow',
        'filter': 'withbody'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error fetching data from StackOverflow API: {response.status_code}")
        return None

def fetch_answers(question_id):
    url = f'https://api.stackexchange.com/2.3/questions/{question_id}/answers'
    params = {
        'order': 'desc',
        'sort': 'activity',
        'site': 'stackoverflow',
        'filter': 'withbody'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error fetching answers from StackOverflow API: {response.status_code}")
        return None

def generate_pdf(questions, pdf_filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for question in questions:
        pdf.set_font("Arial", 'B', size=14)
        pdf.cell(200, 10, txt=question['title'], ln=True, align='L')

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=question['body'])
        pdf.ln()

        answers = fetch_answers(question['question_id'])
        if answers:
            pdf.set_font("Arial", 'I', size=12)
            pdf.cell(200, 10, txt="Answers:", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for answer in answers:
                pdf.multi_cell(0, 10, txt=answer['body'])
                pdf.ln()

        pdf.add_page()

    pdf.output(pdf_filename)

def send_email(pdf_filename, sender_email, app_password, receiver_email):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "StackOverflow Questions and Answers PDF"

    body = "Please find the attached PDF file containing the StackOverflow questions and answers."
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(pdf_filename)}")

        msg.attach(part)

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def main():
    topic = input("Enter the topic you are interested in: ")
    tag = input("Enter the tag to filter questions: ")
    sender_email = input("Enter your Gmail address: ")
    app_password = input("Enter your Gmail app password: ")
    receiver_email = input("Enter the receiver's email address: ")

    questions = fetch_stackoverflow_questions(topic, tag)
    pdf_filename = "StackOverflow_Questions_and_Answers.pdf"

    if questions:
        generate_pdf(questions, pdf_filename)
        send_email(pdf_filename, sender_email, app_password, receiver_email)
        print("PDF generated and email sent successfully.")
    else:
        print("No questions found.")

if __name__ == "__main__":
    main()
```


## Utilisation du script

| Tags |
|------|
| `Python` `Gmail` `Script` `PDF` `Email` |

1.  Générez un mot de passe d'application pour Gmail en suivant les étapes.
2.  Exécutez le script.
3.  Entrez un sujet (par exemple, "Python").
4.  Entrez un tag pour filtrer les questions (par exemple, "pandas").
5.  Entrez votre adresse Gmail : [EMAIL].
6.  Entrez le mot de passe d'application généré.
7.  Entrez l'adresse email du destinataire.

Le script génère un fichier PDF nommé `StackOverflow_Questions_and_Answers.pdf` et l'envoie par email à l'adresse spécifiée. L'utilisation d'un mot de passe d'application garantit la sécurité de l'envoi d'emails, même avec la double authentification activée sur votre compte Google.


## Suivi des articles StackOverflow et filtrage

| Tags |
|------|
| `Python` `API` `StackOverflow` `email` `PDF` |

Pour améliorer le script afin de garder une trace des articles envoyés et éviter les doublons, ainsi que pour envoyer uniquement les questions ayant au moins 2 réponses, nous allons faire les ajustements suivants :

<ol>
<li>Utiliser un fichier pour stocker les identifiants des questions déjà envoyées.</li>
<li>Filtrer les questions pour inclure seulement celles qui ont au moins 2 réponses.</li>
</ol>

Voici comment vous pouvez procéder :

<ol>
<li>Créez un fichier <code>sent_questions.txt</code> pour garder une trace des questions envoyées.</li>
<li>Modifiez le script pour lire et écrire dans ce fichier, et pour filtrer les questions.</li>
</ol>

Voici le script mis à jour :

```python
import requests
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def fetch_stackoverflow_questions(topic, tag):
    url = f'https://api.stackexchange.com/2.3/search/advanced'
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': topic,
        'tagged': tag,
        'site': 'stackoverflow',
        'filter': 'withbody'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error fetching data from StackOverflow API: {response.status_code}")
        return None

def fetch_answers(question_id):
    url = f'https://api.stackexchange.com/2.3/questions/{question_id}/answers'
    params = {
        'order': 'desc',
        'sort': 'activity',
        'site': 'stackoverflow',
        'filter': 'withbody'
    }

    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error fetching answers from StackOverflow API: {response.status_code}")
        return None

def generate_pdf(questions, pdf_filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for question in questions:
        pdf.set_font("Arial", 'B', size=14)
        pdf.cell(200, 10, txt=question['title'], ln=True, align='L')
        
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=question['body'])
        pdf.ln()

        answers = fetch_answers(question['question_id'])
        if answers:
            pdf.set_font("Arial", 'I', size=12)
            pdf.cell(200, 10, txt="Answers:", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for answer in answers:
                pdf.multi_cell(0, 10, txt=answer['body'])
                pdf.ln()
        
        pdf.add_page()

    pdf.output(pdf_filename)

def send_email(pdf_filename, sender_email, app_password, receiver_email):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "StackOverflow Questions and Answers PDF"

    body = "Please find the attached PDF file containing the StackOverflow questions and answers."
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(pdf_filename)}")

        msg.attach(part)

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def read_sent_questions(file_path):
    if not os.path.exists(file_path):
        return set()
    with open(file_path, 'r') as file:
        return set(file.read().splitlines())

def write_sent_questions(file_path, question_ids):
    with open(file_path, 'a') as file:
        for question_id in question_ids:
            file.write(f"{question_id}\n")

def filter_questions(questions, sent_questions):
    filtered_questions = []
    new_question_ids = []
    for question in questions:
        if question['question_id'] not in sent_questions and question['answer_count'] >= 2:
            filtered_questions.append(question)
            new_question_ids.append(question['question_id'])
    return filtered_questions, new_question_ids

def main():
    topic = input("Enter the topic you are interested in: ")
    tag = input("Enter the tag to filter questions: ")
    sender_email = input("Enter your Gmail address: ")
    app_password = input("Enter your Gmail app password: ")
    receiver_email = input("Enter the receiver's email address: ")

    sent_questions_file = "sent_questions.txt"
    sent_questions = read_sent_questions(sent_questions_file)

    questions = fetch_stackoverflow_questions(topic, tag)
    pdf_filename = "StackOverflow_Questions_and_Answers.pdf"

    if questions:
        filtered_questions, new_question_ids = filter_questions(questions, sent_questions)
        if filtered_questions:
            generate_pdf(filtered_questions, pdf_filename)
            send_email(pdf_filename, sender_email, app_password, receiver_email)
            write_sent_questions(sent_questions_file, new_question_ids)
            print("PDF generated and email sent successfully.")
        else:
            print("No new questions to send.")
    else:
        print("No questions found.")

if __name__ == "__main__":
    main()
```


## Fonctions principales et mises à jour
| Tags |
|------|
| `Python` `Fonctions` `Filtrage` `Fichiers` |

<ol>
<li><strong>read_sent_questions(file_path)</strong> : Cette fonction lit les identifiants des questions déjà envoyées depuis un fichier.</li>
<li><strong>write_sent_questions(file_path, question_ids)</strong> : Cette fonction écrit les nouveaux identifiants des questions envoyées dans un fichier.</li>
<li><strong>filter_questions(questions, sent_questions)</strong> : Cette fonction filtre les questions pour inclure seulement celles qui n'ont pas encore été envoyées et qui ont au moins 2 réponses.</li>
<li><strong>main()</strong> : La fonction principale a été mise à jour pour utiliser les nouvelles fonctions de lecture et d'écriture des questions envoyées, et pour filtrer les questions avant de générer le PDF et d'envoyer l'email.</li>
</ol>


## Guide d'utilisation du script

| Tags |
|------|
| `script` `Python` `email` `PDF` |

1.  Créer un fichier nommé <code>sent_questions.txt</code> dans le même répertoire que le script.

2.  Exécuter le script.

3.  Saisir un sujet (ex: &quot;Python&quot;).

4.  Saisir un tag de filtrage (ex: &quot;pandas&quot;).

5.  Saisir votre adresse Gmail : [EMAIL].

6.  Saisir le mot de passe d'application généré.

7.  Saisir l'adresse email du destinataire.

Ce script génère un fichier PDF nommé <code>StackOverflow_Questions_and_Answers.pdf</code>, envoie un email avec le PDF en pièce jointe et enregistre les questions envoyées pour éviter les doublons.


## Suivi des articles envoyés et des réponses

| Tags |
|------|
| `Python` `JSON` `Stack Overflow` |

Pour assurer le suivi des articles envoyés, du nombre de réponses et pour renvoyer les articles mis à jour en cas de nouvelles réponses, un mécanisme de suivi et de mise à jour des réponses est nécessaire. Voici les étapes à suivre :

1.  **Utilisation d'un fichier JSON** pour stocker les articles envoyés et le nombre de leurs réponses.
2.  **Mise à jour du script** pour lire et écrire dans ce fichier JSON.
3.  **Renvoi de l'article** si le nombre de réponses a augmenté.

Le script mis à jour est présenté ci-dessous :

```python
import requests
from fpdf import FPDF
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import json

def fetch_stackoverflow_questions(topic, tag):
    url = f'https://api.stackexchange.com/2.3/search/advanced'
    params = {
        'order': 'desc',
        'sort': 'relevance',
        'q': topic,
        'tagged': tag,
        'site': 'stackoverflow',
        'filter': 'withbody'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error fetching data from StackOverflow API: {response.status_code}")
        return None

def fetch_answers(question_id):
    url = f'https://api.stackexchange.com/2.3/questions/{question_id}/answers'
    params = {
        'order': 'desc',
        'sort': 'activity',
        'site': 'stackoverflow',
        'filter': 'withbody'
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data['items']
    else:
        print(f"Error fetching answers from StackOverflow API: {response.status_code}")
        return None

def generate_pdf(questions, pdf_filename):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for question in questions:
        pdf.set_font("Arial", 'B', size=14)
        pdf.cell(200, 10, txt=question['title'], ln=True, align='L')

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=question['body'])
        pdf.ln()

        answers = fetch_answers(question['question_id'])
        if answers:
            pdf.set_font("Arial", 'I', size=12)
            pdf.cell(200, 10, txt="Answers:", ln=True, align='L')
            pdf.set_font("Arial", size=12)
            for answer in answers:
                pdf.multi_cell(0, 10, txt=answer['body'])
                pdf.ln()

        pdf.add_page()

    pdf.output(pdf_filename)

def send_email(pdf_filename, sender_email, app_password, receiver_email):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "StackOverflow Questions and Answers PDF"

    body = "Please find the attached PDF file containing the StackOverflow questions and answers."
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF file
    with open(pdf_filename, "rb") as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {os.path.basename(pdf_filename)}")

        msg.attach(part)

    # Send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, app_password)
    text = msg.as_string()
    server.sendmail(sender_email, receiver_email, text)
    server.quit()

def read_sent_questions(file_path):
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as file:
        return json.load(file)

def write_sent_questions(file_path, sent_questions):
    with open(file_path, 'w') as file:
        json.dump(sent_questions, file, indent=4)

def filter_questions(questions, sent_questions):
    filtered_questions = []
    new_sent_questions = sent_questions.copy()

    for question in questions:
        question_id = str(question['question_id'])
        if question_id not in sent_questions and question['answer_count'] >= 2:
            filtered_questions.append(question)
            new_sent_questions[question_id] = question['answer_count']
        elif question_id in sent_questions and question['answer_count'] > sent_questions[question_id]:
            filtered_questions.append(question)
            new_sent_questions[question_id] = question['answer_count']

    return filtered_questions, new_sent_questions

def main():
    topic = input("Enter the topic you are interested in: ")
    tag = input("Enter the tag to filter questions: ")
    sender_email = input("Enter your Gmail address: ")
    app_password = input("Enter your Gmail app password: ")
    receiver_email = input("Enter the receiver's email address: ")

    sent_questions_file = "sent_questions.json"
    sent_questions = read_sent_questions(sent_questions_file)

    questions = fetch_stackoverflow_questions(topic, tag)
    pdf_filename = "StackOverflow_Questions_and_Answers.pdf"

    if questions:
        filtered_questions, new_sent_questions = filter_questions(questions, sent_questions)
        if filtered_questions:
            generate_pdf(filtered_questions, pdf_filename)
            send_email(pdf_filename, sender_email, app_password, receiver_email)
            write_sent_questions(sent_questions_file, new_sent_questions)
            print("PDF generated and email sent successfully.")
        else:
            print("No new questions to send.")
    else:
        print("No questions found.")

if __name__ == "__main__":
    main()
```


## Fonctionnalités principales du programme

| Tags |
|------|
| `Python` `JSON` `Fonctions` `Filtrage` |

<ol>
<li><strong>read_sent_questions(file_path)</strong> et <strong>write_sent_questions(file_path, sent_questions)</strong> : Ces fonctions gèrent la lecture et l'écriture dans un fichier JSON. Elles sont utilisées pour persister les identifiants des questions envoyées ainsi que le nombre de réponses.</li>
<li><strong>filter_questions(questions, sent_questions)</strong> : Cette fonction filtre les questions en fonction de leur statut. Elle sélectionne les questions qui n'ont pas encore été envoyées ou celles pour lesquelles de nouvelles réponses sont disponibles.</li>
<li><strong>main()</strong> : La fonction principale est mise à jour pour intégrer la lecture et l'écriture dans le fichier JSON, ainsi que l'utilisation du mécanisme de filtrage.</li>
</ol>


## Instructions d'utilisation du script

| Tags |
|------|
| `script` `JSON` `PDF` `email` |

1.  Créer un fichier JSON nommé <code>sent_questions.json</code> dans le même répertoire que le script.
2.  Exécuter le script.
3.  Saisir un sujet (ex : "Python").
4.  Saisir un tag pour filtrer les questions (ex : "pandas").
5.  Saisir l'adresse Gmail : [EMAIL].
6.  Saisir le mot de passe d'application généré.
7.  Saisir l'adresse email du destinataire.

Le script génère un fichier PDF nommé <code>StackOverflow_Questions_and_Answers.pdf</code>, envoie un email avec le PDF en pièce jointe, et enregistre les questions envoyées ainsi que leur nombre de réponses. L'objectif est d'éviter les doublons et de renvoyer les articles mis à jour en cas de nouvelles réponses.
