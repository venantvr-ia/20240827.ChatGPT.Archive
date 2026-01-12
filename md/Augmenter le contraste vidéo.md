## Amélioration du contraste vidéo

| Tags |
|------|
| `vidéo` `traitement d'image` `contraste` `luminosité` |

Pour améliorer le contraste d'une vidéo, plusieurs méthodes peuvent être employées. L'une des approches courantes consiste à ajuster les paramètres de luminosité et de contraste à l'aide d'un logiciel de montage vidéo.

Par exemple, dans FFmpeg, une commande pour ajuster le contraste pourrait ressembler à ceci :

```bash
ffmpeg -i input.mp4 -vf "eq=contrast=2:brightness=0.1" output.mp4
```

Dans cet exemple :

*   `input.mp4` est la vidéo d'entrée.
*   `-vf` spécifie un filtre vidéo.
*   `eq` est le filtre d'égalisation.
*   `contrast=2` augmente le contraste.
*   `brightness=0.1` augmente légèrement la luminosité.
*   `output.mp4` est le fichier de sortie.

D'autres logiciels comme Adobe Premiere Pro, Final Cut Pro ou DaVinci Resolve offrent également des outils similaires pour ajuster le contraste et la luminosité de manière intuitive grâce à des interfaces graphiques.

Il est important de noter que des ajustements trop importants peuvent entraîner une dégradation de la qualité de l'image, avec la perte de détails dans les zones sombres ou claires. Il est donc recommandé de procéder par petites étapes et d'évaluer le résultat visuellement.


## Augmenter le contraste vidéo avec OpenCV en Python

| Tags |
|------|
| `Python` `OpenCV` `traitement vidéo` `contraste` |

Pour augmenter le contraste d'une vidéo en Python, la bibliothèque OpenCV peut être utilisée. L'exemple de code suivant illustre cette opération :

```python
import cv2

# Ouvrir la vidéo en lecture
video_capture = cv2.VideoCapture("nom_de_la_video.mp4")

while True:
    # Lire une image de la vidéo
    ret, frame = video_capture.read()

    if ret:
        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Augmenter le contraste de l'image
        alpha = 1.5 # Facteur de contraste
        beta = 0    # Valeur d'ajustement du contraste
        adjusted = cv2.convertScaleAbs(gray, alpha=alpha, beta=beta)

        # Afficher l'image
        cv2.imshow('Contrast Adjusted Video', adjusted)

        # Attendre une touche
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libérer la capture vidéo et fermer la fenêtre d'affichage
video_capture.release()
cv2.destroyAllWindows()
```

La fonction `cv2.convertScaleAbs()` est utilisée pour ajuster le contraste, en multipliant chaque pixel par un facteur `alpha` et en ajoutant une valeur `beta`. Les valeurs de `alpha` et `beta` permettent de contrôler le niveau de contraste.  Le code traite la vidéo image par image, applique l'ajustement de contraste sur chaque image convertie en niveaux de gris, et affiche le résultat. La boucle se termine lorsque la touche "q" est pressée.


## Installation de la bibliothèque cv2 avec pip

| Tags |
|------|
| `Python` `OpenCV` `cv2` `pip` |

Pour installer la bibliothèque OpenCV (cv2) en Python, utilisez pip, le gestionnaire de packages Python.

1.  Ouvrez une invite de commande ou un terminal.
2.  Exécutez la commande suivante pour installer OpenCV avec pip :

```python
pip install opencv-python
```

3.  Attendez la fin de l'installation. Vérifiez l'installation en important cv2 dans Python :

```python
import cv2
```

Si aucune erreur n'est affichée, l'installation est réussie.

Pour les versions de Python antérieures à 3.6, utilisez :

```python
pip install opencv-python-headless
```

Ceci installe une version d'OpenCV sans interface graphique, adaptée aux serveurs ou aux machines sans interface.


## Redimensionner une vidéo avec OpenCV

| Tags |
|------|
| `OpenCV` `Python` `vidéo` `cv2.resize` |

```python
import cv2

# Ouvrir la vidéo en lecture
video_capture = cv2.VideoCapture("nom_de_la_video.mp4")

# Obtenir les dimensions d'origine de la vidéo
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Définir les nouvelles dimensions
new_width = 640
new_height = 480

while True:
    # Lire une image de la vidéo
    ret, frame = video_capture.read()

    if ret:
        # Redimensionner l'image
        resized = cv2.resize(frame, (new_width, new_height))

        # Afficher l'image
        cv2.imshow('Resized Video', resized)

        # Attendre une touche
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libérer la capture vidéo et fermer la fenêtre d'affichage
video_capture.release()
cv2.destroyAllWindows()
```

