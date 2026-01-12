## Proxy Inverse avec Python Flask

| Tags |
|------|
| `Python` `Flask` `Proxy Inverse` |

Le proxy inverse est implémenté en Python avec Flask.

Voici la structure du code :

```python
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def proxy(path):
    # Construction de l'URL cible
    target_url = f'http://[IP]/{path}'
    if request.query_string:
        target_url += '?' + request.query_string.decode('utf-8')

    # Envoi de la requête au serveur cible
    try:
        response = requests.request(
            method=request.method,
            url=target_url,
            headers=request.headers,
            data=request.get_data(),
            verify=False  # Désactiver la vérification SSL (pour les tests)
        )
    except requests.exceptions.RequestException as e:
        return str(e), 500

    # Retour de la réponse du serveur cible
    return response.content, response.status_code, response.headers.items()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Explication :

1.  **Import des librairies :** Flask et requests.
2.  **Initialisation de l'application Flask :** `app = Flask(__name__)`.
3.  **Définition de la route principale :** `@app.route('/', defaults={'path': ''})` et `@app.route('/<path:path>')`. Cette configuration intercepte toutes les requêtes.
4.  **Construction de l'URL cible :** L'URL cible est construite en combinant l'adresse IP et le chemin de la requête. Les paramètres de requête sont également inclus.
5.  **Envoi de la requête au serveur cible :** La requête est envoyée en utilisant la librairie `requests`.  `verify=False` est utilisé pour désactiver la vérification SSL (uniquement pour les tests et non recommandé en production).
6.  **Gestion des erreurs :** Un bloc `try...except` gère les exceptions `requests.exceptions.RequestException`.
7.  **Retour de la réponse :** La réponse du serveur cible est renvoyée au client.
8.  **Démarrage de l'application :** L'application est démarrée en mode debug, accessible sur toutes les interfaces, et écoutant sur le port 5000.

Pour exécuter le code :

1.  **Enregistrez** le code dans un fichier (par exemple, `proxy.py`).
2.  **Installez** les librairies nécessaires : `pip install flask requests`.
3.  **Exécutez** le script : `python proxy.py`.

L'application est maintenant en cours d'exécution et sert de proxy inverse pour l'adresse [IP]. Toutes les requêtes envoyées à l'application sont redirigées vers le serveur cible.


## Reverse Proxy Python

| Tags |
|------|
| `Python` `Reverse Proxy` `HTTP` `Redirection` |

Voici un script Python pour créer un reverse proxy simple :

```python
from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import urllib.request
import urllib.parse
import ssl

