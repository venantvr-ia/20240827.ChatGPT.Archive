## Formation Node.js (5 jours)

| Tags |
|------|
| `Node.js` `JavaScript` `Express.js` `API` `Backend` |

**Jour 1 : Introduction à Node.js et JavaScript**

*   Présentation de Node.js :
    *   Qu'est-ce que Node.js ?
    *   Pourquoi utiliser Node.js ?
    *   Architecture événementielle et non bloquante.
    *   Installation et configuration de Node.js et npm.
*   JavaScript pour Node.js :
    *   Rappels sur JavaScript : variables, types de données, opérateurs, structures de contrôle.
    *   Fonctions et portée des variables.
    *   Objets et programmation orientée objet en JavaScript.
    *   Modules et gestion des dépendances avec npm.
*   Premier pas avec Node.js :
    *   Création et exécution d'un script Node.js.
    *   Utilisation du module `fs` pour la manipulation de fichiers.
    *   Le module `http` pour créer un serveur web simple.

    ```javascript
    // Exemple de script Node.js
    const http = require('http');

    const server = http.createServer((req, res) => {
      res.statusCode = 200;
      res.setHeader('Content-Type', 'text/plain');
      res.end('Hello, World!\n');
    });

    server.listen(3000, '[IP]', () => {
      console.log('Server running at http://[IP]:3000/');
    });
    ```

**Jour 2 : Gestion des modules et npm**

*   Approfondissement des modules :
    *   Création et utilisation de modules personnalisés.
    *   Gestion des exports et imports.
    *   Les modules intégrés de Node.js (fs, http, path, os, etc.).
*   npm (Node Package Manager) :
    *   Gestion des dépendances : `npm install`, `npm update`, `npm uninstall`.
    *   Le fichier `package.json` : comprendre et configurer.
    *   Publication de packages sur npm (si applicable).
*   Gestion des erreurs et débogage :
    *   Gestion des erreurs avec `try...catch`.
    *   Les événements `error` et `uncaughtException`.
    *   Utilisation du débogueur intégré de Node.js.

    ```bash
    # Exemple d'installation d'un package
    npm install express --save
    ```

**Jour 3 : Express.js : Développement d'API REST**

*   Introduction à Express.js :
    *   Qu'est-ce qu'Express.js ?
    *   Pourquoi utiliser Express.js ?
    *   Installation et configuration d'Express.js.
*   Création d'une API REST avec Express.js :
    *   Définition des routes (GET, POST, PUT, DELETE).
    *   Gestion des requêtes et des réponses.
    *   Utilisation des middlewares (gestion des requêtes, authentification, etc.).
    *   Gestion des paramètres de requête et du corps de la requête.
