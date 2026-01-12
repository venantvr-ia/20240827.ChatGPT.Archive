## Nettoyage de noms de fichiers

| Tags |
|------|
| `Python` `nettoyage` `fichiers` |

Le script Python suivant nettoie les noms de fichiers dans un répertoire donné. Il remplace les caractères spéciaux et les espaces par des underscores.

```python
import os
import re

def nettoyer_nom_fichier(nom_fichier):
    """
    Nettoie un nom de fichier en remplaçant les caractères spéciaux et les espaces.
    """
    nom_sans_extension, extension = os.path.splitext(nom_fichier)
    nom_nettoye = re.sub(r'[^a-zA-Z0-9_.-]', '_', nom_sans_extension)
    nom_nettoye = re.sub(r'\s+', '_', nom_nettoye)
    return nom_nettoye + extension

def nettoyer_fichiers_dans_repertoire(repertoire):
    """
    Nettoie les noms de fichiers dans un répertoire.
    """
    for nom_fichier in os.listdir(repertoire):
        chemin_fichier = os.path.join(repertoire, nom_fichier)
        if os.path.isfile(chemin_fichier):
            nom_nettoye = nettoyer_nom_fichier(nom_fichier)
            if nom_nettoye != nom_fichier:
                nouveau_chemin_fichier = os.path.join(repertoire, nom_nettoye)
                try:
                    os.rename(chemin_fichier, nouveau_chemin_fichier)
                    print(f"Renommage de '{nom_fichier}' en '{nom_nettoye}'")
                except OSError as e:
                    print(f"Erreur lors du renommage de '{nom_fichier}': {e}")

# Exemple d'utilisation
if __name__ == "__main__":
    repertoire_a_nettoyer = "./dossier_a_nettoyer"  # Remplacez par le répertoire souhaité
    if not os.path.exists(repertoire_a_nettoyer):
        os.makedirs(repertoire_a_nettoyer)  # Crée le répertoire s'il n'existe pas
        print(f"Répertoire '{repertoire_a_nettoyer}' créé.")
    nettoyer_fichiers_dans_repertoire(repertoire_a_nettoyer)
    print("Nettoyage terminé.")
```

Pour utiliser ce script:

1.  **Enregistrez le script :** Sauvegardez le code dans un fichier nommé, par exemple, `nettoyer_fichiers.py`.
2.  **Modifiez le répertoire :** Changez la variable `repertoire_a_nettoyer` dans le script avec le chemin du répertoire contenant les fichiers à nettoyer.
3.  **Exécutez le script :** Ouvrez un terminal ou une invite de commandes, naviguez jusqu'au répertoire où vous avez enregistré le script et exécutez-le en utilisant la commande `python nettoyer_fichiers.py`.

Ce script est conçu pour être exécuté sur différents systèmes d'exploitation. Assurez-vous d'avoir Python installé sur votre système. Ce script utilise les modules `os` et `re` qui font partie de la bibliothèque standard de Python. Aucune installation supplémentaire n'est requise.


## Nettoyage de noms de fichiers en PHP

| Tags |
|------|
| `PHP` `regex` `preg_replace` `string manipulation` |

Pour nettoyer un nom de fichier en PHP, en ne conservant que les caractères alphanumériques (a-zA-Z0-9), utilisez les expressions régulières et la fonction <code>preg_replace()</code>.

Voici une fonction prenant un nom de fichier en entrée et renvoyant le nom nettoyé :

```php
function sanitizeFilename($filename) {
    // Remplace tous les caractères non alphanumériques par une chaîne vide
    $sanitizedFilename = preg_replace('/[^a-zA-Z0-9]/', '', $filename);
    
    return $sanitizedFilename;
}

// Exemple d'utilisation
$filename = "fichier_@#àé&%$nom.txt";
$sanitizedFilename = sanitizeFilename($filename);

echo $sanitizedFilename;  // affiche "fichieraenom.txt"
```

La fonction <code>preg_replace('/[^a-zA-Z0-9]/', '', $filename)</code> utilise une expression régulière (<code>/[^a-zA-Z0-9]/</code>) pour rechercher tous les caractères qui ne sont pas des lettres ou des chiffres, et les remplace par une chaîne vide.

Pour remplacer les caractères non alphanumériques par un autre caractère (par exemple, un tiret bas), modifiez la fonction comme suit :

```php
function sanitizeFilename($filename) {
    // Remplace tous les caractères non alphanumériques par un tiret bas
    $sanitizedFilename = preg_replace('/[^a-zA-Z0-9]/', '_', $filename);
    
    return $sanitizedFilename;
}

// Exemple d'utilisation
$filename = "fichier_@#àé&%$nom.txt";
$sanitizedFilename = sanitizeFilename($filename);

echo $sanitizedFilename;  // affiche "fichier_aenom.txt"
```
