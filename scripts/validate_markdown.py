import os
import re


def check_markdown_structure(file_path):
    """
    Vérifie la cohérence de la structure d'un fichier Markdown.

    :param file_path: Chemin du fichier Markdown à vérifier
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    errors = []

    # Variables de vérification des titres
    last_header_level = 0

    # Expressions régulières pour différentes vérifications
    header_pattern = re.compile(r'^(#+) ')
    bold_italic_pattern = re.compile(r'(\*\*.*?\*\*|__.*?__|_.*?_|~~.*?~~)')
    link_image_pattern = re.compile(r'(!?\[.*?]\(.*?\))')

    for i, line in enumerate(lines):
        line = line.strip()

        # Vérification des titres
        header_match = header_pattern.match(line)
        if header_match:
            current_header_level = len(header_match.group(1))
            if current_header_level > last_header_level + 1:
                errors.append(
                    f"Ligne {i + 1}: Titre de niveau {current_header_level} sans titre de niveau {current_header_level - 1} précédent.")
            last_header_level = current_header_level

        # Vérification des balises de formatage (bold, italic, strikethrough)
        for match in re.findall(bold_italic_pattern, line):
            if match.count('**') % 2 != 0 or match.count('__') % 2 != 0 or match.count('_') % 2 != 0 or match.count(
                    '~~') % 2 != 0:
                errors.append(f"Ligne {i + 1}: Balise de formatage incorrecte détectée.")

        # Vérification des liens et des images
        for match in re.findall(link_image_pattern, line):
            if match.count('[') != match.count(']') or match.count('(') != match.count(')'):
                errors.append(f"Ligne {i + 1}: Lien ou image mal formatté détecté.")

    if errors:
        print("Des incohérences ont été trouvées dans le fichier Markdown :")
        for error in errors:
            print(error)
    else:
        print("Le fichier Markdown est structurellement cohérent.")


# Exemple d'utilisation
directory = "../md"  # Remplacez par le chemin de votre fichier Markdown
for root, dirs, files in os.walk(directory):
    for filename in files:
        check_markdown_structure("../md/" + filename)
