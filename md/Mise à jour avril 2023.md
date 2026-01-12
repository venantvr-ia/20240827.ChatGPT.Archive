## Mise à jour – Avril 2023

| Tags |
|------|
| `mise à jour` `version` `documentation` |


## Date de la dernière mise à jour

| Tags |
|------|
| `mise à jour` `date` `information` |

Ma dernière mise à jour date d'avril 2023.


## Aspects Techniques de l'Architecture

| Tags |
|------|
| `GPT-4` `OpenAI` `Modèle de langage` |

Techniquement, l'architecture repose sur le modèle GPT-4 d'OpenAI. Le modèle est conçu pour la compréhension et la génération de texte, utilisant les connaissances acquises jusqu'à la dernière mise à jour en avril 2023. L'accès aux informations et les flux de données après cette date ne sont pas pris en compte.


## Nombre de tokens utilisés

| Tags |
|------|
| `GPT-4` `tokens` `LLM` |

GPT-4, l'architecture sur laquelle je suis basé, peut traiter jusqu'à 4096 tokens par demande. Cela inclut à la fois le texte que l'utilisateur envoie et le texte généré en réponse. Un token peut être un mot, un morceau de mot, ou même de la ponctuation, en fonction de la langue et de la manière dont le modèle a été entraîné à découper le texte en morceaux traitables.


## Débogage Python en tant que root dans PyCharm

| Tags |
|------|
| `PyCharm` `Python` `débogage` `root` `sudo` |

Pour déboguer un script Python en tant qu'utilisateur root dans PyCharm, en particulier sur des systèmes de type Unix où les permissions root sont requises, il est impératif de procéder avec prudence afin d'éviter les risques de sécurité. Voici les étapes générales :

1.  **Configurer un interpréteur Python avec les privilèges root :**

    *   Accéder aux paramètres de PyCharm (File &gt; Settings sur Windows ou PyCharm &gt; Preferences sur macOS).
    *   Naviguer vers Project: \[nom de votre projet] &gt; Project Interpreter.
    *   Cliquer sur le rouage à côté de l'interpréteur actuel et sélectionner "Add".
    *   Dans la boîte de dialogue, il est possible d'ajouter un nouvel interpréteur Python exécuté en tant que superutilisateur. Cela peut se faire via <code>sudo</code> ou en configurant l'interpréteur pour qu'il s'exécute dans un environnement virtuel avec des permissions élevées.
2.  **Modifier la configuration de débogage :**

    *   Accéder à la configuration de débogage (Run &gt; Edit Configurations).
    *   Sélectionner la configuration de votre script.
    *   Dans l'onglet "Configuration" ou similaire, vérifier que l'interpréteur Python approprié, avec les privilèges root, est sélectionné.
3.  **Déboguer en tant que root :**

    *   Le débogage peut maintenant être lancé. PyCharm demandera le mot de passe root si nécessaire.
4.  **Utilisation de 'sudo' pour l'exécution :**

    *   Si le lancement du débogueur avec <code>sudo</code> est requis, on peut créer un script wrapper pour PyCharm ou modifier les paramètres de l'IDE pour lancer le processus de débogage avec <code>sudo</code>. Cette approche peut impliquer des modifications avancées et est généralement déconseillée en raison des implications de sécurité.

**Avertissement :** Déboguer en tant que root présente des risques car cela octroie un accès total au système. Il est conseillé de n'exécuter que du code totalement approuvé avec ces privilèges. De plus, il est crucial d'éviter d'utiliser les privilèges root sauf nécessité absolue et de bien comprendre les implications de sécurité.

Si les scripts nécessitent des privilèges élevés, il est recommandé de minimiser ces exigences autant que possible ou d'utiliser des conteneurs tels que Docker pour isoler l'environnement d'exécution.


## Mocker la commande aircrack-ng

| Tags |
|------|
| `Python` `unittest.mock` `aircrack-ng` `Mocking` |

