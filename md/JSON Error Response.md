## Erreurs de réponse JSON

| Tags |
|------|
| `JSON` `Erreur` `API` |

Dans le contexte d'une API, les erreurs sont souvent formatées en JSON pour faciliter l'analyse par les applications clientes. Voici un exemple de structure courante :

```json
{
  "code": "400",
  "status": "Bad Request",
  "message": "Le paramètre 'id' est invalide",
  "details": [
    {
      "field": "id",
      "message": "L'identifiant doit être un entier positif."
    }
  ]
}
```

*   **`code`**: Code d'état HTTP.
*   **`status`**: Description du code d'état HTTP.
*   **`message`**: Message d'erreur général.
*   **`details`**: Liste d'erreurs spécifiques aux champs (optionnel).

L'exemple suivant montre une réponse d'erreur 401 (Non autorisé) :

```json
{
  "code": "401",
  "status": "Unauthorized",
  "message": "Authentification requise",
  "details": []
}
```

**Exemple d'implémentation Python (Flask):**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/resource/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    if resource_id <= 0:
        response = jsonify({
            "code": "400",
            "status": "Bad Request",
            "message": "ID invalide",
            "details": [{
                "field": "resource_id",
                "message": "L'ID doit être supérieur à 0"
            }]
        })
        response.status_code = 400
        return response

    # Logique pour récupérer la ressource
    return jsonify({"id": resource_id, "data": "Quelques données"})

if __name__ == '__main__':
    app.run(debug=True)
```

Dans cet exemple, si l'ID de la ressource est invalide, l'API renvoie une réponse JSON d'erreur avec le code d'état HTTP 400.

**Bonnes pratiques :**

*   **Cohérence :** Utiliser un format JSON cohérent pour toutes les erreurs.
*   **Clarté :** Fournir des messages d'erreur clairs et précis.
*   **Détails :** Inclure des détails pertinents pour aider le développeur à identifier et corriger l'erreur.
*   **Codes d'état HTTP :** Utiliser les codes d'état HTTP appropriés pour indiquer le type d'erreur.

**Exemple d'utilisation de cURL :**

Pour tester, on peut utiliser cURL :

```bash
curl -i -X GET http://[IP]:5000/resource/-1
```

La commande ci-dessus renverra une réponse d'erreur 400 avec le format JSON défini dans l'application Flask.

**Remarques :**

*   Les logs du serveur contiennent également des informations utiles pour le débogage.
*   L'intégration d'un système de monitoring permet de détecter et de gérer les erreurs plus efficacement.


## Formatage d'un payload JSON

| Tags |
|------|
| `JSON` `payload` `erreur HTTP` |

Voici un exemple de payload JSON indiquant une erreur 403 avec le message "presque" :

```json
{
  "error": 403,
  "message": "presque"
}
```

Ce payload simple et clair indique l'erreur HTTP 403 (Forbidden) avec le message d'erreur "presque".


## Formatage d'un payload JSON d'erreur

| Tags |
|------|
| `JSON` `erreur` `403` |

Voici un exemple de payload JSON illustrant une erreur 403 avec les messages spécifiés :

```json
{
  "error": {
    "code": 403,
    "messages": [
      "encore un GUID",
      "note-le dans ton cahier, il est important celui-là"
    ]
  }
}
```