La fonction `cv2.resize()` redimensionne chaque image de la vidéo aux dimensions spécifiées (`new_width`, `new_height`). Le code lit la vidéo image par image, la redimensionne, puis affiche le résultat. La boucle s'arrête lorsque la touche "q" est pressée.


##  Causes et solutions de lecture vidéo accélérée

| Tags |
|------|
| `vidéo` `lecture` `codec` `performance` |

Il existe plusieurs raisons pour lesquelles une vidéo peut être jouée en accéléré. Les causes les plus courantes sont les suivantes :

1.  **Problèmes de vitesse de lecture :** La vitesse de lecture vidéo peut être affectée par des paramètres tels que la vitesse de lecture, les propriétés de synchronisation et les codecs. Une configuration incorrecte de ces paramètres peut entraîner une lecture accélérée.

2.  **Erreurs de codage vidéo :** Des erreurs ou des problèmes de compression lors de l'encodage vidéo peuvent provoquer une lecture accélérée. Ces erreurs peuvent résulter d'une mauvaise qualité vidéo ou d'une configuration incorrecte des codecs.

3.  **Problèmes matériels :** Un ordinateur ou un appareil mobile insuffisant en puissance de traitement peut entraîner une lecture accélérée ou saccadée.

4.  **Problèmes de lecteur multimédia :** Un lecteur multimédia défectueux ou incompatible avec le format vidéo peut causer une lecture accélérée.

Pour résoudre ce problème, essayez les solutions suivantes :

1.  Vérifiez et corrigez les paramètres de lecture vidéo.

2.  Testez la vidéo avec un autre lecteur multimédia.

3.  Fermez les applications inutiles pour libérer des ressources système si la puissance de traitement est insuffisante.

4.  Trouvez une version correctement encodée de la vidéo si elle contient des erreurs.


## Faire durer une vidéo 8 secondes avec OpenCV

| Tags |
|------|
| `Python` `OpenCV` `Vidéo` `Traitement d'image` |

Pour faire durer une vidéo 8 secondes lors de sa lecture avec la bibliothèque OpenCV en Python, il est nécessaire de modifier la vitesse de lecture. L'extrait de code suivant illustre cette démarche :

```python
import cv2

# Ouvrir la vidéo en lecture
video_capture = cv2.VideoCapture("nom_de_la_video.mp4")

# Obtenir la fréquence d'images de la vidéo
fps = int(video_capture.get(cv2.CAP_PROP_FPS))

# Définir la durée de lecture souhaitée (en secondes)
duration = 8

# Calculer le nombre total de frames pour la durée de lecture souhaitée
frame_count = int(duration * fps)

while True:
    # Lire une image de la vidéo
    ret, frame = video_capture.read()

    if ret:
        # Afficher l'image
        cv2.imshow('Video', frame)

        # Décrémenter le nombre de frames restantes
        frame_count -= 1

        # Sortir de la boucle lorsque le nombre de frames restantes est égal à zéro
        if frame_count == 0:
            break

        # Attendre la durée d'affichage de chaque image
        cv2.waitKey(int(1000/fps))
    else:
        break

# Libérer la capture vidéo et fermer la fenêtre d'affichage
video_capture.release()
cv2.destroyAllWindows()
```

Le code utilise la variable `duration` définie à 8 secondes. La fréquence d'images (`fps`) est récupérée pour calculer le nombre total de frames nécessaires. La boucle lit et affiche les frames, en décrémentant le compteur. La fonction `cv2.waitKey()` gère la durée d'affichage de chaque frame, permettant ainsi d'atteindre la durée de lecture souhaitée.


## Enregistrer une vidéo modifiée avec OpenCV

| Tags |
|------|
| `OpenCV` `Python` `vidéo` `cv2.VideoWriter` |

```python
import cv2

# Ouvrir la vidéo en lecture
video_capture = cv2.VideoCapture("nom_de_la_video.mp4")

# Obtenir les dimensions d'origine de la vidéo
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Créer un objet VideoWriter pour écrire la vidéo modifiée
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('nom_de_la_video_modifiee.mp4', fourcc, 30, (width, height))

while True:
    # Lire une image de la vidéo
    ret, frame = video_capture.read()

    if ret:
        # Effectuer une modification sur l'image
        # Exemple : Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Écrire l'image modifiée dans la vidéo de sortie
        out.write(gray)

        # Afficher l'image
        cv2.imshow('Modified Video', gray)

        # Attendre une touche
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libérer la capture vidéo, fermer la fenêtre d'affichage et libérer l'objet VideoWriter
video_capture.release()
out.release()
cv2.destroyAllWindows()
```

