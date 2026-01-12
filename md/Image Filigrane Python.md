## Filigrane d'image en Python

| Tags |
|------|
| `Python` `Image` `Filigrane` |

Ce document présente une méthode pour ajouter un filigrane à une image en utilisant Python.

```python
from PIL import Image

def ajouter_filigrane(image_source, filigrane, position, opacite):
    """
    Ajoute un filigrane à une image.

    Args:
        image_source (str): Chemin vers l'image source.
        filigrane (str): Chemin vers le fichier filigrane.
        position (tuple): Position du filigrane (x, y).
        opacite (float): Opacité du filigrane (0.0 à 1.0).

    Returns:
        Image: L'image avec le filigrane.
    """
    try:
        image = Image.open(image_source).convert("RGBA")
        filigrane_image = Image.open(filigrane).convert("RGBA")
    except FileNotFoundError as e:
        print(f"Erreur lors de l'ouverture des images : {e}")
        return None

    # Redimensionner le filigrane si nécessaire
    largeur_filigrane, hauteur_filigrane = filigrane_image.size
    if largeur_filigrane > image.width or hauteur_filigrane > image.height:
        filigrane_image = filigrane_image.resize((image.width // 4, image.height // 4))  # Redimensionnement arbitraire

    # Appliquer l'opacité
    filigrane_image = filigrane_image.resize(image.size)
    filigrane_data = filigrane_image.getdata()
    nouveau_filigrane_data = []
    for item in filigrane_data:
        # Appliquer l'opacité au canal alpha
        nouveau_filigrane_data.append((item[0], item[1], item[2], int(item[3] * opacite)))
    filigrane_image.putdata(nouveau_filigrane_data)

    # Coller le filigrane sur l'image source
    image.paste(filigrane_image, position, filigrane_image)

    return image


# Exemple d'utilisation
if __name__ == "__main__":
    image_source = "image_source.png"  # Remplacez par le chemin de votre image source
    filigrane = "filigrane.png"  # Remplacez par le chemin de votre filigrane
    position = (0, 0)  # Position du filigrane (coin supérieur gauche)
    opacite = 0.5  # Opacité du filigrane (0.0 à 1.0)

    image_avec_filigrane = ajouter_filigrane(image_source, filigrane, position, opacite)

    if image_avec_filigrane:
        try:
            image_avec_filigrane.save("image_avec_filigrane.png")  # Enregistre l'image résultante
            print("Filigrane ajouté avec succès!")
        except IOError:
            print("Erreur lors de l'enregistrement de l'image.")
```

**Explication du code :**

1.  **Importation :** Le code commence par importer la bibliothèque `PIL` (Pillow), qui est une bibliothèque d'imagerie Python.
2.  **Fonction `ajouter_filigrane()` :**
    *   Prend en entrée le chemin de l'image source, le chemin du fichier filigrane, la position du filigrane et l'opacité.
    *   Ouvre les deux images. Gère les erreurs potentielles de fichiers non trouvés.
    *   Redimensionne le filigrane s'il est trop grand.
    *   Applique l'opacité au filigrane en ajustant le canal alpha de chaque pixel.
    *   Colle le filigrane sur l'image source à la position spécifiée.
    *   Retourne l'image modifiée.
3.  **Bloc `if __name__ == "__main__":` :**
    *   Définit les chemins des fichiers source et filigrane, la position et l'opacité du filigrane.  Ces valeurs doivent être adaptées à vos propres images.
    *   Appelle la fonction `ajouter_filigrane()` pour créer l'image avec filigrane.
    *   Enregistre l'image résultante dans un nouveau fichier. Gère les erreurs potentielles d'écriture de fichier.

**Pour utiliser le code :**

1.  **Installation de Pillow :**  Si vous ne l'avez pas déjà, installez la bibliothèque Pillow :  `pip install Pillow`
2.  **Préparation des images :**  Assurez-vous d'avoir une image source et une image filigrane (de préférence avec un fond transparent, format PNG).
3.  **Modification du code :**  Modifiez les variables `image_source`, `filigrane`, `position` et `opacite` dans le bloc `if __name__ == "__main__":` pour correspondre à vos images et à vos préférences.
4.  **Exécution du script :** Exécutez le script Python. L'image avec filigrane sera enregistrée dans un nouveau fichier.


## Charger une image et ajouter un filigrane en Python

| Tags |
|------|
| `Python` `PIL` `Pillow` `Image` `Filigrane` |

```python
from PIL import Image, ImageDraw, ImageFont

# Charger l'image
image = Image.open("chemin/vers/votre/image.jpg")

# Créer un objet ImageDraw
draw = ImageDraw.Draw(image)

# Définir le texte du filigrane et la police
texte_filigrane = "Mon filigrane"
police = ImageFont.truetype("chemin/vers/votre/police.ttf", 40)

# Définir les coordonnées de départ pour le filigrane en diagonale
x = 0
y = 0

# Ajouter le filigrane en diagonale
largeur, hauteur = image.size
while y < hauteur:
    draw.text((x, y), texte_filigrane, fill=(255, 255, 255), font=police)
    x += 10  # Décalage horizontal
    y += 10  # Décalage vertical

# Enregistrer l'image avec le filigrane
image.save("chemin/vers/votre/image_avec_filigrane.jpg")
```

Assurez-vous de remplacer "chemin/vers/votre/image.jpg" par le chemin d'accès à votre propre image, et "chemin/vers/votre/police.ttf" par le chemin d'accès à la police TrueType que vous souhaitez utiliser pour le filigrane.

Ce code ouvre l'image spécifiée, crée un objet ImageDraw pour dessiner sur l'image, définit le texte et la police pour le filigrane, puis ajoute le filigrane en diagonale en itérant sur les coordonnées (x, y) avec des décalages horizontaux et verticaux. Enfin, l'image modifiée est enregistrée sous un nouveau nom.
