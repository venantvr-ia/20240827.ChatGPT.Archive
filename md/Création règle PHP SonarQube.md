## Création d'une règle PHP SonarQube

| Tags |
|------|
| `SonarQube` `PHP` `SonarQube API` |

L'objectif est de créer une règle personnalisée pour l'analyse du code PHP avec SonarQube. Cela implique l'utilisation de l'API SonarQube et la configuration d'un profil de qualité personnalisé.

### Prérequis

*   Accès à une instance SonarQube.
*   Droits d'administration pour la gestion des profils de qualité et des règles.
*   Connaissance de PHP et de l'API SonarQube.

### Étapes

1.  **Identifier le besoin**: Déterminer la règle à créer. Par exemple, interdire l'utilisation de la fonction `eval()` pour des raisons de sécurité.

2.  **Création de la règle via l'API SonarQube**:

    *   Utiliser l'API pour créer une nouvelle règle. L'API doit être appelée avec les informations de la règle, telles que la clé, le nom, la description et la sévérité.

    ```bash
    curl -u [NOM]:[PASSWORD] -X POST -d '{"name":"Avoid eval()","key":"avoid-eval","severity":"MAJOR","templateKey":"custom-php-rule"}' "[SONARQUBE_URL]/api/rules/create?language=php"
    ```

    *   Remplacer `[NOM]`, `[PASSWORD]` et `[SONARQUBE_URL]` par les informations appropriées.
    *   `templateKey` peut être un identifiant de template existant ou un identifiant personnalisé.

3.  **Développement du plugin PHP (si nécessaire)** : Si la règle nécessite une logique d'analyse complexe, un plugin SonarQube peut être développé en PHP. Ce plugin analysera le code PHP et identifiera les occurrences de `eval()`.
    *   Structure du plugin (simplifiée) :

    ```php
    <?php
    // Définition de la classe du plugin
    class AvoidEvalRule extends \SonarSource\PHP\Plugin\AbstractRule
    {
        public function getRuleKey() {
            return 'avoid-eval';
        }

        public function getName() {
            return 'Avoid eval()';
        }

        public function getDescription() {
            return 'Avoid using the eval() function for security reasons.';
        }

        public function getSeverity() {
            return 'MAJOR';
        }

        public function scanFile(\SonarSource\PHP\Ast\File $file) {
            $code = $file->getContent();
            if (strpos($code, 'eval(') !== false) {
                $this->addIssue($file, 1, 'The use of eval() is forbidden.');
            }
        }
    }
    ```

    *   Ce code est une ébauche, il devra être intégré à un plugin SonarQube. L'implémentation complète nécessite l'utilisation des API SonarQube pour l'analyse du code PHP.

4.  **Installation du plugin (si applicable)** : Déployer le plugin SonarQube sur l'instance SonarQube.

5.  **Configuration du profil de qualité**:

    *   Accéder à l'interface SonarQube.
    *   Créer un nouveau profil de qualité (ou modifier un profil existant) pour PHP.
    *   Activer la nouvelle règle dans le profil.

6.  **Analyse du code**:

    *   Lancer une analyse du code source PHP avec SonarQube.
    *   Vérifier que la règle est appliquée et que les violations sont détectées.

7.  **Vérification des résultats**: Consulter les résultats de l'analyse dans SonarQube pour s'assurer que les violations sont correctement signalées.

### Exemple de configuration (profil de qualité)

1.  Accéder à "Quality Profiles" dans l'interface SonarQube.
2.  Sélectionner le profil de qualité PHP souhaité (ou créer un nouveau).
3.  Rechercher la règle "Avoid eval()" (ou le nom donné à la règle).
4.  Activer la règle en modifiant le statut de la règle (par exemple, de "Inactive" à "Active").
5.  Sauvegarder le profil de qualité.

### Conclusion

La création d'une règle personnalisée SonarQube pour PHP permet d'améliorer la qualité et la sécurité du code. Les étapes décrites ici fournissent un guide pour la mise en œuvre de cette tâche.


## Création d'une règle PHP personnalisée SonarQube

| Tags |
|------|
| `SonarQube` `PHP` `Plugin` `Règle personnalisée` |

Créer une règle personnalisée PHP sous SonarQube implique plusieurs étapes clés :

1.  **Création d'un plugin SonarQube** : Développez un plugin, généralement via Maven, qui servira de conteneur pour vos règles personnalisées. Un exemple est disponible sur le dépôt GitHub de SonarQube : [https://github.com/SonarSource/sonar-custom-rules-examples](https://github.com/SonarSource/sonar-custom-rules-examples).
2.  **Définition de la règle** : Indiquez le nom, la description, le type de problème (bug, vulnérabilité, etc.) et la gravité de la règle.
3.  **Implémentation de la règle** : Écrivez la logique de la règle, c'est-à-dire le code qui analysera le code source PHP pour détecter les problèmes.
4.  **Tests de la règle** : Validez son fonctionnement grâce à des tests unitaires.
5.  **Déploiement de la règle** : Construisez le plugin avec Maven et déployez-le dans le répertoire des plugins de votre instance SonarQube.
6.  **Activation de la règle** : Activez la règle dans le profil de qualité via l'interface utilisateur de SonarQube.

