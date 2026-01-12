## Lister les fichiers supprimés dans Git

| Tags |
|------|
| `Git` `fichiers supprimés` `historique` |

Pour lister les fichiers supprimés dans Git, plusieurs méthodes sont disponibles.

**Méthode 1 : Utilisation de `git log --diff-filter=D --summary`**

Cette commande affiche le journal des commits, filtré pour afficher uniquement les suppressions (D pour Deleted) et un résumé des modifications.

```bash
git log --diff-filter=D --summary
```

**Méthode 2 : Utilisation de `git diff --name-only --diff-filter=D <commit>`**

Cette commande affiche les noms des fichiers supprimés dans un commit spécifique. Remplacez `<commit>` par l'identifiant du commit, par exemple, `HEAD` pour le dernier commit.

```bash
git diff --name-only --diff-filter=D HEAD
```

Pour afficher les fichiers supprimés sur une plage de commits :

```bash
git diff --name-only --diff-filter=D <commit1> <commit2>
```

**Méthode 3 : Utilisation de `git ls-tree -r -d --name-only <commit>`**

Cette commande liste les fichiers supprimés en affichant l'arborescence d'un commit spécifique et en filtrant les entrées de type "blob" (fichiers).

```bash
git ls-tree -r -d --name-only HEAD
```

**Exemple concret**