class ProxyHandler(BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'

    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()

    def handle_request(self):
        try:
            url, port = self.determine_target()
            if not url or not port:
                self.send_error(404, 'Not Found')
                return

            # Construire l'URL cible
            target_url = f'http://{url}:{port}{self.path}'

            # Ajouter les paramètres de requête
            if self.command == 'POST':
                content_length = int(self.headers['Content-Length'])
                post_data = self.rfile.read(content_length)
                req = urllib.request.Request(target_url, data=post_data, method=self.command)
            else:
                req = urllib.request.Request(target_url, method=self.command)

            # Transférer les headers
            for header, value in self.headers.items():
                if header not in ('Host', 'Content-Length'):
                    req.add_header(header, value)

            # Effectuer la requête vers le serveur cible
            with urllib.request.urlopen(req) as response:
                # Transférer les headers de la réponse
                self.send_response(response.status)
                for header, value in response.getheaders():
                    self.send_header(header, value)
                self.end_headers()

                # Transférer le corps de la réponse
                self.wfile.write(response.read())

        except Exception as e:
            self.send_error(500, f'Internal Server Error: {e}')
            print(f"Erreur : {e}")

    def determine_target(self):
        if self.path.startswith('/app1'):
            return '127.0.0.1', 5000
        elif self.path.startswith('/app2'):
            return '127.0.0.1', 5001
        else:
            return None, None

def run(server_class=HTTPServer, handler_class=ProxyHandler, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Démarrage du proxy sur le port {port}...')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
```

Ce script utilise le module `http.server` de Python pour créer un serveur HTTP.  `ProxyHandler` gère les requêtes. `determine_target` mappe les chemins vers les serveurs backend. Les requêtes sont transférées en utilisant `urllib.request`.  Les requêtes GET et POST sont gérées.  Le script est exécuté sur le port 80 par défaut.

Pour l'exécuter:

1.  Sauvegarder le code dans un fichier (ex: `proxy.py`).
2.  Exécuter avec `python proxy.py`.

Pour tester :

*   Assurez-vous que les applications sur les ports 5000 et 5001 sont en cours d'exécution.
*   Accédez à `http://127.0.0.1/app1/quelquechose` et `http://127.0.0.1/app2/quelquechose` dans votre navigateur.
*   Les requêtes seront redirigées vers les applications correspondantes.


## Création d'un Reverse Proxy avec Python et Flask

| Tags |
|------|
| `Python` `Flask` `Reverse Proxy` `HTTP` |

Créer un reverse proxy en Python pour rediriger les requêtes vers différents ports est un excellent exercice pratique pour renforcer vos compétences en programmation réseau. Nous utiliserons <code>Flask</code> pour le serveur web et <code>requests</code> pour gérer les requêtes HTTP.

Voici les étapes pour créer un reverse proxy simple :

<ol>
<li>
<strong>Installer Flask et requests</strong> : Si vous ne les avez pas déjà installés, vous pouvez le faire via pip :
<pre><code class="language-bash">pip install flask requests
</code></pre>
</li>
<li>
<strong>Créer un fichier Python pour le serveur proxy</strong> : Dans ce fichier, nous allons définir les routes pour <code>/app1</code> et <code>/app2</code>, et rediriger les requêtes vers les ports appropriés.
</li>
</ol>

Voici un exemple de code pour votre reverse proxy :

<pre><code class="language-python">from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route(&#x27;/app1/&lt;path:path&gt;&#x27;, methods=[&#x27;GET&#x27;, &#x27;POST&#x27;, &#x27;PUT&#x27;, &#x27;DELETE&#x27;])
def proxy_app1(path):
    response = requests.request(
        method=request.method,
        url=f&#x27;http://127.0.0.1:5000/{path}&#x27;,
        headers={key: value for (key, value) in request.headers if key != &#x27;Host&#x27;},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = [&#x27;content-encoding&#x27;, &#x27;content-length&#x27;, &#x27;transfer-encoding&#x27;, &#x27;connection&#x27;]
    headers = [(name, value) for (name, value) in response.raw.headers.items()
               if name.lower() not in excluded_headers]

    return Response(response.content, response.status_code, headers)

@app.route(&#x27;/app2/&lt;path:path&gt;&#x27;, methods=[&#x27;GET&#x27;, &#x27;POST&#x27;, &#x27;PUT&#x27;, &#x27;DELETE&#x27;])
def proxy_app2(path):
    response = requests.request(
        method=request.method,
        url=f&#x27;http://127.0.0.1:5001/{path}&#x27;,
        headers={key: value for (key, value) in request.headers if key != &#x27;Host&#x27;},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False)

    excluded_headers = [&#x27;content-encoding&#x27;, &#x27;content-length&#x27;, &#x27;transfer-encoding&#x27;, &#x27;connection&#x27;]
    headers = [(name, value) for (name, value) in response.raw.headers.items()
               if name.lower() not in excluded_headers]

    return Response(response.content, response.status_code, headers)

if __name__ == &#x27;__main__&#x27;:
    app.run(debug=True)
</code></pre>

Ce code configure deux routes dans Flask, <code>/app1/&lt;path:path&gt;</code> et <code>/app2/&lt;path:path&gt;</code>. Chaque route redirige les requêtes vers le port spécifié (5000 pour app1, 5001 pour app2), en conservant la méthode HTTP, les en-têtes, les données et les cookies. Les en-têtes spécifiques à la transmission HTTP sont exclus pour éviter les conflits.

Pour l'utiliser, exécutez ce script Python et il démarrera un serveur Flask sur le port 5000. Ensuite, vous pouvez accéder à <code>http://127.0.0.1:5000/app1</code> pour interagir avec l'application sur le port 5000, et <code>http://127.0.0.1:5000/app2</code> pour celle sur le port 5001.

Assurez-vous que les applications cibles sont en cours d'exécution sur les ports 5000 et 5001 respectivement.


## Application Flask : Lecture de ports et onglets

| Tags |
|------|
| `Flask` `Python` `Jinja2` `Web application` |

Créer une application Flask qui lit les ports à partir de fichiers de configuration et affiche des onglets pour accéder aux URLs correspondantes est un projet. Ce projet utilise Flask pour le serveur web et Jinja2 pour le rendu du template HTML.

Les étapes pour réaliser ce projet sont les suivantes :

1.  **Structure du projet** : Créez un répertoire pour votre projet et ajoutez-y des fichiers de configuration pour les ports (ex: `app1.conf` et `app2.conf`).
2.  **Fichiers de configuration** : Chaque fichier de configuration contient un numéro de port (ex: `app1.conf` contient `5000` et `app2.conf` contient `5001`).
3.  **Lecture des fichiers de configuration** : L'application Flask lit ces fichiers pour obtenir les numéros de port.
4.  **Rendu des onglets dans une page HTML** : Utilisez Jinja2 pour créer une page avec des onglets qui redirigent vers les URLs correspondantes.

Voici un exemple de code pour l'application Flask :

```python
from flask import Flask, render_template
import os

app = Flask(__name__)

def read_port_from_conf(file_name):
    with open(file_name, 'r') as file:
        return file.read().strip()

@app.route('/')
def index():
    port1 = read_port_from_conf('app1.conf')
    port2 = read_port_from_conf('app2.conf')
    url1 = f'http://127.0.0.1:{port1}'
    url2 = f'http://127.0.0.1:{port2}'
    return render_template('index.html', url1=url1, url2=url2)

if __name__ == '__main__':
    app.run(debug=True)
```

Pour le fichier `index.html`, placez-le dans un dossier nommé `templates` à la racine de votre projet Flask. Voici un exemple de ce fichier :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>App Links</title>
</head>
<body>
    <h1>Welcome to the App Portal</h1>
    <div>
        <a href="{{ url1 }}" target="_blank">App 1</a> | 
        <a href="{{ url2 }}" target="_blank">App 2</a>
    </div>
</body>
</html>
```

Dans cet exemple, l'application Flask lit les ports à partir des fichiers `app1.conf` et `app2.conf`, puis passe ces informations au template `index.html`. La page affiche deux liens (onglets) qui ouvrent les applications respectives dans de nouveaux onglets du navigateur.

N'oubliez pas de créer les fichiers `app1.conf` et `app2.conf` avec les numéros de port appropriés dans le même répertoire que votre script Flask.


## Configuration dynamique des applications Flask

| Tags |
|------|
| `Flask` `Python` `Configuration` `Jinja2` `Web` |

Pour adapter l'application Flask afin de gérer un nombre variable de fichiers de configuration, modifiez le code pour lire tous les fichiers de configuration d'un répertoire spécifié et créer dynamiquement des onglets pour chaque application.

Suivez les étapes suivantes :

1.  **Structure du projet** : Placez tous vos fichiers de configuration dans un dossier spécifique, par exemple `config`.
2.  **Nommer les fichiers de configuration** : Chaque fichier de configuration doit avoir un format reconnaissable, par exemple, `app1.conf`, `app2.conf`, etc.
3.  **Modifier l'application Flask** : Le code va lire tous les fichiers dans le dossier `config` et stocker les informations dans une structure utilisable pour générer les onglets.

Voici le code modifié :

```python
from flask import Flask, render_template
import os

app = Flask(__name__)

def read_ports_from_conf(directory):
    ports = {}
    for file_name in os.listdir(directory):
        if file_name.endswith('.conf'):
            app_name = file_name.split('.')[0]
            with open(os.path.join(directory, file_name), 'r') as file:
                ports[app_name] = file.read().strip()
    return ports

@app.route('/')
def index():
    ports = read_ports_from_conf('config')
    urls = {app: f'http://127.0.0.1:{port}' for app, port in ports.items()}
    return render_template('index.html', urls=urls)

if __name__ == '__main__':
    app.run(debug=True)
```

Modifiez le fichier `index.html` pour gérer dynamiquement les onglets :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>App Links</title>
</head>
<body>
    <h1>Welcome to the App Portal</h1>
    <div>
        {% for app, url in urls.items() %}
            <a href="{{ url }}" target="_blank">{{ app }}</a> |
        {% endfor %}
    </div>
</body>
</html>
```

Dans cet exemple, le script Python lit tous les fichiers `.conf` du dossier `config` et les stocke dans un dictionnaire. Chaque clé du dictionnaire correspond au nom de l'application et chaque valeur au port lu à partir du fichier de configuration. Le template `index.html` utilise ensuite une boucle Jinja2 pour créer un lien pour chaque application.

Assurez-vous que le dossier `config` existe et qu'il contient les fichiers de configuration nécessaires. Cette approche rend l'application plus flexible et capable de gérer un nombre variable d'applications.


## Intégration de Bootstrap dans Flask : Exemple

| Tags |
|------|
| `Bootstrap` `Flask` `HTML` `CSS` `CDN` |

Pour intégrer Bootstrap à votre application Flask et améliorer l'aspect visuel de votre page avec des onglets, suivez les étapes suivantes. Bootstrap est un framework CSS populaire qui simplifie la création d'interfaces web élégantes et réactives.

1.  **Inclure Bootstrap** : Intégrez Bootstrap à votre projet via son CDN dans le fichier HTML.

2.  **Modifier le fichier HTML** : Utilisez les classes Bootstrap pour structurer la page et les onglets.

Voici le code modifié de `index.html` avec Bootstrap intégré :

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>App Links</title>
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body>
    <div class="container mt-5">
        <h1 class="mb-3">Welcome to the App Portal</h1>
        <ul class="nav nav-tabs">
            {% for app, url in urls.items() %}
                <li class="nav-item">
                    <a class="nav-link" href="{{ url }}" target="_blank">{{ app }}</a>
                </li>
            {% endfor %}
        </ul>
    </div>

    <!-- Bootstrap JS and Popper.js -->
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.4.0/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>
```

Ce code intègre Bootstrap via son CDN. Les onglets sont créés à l'aide des classes de navigation de Bootstrap, ce qui apporte un style élégant et fonctionnel aux liens.

Votre application Flask reste inchangée. Elle lit les fichiers de configuration et transmet les URLs au template HTML, qui les affiche sous forme d'onglets grâce à Bootstrap.

Assurez-vous d'avoir une connexion Internet active pour charger les fichiers CSS et JS de Bootstrap depuis leur CDN. Cela améliorera significativement l'apparence et la convivialité de votre application web.


## Définir le port d'écoute d'une application Flask

| Tags |
|------|
| `Flask` `Python` `Web server` `port` `host` |

Pour définir le port d'écoute d'une application Flask, spécifiez le numéro de port lors du démarrage via la méthode <code>app.run()</code>.  Par exemple, pour écouter sur le port 8080 :

```python
if __name__ == '__main__':
    app.run(port=8080)
```

Par défaut, Flask utilise le port 5000.  L'argument <code>host</code> permet de définir l'adresse IP.  Pour écouter sur toutes les interfaces, utilisez <code>host='0.0.0.0'</code> :

```python
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
```

En production, Flask est généralement déployé derrière un serveur web tel que Gunicorn ou uWSGI, qui configure le port et l'adresse IP.