La documentation officielle de SonarQube est la référence pour les informations les plus à jour et précises.

## Langage pour les règles SonarQube

| Tags |
|------|
| `SonarQube` `Java` `Règles personnalisées` |

Les règles personnalisées SonarQube sont principalement développées en Java. Cette dépendance découle du fait que SonarQube est lui-même construit en Java, et les plugins SonarQube, qui servent à implémenter les règles personnalisées, sont des artefacts Java.

L'écriture d'une règle personnalisée implique la création d'une classe Java qui définit la logique et les spécifications de la règle. Cette classe est ensuite intégrée dans le processus d'analyse de SonarQube, permettant la détection des problèmes de code ciblés par la règle.

Il est essentiel de comprendre que bien que les règles soient codées en Java, elles peuvent être utilisées pour analyser du code écrit dans n'importe quel langage pris en charge par SonarQube. Par exemple, une règle Java peut analyser du code PHP, JavaScript, Python, etc.


## Exemple de code

| Tags |
|------|
| `JSON` `GitHub` `SonarSource` |

```json
{
"link": "https://github.com/SonarSource/sonar-custom-rules-examples",
"user_has_request": true
}
```


## Exemples de Règles Personnalisées SonarQube

| Tags |
|------|
| `SonarQube` `Règles Personnalisées` `COBOL` `PHP` `Python` `RPG` |

Le dépôt GitHub SonarSource `sonar-custom-rules-examples` fournit des exemples de projets pour démarrer le développement de règles personnalisées pour COBOL, PHP, Python et RPG. Ces projets peuvent être clonés directement.

Un exemple de règle personnalisée est disponible dans le sous-répertoire "php-custom-rules". Le code source doit être consulté directement via le dépôt GitHub.

La documentation complète est disponible à l'adresse suivante : [https://docs.sonarqube.org/latest/extend/adding-coding-rules/](https://docs.sonarqube.org/latest/extend/adding-coding-rules/).

Les problèmes GitHub sont désactivés pour ce dépôt. Pour toute demande de commentaires ou d'assistance, veuillez utiliser le forum de la communauté Sonar.


## Automatisation de SonarQube avec Python

| Tags |
|------|
| `SonarQube` `Python` `API` `SonarScanner` `CI/CD` |

Pour automatiser SonarQube avec Python, utilisez le module `sonarqube`, une interface Python pour l'API Web de SonarQube. Il permet d'interagir avec SonarQube pour obtenir des informations sur les projets, les créer, gérer les règles, etc.

Exemple de base pour obtenir des informations sur un projet :

```python
from sonarqube import SonarQubeClient

sonar = SonarQubeClient(sonarqube_url="http://localhost:9000", token="your_token")

# Get project information
project_info = sonar.projects.search_projects(projects="your_project_key")
print(project_info)
```

Remplacez `"http://localhost:9000"` par l'URL de votre instance SonarQube, `"your_token"` par votre token d'authentification SonarQube et `"your_project_key"` par la clé de votre projet.

Le module `sonarqube` permet également d'automatiser la création de projets, la gestion des règles et l'obtention de métriques. Pour plus d'informations, consultez la <a href="https://python-sonarqube-api.readthedocs.io/en/latest/">documentation</a>.

Pour automatiser l'analyse de code avec SonarQube, utilisez SonarScanner. Configurez-le pour qu'il s'exécute automatiquement lors de la construction du projet, par exemple en l'intégrant à votre pipeline CI/CD. Pour plus d'informations, consultez la <a href="https://docs.sonarqube.org/latest/analysis/overview/">documentation de SonarQube</a>.


## Erreur "Could not find a..." pour SonarQube

| Tags |
|------|
| `SonarQube` `API` `Python` `requests` |

I apologize for the confusion. As of my knowledge cutoff in September 2021, there isn't a Python package named `sonarqube` available on PyPi.

However, you can interact with SonarQube's Web API directly using Python's built-in libraries such as `requests`. Here's a simple example of how you might do this:

```python
import requests

# replace with your SonarQube URL and auth token
sonarqube_url = "http://localhost:9000"
auth_token = "your_auth_token"

# set the API endpoint
api_url = f"{sonarqube_url}/api/issues/search"

# set the headers for the API request
headers = {
    "Authorization": f"Basic {auth_token}"
}

# make the API request
response = requests.get(api_url, headers=headers)

# print the response
print(response.json())
```

In this example, you would replace `"http://localhost:9000"` with your SonarQube URL and `"your_auth_token"` with your SonarQube authentication token. This script sends a GET request to the SonarQube API's `issues/search` endpoint, which
returns a list of issues.

Please note that the actual usage may vary depending on your SonarQube version and configuration. Always refer to the [SonarQube Web API documentation](https://docs.sonarqube.org/latest/extend/web-api/) for the most accurate information.