Supposons que vous ayez supprimé un fichier nommé `mon_fichier.txt`.  Après avoir exécuté une des commandes ci-dessus (en adaptant l'identifiant du commit), vous devriez voir `mon_fichier.txt` listé dans la sortie.

**Note** :  Ces commandes n'affichent pas les fichiers qui ont été supprimés et ensuite ajoutés dans le même commit. Dans ce cas, il faudrait analyser les modifications complètes du commit.


## Lister les fichiers supprimés sur GitHub

| Tags |
|------|
| `Git` `GitHub` `Ligne de commande` `git log` |

Pour lister les fichiers supprimés depuis une date donnée sur GitHub, utilisez Git en ligne de commande.

1.  **Cloner ou naviguer vers le dépôt local :**

    Si le dépôt n'est pas cloné, exécutez :

    ```bash
    git clone <url_du_depot>
    cd <nom_du_depot>
    ```

    Sinon, accédez au répertoire du dépôt.

2.  **Utiliser la commande `git log` :**

    La commande `git log` avec les options appropriées permet d'afficher l'historique des commits filtré sur les fichiers supprimés depuis une date donnée :

    ```bash
    git log --diff-filter=D --since="YYYY-MM-DD" --name-only --pretty=format:
    ```

    *   `--diff-filter=D` : filtre les suppressions.
    *   `--since="YYYY-MM-DD"` : filtre par date.
    *   `--name-only` : affiche les noms de fichiers.
    *   `--pretty=format:` : sortie compacte.

    Exemple : lister les fichiers supprimés depuis le 1er janvier 2023 :

    ```bash
    git log --diff-filter=D --since="2023-01-01" --name-only --pretty=format:
    ```

3.  **Analyser les résultats :**

    La commande renvoie une liste des fichiers supprimés depuis la date spécifiée.

    Exemple de sortie :

    ```
    src/old_file1.txt
    docs/obsolete_file.md
    tests/deprecated_test.py
    ```


## Identifier les fichiers supprimés avec Git

| Tags |
|------|
| `Git` `suppression` `historique` `commande` |

Imaginons un dépôt où plusieurs fichiers ont été supprimés depuis le début de l'année 2023. L'exécution de la commande suivante permet d'identifier ces fichiers :

```bash
git log --diff-filter=D --since="2023-01-01" --name-only --pretty=format:
```

La sortie résultante pourrait ressembler à ceci :

```
src/deprecated_functionality.js
docs/old_readme.md
config/unused_config.json
```

Cette sortie indique que les fichiers listés ont été supprimés après le 1er janvier 2023.


## Affichage avancé des résultats Git

| Tags |
|------|
| `Git` `Commandes Git` `Affichage` |

Si vous souhaitez inclure des détails supplémentaires dans les résultats, tels que les messages de commit ou les dates de commit, vous pouvez modifier le format de sortie. Exemple :

```bash
git log --diff-filter=D --since="2023-01-01" --name-status
```

Cette commande affiche les fichiers supprimés et les informations de commit associées.


## Lister les fichiers supprimés avec Git

| Tags |
|------|
| `Git` `suppression de fichiers` `historique` |

Utiliser Git pour lister les fichiers supprimés depuis une date donnée est une compétence précieuse pour comprendre l'historique des modifications dans un projet. Cela peut aider à suivre les changements importants et à gérer efficacement le code dans votre dépôt.


## Lister les chemins des fichiers supprimés avec Git

| Tags |
|------|
| `Git` `commande` `fichier supprimé` |

Pour obtenir uniquement le chemin et le nom des fichiers supprimés depuis une date donnée, utilisez la commande Git suivante dans votre terminal. Cette commande filtre et affiche uniquement les noms des fichiers supprimés :

```bash
git log --diff-filter=D --since="YYYY-MM-DD" --name-only --pretty=format:
```

Par exemple, pour lister les fichiers supprimés depuis le 1er janvier 2023 :

```bash
git log --diff-filter=D --since="2023-01-01" --name-only --pretty=format:
```

Cette commande génère une liste des fichiers supprimés depuis la date spécifiée, en affichant leurs chemins et noms. Exemple de sortie :

```
src/old_file1.txt
docs/obsolete_file.md
tests/deprecated_test.py
```

La sortie affiche uniquement les chemins et noms des fichiers supprimés.


## Lister les fichiers réellement supprimés

| Tags |
|------|
| `git` `bash` `script` `deleted files` |

Pour lister les fichiers supprimés depuis une date donnée et qui n'ont pas été réintroduits, suivez les étapes suivantes :

<ol>
<li>
<strong>Lister les fichiers supprimés depuis une date donnée :</strong>
Utilisez la commande <code>git log</code> pour lister les fichiers supprimés depuis une date donnée.
</li>
<li>
<strong>Vérifier l'existence actuelle des fichiers :</strong>
Filtrez la liste pour ne garder que les fichiers qui n'existent plus dans la branche actuelle.
</li>
</ol>
Voici un script Bash pour accomplir cela :

```bash
#!/bin/bash

# Date à partir de laquelle vous souhaitez commencer à lister les fichiers supprimés
START_DATE="2023-01-01"

# Lister les fichiers supprimés depuis la date donnée
deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format:)

# Filtrer les fichiers qui n'existent plus dans la branche actuelle
for file in $deleted_files; do
    if [ ! -e "$file" ]; then
        echo "$file"
    fi
done
```

Vous pouvez enregistrer ce script dans un fichier, par exemple <code>list_deleted_files.sh</code>, puis le rendre exécutable et l'exécuter :

```bash
chmod +x list_deleted_files.sh
./list_deleted_files.sh
```

Ce script effectue les actions suivantes :

<ol>
<li>Utilise <code>git log</code> pour obtenir la liste des fichiers supprimés depuis la date spécifiée.</li>
<li>Vérifie, pour chaque fichier, s'il existe dans le répertoire actuel.</li>
<li>Affiche uniquement les fichiers qui n'existent plus.</li>
</ol>


## Explication des commandes Git

| Tags |
|------|
| `git` `commandes` `suppression` `scripts` |

*   `git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format:` : Liste les fichiers supprimés depuis `START_DATE`.
*   `for file in $deleted_files; do ... done` : Boucle sur chaque fichier supprimé.
*   `if [ ! -e "$file" ]; then ... fi` : Vérifie si le fichier n'existe pas dans le répertoire actuel.
*   `echo "$file"` : Affiche le chemin et le nom du fichier qui n'existe plus.

Ces commandes fournissent une liste des fichiers supprimés qui n'ont pas été réintroduits dans la branche actuelle.


## Empêcher le découpage des noms de fichiers

| Tags |
|------|
| `git` `bash` `script` `nom de fichier` |

Pour gérer les noms de fichiers contenant des espaces et éviter qu'ils ne soient coupés sur plusieurs lignes, il faut adapter le script pour qu'il traite correctement ces noms. Voici une version modifiée du script :

```bash
#!/bin/bash

# Date de début pour lister les fichiers supprimés
START_DATE="2023-01-01"

# Lister les fichiers supprimés depuis la date donnée, gérant les espaces
deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format: | tr '\n' '\0')

# Filtrer les fichiers qui n'existent plus dans la branche actuelle
echo "$deleted_files" | xargs -0 -I {} sh -c '[ ! -e "{}"] && echo "{}"'
```


## Explication des modifications de fichiers

| Tags |
|------|
| `shell` `xargs` `linux` |

La section décrit les modifications apportées à un script.

*   `tr '\n' '\0'` : Remplace les nouvelles lignes par des caractères nuls (`\0`). Cette opération est utile pour gérer correctement les fichiers contenant des espaces.
*   `echo "$deleted_files" | xargs -0 -I {} sh -c '[ ! -e "{}" ] && echo "{}"'` : Cette commande utilise `xargs` avec l'option `-0` pour traiter les fichiers séparés par des caractères nuls. Pour chaque fichier, elle vérifie s'il existe dans le répertoire actuel. Si le fichier n'existe pas, il est affiché.


## Exécution du script

| Tags |
|------|
| `bash` `script` `exécution` |

Pour exécuter le script :

1.  Enregistrez le script dans un fichier, par exemple <code>list_deleted_files.sh</code>.
2.  Rendez le fichier exécutable et exécutez-le :

```bash
chmod +x list_deleted_files.sh
./list_deleted_files.sh
```

Le script traitera correctement les fichiers avec des espaces et fournira une liste des fichiers supprimés qui n'existent plus dans la branche actuelle.


## Liste des fichiers supprimés avec espaces et vérification

| Tags |
|------|
| `git` `bash` `script` `fichiers` `suppression` |

Je m'excuse pour le problème. Voici une version corrigée du script qui gère correctement les noms de fichiers avec des espaces et vérifie leur existence :

```bash
#!/bin/bash

# Date à partir de laquelle vous souhaitez commencer à lister les fichiers supprimés
START_DATE="2023-01-01"

# Lister les fichiers supprimés depuis la date donnée
deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format: | sort -u)

# Filtrer les fichiers qui n'existent plus dans la branche actuelle
while IFS= read -r file; do
    if [ ! -e "$file" ]; then
        echo "$file"
    fi
done <<< "$deleted_files"
```


## Compréhension des changements de fichiers supprimés

| Tags |
|------|
| `Git` `Shell` `Suppression de fichiers` |

La section suivante détaille le processus d'identification des fichiers supprimés.

*   `deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format: | sort -u)` : Cette commande extrait les noms des fichiers supprimés depuis une date spécifiée (`$START_DATE`). L'option `--diff-filter=D` filtre les commits pour afficher uniquement les suppressions. `--name-only` affiche uniquement les noms de fichiers. `sort -u` assure que les noms de fichiers sont uniques.

*   `while IFS= read -r file; do ... done <<< "$deleted_files"` : Cette boucle `while` itère sur chaque nom de fichier supprimé. `IFS= read -r` permet de lire les noms de fichiers contenant des espaces correctement.


## Exécution du script

| Tags |
|------|
| `script` `bash` `exécution` |

Pour exécuter le script :

1.  Enregistrez le script dans un fichier, par exemple <code>list_deleted_files.sh</code>.
2.  Rendez le fichier exécutable et exécutez-le :

```bash
chmod +x list_deleted_files.sh
./list_deleted_files.sh
```

Ce script traite correctement les fichiers avec des espaces et fournit une liste des fichiers supprimés qui n'existent plus dans la branche actuelle.


## Script Bash : Éviter les lignes vides avec `echo`

| Tags |
|------|
| `Bash` `Scripting` `Git` `rm` |

Pour éviter l'affichage d'une ligne vide au début, ajustez le script pour gérer la liste des fichiers supprimés et prévenir les sorties non désirées. Voici la version corrigée du script :

```bash
#!/bin/bash

# Date de début de la liste des fichiers supprimés
START_DATE="2023-01-01"

# Lister les fichiers supprimés depuis la date spécifiée
deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format: | sort -u)

# Filtrer les fichiers qui n'existent plus dans la branche actuelle
while IFS= read -r file; do
    if [ -n "$file" ] && [ ! -e "$file" ]; then
        echo "rm \"$file\""
    fi
done <<< "$deleted_files"
```


## Amélioration de la vérification de fichier

| Tags |
|------|
| `Bash` `Scripting` `Vérification` |

L'extrait de code a été modifié comme suit :

*   Ajout de la condition `[ -n "$file" ]` pour s'assurer que la variable `$file` n'est pas vide avant de vérifier l'existence du fichier et d'afficher le message.


## Utilisation du script : Guide pas à pas

| Tags |
|------|
| `shell script` `bash` `command line` |

1.  Enregistrez le script dans un fichier nommé, par exemple, `list_deleted_files.sh`.
2.  Rendez le fichier exécutable et exécutez-le :

```bash
chmod +x list_deleted_files.sh
./list_deleted_files.sh
```

Ce script traite correctement les fichiers contenant des espaces, élimine les lignes vides en début de sortie, et génère une liste des fichiers supprimés absents de la branche actuelle, précédée de la commande `rm` pour chaque fichier.


## Traitement des lignes vides dans un script bash

| Tags |
|------|
| `bash` `rm` `script` `git` |

Je comprends qu'il y ait un problème avec le traitement des lignes vides. La solution consiste à ajuster le script pour s'assurer que seules les lignes non vides sont traitées. Voici une version améliorée du script :

```bash
#!/bin/bash

# Date à partir de laquelle vous souhaitez commencer à lister les fichiers supprimés
START_DATE="2023-01-01"

# Lister les fichiers supprimés depuis la date donnée
deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format: | sort -u)

# Filtrer les fichiers qui n'existent plus dans la branche actuelle
while IFS= read -r file; do
    if [ -n "$file" ] && [ ! -e "$file" ]; then
        echo "rm \"$file\""
    fi
done <<< "$deleted_files"
```


## Analyse de la Suppression de Fichiers avec Git

| Tags |
|------|
| `Git` `Bash` `Suppression de fichiers` |

<ol>
<li>
<p><strong>Identification des fichiers supprimés :</strong></p>
<p>La commande suivante identifie les fichiers supprimés depuis une date spécifiée, en éliminant les doublons :</p>
<pre><code class="language-bash">deleted_files=$(git log --diff-filter=D --since=&quot;$START_DATE&quot; --name-only --pretty=format: | sort -u)
</code></pre>
</li>
<li>
<p><strong>Traitement des fichiers supprimés :</strong></p>
<p>Une boucle itère sur la liste des fichiers supprimés pour générer les commandes de suppression :</p>
<pre><code class="language-bash">while IFS= read -r file; do
    if [ -n &quot;$file&quot; ] &amp;&amp; [ ! -e &quot;$file&quot; ]; then
        echo &quot;rm \&quot;$file\&quot;&quot;
    fi
done &lt;&lt;&lt; &quot;$deleted_files&quot;
</code></pre>
<ul>
<li><code>IFS=</code> : Ajuste l'Internal Field Separator pour gérer correctement les espaces dans les noms de fichiers.</li>
<li><code>read -r file</code> : Lit chaque fichier supprimé.</li>
<li><code>if [ -n &quot;$file&quot; ] &amp;&amp; [ ! -e &quot;$file&quot; ]; then</code> : Vérifie si le fichier existe encore.</li>
<li><code>echo &quot;rm \&quot;$file\&quot;&quot;</code> : Affiche la commande <code>rm</code> pour supprimer le fichier.</li>
</ul>
</li>
</ol>


## Exécution du script

| Tags |
|------|
| `shell` `script` `exécution` |

<ol>
<li>Enregistrez le script dans un fichier, par exemple <code>list_deleted_files.sh</code>.</li>
<li>
Rendez le fichier exécutable :
<pre><code class="language-bash">chmod +x list_deleted_files.sh
</code></pre>
</li>
<li>
Exécutez le script :
<pre><code class="language-bash">./list_deleted_files.sh
</code></pre>
</li>
</ol>
<p>Ce script devrait maintenant fonctionner correctement et éviter d'afficher des lignes vides en sortie.</p>


## Déplacer les fichiers supprimés avec Git et Bash

| Tags |
|------|
| `Git` `Bash` `Scripting` `Déplacement de fichiers` |

D'accord, pour déplacer les fichiers supprimés depuis une date donnée dans un répertoire temporaire, vous pouvez modifier le script pour utiliser la commande `mv` et construire le chemin de destination en conséquence. Voici comment faire :

```bash
#!/bin/bash

# Date à partir de laquelle vous souhaitez commencer à lister les fichiers supprimés
START_DATE="2023-01-01"

# Répertoire de destination
DEST_DIR="/tmp"

# Lister les fichiers supprimés depuis la date donnée
deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format: | sort -u)

# Filtrer les fichiers qui n'existent plus dans la branche actuelle
while IFS= read -r file; do
    if [ -n "$file" ] && [ ! -e "$file" ]; then
        dest_path="$DEST_DIR/$file"
        mkdir -p "$(dirname "$dest_path")"
        echo "mv \"$file\" \"$dest_path\""
    fi
done <<< "$deleted_files"
```


## Configuration et Déplacement de Fichiers

| Tags |
|------|
| `bash` `répertoire` `déplacement de fichiers` |

1.  **Répertoire de Destination :**

    ```bash
    DEST_DIR="/tmp"
    ```

    Modifiez `DEST_DIR` pour définir le répertoire de destination souhaité.

2.  **Création des Répertoires et Déplacement des Fichiers :**

    ```bash
    dest_path="$DEST_DIR/$file"
    mkdir -p "$(dirname "$dest_path")"
    echo "mv \"$file\" \"$dest_path\""
    ```

    *   `dest_path="$DEST_DIR/$file"` : Crée le chemin de destination en combinant le chemin du fichier avec le répertoire de destination.
    *   `mkdir -p "$(dirname "$dest_path")"` : Crée les répertoires nécessaires dans le chemin de destination.
    *   `echo "mv \"$file\" \"$dest_path\""` : Affiche la commande `mv` pour déplacer le fichier.


## Exécution du script

| Tags |
|------|
| `shell` `scripting` `linux` |

<ol>
<li>Enregistrez le script dans un fichier, par exemple <code>move_deleted_files.sh</code>.</li>
<li>
Rendez le fichier exécutable :
<pre><code class="language-bash">chmod +x move_deleted_files.sh
</code></pre>
</li>
<li>
Exécutez le script :
<pre><code class="language-bash">./move_deleted_files.sh
</code></pre>
</li>
</ol>
<p>Ce script va générer les commandes <code>mv</code> pour déplacer les fichiers supprimés dans le répertoire <code>/tmp</code>, en recréant la structure de répertoires d'origine.</p>


## Exécution directe des commandes

| Tags |
|------|
| `Git` `Bash` `Scripting` `Fichiers` |

Si vous souhaitez exécuter les commandes directement, remplacez `echo` par `mv` dans le script :

```bash
#!/bin/bash

# Date à partir de laquelle vous souhaitez commencer à lister les fichiers supprimés
START_DATE="2023-01-01"

# Répertoire de destination
DEST_DIR="/tmp"

# Lister les fichiers supprimés depuis la date donnée
deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format: | sort -u)

# Filtrer les fichiers qui n'existent plus dans la branche actuelle
while IFS= read -r file; do
    if [ -n "$file" ] && [ ! -e "$file" ]; then
        dest_path="$DEST_DIR/$file"
        mkdir -p "$(dirname "$dest_path")"
        mv "$file" "$dest_path"
    fi
done <<< "$deleted_files"
```

Avec cette version, les fichiers seront déplacés directement dans le répertoire de destination.


## Correction d'une commande Bash avec des guillemets

| Tags |
|------|
| `bash` `shell` `git` `dirname` `guillemets` |

Compris. Les guillemets autour de `$(dirname "$dest_path")` peuvent engendrer des erreurs lors de l'interprétation par `echo`. Pour corriger ceci, il faut échapper correctement les guillemets. Voici la correction :

```bash
#!/bin/bash

# Date de début pour lister les fichiers supprimés
START_DATE="2023-01-01"

# Répertoire de destination
DEST_DIR="/tmp"

# Lister les fichiers supprimés depuis la date donnée
deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format: | sort -u)

# Filtrer les fichiers qui n'existent plus dans la branche actuelle
while IFS= read -r file; do
    if [ -n "$file" ] && [ ! -e "$file" ]; then
        dest_path="$DEST_DIR/$file"
        echo "mkdir -p \"$(dirname \"$dest_path\")\""
        echo "mv \"$file\" \"$dest_path\""
    fi
done <<< "$deleted_files"
```


## Expliquer la commande dirname et les guillemets

| Tags |
|------|
| `Bash` `dirname` `guillemets` `échappement` |

Utilisation de guillemets doubles et d'échappement pour garantir une évaluation correcte de la commande <code>dirname</code>.

<code>\&quot;$(dirname &quot;$dest_path&quot;)\&quot;</code>: Emploi de guillemets doubles avec échappement pour permettre un traitement précis du chemin du répertoire par <code>mkdir -p</code>.


## Instructions d'utilisation du script

| Tags |
|------|
| `Bash` `Git` `Scripting` `Déplacement de fichiers` |

<ol>
<li>Enregistrez le script dans un fichier, par exemple <code>move_deleted_files.sh</code>.</li>
<li>
Rendez le fichier exécutable :
<pre><code class="language-bash">chmod +x move_deleted_files.sh
</code></pre>
</li>
<li>
Exécutez le script :
<pre><code class="language-bash">./move_deleted_files.sh
</code></pre>
</li>
</ol>
<p>Ce script génère les commandes <code>mkdir -p</code> et <code>mv</code>, en affichant des chemins correctement échappés. Pour exécuter les commandes directement, modifiez le script en supprimant <code>echo</code> :</p>
<pre><code class="language-bash">#!/bin/bash

# Date à partir de laquelle vous souhaitez commencer à lister les fichiers supprimés
START_DATE="2023-01-01"

# Répertoire de destination
DEST_DIR="/tmp"

# Lister les fichiers supprimés depuis la date donnée
deleted_files=$(git log --diff-filter=D --since="$START_DATE" --name-only --pretty=format: | sort -u)

# Filtrer les fichiers qui n'existent plus dans la branche actuelle
while IFS= read -r file; do
    if [ -n "$file" ] && [ ! -e "$file" ]; then
        dest_path="$DEST_DIR/$file"
        mkdir -p "$(dirname "$dest_path")"
        mv "$file" "$dest_path"
    fi
done <<< "$deleted_files"
</code></pre>
<p>Cette version crée les répertoires et déplace les fichiers directement.</p>
