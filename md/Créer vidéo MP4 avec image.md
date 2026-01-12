## Création de vidéo MP4 à partir d'une image

| Tags |
|------|
| `FFmpeg` `MP4` `Vidéo` `Image` |

Pour créer une vidéo MP4 à partir d'une image fixe, vous pouvez utiliser FFmpeg. Voici une commande type :

```bash
ffmpeg -loop 1 -i image.jpg -c:v libx264 -t 10 -pix_fmt yuv420p video.mp4
```

Cette commande effectue les opérations suivantes :

*   `-loop 1` :  Boucle l'image d'entrée.
*   `-i image.jpg` : Spécifie le fichier image d'entrée.
*   `-c:v libx264` :  Spécifie le codec vidéo (libx264 pour le format MP4).
*   `-t 10` : Définit la durée de la vidéo à 10 secondes.
*   `-pix_fmt yuv420p` : Définit le format de pixel (compatible avec de nombreux lecteurs).
*   `video.mp4` : Spécifie le nom du fichier vidéo de sortie.

Remplacez `image.jpg` par le nom de votre fichier image et ajustez la durée (`-t`) selon vos besoins.  La vidéo résultante sera enregistrée sous le nom `video.mp4`.


## Créer une vidéo Python avec moviepy

| Tags |
|------|
| `Python` `moviepy` `vidéo` `image` `MP4` |

Pour créer une vidéo en Python qui combine un fichier MP4 à gauche et une image statique à droite, utilisez des bibliothèques telles que `moviepy`. Procédez comme suit :

1.  **Installation des bibliothèques nécessaires** : Si vous n'avez pas installé `moviepy`, installez-le avec `pip` :

    ```bash
    pip install moviepy
    ```

2.  **Écriture du script** : Chargez la vidéo et l'image, ajustez-les à la même hauteur, puis combinez-les côte à côte. Exemple :

    ```python
    from moviepy.editor import VideoFileClip, ImageClip, clips_array

    # Chargement de la vidéo
    video_clip = VideoFileClip("chemin/vers/votre/video.mp4")

    # Chargement de l'image et conversion en clip vidéo avec la même durée que le clip vidéo
    image_clip = ImageClip("chemin/vers/votre/image.jpg").set_duration(video_clip.duration)

    # Redimensionnement de l'image pour qu'elle ait la même hauteur que la vidéo
    image_clip = image_clip.resize(height=video_clip.size[1])

    # Création d'un clip composite avec la vidéo à gauche et l'image à droite
    final_clip = clips_array([[video_clip, image_clip]])

    # Exportation du résultat en un fichier MP4
    final_clip.write_videofile("video_finale.mp4", codec='libx264')
    ```

3.  **Exécution du script** : Exécutez le script dans votre environnement Python en vérifiant les chemins d'accès aux fichiers.

Ce script charge la vidéo et l'image, les redimensionne, et les assemble côte à côte. Il exporte ensuite le résultat en MP4. Pour des ajustements supplémentaires, explorez les options de `moviepy` (format de sortie, qualité, manipulation des clips).