*   Structure d'une application Express.js :
    *   Organisation des fichiers et des dossiers.
    *   Configuration des variables d'environnement.

    ```javascript
    // Exemple d'application Express.js
    const express = require('express');
    const app = express();
    const port = 3000;

    app.get('/', (req, res) => {
      res.send('Hello World!');
    });

    app.listen(port, () => {
      console.log(`Example app listening at http://[IP]:${port}`);
    });
    ```

**Jour 4 : Bases de données et persistance des données**

*   Introduction aux bases de données NoSQL :
    *   Pourquoi choisir une base de données NoSQL ?
    *   Présentation de MongoDB.
    *   Installation et configuration de MongoDB.
*   Intégration de MongoDB avec Node.js :
    *   Utilisation du driver MongoDB pour Node.js.
    *   Connexion à la base de données.
    *   Opérations CRUD (Create, Read, Update, Delete).
    *   Modélisation des données avec Mongoose (si applicable).
*   Interaction avec une base de données relationnelle (si le temps le permet) :
    *   Présentation de Sequelize.
    *   Configuration de la connexion à la base de données.

    ```javascript
    // Exemple de connexion à MongoDB
    const { MongoClient } = require('mongodb');
    const uri = "mongodb://[NOM]:[MOT DE PASSE]@[NOM].mongodb.net/[NOM]?retryWrites=true&w=majority"; // Remplacez par vos informations de connexion
    const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

    async function connectToDatabase() {
      try {
        await client.connect();
        console.log("Connected successfully to server");
      } catch (e) {
        console.error(e);
      } finally {
        await client.close();
      }
    }

    connectToDatabase().catch(console.error);
    ```

**Jour 5 : Tests, sécurité et déploiement**

*   Tests unitaires et tests d'intégration :
    *   Introduction aux tests.
    *   Utilisation de frameworks de tests (Jest, Mocha, etc.).
    *   Écriture de tests unitaires et d'intégration.
*   Sécurité des applications Node.js :
    *   Vulnérabilités courantes et bonnes pratiques de sécurité.
    *   Protection contre les attaques XSS, CSRF, et injection SQL.
    *   Authentification et autorisation (JWT, OAuth).
*   Déploiement d'une application Node.js :
    *   Présentation des plateformes de déploiement (Heroku, AWS, etc.).
    *   Configuration du serveur.
    *   Déploiement de l'application.
    *   Surveillance et gestion des logs.

    ```bash
    # Exemple de commande pour déployer sur Heroku
    heroku create
    git push heroku main
    heroku open
    ```

**Ressources et outils supplémentaires**

*   Documentation officielle de Node.js : [https://nodejs.org/en/docs/](https://nodejs.org/en/docs/)
*   Documentation officielle d'Express.js : [https://expressjs.com/](https://expressjs.com/)
*   Documentation de MongoDB : [https://www.mongodb.com/docs/](https://www.mongodb.com/docs/)
*   [NOM] - [EMAIL]


## Plan de formation Node.js en 5 jours

| Tags |
|------|
| `Node.js` `JavaScript` `Express.js` `MongoDB` `Mongoose` |

<p>Voici un plan de formation pour Node.js en 5 jours. Il est recommandé d'avoir des connaissances préalables en JavaScript.</p>

<p><strong>Jour 1 : Introduction à Node.js</strong></p>
<ul>
<li>Introduction à Node.js : Concepts, utilisations et fonctionnement.</li>
<li>Installation et configuration de l'environnement de développement.</li>
<li>Création d'un premier script Node.js.</li>
<li>Compréhension du système de modules Node.js : <code>require</code>, <code>exports</code>, <code>module.exports</code>.</li>
</ul>

<p><strong>Jour 2 : Gestion des entrées/sorties et des événements</strong></p>
<ul>
<li>Comprendre les entrées/sorties non bloquantes.</li>
<li>Utilisation du système de fichiers (module <code>fs</code>).</li>
<li>Gestion des événements avec <code>EventEmitter</code>.</li>
<li>Compréhension des streams et des buffers.</li>
</ul>

<p><strong>Jour 3 : Développement web avec Express.js</strong></p>
<ul>
<li>Introduction à Express.js : Concepts et utilisations.</li>
<li>Installation et configuration d'Express.js.</li>
<li>Création d'une application web simple avec Express.js.</li>
<li>Gestion des routes, des requêtes et des réponses.</li>
</ul>

<p><strong>Jour 4 : Bases de données et authentification</strong></p>
<ul>
<li>Introduction à MongoDB et Mongoose pour la gestion des bases de données.</li>
<li>Création d'un modèle de données simple et interaction avec la base de données.</li>
<li>Introduction à l'authentification avec Passport.js.</li>
</ul>

<p><strong>Jour 5 : Déploiement et bonnes pratiques</strong></p>
<ul>
<li>Introduction au déploiement avec Heroku ou un autre service similaire.</li>
<li>Comprendre les promesses et <code>async/await</code> pour la gestion des opérations asynchrones.</li>
<li>Bonnes pratiques de développement avec Node.js.</li>
<li>Révision générale et résolution de problèmes.</li>
</ul>

<p>Ce plan de formation est intensif. La maîtrise de Node.js nécessite du temps et de la pratique. Après ces 5 jours, il est conseillé de continuer à pratiquer en développant vos propres projets et en explorant d'autres aspects de Node.js et de son écosystème.</p>


## Promises vs. Async/Await en JavaScript

| Tags |
|------|
| `JavaScript` `Promises` `Async/Await` `Asynchrone` |

Les Promises et async/await sont deux approches pour la gestion des opérations asynchrones en JavaScript. Elles visent à simplifier le développement par rapport aux callbacks et à éviter le "callback hell".

**Promises:**

Une Promise représente l'issue d'une opération asynchrone, avec trois états possibles :

*   Pending (en attente) : Opération non terminée.
*   Fulfilled (réussie) : Opération réussie.
*   Rejected (échouée) : Opération ayant échoué.

Exemple :

```javascript
let promise = new Promise((resolve, reject) => {
  let condition = true; // Simule le résultat d'une opération asynchrone
  if(condition) {
    resolve('Success!');
  } else {
    reject('Failure!');
  }
});

