## Extension Firefox d'enregistrement HAR

| Tags |
|------|
| `Firefox` `Extension` `HAR` `HTTP Archive` |

L'extension Firefox enregistrant les requêtes HTTP au format HAR est un outil précieux pour le débogage et l'analyse des performances web. Elle capture et enregistre les informations relatives aux requêtes et réponses HTTP, permettant d'identifier les problèmes de performance, les erreurs et d'autres aspects liés au fonctionnement d'une application web.

### Installation et utilisation

1.  **Installation :** L'extension peut être installée directement depuis le navigateur Firefox via le gestionnaire des extensions. Recherchez "HAR export" ou un terme similaire.
2.  **Activation :** Une fois installée, l'extension est généralement accessible via les outils de développement de Firefox (clic droit -> "Inspecter" -> onglet "Réseau").
3.  **Enregistrement :**
    *   Ouvrez les outils de développement et naviguez vers l'onglet "Réseau".
    *   Assurez-vous que l'enregistrement est activé (bouton "enregistrer" ou cercle rouge).
    *   Effectuez les actions que vous souhaitez enregistrer (naviguez sur le site web, etc.).
4.  **Export :** Une fois l'enregistrement terminé, l'extension permet d'exporter les données capturées au format HAR. Cela se fait généralement via un bouton "Exporter" ou une option dans le menu contextuel de l'onglet "Réseau".

### Analyse du fichier HAR

Le fichier HAR résultant est un fichier JSON contenant des informations détaillées sur chaque requête HTTP effectuée par le navigateur. Ces informations incluent :

*   URL de la requête
*   Méthode HTTP (GET, POST, etc.)
*   En-têtes de la requête et de la réponse
*   Corps de la requête et de la réponse (si applicable)
*   Codes de statut HTTP
*   Chronologie des événements (temps de connexion, de transfert, etc.)

Des outils en ligne et des logiciels spécialisés peuvent être utilisés pour analyser le fichier HAR et identifier les problèmes de performance, tels que :

*   Temps de chargement lents
*   Requêtes bloquantes
*   Erreurs HTTP
*   Goulots d'étranglement

### Exemples d'outils d'analyse HAR