La classe `cv2.VideoWriter()` est utilisée pour enregistrer la vidéo modifiée. Les paramètres sont :

*   `nom_de_la_video_modifiee.mp4` : Nom du fichier de sortie.
*   `fourcc` : Codec vidéo (mp4v dans l'exemple).
*   `30` : Fréquence d'images (FPS).
*   `(width, height)` : Dimensions de la vidéo.

Une boucle lit chaque frame, applique une modification (ici, conversion en niveaux de gris), écrit la frame modifiée avec `out.write()`, et affiche la frame. La boucle s'arrête en appuyant sur "q". Finalement, les ressources sont libérées.


## Obtenir les dimensions d'une vidéo avec OpenCV

| Tags |
|------|
| `OpenCV` `Python` `vidéo` `dimensions` |

Pour déterminer les dimensions d'une vidéo source en Python, avec la librairie OpenCV, utilisez `cv2.CAP_PROP_FRAME_WIDTH` pour la largeur et `cv2.CAP_PROP_FRAME_HEIGHT` pour la hauteur. L'exemple suivant illustre comment lire une vidéo et afficher ses dimensions :

```python
import cv2

# Ouvrir la vidéo en lecture
video_capture = cv2.VideoCapture("nom_de_la_video.mp4")

# Obtenir les dimensions de la vidéo
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

print("Dimensions de la vidéo d'origine : {}x{}".format(width, height))

while True:
    # Lire une image de la vidéo
    ret, frame = video_capture.read()

    if ret:
        # Afficher l'image
        cv2.imshow('Original Video', frame)

        # Attendre une touche
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libérer la capture vidéo et fermer la fenêtre d'affichage
video_capture.release()
cv2.destroyAllWindows()
```

Le code utilise `cv2.CAP_PROP_FRAME_WIDTH` et `cv2.CAP_PROP_FRAME_HEIGHT` pour récupérer respectivement la largeur et la hauteur. Ces dimensions sont ensuite affichées avec `print()`. La boucle lit et affiche chaque frame jusqu'à l'appui sur la touche "q", puis libère la capture et ferme la fenêtre.


## Dépannage de l'enregistrement vidéo avec cv2.VideoWriter

| Tags |
|------|
| `OpenCV` `Python` `cv2.VideoWriter` `Codec` `Permissions` `Chemin` |

Si des problèmes surviennent lors de l'enregistrement d'une vidéo modifiée via la classe <code>cv2.VideoWriter()</code> en Python, voici les causes possibles et leurs solutions :

1.  **Problèmes de codec :** Le codec utilisé pour la vidéo de sortie peut ne pas être pris en charge. Essayez d'utiliser un autre codec ou format de fichier.

2.  **Problèmes de permission :** Vérifiez que vous avez les droits d'écriture nécessaires pour le dossier cible.

3.  **Problèmes de chemin d'accès :** Assurez-vous que le chemin d'accès à la vidéo de sortie est valide et que le dossier existe.

4.  **Conflits de noms de fichier :** Vérifiez que le nom de fichier spécifié n'existe pas déjà dans le dossier cible.

**Solutions possibles :**

1.  Changez le codec ou le format de fichier de sortie.
2.  Vérifiez et ajustez les permissions d'écriture du dossier cible.
3.  Validez le chemin d'accès à la vidéo de sortie et assurez-vous de l'existence du dossier.
4.  Utilisez un nom de fichier différent pour éviter les conflits.

En cas de persistance du problème, consultez les messages ou codes d'erreur retournés par <code>cv2.VideoWriter()</code> pour une analyse plus approfondie.


## Déterminer le Codec Vidéo avec OpenCV en Python

| Tags |
|------|
| `OpenCV` `Python` `Codec` `Vidéo` |

```python
import cv2

# Ouvrir la vidéo en lecture
video_capture = cv2.VideoCapture("nom_de_la_video.mp4")

# Obtenir le codec de la vidéo
fourcc = int(video_capture.get(cv2.CAP_PROP_FOURCC))

# Convertir le code fourcc en une chaîne de caractères
codec = chr(fourcc & 0xFF) + chr((fourcc >> 8) & 0xFF) + chr((fourcc >> 16) & 0xFF) + chr((fourcc >> 24) & 0xFF)

print("Codec de la vidéo d'origine : {}".format(codec))

while True:
    # Lire une image de la vidéo
    ret, frame = video_capture.read()

    if ret:
        # Afficher l'image
        cv2.imshow('Original Video', frame)

        # Attendre une touche
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libérer la capture vidéo et fermer la fenêtre d'affichage
video_capture.release()
cv2.destroyAllWindows()
```

Ce code utilise la bibliothèque OpenCV pour déterminer le codec d'une vidéo.  La fonction `cv2.CAP_PROP_FOURCC` est employée pour récupérer le code FourCC, une valeur numérique de 32 bits identifiant le codec. Ce code est ensuite converti en une chaîne de caractères pour faciliter son interprétation. Le code inclut également une boucle pour afficher la vidéo et permet à l'utilisateur d'arrêter la lecture avec la touche "q".  Enfin, les ressources sont libérées correctement.


## Enregistrer une vidéo sans codec avec OpenCV

| Tags |
|------|
| `OpenCV` `Python` `vidéo` `codec` `cv2.VideoWriter` |

Il est recommandé d'utiliser un codec pour enregistrer une vidéo afin de la compresser et de réduire sa taille. Cependant, il est possible d'enregistrer une vidéo sans codec avec la bibliothèque OpenCV en Python, via la méthode `cv2.VideoWriter()` en définissant le paramètre `isColor` sur False. Cela permet d'enregistrer une vidéo en niveaux de gris sans codec.

Voici un exemple de code qui lit une vidéo, la convertit en niveaux de gris et l'enregistre sans codec :

```python
import cv2

# Ouvrir la vidéo en lecture
video_capture = cv2.VideoCapture("nom_de_la_video.mp4")

# Obtenir les dimensions d'origine de la vidéo
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Créer un objet VideoWriter pour écrire la vidéo modifiée
out = cv2.VideoWriter('nom_de_la_video_modifiee.avi', cv2.VideoWriter_fourcc('M','J','P','G'), 30.0, (width, height), isColor=False)

while True:
    # Lire une image de la vidéo
    ret, frame = video_capture.read()

    if ret:
        # Convertir l'image en niveaux de gris
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Écrire l'image dans la vidéo de sortie
        out.write(gray)

        # Afficher l'image
        cv2.imshow('Modified Video', gray)

        # Attendre une touche
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libérer la capture vidéo, fermer la fenêtre d'affichage et libérer l'objet VideoWriter
video_capture.release()
out.release()
cv2.destroyAllWindows()
```

Dans ce code, le paramètre `isColor` est défini sur False lors de la création de l'objet `cv2.VideoWriter()`. Cela permet d'enregistrer la vidéo en niveaux de gris sans utiliser de codec. Le paramètre `fourcc` est toujours utilisé pour spécifier un codec, mais dans ce cas, il est spécifié comme `'MJPG'` pour indiquer que la vidéo doit être enregistrée sans compression.

Ensuite, une boucle est utilisée pour lire chaque image de la vidéo, convertir l'image en niveaux de gris, écrire l'image dans la vidéo de sortie à l'aide de la méthode `out.write()`, puis afficher l'image modifiée dans une fenêtre. La boucle se termine lorsque l'utilisateur appuie sur la touche "q".

Enfin, les objets `video_capture`, `out` et la fenêtre d'affichage sont libérés à l'aide des méthodes `release()` et `cv2.destroyAllWindows()`.


## Capturer 10 images PNG de qualité maximale avec OpenCV

| Tags |
|------|
| `Python` `OpenCV` `PNG` `Vidéo` |

```python
import cv2

# Ouvrir la vidéo en lecture
video_capture = cv2.VideoCapture("nom_de_la_video.mp4")

# Obtenir la fréquence d'images de la vidéo
fps = video_capture.get(cv2.CAP_PROP_FPS)

# Obtenir les dimensions d'origine de la vidéo
width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Calculer l'intervalle entre chaque image (en nombre de frames)
interval = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT) / 10)

# Initialiser le compteur de frames
frame_count = 0

while True:
    # Lire une image de la vidéo
    ret, frame = video_capture.read()

    if ret:
        # Vérifier si c'est le moment de capturer une image
        if frame_count % interval == 0:
            # Définir le nom de fichier pour l'image
            filename = "image_{}.png".format(int(frame_count / interval))

            # Enregistrer l'image en tant qu'image PNG qualité maximale
            cv2.imwrite(filename, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])

        # Incrémenter le compteur de frames
        frame_count += 1

        # Afficher l'image
        cv2.imshow('Original Video', frame)

        # Attendre une touche
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Libérer la capture vidéo et fermer la fenêtre d'affichage
video_capture.release()
cv2.destroyAllWindows()
```


## Estimer un coefficient de fuite avec OpenCV

| Tags |
|------|
| `OpenCV` `Python` `Perspective` `HoughLinesP` `np.polyfit` |

Pour estimer le coefficient de fuite en perspective fuyante avec OpenCV et Python, la méthode <code>cv2.HoughLinesP()</code> est utilisée pour détecter les lignes dans l'image. Ensuite, <code>np.polyfit()</code> est utilisé pour ajuster une ligne de régression aux points détectés, permettant d'estimer le coefficient de fuite.

Exemple de code :

```python
import cv2
import numpy as np

# Charger l'image
img = cv2.imread('image.png')

# Convertir l'image en niveaux de gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Appliquer un flou gaussien à l'image
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Détecter les lignes dans l'image à l'aide de la méthode cv2.HoughLinesP()
lines = cv2.HoughLinesP(blur, 1, np.pi / 180, 50, minLineLength=100, maxLineGap=50)

# Ajuster une ligne de régression aux points détectés
x = []
y = []
for line in lines:
    for x1, y1, x2, y2 in line:
        x += [x1, x2]
        y += [y1, y2]
fit = np.polyfit(x, y, 1)

# Dessiner la ligne de régression sur l'image
cv2.line(img, (0, int(fit[1])), (img.shape[1], int(fit[0] * img.shape[1] + fit[1])), (0, 0, 255), 2)

# Estimer le coefficient de fuite
angle = np.arctan(fit[0]) * 180 / np.pi

print("Coefficient de fuite : {:.2f} degrés".format(angle))

# Afficher l'image avec la ligne de régression
cv2.imshow('Perspective Fuyante', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Le code charge l'image avec <code>cv2.imread()</code>, la convertit en niveaux de gris avec <code>cv2.cvtColor()</code>, et applique un flou gaussien via <code>cv2.GaussianBlur()</code> pour réduire le bruit. <code>cv2.HoughLinesP()</code> détecte les lignes, avec des paramètres pour le filtrage.  <code>np.polyfit()</code> est utilisé pour l'ajustement de la ligne de régression. Le coefficient de fuite est ensuite estimé à partir de la pente de la ligne. L'image avec la ligne de régression est affichée avec <code>cv2.imshow()</code>.


## Calcul d'homothétie en perspective fuyante avec OpenCV

| Tags |
|------|
| `OpenCV` `Python` `Perspective` `Homothétie` `Transformation` |

Pour calculer l'homothétie dans une perspective fuyante en utilisant la bibliothèque OpenCV en Python, la méthode `cv2.getPerspectiveTransform()` calcule la matrice de transformation. Cette matrice transforme une image en une autre avec une perspective différente.  Elle est ensuite utilisée avec `cv2.warpPerspective()` pour appliquer l'homothétie.

Exemple de code :

```python
import cv2
import numpy as np

# Charger l'image
img = cv2.imread('image.png')

# Définir les points de la zone d'intérêt (ROI)
src = np.float32([[30, 100], [400, 100], [200, 350], [500, 350]])

# Définir les points de destination
dst = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# Calculer la matrice de transformation
M = cv2.getPerspectiveTransform(src, dst)

# Appliquer l'homothétie à l'image à l'aide de la méthode cv2.warpPerspective()
warped_img = cv2.warpPerspective(img, M, (300, 300))

# Afficher l'image originale et l'image homothétique
cv2.imshow('Original', img)
cv2.imshow('Warped', warped_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

Dans ce code, `src` (tableau numpy 4x2) définit la ROI dans l'image d'origine. `dst` (tableau numpy 4x2) définit les points de destination. `cv2.getPerspectiveTransform()` calcule la matrice de transformation `M`. `cv2.warpPerspective()` applique l'homothétie.  Enfin, les images sont affichées avec `cv2.imshow()`, et la fonction `cv2.waitKey()` et `cv2.destroyAllWindows()` gèrent l'interaction utilisateur et la fermeture des fenêtres.