promise
  .then((message) => {
    console.log(message); // Affiche 'Success!'
  })
  .catch((message) => {
    console.log(message); // Affiche 'Failure!'
  });
```

**Async/Await:**

Async/await est une syntaxe facilitant l'utilisation des Promises. Une fonction `async` retourne toujours une Promise. Le mot-clé `await` suspend l'exécution d'une fonction `async` jusqu'à ce qu'une Promise soit résolue ou rejetée.

Exemple :

```javascript
async function myFunction() {
  try {
    let condition = true; // Simule le résultat d'une opération asynchrone
    if(condition) {
      console.log('Success!');
    } else {
      throw new Error('Failure!');
    }
  } catch (error) {
    console.log(error.message);
  }
}

myFunction();
```

En résumé, async/await offre une syntaxe plus lisible et proche du code synchrone. Toutefois, async/await s'appuie sur les Promises, dont la compréhension est essentielle.


## Non-utilisation de async/await en JavaScript

| Tags |
|------|
| `JavaScript` `async/await` `Promises` `asynchrone` |

Si <code>async/await</code> n'est pas utilisé dans le code JavaScript, les opérations asynchrones doivent être gérées différemment, typiquement avec des callbacks ou des Promises directement.

Lorsqu'une fonction retourne une Promise sans utiliser <code>await</code>, elle continue son exécution sans attendre la résolution de la Promise. Tenter d'accéder à la valeur résolue de la Promise immédiatement après l'appel de la fonction retournera probablement une Promise non résolue.

Exemple :

```javascript
function getPromise() {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      resolve('Hello, World!');
    }, 2000);
  });
}

let promise = getPromise();
console.log(promise); // Affiche 'Promise { <pending> }'
```

Dans cet exemple, <code>console.log(promise)</code> est exécuté avant la résolution de la Promise, affichant donc <code>Promise { &lt;pending&gt; }</code>.

Pour obtenir la valeur résolue, il faut utiliser <code>.then()</code> :

```javascript
getPromise().then((value) => {
  console.log(value); // Affiche 'Hello, World!'
});
```

Alternativement, <code>async/await</code> peut être utilisé pour améliorer la lisibilité :

```javascript
async function printValue() {
  let value = await getPromise();
  console.log(value); // Affiche 'Hello, World!'
}