Si vous apprenez l'éthique du hacking et souhaitez tester ou démontrer une attaque sans capturer de trafic Wi-Fi avec aircrack-ng, vous pouvez simuler des sorties en créant des données fictives, ou en "mockant".

Le "mocking" imite le comportement d'un programme ou d'une fonction dans un environnement contrôlé. En Python, utilisez des bibliothèques comme <code>unittest.mock</code>.

Procédure pour mocker <code>airodump-ng</code> :

1.  **Créer un fichier de sortie simulé :**

    *   Générez un fichier texte imitant la sortie standard d'<code>airodump-ng</code>.
    *   Ce fichier doit contenir les mêmes en-têtes et types de données que la sortie réelle d'<code>airodump-ng</code>.
2.  **Écrire un script de mock :**

    *   Écrivez un script Python qui lit le fichier de sortie simulé et imprime les données comme si elles provenaient d'<code>airodump-ng</code>.
3.  **Utiliser unittest.mock pour mocker l'exécution de la commande :**

    *   Utilisez <code>unittest.mock.patch</code> pour remplacer la méthode d'exécution d'<code>airodump-ng</code> par une fonction retournant le contenu de votre fichier de sortie simulé.

Exemple Python :

```python
import unittest.mock as mock

# Simuler la fonction qui appelle airodump-ng et retourne une sortie
def fake_airodump():
    with open('fake_airodump_output.txt', 'r') as file:
        data = file.read()
    return data

# Utiliser le patcher pour remplacer la fonction réelle par notre fonction factice
with mock.patch('module_containing_function.calling_airodump', new=fake_airodump):
    # Ici, le code qui appelle airodump-ng utilisera notre version factice au lieu de la réelle
    pass
```

Remplacez <code>module_containing_function.calling_airodump</code> par le chemin réel de la fonction à mocker.

Le mocking d'outils comme <code>airodump-ng</code> doit être effectué de manière responsable et légale, uniquement à des fins de tests ou de démonstrations éducatives dans un environnement contrôlé et avec les permissions appropriées.


## Vérification du statut d'airodump-ng en Python

| Tags |
|------|
| `Python` `subprocess` `airodump-ng` `process` |

```python
import subprocess

# Commande pour chercher airodump-ng dans la liste des processus
command = "ps -aux | grep airodump-ng"

# Exécute la commande
process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Récupère la sortie de la commande
stdout, stderr = process.communicate()

# Vérifie si 'airodump-ng' est dans la sortie de la commande
if 'airodump-ng' in str(stdout):
    print("airodump-ng est lancé.")
else:
    print("airodump-ng n'est pas lancé.")
```

Ce script utilise `ps -aux` pour lister les processus et `grep` pour filtrer ceux contenant `airodump-ng`. La présence de `airodump-ng` dans la sortie indique son exécution.

**Avertissement de sécurité :** L'utilisation de `shell=True` dans `subprocess.Popen` peut engendrer des risques si les entrées sont contrôlées par l'utilisateur. Assurez-vous de la sécurité des commandes exécutées.

**Responsabilité :** L'exécution de scripts de ce type nécessite une autorisation préalable sur les réseaux/machines ciblés.


## Mocking d'une commande avec unittest.mock

| Tags |
|------|
| `Python` `unittest.mock` `Mocking` `Tests unitaires` |

Pour simuler le comportement d'une commande, telle que `airodump-ng`, dans un environnement Python, la bibliothèque `unittest.mock` peut être utilisée. L'exemple suivant illustre comment mocker la réponse d'une fonction simulant l'exécution d'`airodump-ng` et vérifier si le processus est en cours :

