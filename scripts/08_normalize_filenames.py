import os


def normalize_filename_spaces(directory):
    """
    Scanne le répertoire donné et renomme les fichiers en supprimant
    les espaces multiples dans leur nom, ne conservant qu'un seul espace.

    :param directory: Chemin du répertoire à scanner
    """
    # Itérer sur tous les fichiers et dossiers du répertoire
    for root, dirs, files in os.walk(directory):
        for filename in files:
            # Vérifier s'il y a plusieurs espaces consécutifs dans le nom du fichier
            if '  ' in filename:
                # Nouveau nom avec les espaces multiples réduits à un seul espace
                new_filename = ' '.join(filename.split())

                # Chemin complet du fichier actuel et du nouveau fichier
                old_path = os.path.join(root, filename)
                new_path = os.path.join(root, new_filename)

                # Renommer le fichier
                os.rename(old_path, new_path)
                print(f"Renommé : '{old_path}' -> '{new_path}'")

        # Vous pouvez également renommer les dossiers si vous le souhaitez
        for dirname in dirs:
            if '  ' in dirname:
                new_dirname = ' '.join(dirname.split())
                old_dirpath = os.path.join(root, dirname)
                new_dirpath = os.path.join(root, new_dirname)
                os.rename(old_dirpath, new_dirpath)
                print(f"Renommé le dossier : '{old_dirpath}' -> '{new_dirpath}'")


directory_to_scan = "../md"  # Remplacez par le chemin de votre répertoire
normalize_filename_spaces(directory_to_scan)
