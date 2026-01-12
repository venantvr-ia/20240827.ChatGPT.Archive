## Reformater le JSON en Python

| Tags |
|------|
| `Python` `JSON` `Formatage` |

Le formatage des fichiers JSON est une tâche courante en développement. Python offre des outils intégrés pour faciliter cette opération.

### Formatage de base

Le module `json` de Python fournit des fonctions pour travailler avec des données JSON. Pour formater un fichier JSON, on utilise la fonction `json.dumps()` avec les paramètres appropriés.

```python
import json

data = {
    "name": "[NOM]",
    "age": 30,
    "city": "New York"
}

formatted_json = json.dumps(data, indent=4)
print(formatted_json)
```

Dans cet exemple, `indent=4` ajoute 4 espaces pour l'indentation, rendant le JSON plus lisible.

### Formatage avancé

Pour des besoins plus spécifiques, on peut personnaliser le formatage en utilisant d'autres paramètres de `json.dumps()`.

```python
import json

data = {
    "name": "[NOM]",
    "age": 30,
    "city": "New York",
    "address": {
        "street": "123 Main St",
        "zip": "10001"
    }
}

formatted_json = json.dumps(data, indent=4, separators=(',', ': '))
print(formatted_json)
```

Le paramètre `separators` permet de contrôler les séparateurs utilisés (ici, `,` et `: `).

### Gestion des erreurs

Il est important de gérer les erreurs lors de la manipulation de fichiers JSON, par exemple, lorsqu'un fichier JSON est mal formé.

```python
import json

try:
    with open('data.json', 'r') as f:
        data = json.load(f)
    formatted_json = json.dumps(data, indent=4)
    print(formatted_json)
except FileNotFoundError:
    print("Le fichier n'a pas été trouvé.")
except json.JSONDecodeError as e:
    print(f"Erreur de décodage JSON: {e}")
```

Cet exemple montre comment gérer les exceptions potentielles telles que `FileNotFoundError` et `JSONDecodeError`.

### Exemple de script complet

Voici un exemple de script complet pour formater un fichier JSON existant.

```python
import json

def format_json_file(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        formatted_json = json.dumps(data, indent=4)
        print(formatted_json)
    except FileNotFoundError:
        print(f"Le fichier {file_path} n'a pas été trouvé.")
    except json.JSONDecodeError as e:
        print(f"Erreur de décodage JSON dans {file_path}: {e}")

# Utilisation
format_json_file('data.json')
```


## Charger et formater un fichier JSON en Python

| Tags |
|------|
| `Python` `JSON` `json.load` `json.dump` |

Pour formater un fichier JSON non formaté en Python, utilisez le module `json`. Ce module permet de charger un fichier JSON et de le réécrire avec un format plus lisible.

1.  **Chargement du JSON non formaté :**

    ```python
    import json

    # Supposons que vous ayez un fichier JSON non formaté appelé 'data.json'
    with open('data.json', 'r') as file:
        data = json.load(file)  # Charger le JSON non formaté
    ```

2.  **Reformater le JSON :**

    ```python
    # Écrire le JSON formaté dans un nouveau fichier 'formatted_data.json'
    with open('formatted_data.json', 'w') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    ```

3.  **Explications :**

    *   `json.load(file)` : Charge le contenu JSON du fichier et le convertit en un dictionnaire Python.
    *   `json.dump(data, file, indent=4, ensure_ascii=False)` : Écrit le dictionnaire dans un nouveau fichier avec une indentation de 4 espaces par niveau, améliorant la lisibilité du JSON. `ensure_ascii=False` assure une écriture correcte des caractères non-ASCII (utile pour les textes avec caractères spéciaux).


## Exemple Pratique de Formatage JSON

| Tags |
|------|
| `JSON` `Formatage` `Exemple` |

Si vous disposez d'un fichier `data.json` avec le contenu suivant (sur une seule ligne) :

```json
{"name":"Alice","age":30,"city":"Paris","skills":["Python","Machine Learning"]}
```

Après exécution du script, le contenu de `formatted_data.json` sera :

```json
{
    "name": "Alice",
    "age": 30,
    "city": "Paris",
    "skills": [
        "Python",
        "Machine Learning"
    ]
}
```

Ce format est plus lisible et structuré.


## Prompt "oui/non" en Python

| Tags |
|------|
| `Python` `input` `prompt` `oui/non` |

```python
def demander_confirmation():
    while True:
        reponse = input("Voulez-vous continuer ? (oui/non) : ").strip().lower()
        if reponse in ['oui', 'o', 'yes', 'y']:
            return True
        elif reponse in ['non', 'n', 'no']:
            return False
        else:
            print("Réponse non valide. Veuillez répondre par 'oui' ou 'non'.")

# Exemple d'utilisation :
if demander_confirmation():
    print("Poursuite de l'exécution...")
    # Ajoutez ici le code à exécuter si l'utilisateur choisit de continuer
else:
    print("Exécution arrêtée.")
    # Ajoutez ici le code à exécuter si l'utilisateur choisit de ne pas continuer
```


## Fonction de Confirmation Utilisateur

| Tags |
|------|
| `Python` `Fonction` `Interaction Utilisateur` |

<ol>
<li>
<p><strong>Fonction <code>demander_confirmation</code></strong> :</p>
<ul>
<li>Cette fonction sollicite une réponse "oui" ou "non" de l'utilisateur.</li>
<li><code>strip().lower()</code> est employé pour éliminer les espaces et convertir la réponse en minuscules, améliorant ainsi la flexibilité de l'entrée utilisateur.</li>
<li>Elle renvoie <code>True</code> si l'entrée est "oui", "o", "yes", ou "y".</li>
<li>Elle renvoie <code>False</code> si l'entrée est "non", "n", ou "no".</li>
<li>En cas de réponse invalide, la boucle se répète jusqu'à obtention d'une réponse valide.</li>
</ul>
</li>
<li>
<p><strong>Exemple d'utilisation</strong> :</p>
<ul>
<li>Le programme utilise <code>demander_confirmation()</code> pour contrôler le déroulement de l'exécution. Les différentes sections de code sont exécutées en fonction de la réponse utilisateur.</li>
</ul>
</li>
</ol>


## Contrôle de l'exécution : Exemple pratique

| Tags |
|------|
| `prompt` `exécution` `script` |

Si l'utilisateur entre "oui", le programme continuera son exécution. Si l'utilisateur entre "non", le programme affichera "Exécution arrêtée." et s'arrêtera (ou exécutera un autre bloc de code selon votre choix).

Ce type de prompt est utile pour permettre à l'utilisateur de contrôler l'exécution du programme, en particulier dans les scripts interactifs ou les scripts qui effectuent des actions potentiellement destructrices.