printValue();
```

En conclusion, sans <code>async/await</code>, d'autres mécanismes de gestion des Promises doivent être employés pour assurer l'attente des opérations asynchrones avant de poursuivre l'exécution du code.


## Déterminer si une fonction retourne une Promise

| Tags |
|------|
| `JavaScript` `Promise` `asynchrone` |

En JavaScript, les fonctions asynchrones retournent généralement une `Promise`. Cette pratique est courante dans de nombreuses bibliothèques et dans le langage lui-même. Par exemple, les fonctions telles que `fetch()` pour les requêtes HTTP, `fs.readFile()` dans Node.js pour la lecture de fichiers, ou `setTimeout()` pour des opérations différées, retournent toutes des `Promises`.

Pour vérifier si une fonction retourne une `Promise`, utilisez `instanceof` :

```javascript
let maybePromise = someFunction();
if (maybePromise instanceof Promise) {
  console.log('This function returns a Promise.');
} else {
  console.log('This function does not return a Promise.');
}
```

Si une fonction retourne une `Promise`, utilisez `then()` pour traiter la valeur résolue, ou `catch()` pour gérer les erreurs. Vous pouvez également utiliser `async/await`.

```javascript
someFunction().then((resolvedValue) => {
  // Traiter resolvedValue
}).catch((error) => {
  // Gérer l'erreur
});
```

Ou avec `async/await` :

```javascript
try {
  let resolvedValue = await someFunction();
  // Traiter resolvedValue
} catch (error) {
  // Gérer l'erreur
}
```

L'utilisation de `await` requiert une fonction `async`.


## Création d'une Promise en JavaScript

| Tags |
|------|
| `JavaScript` `Promise` `Asynchrone` `async/await` |

En JavaScript, une `Promise` se crée en utilisant le constructeur `Promise`. Ce constructeur prend une fonction d'exécuteur comme argument, laquelle prend elle-même deux fonctions comme arguments : `resolve` et `reject`.

Voici un exemple de création d'une `Promise` :

```javascript
let myPromise = new Promise((resolve, reject) => {
  // Opération asynchrone appelant :
  //
  // resolve(someValue); // en cas de succès
  // ou
  // reject("failure reason"); // en cas d'échec
});
```

Par exemple, une `Promise` peut être créée pour se résoudre après un certain délai :

```javascript
let myPromise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve('Promise résolue!');
  }, 2000);
});
```

Dans ce cas, la `Promise` est résolue avec la valeur `'Promise résolue!'` après 2 secondes.

Il est possible d'utiliser `then` pour exécuter du code une fois la `Promise` résolue, ou `catch` pour gérer les erreurs :

```javascript
myPromise.then((value) => {
  console.log(value); // Affiche 'Promise résolue!'
}).catch((error) => {
  console.log(error);
});
```

Alternativement, `async/await` peut être utilisé pour attendre la résolution d'une `Promise` :

```javascript
async function waitForPromise() {
  try {
    let value = await myPromise;
    console.log(value); // Affiche 'Promise résolue!'
  } catch (error) {
    console.log(error);
  }
}

waitForPromise();
```

L'utilisation de `await` doit se faire au sein d'une fonction déclarée avec le mot-clé `async`.


## Synchronisation vs. Asynchronisation en JavaScript

| Tags |
|------|
| `JavaScript` `asynchrone` `synchrone` `Promises` |

Pas nécessairement. En JavaScript, le code synchrone et le code asynchrone peuvent coexister. Il n'est pas nécessaire de transformer tout le code synchrone en code basé sur des Promises. Pour de nombreuses opérations, le code synchrone est plus approprié et plus facile à comprendre.

Cependant, lors de l'utilisation d'opérations qui prennent du temps pour se terminer, telles que les requêtes réseau, la lecture de fichiers, ou toute autre opération impliquant une attente, il est généralement préférable d'utiliser des Promises ou d'autres formes de code asynchrone. Cela permet au programme de continuer à exécuter d'autres tâches pendant que l'opération longue est en cours.

Par exemple, si une fonction lit un fichier (une opération qui peut prendre du temps), il est préférable de la transformer en une fonction qui retourne une Promise. Cela permet au programme de continuer à exécuter d'autres tâches pendant que le fichier est lu.

Voici un exemple de la façon dont transformer une fonction synchrone en une fonction qui retourne une Promise :

```javascript
const fs = require('fs');

// Version synchrone
function readFileSync(path) {
  return fs.readFileSync(path, 'utf8');
}