*   **Outils en ligne :**
    *   [https://toolbox.googleapps.com/apps/har_analyzer/](https://toolbox.googleapps.com/apps/har_analyzer/)
    *   [https://www.software-testers.com/har-viewer/](https://www.software-testers.com/har-viewer/)
*   **Logiciels :**
    *   Chrome DevTools (possibilité d'importer et d'analyser des fichiers HAR)
    *   Fiddler (outil de débogage HTTP)

### Cas d'utilisation

*   **Débogage des problèmes de performance :** Identifier les requêtes lentes, les ressources bloquantes et optimiser le temps de chargement des pages web.
*   **Identification des erreurs HTTP :** Détecter les codes d'erreur et les problèmes de communication entre le navigateur et le serveur.
*   **Analyse du trafic réseau :** Examiner les requêtes et les réponses pour comprendre le comportement d'une application web.
*   **Collaboration :** Partager les fichiers HAR avec d'autres développeurs ou ingénieurs pour faciliter la résolution des problèmes.

### Sécurité

Il est important de noter que les fichiers HAR peuvent contenir des informations sensibles, telles que :

*   Cookies
*   Mots de passe (si les formulaires sont soumis via HTTP)
*   Données personnelles
*   Informations spécifiques à l'application

**Recommandations de sécurité :**

*   **Examinez attentivement le contenu du fichier HAR avant de le partager.**
*   **Supprimez les informations sensibles avant de partager le fichier.**
*   **Ne partagez pas de fichiers HAR avec des personnes non autorisées.**
*   **Considérez l'utilisation d'un outil d'anonymisation pour masquer les informations sensibles.**

### Exemple de script pour traiter un fichier HAR avec Python

```python
import json

def extraire_url(fichier_har):
    """Extrait les URL de toutes les requêtes du fichier HAR."""
    with open(fichier_har, 'r', encoding='utf-8') as f:
        har_data = json.load(f)

    urls = []
    for entry in har_data['log']['entries']:
        urls.append(entry['request']['url'])
    return urls

if __name__ == '__main__':
    fichier_har = 'exemple.har'  # Remplacez par le nom de votre fichier HAR
    urls = extraire_url(fichier_har)
    for url in urls:
        print(url)
```

Ce script Python simple ouvre un fichier HAR, extrait les URL de toutes les requêtes et les affiche.  Il peut être étendu pour extraire d'autres informations et effectuer des analyses plus complexes.  N'oubliez pas d'installer le module `json` si vous ne l'avez pas déjà : `pip install json`.  Dans un contexte plus large, ce script pourrait être intégré à un processus de test automatisé pour valider le comportement d'une application web.

### Dépannage

*   **L'extension ne capture pas les requêtes :** Vérifiez que l'enregistrement est activé dans les outils de développement.  Assurez-vous que l'extension est correctement installée et activée.  Essayez de redémarrer Firefox.
*   **Problèmes d'export :** Vérifiez que vous avez les permissions nécessaires pour écrire le fichier. Essayez d'exporter le fichier dans un autre répertoire.
*   **Fichier HAR corrompu :** Essayez d'ouvrir le fichier HAR dans un autre outil d'analyse pour vérifier sa validité.  Si le fichier est corrompu, réenregistrez les données.
*   **Erreurs de sécurité :**  Consultez la section "Sécurité" ci-dessus pour des recommandations sur la gestion des informations sensibles.  Si vous suspectez un problème de sécurité, contactez immédiatement [NOM] à [EMAIL].

### Ressources supplémentaires

*   [Documentation officielle de Firefox Developer Tools]([URL_OFFICIELLE_FIREFOX_DEVTOOLS])
*   [Format HAR (HTTP Archive)]([URL_FORMAT_HAR])
*   Articles et tutoriels en ligne sur l'analyse des fichiers HAR (recherches Google)

### Contact

Pour toute question ou assistance, veuillez contacter [NOM] à [EMAIL]. Pour signaler un problème de sécurité, veuillez contacter [NOM] à [EMAIL] ou [NOM] à [EMAIL] ou contacter le support de Firefox.  Pour toute question technique, vous pouvez également consulter la documentation de l'API Firefox.  L'équipe de sécurité peut être contactée à [EMAIL] et le responsable de la sécurité à [EMAIL].  En cas d'attaque, contactez immédiatement [NOM] à [EMAIL] et signalez l'incident au [IP].


## Création d'une extension Firefox

| Tags |
|------|
| `Firefox` `Extension` `JavaScript` `HTML` `CSS` `HAR` |

Creating a Firefox extension involves several steps and requires some knowledge in web development, particularly JavaScript, HTML, and CSS. Here’s a high-level outline of how you might create an extension to handle HAR (HTTP Archive) file
creation and management within Firefox:

1.  **Learn the Basics**:
    *   Familiarize yourself with the basics of Firefox extension development. Mozilla provides an excellent [tutorial and documentation](https://extensionworkshop.com/).
2.  **Setup**


## Extension Firefox : bouton pour fichiers HAR

| Tags |
|------|
| `Firefox` `Extension` `HAR` `JavaScript` |

Peux-tu créer une extension Firefox qui ajoute un bouton permettant d'activer ou de désactiver la création de fichiers HAR et de les sauvegarder dans un répertoire local.


## Création d'une extension Firefox (HAR Recorder)

| Tags |
|------|
| `Firefox` `Extension` `JavaScript` `HTML` `CSS` `Manifest` `HAR` |

Créer une extension Firefox nécessite des compétences en JavaScript, HTML et CSS. Voici une approche simplifiée :

1.  **Initialisation du projet** :
    *   Créez un dossier (ex : `har_recorder`).
    *   Créez trois fichiers : `manifest.json`, `popup.html` et `script.js`.

2.  **Configuration de l'extension** :
    *   Ouvrez `manifest.json` et ajoutez :

```json
{
    "manifest_version": 2,
    "name": "HAR Recorder",
    "version": "1.0",
    "description": "Un simple enregistreur HAR",
    "permissions": ["webRequest", "browsingData", "<all_urls>", "storage"],
    "browser_action": {
        "default_icon": "icon.png",
        "default_popup": "popup.html"
    },
    "background": {
        "scripts": ["script.js"],
        "persistent": false
    }
}
```

3.  **Création de l'interface utilisateur** :
    *   Ouvrez `popup.html` et ajoutez :

```html
<!DOCTYPE html>
<html>
<head>
    <title>HAR Recorder</title>
    <style>
        button { margin: 5px; }
    </style>
</head>
<body>
    <button id="toggleRecording">Démarrer l'enregistrement</button>
    <script src="script.js"></script>
</body>
</html>
```

4.  **Script de l'extension** :
    *   Ouvrez `script.js` et ajoutez :

```javascript
let isRecording = false;

document.getElementById('toggleRecording').addEventListener('click', () => {
    isRecording = !isRecording;
    document.getElementById('toggleRecording').textContent = isRecording ? 'Arrêter l\'enregistrement' : 'Démarrer l\'enregistrement';

    if (isRecording) {
        // Démarrez l'enregistrement ici
    } else {
        // Arrêtez l'enregistrement et proposez de sauvegarder le fichier HAR
    }
});
```

5.  **Gestion de l'enregistrement HAR** :
    *   Firefox n'a pas d'API native pour créer des fichiers HAR directement. Utilisez des bibliothèques tierces ou des services externes.

6.  **Icône** :
    *   Créez une icône (ex : `icon.png`) et placez-la dans le dossier de l'extension.

7.  **Test de l'extension** :
    *   Chargez l'extension dans Firefox via `about:debugging` > `This Firefox` > `Load Temporary Add-on...` et sélectionnez `manifest.json`.

8.  **Enregistrement et sauvegarde des fichiers HAR** :
    *   Implémentez une logique pour enregistrer et sauvegarder les fichiers HAR sur le disque local de l'utilisateur.

Ce code est simplifié. Pour une extension complète, un développement supplémentaire est nécessaire, notamment pour la gestion de l'enregistrement HAR. Utilisez des bibliothèques ou des services adaptés.

Pour plus d'informations, consultez la documentation de Mozilla : [Mozilla Extension Workshop](https://extensionworkshop.com/).


## Sauvegarde des fichiers HAR dans l'extension Firefox

| Tags |
|------|
| `Firefox` `webRequest` `HAR` `manifest.json` `JavaScript` |

La création et la sauvegarde de fichiers HAR directement depuis une extension Firefox impliquent des étapes spécifiques. En raison des restrictions de sécurité, les extensions de navigateur ne peuvent pas écrire directement sur le disque dur de l'utilisateur. La solution consiste à utiliser l'API `webRequest` de Firefox pour capturer le trafic réseau et à le formater en HAR.

Voici les étapes pour enregistrer le trafic réseau en format HAR :

1.  **Mise à jour du fichier `manifest.json`** :
    *   Ajoutez les permissions "webRequest" et "webRequestBlocking" :

    ```json
    "permissions": ["webRequest", "webRequestBlocking", "<all_urls>"],
    ```

2.  **Mise à jour du fichier `script.js`** :

    ```javascript
    let isRecording = false;
    let harData = [];

    document.getElementById('toggleRecording').addEventListener('click', () => {
        isRecording = !isRecording;
        document.getElementById('toggleRecording').textContent = isRecording ? 'Arrêter l\'enregistrement' : 'Démarrer l\'enregistrement';

        if (isRecording) {
            startRecording();
        } else {
            stopRecording();
            saveHarData();
        }
    });

    function startRecording() {
        browser.webRequest.onBeforeRequest.addListener(
            logRequest,
            { urls: ["<all_urls>"] },
            ["blocking"]
        );
    }

    function stopRecording() {
        browser.webRequest.onBeforeRequest.removeListener(logRequest);
    }

    function logRequest(details) {
        harData.push(details);
    }

    function saveHarData() {
        // Convert harData to HAR format
        let har = { log: { entries: harData } };
        let harBlob = new Blob([JSON.stringify(har)], { type: 'application/json' });
        let url = URL.createObjectURL(harBlob);
        browser.downloads.download({
            url: url,
            filename: 'record.har',
            saveAs: true,
            conflictAction: 'uniquify'
        });
        harData = [];  // Clear the harData array for the next recording session
    }
    ```

    Ce code utilise une fonction `startRecording` pour commencer l'écoute des requêtes réseau et `stopRecording` pour l'arrêter. Les requêtes sont stockées dans l'array `harData`. La fonction `saveHarData` convertit ces données en format HAR, crée un Blob, et utilise l'API `downloads` de Firefox pour proposer à l'utilisateur de sauvegarder le fichier HAR.

    Pour l'API `downloads`, assurez-vous d'ajouter l'autorisation "downloads" dans votre fichier `manifest.json`.

    Ce code est une implémentation simplifiée et peut nécessiter des ajustements pour générer un fichier HAR complet et précis.


## Comprendre l'utilisation du paramètre "blocking"

| Tags |
|------|
| `webRequest` `Firefox` `API` `blocking` `JavaScript` |

L'option `"blocking"` dans l'API `webRequest` de Firefox permet de suspendre une requête réseau jusqu'à la fin du traitement par l'écouteur. Cela autorise la modification, la redirection ou l'annulation de la requête avant son envoi. Utile pour modifier ou annuler une requête en fonction de conditions spécifiques.

Dans le code présenté, l'option `"blocking"` est utilisée dans l'appel à `browser.webRequest.onBeforeRequest.addListener`, mais n'est pas indispensable pour l'enregistrement d'informations. Son ajout initial facilitait des modifications ou filtrages de requêtes.

L'option `"blocking"` peut être supprimée si aucune modification ou annulation de requêtes n'est requise. Le code conservera sa fonction d'enregistrement. Voici un exemple :

```javascript
function startRecording() {
    browser.webRequest.onBeforeRequest.addListener(
        logRequest,
        { urls: ["<all_urls>"] }
    );
}
```

Supprimer `"blocking"` simplifie le code et évite la suspension de la requête, potentiellement améliorant les performances.


## Code source complet de l'extension Firefox HAR

| Tags |
|------|
| `Firefox` `Extension` `HAR` `JSON` `JavaScript` |

Bien sûr, voici le code complet pour une extension Firefox simplifiée qui enregistre des données de requête réseau basiques dans un format HAR rudimentaire :

<ol>
<li>
<strong>Structure de Dossier</strong>:
<ul>
<li>
<code>/har_recorder</code><ul>
<li><code>manifest.json</code></li>
<li><code>popup.html</code></li>
<li><code>script.js</code></li>
<li><code>icon.png</code> (créez une icône 48x48 pixels et sauvegardez-la en tant que <code>icon.png</code>)</li>
</ul>
</li>
</ul>
</li>
<li>
<strong>manifest.json</strong>:
</li>
</ol>
<pre><code class="language-json">{
    &quot;manifest_version&quot;: 2,
    &quot;name&quot;: &quot;HAR Recorder&quot;,
    &quot;version&quot;: &quot;1.0&quot;,
    &quot;description&quot;: &quot;Un simple enregistreur HAR&quot;,
    &quot;permissions&quot;: [&quot;webRequest&quot;, &quot;&lt;all_urls&gt;&quot;, &quot;downloads&quot;],
    &quot;browser_action&quot;: {
        &quot;default_icon&quot;: &quot;icon.png&quot;,
        &quot;default_popup&quot;: &quot;popup.html&quot;
    },
    &quot;background&quot;: {
        &quot;scripts&quot;: [&quot;script.js&quot;],
        &quot;persistent&quot;: false
    }
}
</code></pre>
<ol start="3">
<li><strong>popup.html</strong>:</li>
</ol>
<pre><code class="language-html">&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;HAR Recorder&lt;/title&gt;
    &lt;style&gt;
        button { margin: 5px; }
    &lt;/style&gt;
&lt;/head&gt;
&lt;body&gt;
    &lt;button id=&quot;toggleRecording&quot;&gt;Démarrer l&#x27;enregistrement&lt;/button&gt;
    &lt;script src=&quot;script.js&quot;&gt;&lt;/script&gt;
&lt;/body&gt;
&lt;/html&gt;
</code></pre>
<ol start="4">
<li><strong>script.js</strong>:</li>
</ol>
<pre><code class="language-javascript">let isRecording = false;
let harData = [];

document.getElementById(&#x27;toggleRecording&#x27;).addEventListener(&#x27;click&#x27;, () =&gt; {
    isRecording = !isRecording;
    document.getElementById(&#x27;toggleRecording&#x27;).textContent = isRecording ? &#x27;Arrêter l&#x27;enregistrement&#x27; : &#x27;Démarrer l&#x27;enregistrement&#x27;;

    if (isRecording) {
        startRecording();
    } else {
        stopRecording();
        saveHarData();
    }
});

function startRecording() {
    browser.webRequest.onBeforeRequest.addListener(
        logRequest,
        { urls: [&quot;&lt;all_urls&gt;&quot;] }
    );
}

function stopRecording() {
    browser.webRequest.onBeforeRequest.removeListener(logRequest);
}

function logRequest(details) {
    harData.push(details);
}

function saveHarData() {
    // Convert harData to HAR format
    let har = { log: { entries: harData } };
    let harBlob = new Blob([JSON.stringify(har)], { type: &#x27;application/json&#x27; });
    let url = URL.createObjectURL(harBlob);
    browser.downloads.download({
        url: url,
        filename: &#x27;record.har&#x27;,
        saveAs: true,
        conflictAction: &#x27;uniquify&#x27;
    });
    harData = [];  // Clear the harData array for the next recording session
}
</code></pre>
<ol start="5">
<li>
<strong>Test de l'extension</strong>:<ul>
<li>Ouvrez Firefox.</li>
<li>Allez à <code>about:debugging</code>.</li>
<li>Cliquez sur &quot;Ce Firefox&quot; dans la barre latérale.</li>
<li>Cliquez sur &quot;Charger un module complémentaire temporaire...&quot; et sélectionnez le fichier <code>manifest.json</code> dans le dossier <code>har_recorder</code>.</li>
</ul>
</li>
</ol>
<p>Ceci est un code très simplifié et le format HAR généré est également très simplifié. Dans un scénario réel, vous voudriez probablement capturer plus d'informations sur chaque requête, et vous auriez besoin de formater ces informations
conformément à la spécification HAR.</p>


## Structure du fichier HAR généré

| Tags |
|------|
| `HAR` `Firefox` `webRequest` `format` |

Non, le code fourni génère un fichier HAR simplifié, non conforme à la spécification HAR complète. La spécification HAR impose une structure précise avec des champs obligatoires et optionnels pour une validité complète.

Le fichier HAR résultant contiendra une liste de requêtes, avec les détails issus de l'API <code>webRequest</code> de Firefox. Il manquera d'informations cruciales pour un fichier HAR valide, comme les réponses, les en-têtes, les cookies, le contenu et les informations de chronométrage.

Pour générer un fichier HAR valide, il est nécessaire de capturer et de formater davantage de données que celles fournies par l'API <code>webRequest</code> de Firefox. L'utilisation de bibliothèques tierces ou d'outils dédiés est recommandée pour capturer et formater ces données de manière appropriée.

Si l'objectif est de créer des fichiers HAR valides avec une extension Firefox, il est conseillé d'utiliser une bibliothèque existante ou de s'inspirer d'exemples de code démontrant comment capturer et formater correctement toutes les données requises. Une analyse approfondie et l'étude de la documentation sur la spécification HAR sont indispensables pour comprendre la création d'un fichier HAR valide.


## Bibliothèques pour extension Firefox HAR

| Tags |
|------|
| `Firefox` `Extension` `HAR` `chrome-har-capturer` `puppeteer-har` `DevTools` `JavaScript` |

Pour créer une extension Firefox capable d'activer/désactiver la création de fichiers HAR et de les sauvegarder localement, plusieurs bibliothèques et approches sont possibles.

1.  **Module Node.js `chrome-har-capturer`** :

    *   Ce module capture les fichiers HAR à partir d'une instance Chrome. Il utilise `chrome-remote-interface` pour instrumenter Chrome et générer des fichiers HAR conformes à la spécification HAR 1.2.
    *   Exemple de code :

    ```javascript
    const lighthouse = require('lighthouse');
    const chromeLauncher = require('chrome-launcher');
    const { fromLog } = require('chrome-har-capturer');
    const { writeFileSync } = require('fs');

    (async () => {
      const chrome = await chromeLauncher.launch({chromeFlags: ['--headless']});
      const options = {port: chrome.port, emulatedFormFactor: 'desktop'};
      const url = 'https://leonardofaria.net';
      const { artifacts: { devtoolsLogs: { defaultPass } } } = await lighthouse(url, options);

      const har = await fromLog(url, defaultPass);
      writeFileSync('page.har', JSON.stringify(har));

      await chrome.kill();
    })();
    ```

    *   L'adaptation de ce code pour une extension Firefox peut nécessiter des ajustements pour l'intégration avec les APIs Firefox ou l'exécution dans un environnement Node.js séparé.

2.  **Utilisation de `puppeteer-har`** :

    *   La bibliothèque `puppeteer-har` permet également de générer des fichiers HAR, bien que des limitations aient été notées.

3.  **Utilisation de l'API DevTools de Firefox** :

    *   Firefox offre la méthode `browser.devtools.network.getHAR()` pour récupérer les logs HAR. Cette méthode s'appuie sur l'API `chrome.devtools.network` de Chromium, et peut exiger une configuration supplémentaire dans Firefox.
    *   Exemple de code pour démarrer et arrêter l'enregistrement avec l'API DevTools :

    ```javascript
    let harLog;
    let recording = false;

    document.getElementById('startRecording').addEventListener('click', async () => {
        if (!recording) {
            recording = true;
            await browser.devtools.network.enable();
        }
    });

    document.getElementById('stopRecording').addEventListener('click', async () => {
        if (recording) {
            recording = false;
            harLog = await browser.devtools.network.getHAR();
            await browser.devtools.network.disable();
            // Save the HAR log to a local directory
            // ...
        }
    });
    ```

    *   Dans ce code, les boutons avec les identifiants `startRecording` et `stopRecording` gèrent le démarrage et l'arrêt de l'enregistrement. `browser.devtools.network.getHAR()` récupère le log HAR, qui peut ensuite être sauvegardé localement.
    *   La sauvegarde dans un répertoire local peut nécessiter une logique côté serveur ou une approche alternative en raison des restrictions d'accès au système de fichiers imposées par les extensions de navigateur.

En conclusion, la création d'une extension Firefox pour la gestion des fichiers HAR implique une combinaison d'APIs de navigateur, de bibliothèques externes, et potentiellement un environnement serveur pour le stockage des fichiers.


## Capturer les fichiers HAR avec chrome-har-capturer

| Tags |
|------|
| `Node.js` `chrome-har-capturer` `Lighthouse` `HAR` `Chrome` |

Pour créer des fichiers HAR dans Chrome, le module `chrome-har-capturer` peut être utilisé avec Node.js. Voici les étapes :

1.  **Installation des dépendances** :
    Installer `chrome-har-capturer`, `lighthouse`, et `chrome-launcher` via npm :

    ```bash
    npm install chrome-har-capturer lighthouse chrome-launcher
    ```

2.  **Création du script** :
    Créer un fichier, par exemple `har-capturer.js`, et ajouter le code suivant :

    ```javascript
    const lighthouse = require('lighthouse');
    const chromeLauncher = require('chrome-launcher');
    const { fromLog } = require('chrome-har-capturer');
    const { writeFileSync } = require('fs');

    (async () => {
        // Lance une instance de Chrome
        const chrome = await chromeLauncher.launch({chromeFlags: ['--headless']});

        // Définir les options pour Lighthouse
        const options = {port: chrome.port, emulatedFormFactor: 'desktop'};

        // L'URL à analyser
        const url = 'https://example.com';

        // Exécuter Lighthouse pour obtenir les logs DevTools
        const { artifacts: { devtoolsLogs: { defaultPass } } } = await lighthouse(url, options);

        // Générer le fichier HAR à partir des logs
        const har = await fromLog(url, defaultPass);

        // Sauvegarder le fichier HAR sur le disque
        writeFileSync('page.har', JSON.stringify(har));

        // Fermer l'instance de Chrome
        await chrome.kill();
    })();
    ```

3.  **Exécution du script** :
    Exécuter le script en utilisant Node.js :

    ```bash
    node har-capturer.js
    ```

    Ce script lance une instance headless de Chrome, analyse une page web avec Lighthouse, génère un fichier HAR à partir des logs DevTools, et sauvegarde le fichier HAR sur le disque en tant que `page.har`.

    Note : Ce script nécessite une installation locale de Node.js et de npm, ainsi que l'installation des packages `lighthouse`, `chrome-launcher`, et `chrome-har-capturer`. L'utilisation de Lighthouse n'est pas strictement nécessaire, mais c'est une manière simple d'obtenir les logs DevTools nécessaires pour générer le fichier HAR avec `chrome-har-capturer`.