```python
from unittest.mock import patch

# Cette fonction serait celle qui exécute réellement airodump-ng
def check_airdump_running():
    # Logique pour vérifier si airodump-ng est en cours d'exécution
    # Par exemple, elle pourrait utiliser subprocess pour exécuter &#x27;ps&#x27; ou &#x27;pgrep&#x27;
    pass

# Un exemple de sortie attendue de la fonction si airodump-ng est en cours d&#x27;exécution
mock_airdump_output = b&#x27;airodump-ng  3022 root   18u  IPv4  21603      0t0  WLAN0&#x27;

# Utilisez &#x27;patch&#x27; pour remplacer la sortie de la fonction &#x27;check_airdump_running&#x27;
# avec notre sortie factice à chaque fois qu&#x27;elle est appelée
with patch(&#x27;path.to.your.module.check_airdump_running&#x27;, return_value=mock_airdump_output):

    # Ici, lorsqu&#x27;on appelle &#x27;check_airdump_running&#x27;, elle retournera &#x27;mock_airdump_output&#x27;
    output = check_airdump_running()

    # Puisque nous avons mocké la sortie, nous nous attendons à ce que &#x27;output&#x27; soit &#x27;mock_airdump_output&#x27;
    if b&#x27;airodump-ng&#x27; in output:
        print(&quot;airodump-ng est mocké comme étant en cours d&#x27;exécution.&quot;)
    else:
        print(&quot;airodump-ng n&#x27;est pas en cours d&#x27;exécution.&quot;)
```

Ce code crée un mock pour une fonction hypothétique `check_airdump_running`. `patch` est utilisé pour remplacer la sortie réelle de cette fonction par `mock_airdump_output` lors de son appel.

Remplacez `path.to.your.module.check_airdump_running` par le chemin réel de la fonction à mocker dans votre code.

L'exécution de ce code simule la présence d'`airodump-ng` en cours d'exécution en retournant une sortie définie. Ceci est particulièrement utile pour les tests unitaires, afin de tester le comportement du code sans exécuter de commandes réelles pouvant affecter le système.


## Probe Requests Wi-Fi en Mode Broadcast

| Tags |
|------|
| `Wi-Fi` `Probe Request` `Broadcast` `Réseau` |

Dans le contexte du Wi-Fi, un "probe request" est une requête envoyée par un appareil sans fil pour identifier les réseaux sans fil à proximité. Ces requêtes sont émises par des clients tels que smartphones ou ordinateurs portables lors de la recherche de réseaux disponibles pour la connexion.

Un "probe request" en "mode broadcast" indique que la requête de recherche n'est pas ciblée sur un réseau spécifique. L'appareil émetteur ne spécifie pas de SSID (nom de réseau) particulier auquel se connecter. Il diffuse une requête pour que tous les points d'accès (AP) à portée répondent avec des "probe responses". Cette méthode permet à l'appareil d'identifier tous les réseaux sans fil disponibles.

Ces requêtes peuvent être capturées par des outils de surveillance réseau comme `airodump-ng`, permettant aux pentesters d'identifier les appareils cherchant activement à se connecter et de recueillir des informations sur les réseaux environnants. Elles peuvent également servir dans des attaques comme le "Wi-Fi Pineapple" pour créer des points d'accès malveillants, imitant des réseaux connus en réponse aux requêtes des appareils.


## IMSI Catcher : Faisabilité et considérations éthiques

| Tags |
|------|
| `IMSI` `Sécurité mobile` `Surveillance` `Éthique` |

Un IMSI catcher est un outil de surveillance conçu pour intercepter le trafic des téléphones mobiles en se faisant passer pour une station de base. Il capture l'IMSI (International Mobile Subscriber Identity), un identifiant unique d'abonné.

L'utilisation d'un dispositif Wi-Fi pour capturer directement les IMSI est impossible en raison des protocoles différents utilisés par les réseaux Wi-Fi et cellulaires. Les IMSI sont transmis sur les réseaux cellulaires.

La fabrication et l'utilisation d'IMSI catchers sont illégales dans de nombreuses juridictions, en raison des violations de la vie privée et des lois sur la surveillance. La discussion de tels sujets peut également engendrer des problèmes légaux et éthiques.

Il est essentiel de privilégier l'apprentissage des techniques éthiques de test de pénétration et de respecter les lois locales et internationales, comme le GDPR, régissant la surveillance et la collecte de données.