// Version basée sur des Promises
function readFileAsync(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(err);
      } else {
        resolve(data);
      }
    });
  });
}
```

Dans cet exemple, `readFileSync` est une fonction synchrone qui bloque l'exécution du programme jusqu'à ce que le fichier soit lu. D'autre part, `readFileAsync` est une fonction asynchrone qui retourne une Promise. Cette Promise est résolue avec les données du fichier une fois que le fichier est lu, ou rejetée avec une erreur si quelque chose se passe mal. Pendant que le fichier est lu, le programme peut continuer à exécuter d'autres tâches.


## Impact de 'await' en JavaScript

| Tags |
|------|
| `JavaScript` `async/await` `Promise` `performance` |

Oui, l'utilisation intensive de `await` est courante avec les fonctions asynchrones en JavaScript.  Chaque `await` bloque l'exécution de la fonction asynchrone jusqu'à la résolution de la Promise.

Si plusieurs opérations asynchrones peuvent s'exécuter en parallèle, il est préférable de les démarrer simultanément et d'utiliser `Promise.all` pour attendre leur achèvement.

Exemple :

```javascript
async function fetchMultipleUrls() {
  let response1 = await fetch('https://example.com/url1');
  let data1 = await response1.json();

  let response2 = await fetch('https://example.com/url2');
  let data2 = await response2.json();

  return [data1, data2];
}
```

peut être optimisé en :

```javascript
async function fetchMultipleUrls() {
  let fetch1 = fetch('https://example.com/url1').then(response => response.json());
  let fetch2 = fetch('https://example.com/url2').then(response => response.json());

  let [data1, data2] = await Promise.all([fetch1, fetch2]);

  return [data1, data2];
}
```

Dans le second exemple, les requêtes `fetch` démarrent en parallèle, potentiellement améliorant la performance.

Il est crucial de gérer les erreurs avec `await` en utilisant des blocs `try/catch` pour intercepter et gérer les rejets de Promise.


## Comprendre le comportement bloquant d' `await` en JavaScript

| Tags |
|------|
| `JavaScript` `async/await` `asynchrone` `Promise` |

Oui, le mot-clé `await` en JavaScript est "bloquant" car il suspend l'exécution d'une fonction asynchrone jusqu'à la résolution ou le rejet de la Promise. Cependant, cela n'affecte pas l'ensemble du fil d'exécution JavaScript.

L'utilisation de `await` met en pause l'exécution de la fonction asynchrone, permettant l'exécution du reste du code JavaScript. Cela facilite la gestion des opérations asynchrones, en offrant une syntaxe semblable au code synchrone sans bloquer l'ensemble du fil d'exécution.

Exemple :

```javascript
async function myFunction() {
  console.log('Avant await');
  await new Promise(resolve => setTimeout(resolve, 2000));
  console.log('Après await');
}

