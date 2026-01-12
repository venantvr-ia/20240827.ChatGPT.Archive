import os
import re


def detect_specific_headers_in_code_blocks(file_path):
    """
    Détecte les titres spécifiques '## Assistant :' et '## User :'
    à l'intérieur des blocs de code délimités par des backticks triples (```).

    :param file_path: Chemin du fichier Markdown à analyser
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    inside_code_block = False
    errors = []

    # Expression régulière pour détecter '## Assistant :' ou '## User :'
    specific_headers_pattern = re.compile(r'^(## (Assistant|User) :)')

    for i, line in enumerate(lines):
        stripped_line = line.rstrip()  # Utilisation de rstrip() pour gérer les espaces et les nouvelles lignes

        # Détection du début ou de la fin d'un bloc de code
        if stripped_line.startswith('```'):
            inside_code_block = not inside_code_block  # Inverser l'état de inside_code_block
            continue  # Passer à la ligne suivante

        # Si on est à l'intérieur d'un bloc de code, chercher les titres spécifiques
        if inside_code_block and specific_headers_pattern.match(stripped_line):
            errors.append(
                f"{file_path} : Ligne {i + 1}: Titre '{stripped_line}' détecté à l'intérieur d'un bloc de code.")

    if errors:
        print(f"{file_path} : Les titres spécifiques ont été détectés à l'intérieur de blocs de code :")
        for error in errors:
            print(error)


def process_markdown_file(file_path):
    """
    Analyse un fichier Markdown pour détecter les titres spécifiques '## Assistant :' et '## User :'
    à l'intérieur de blocs de code délimités par des backticks triples (```).
    Si un bloc de code est détecté sans fermeture, le script ajoute une fermeture de bloc,
    une ligne rouge "INCOMPLET", une ligne vide, et reprend le texte.

    :param file_path: Chemin du fichier Markdown à analyser et modifier
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    inside_code_block = False
    modified_lines = []
    specific_headers_pattern = re.compile(r'^(## (Assistant|User) :)')

    for i, line in enumerate(lines):
        stripped_line = line.rstrip()

        # Détection du début ou de la fin d'un bloc de code
        if stripped_line.startswith('```'):
            inside_code_block = not inside_code_block  # Inverser l'état de inside_code_block
            modified_lines.append(line)
            continue

        # Si on est à l'intérieur d'un bloc de code, chercher les titres spécifiques
        if inside_code_block and specific_headers_pattern.match(stripped_line):
            # Fermer le bloc de code non fermé
            modified_lines.append('```\n')
            modified_lines.append('<span style="color:red">INCOMPLET</span>\n')
            modified_lines.append('\n')  # Ajouter une ligne vide
            inside_code_block = False  # Reset le flag de code block
            # Ajouter la ligne actuelle en dehors du bloc de code
            modified_lines.append(line)
        else:
            # Ajouter la ligne normalement
            modified_lines.append(line)

    # Vérifier si le dernier bloc de code est toujours ouvert
    if inside_code_block:
        modified_lines.append('```\n')
        modified_lines.append('<span style="color:red">INCOMPLET</span>\n')
        modified_lines.append('\n')

    # Écrire les lignes modifiées dans le fichier
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(modified_lines)

    print(f"Le fichier '{file_path}' a été analysé et modifié.")


# Exemple d'utilisation
directory = "../md"  # Remplacez par le chemin de votre fichier Markdown
for root, dirs, files in os.walk(directory):
    for filename in files:
        detect_specific_headers_in_code_blocks("../md/" + filename)