myFunction();
console.log('Après appel de la fonction');
```

Dans cet exemple, l'exécution de `myFunction` est suspendue pendant 2 secondes par `await`, tandis que le reste du code JavaScript (la dernière ligne) continue de s'exécuter. L'output sera :

```
Avant await
Après appel de la fonction
Après await
```

Cela démontre que `await` suspend l'exécution de la fonction asynchrone, mais ne bloque pas l'intégralité du fil d'exécution JavaScript.


## Promises non résolues : Conséquences et gestion

| Tags |
|------|
| `JavaScript` `Promise` `asynchrone` |

Si une Promise n'est jamais résolue ou rejetée, elle reste dans l'état "pending" indéfiniment. Cela se produit si la fonction exécutrice du constructeur de la Promise n'appelle jamais `resolve()` ou `reject()`.

Cela peut engendrer des problèmes :

*   L'utilisation de `await` sur une Promise non résolue bloque la fonction asynchrone.
*   Les callbacks de `.then()` et `.catch()` ne sont jamais exécutés.

Il est crucial de s'assurer que les Promises sont correctement résolues ou rejetées. En cas d'échec potentiel d'une opération asynchrone, il est recommandé de gérer ce cas pour éviter l'attente indéfinie.

Exemple : Implémentation d'un délai d'attente pour une opération réseau :

```javascript
let myPromise = new Promise((resolve, reject) => {
  let timeout = setTimeout(() => {
    reject(new Error('Operation timed out'));
  }, 5000);

  performNetworkOperation()
    .then(result => {
      clearTimeout(timeout);
      resolve(result);
    })
    .catch(error => {
      clearTimeout(timeout);
      reject(error);
    });
});
```

Dans cet exemple, si `performNetworkOperation()` ne résout ni ne rejette la Promise dans les 5 secondes, le délai d'attente expire et rejette la Promise.


## Fin d'exécution du programme et Promises

| Tags |
|------|
| `JavaScript` `Promise` `asynchrone` `Node.js` |

Si une Promise n'est jamais résolue ou rejetée, elle reste dans l'état "pending" indéfiniment. Toutefois, cela n'empêche pas le programme de se terminer. En JavaScript, la fin du programme est déterminée par l'achèvement de tous les événements dans la boucle d'événements de Node.js.

Cela signifie que si une Promise est en attente, mais qu'il n'y a plus d'autres événements ou tâches asynchrones en attente dans le programme (comme des timeouts, des requêtes réseau, ou des opérations de lecture/écriture de fichiers), le programme se terminera, même si la Promise n'a pas été résolue ou rejetée.

Cependant, si une Promise est en attente et que <code>await</code> est utilisé pour attendre cette Promise dans une fonction asynchrone, alors cette fonction restera en pause indéfiniment, sauf interruption de l'exécution (par exemple, en lançant une erreur).

En résumé, une Promise en attente n'empêche pas le programme de se terminer, mais peut causer des problèmes si l'on attend la résolution ou le rejet de cette Promise. Il est donc essentiel de s'assurer que les Promises sont correctement résolues ou rejetées.


## Empêchement d'arrêt d'un programme Node.js

| Tags |
|------|
| `Node.js` `JavaScript` `asynchrone` `événements` |

En JavaScript, notamment dans un environnement Node.js, plusieurs facteurs peuvent bloquer la terminaison d'un programme, même après l'exécution du code principal.

Les causes potentielles incluent :

1.  **Opérations asynchrones en attente :** Les opérations asynchrones (timeouts, intervalles, requêtes réseau, opérations de fichiers) non terminées.

2.  **Écouteurs d'événements actifs :** Les écouteurs d'événements actifs (sockets, processus).

3.  **Connexions de bases de données ouvertes :** Connexions non fermées vers des bases de données ou ressources externes.

4.  **Promises en attente :** Promises non résolues ou rejetées.

Pour une terminaison correcte, il est essentiel de nettoyer les ressources (fermer les connexions de bases de données), de terminer toutes les opérations asynchrones, et de gérer correctement les Promises et les écouteurs d'événements.


## Débogage Node.js pour identifier les problèmes

| Tags |
|------|
| `Node.js` `débogage` `console.log` `process` `why-is-node-running` |

Si votre programme Node.js ne se termine pas comme prévu, plusieurs techniques permettent de déboguer et d'identifier la cause.

<ol>
<li>
<strong>Utilisation de <code>console.log</code> ou d'un débogueur :</strong> L'ajout de déclarations <code>console.log</code> permet de suivre l'exécution du code. Les débogueurs intégrés aux environnements de développement (Visual Studio Code, par exemple) offrent des capacités d'inspection de l'état du programme.
</li>
<li>
<strong>Utilisation de <code>process._getActiveHandles</code> et <code>process._getActiveRequests</code> :</strong> Ces méthodes non documentées de l'objet <code>process</code> permettent d'identifier les handles (timers, sockets) et les requêtes (opérations de fichiers) actifs, et ainsi de déterminer ce qui bloque la terminaison du programme.
<pre><code class="language-javascript">// Affiche les handles actifs
console.log(process._getActiveHandles());

// Affiche les requêtes actives
console.log(process._getActiveRequests());
</code></pre>
</li>
<li>
<strong>Utilisation de <code>why-is-node-running</code> :</strong> Le module npm <code>why-is-node-running</code> affiche les handles actifs à la fin de l'exécution. Installation : <code>npm install why-is-node-running</code>. Utilisation :
<pre><code class="language-javascript">const log = require(&#x27;why-is-node-running&#x27;); // doit être la première ligne de votre programme

// Votre code ici...

// À la fin de votre programme :
setTimeout(() =&gt; {
  log(); // affiche les handles actifs qui empêchent votre programme de se terminer
}, 100);
</code></pre>
</li>
</ol>

Ces techniques peuvent ne pas suffire pour les problèmes liés aux Promises en attente ou aux opérations asynchrones. Des techniques de débogage plus avancées ou une revue du code sont alors nécessaires.
