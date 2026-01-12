## Suppression de fichiers sur GitHub

| Tags |
|------|
| `GitHub` `Git` `Suppression de fichier` `Ligne de commande` |

Pour supprimer un fichier d'un dépôt GitHub, plusieurs méthodes sont possibles.

### Suppression d'un fichier via l'interface web GitHub

1.  Naviguez jusqu'au dépôt et au fichier que vous souhaitez supprimer.
2.  Cliquez sur l'icône de la corbeille.
3.  Confirmez la suppression en suivant les instructions.
4.  Validez la modification.

### Suppression d'un fichier via la ligne de commande Git

1.  Clonez le dépôt sur votre machine locale.
2.  Utilisez la commande `git rm <nom_du_fichier>` pour supprimer le fichier.
3.  Validez la suppression avec `git commit -m "Suppression de <nom_du_fichier>"`.
4.  Poussez les modifications sur le dépôt distant avec `git push origin <nom_de_la_branche>`.

Exemple :

```bash
git clone https://github.com/[NOM]/[NOM_DU_DEPOT].git
cd [NOM_DU_DEPOT]
git rm mon_fichier.txt
git commit -m "Suppression de mon_fichier.txt"
git push origin main
```


## Suppression de fichiers de l'historique GitHub

| Tags |
|------|
| `Git` `GitHub` `Historique` `Suppression` |

Pour supprimer des fichiers de l'historique sur GitHub, utilisez Git sur votre ordinateur local. Cette opération est requise pour supprimer des fichiers contenant des informations sensibles ou pour réduire la taille du dépôt.

Voici les étapes :


## Cloner le dépôt

| Tags |
|------|
| `git` `clonage` `dépôt` |

Si le dépôt n'est pas déjà cloné, utiliser la commande suivante :

```bash
git clone URL_DU_DEPOT
cd NOM_DU_DEPOT
```

Remplacer <code>URL_DU_DEPOT</code> par l'URL du dépôt GitHub et <code>NOM_DU_DEPOT</code> par le nom du dépôt.


## Suppression de données sensibles avec filter-branch/BFG

| Tags |
|------|
| `Git` `filter-branch` `BFG Repo-Cleaner` `Sécurité` |

La suppression de données sensibles d'un dépôt Git requiert des outils spécifiques. Deux solutions sont courantes : `filter-branch` et BFG Repo-Cleaner.

### Utilisation de filter-branch

`filter-branch` est un outil intégré à Git permettant de réécrire l'historique d'un dépôt. Il peut être utilisé pour supprimer des fichiers, des commits ou des données spécifiques.  Cependant, son utilisation est complexe et peut altérer l'intégrité du dépôt si elle n'est pas effectuée correctement.

Voici un exemple pour supprimer un fichier contenant des informations sensibles :

```bash
git filter-branch --force --index-filter 'git rm --cached --ignore-unmatch [FICHIER_SENSIBLE]' --prune-empty --tag-name-filter cat -- --all
```

**Explication:**

*   `--force`: Force l'exécution de la commande.
*   `--index-filter`:  Applique un filtre à l'index avant chaque commit.
*   `git rm --cached --ignore-unmatch [FICHIER_SENSIBLE]`: Supprime le fichier spécifié de l'index et du dépôt.
*   `--prune-empty`: Supprime les commits vides résultant de la suppression.
*   `--tag-name-filter cat`:  Applique le filtre aux noms des tags.
*   `-- --all`:  Applique le filtre à toutes les branches et tags.

Après avoir exécuté cette commande, il est impératif de :

1.  Supprimer les backups : `rm -rf .git/refs/original/`
2.  Nettoyer le garbage collector : `git gc --prune=all`

### Utilisation de BFG Repo-Cleaner

BFG Repo-Cleaner est un outil tiers, plus rapide et simple d'utilisation que `filter-branch`. Il est spécialisé dans la suppression de données sensibles.

Pour supprimer un fichier contenant des informations sensibles :

1.  Télécharger BFG Repo-Cleaner : [LIEN_BFG]
2.  Exécuter la commande :

```bash
bfg --delete-files [FICHIER_SENSIBLE] [VOTRE_DEPOT.git]
```

Ou pour remplacer des informations sensibles par des données anonymisées :

```bash
bfg --replace-text "[MOT_DE_PASSE_SENSIBLE]" "" [VOTRE_DEPOT.git]
```

**Explication:**

*   `--delete-files`: Supprime les fichiers spécifiés.
*   `--replace-text`: Remplace le texte sensible par une chaîne vide.

Après avoir utilisé BFG, il est nécessaire d'effectuer un `git gc --prune=all` pour nettoyer le dépôt.

**Important :**

Après avoir supprimé des données sensibles, il est essentiel de forcer le push des modifications vers le dépôt distant :

```bash
git push --force --all
git push --force --tags
```

**Avertissement :** La réécriture de l'historique est une opération destructive. Il est fortement recommandé de faire une sauvegarde du dépôt avant d'effectuer ces opérations.  De plus, les personnes ayant déjà cloné le dépôt devront le re-cloner pour s'assurer de ne plus avoir les données sensibles.

[LIEN_BFG] : <https://rtyley.github.io/bfg-repo-cleaner/>


## Suppression d'un fichier avec `git filter-branch`

| Tags |
|------|
| `git` `filter-branch` `historique` `suppression` |

Pour supprimer un fichier de l'historique :

```bash
git filter-branch --force --index-filter \
"git rm --cached --ignore-unmatch CHEMIN_DU_FICHIER_A_SUPPRIMER" \
--prune-empty --tag-name-filter cat -- --all
```

Remplacez `CHEMIN_DU_FICHIER_A_SUPPRIMER` par le chemin du fichier cible.


## Suppression de fichiers avec BFG Repo-Cleaner

| Tags |
|------|
| `Git` `BFG Repo-Cleaner` `Suppression de fichiers` |

<ol>
<li>Téléchargez le <a href="https://rtyley.github.io/bfg-repo-cleaner/">BFG Repo-Cleaner</a>.</li>
<li>Exécutez BFG pour supprimer le fichier ou les fichiers spécifiques :</li>
</ol>
<pre><code class="language-bash">java -jar bfg.jar --delete-files NOM_DU_FICHIER VOTRE_REPO_GIT
</code></pre>
<p>Remplacez <code>NOM_DU_FICHIER</code> par le nom du fichier à supprimer et <code>VOTRE_REPO_GIT</code> par le chemin de votre dépôt local.</p>


## Forcer le push sur GitHub

| Tags |
|------|
| `git` `GitHub` `push` `force` |

Après avoir supprimé les fichiers de l'historique, forcez le push sur GitHub pour mettre à jour le dépôt distant :

```bash
git push origin --force --all
git push origin --force --tags
```


## Avertissements : Réécriture de l'historique Git

| Tags |
|------|
| `Git` `historique` `réécriture` `avertissement` |

*   Ces opérations altèrent l'historique du dépôt. Les collaborateurs ayant cloné ou forké le dépôt pourraient être impactés. Une communication préalable est donc recommandée.
*   Avant d'effectuer des modifications irréversibles, assurez-vous d'avoir une sauvegarde du dépôt.


## Automatisation de la suppression avec GitHub Actions

| Tags |
|------|
| `GitHub Actions` `automatisation` `sécurité` |

Si la suppression de fichiers sensibles est récurrente, l'utilisation de GitHub Actions est recommandée pour automatiser le processus de nettoyage du dépôt. Il est possible de configurer une action pour détecter et supprimer automatiquement les fichiers ou données sensibles lors de chaque push.

Ces étapes permettent de supprimer les fichiers indésirables de l'historique du dépôt GitHub. Il est impératif de prendre en compte les implications de la réécriture de l'historique, notamment dans un contexte collaboratif.


## Ajouter des fichiers avec git-crypt

| Tags |
|------|
| `git-crypt` `Git` `chiffrement` `sécurité` |

<code>git-crypt</code> est un outil conçu pour chiffrer et décrypter des fichiers dans un dépôt Git. Il permet de gérer de manière sécurisée les fichiers contenant des informations sensibles, comme les configurations et les mots de passe, sans les exposer en clair dans le dépôt. Voici comment vous pouvez utiliser <code>git-crypt</code> pour ajouter des fichiers à chiffrer dans votre dépôt Git.


## Installation de git-crypt

| Tags |
|------|
| `git-crypt` `installation` `Debian/Ubuntu` |

Avant de commencer, assurez-vous que `git-crypt` est installé. Sur les systèmes basés sur Debian/Ubuntu, utilisez :

```bash
sudo apt-get install git-crypt
```


## Initialisation de git-crypt dans un dépôt

| Tags |
|------|
| `git-crypt` `Git` `sécurité` |

Pour initialiser <code>git-crypt</code> dans un dépôt Git, naviguez jusqu'au répertoire du dépôt et exécutez la commande suivante :

```bash
git-crypt init
```

Cette commande génère la clé de chiffrement nécessaire au chiffrement et déchiffrement des fichiers.


## Configuration des fichiers pour le chiffrement

| Tags |
|------|
| `git-crypt` `git` `chiffrement` `sécurité` |

Pour configurer les fichiers à chiffrer, créez un fichier <code>.gitattributes</code> à la racine du dépôt si celui-ci n'existe pas déjà.  Ajoutez ensuite les règles pour spécifier les fichiers à chiffrer en utilisant <code>git-crypt</code>.

Exemple :

```plaintext
# Dans le fichier .gitattributes
secrets.txt filter=git-crypt diff=git-crypt
*.key filter=git-crypt diff=git-crypt
config/secret/** filter=git-crypt diff=git-crypt
```

Ces règles indiquent à <code>git-crypt</code> de chiffrer <code>secrets.txt</code>, tous les fichiers ayant l'extension <code>.key</code> et tous les fichiers situés dans le dossier <code>config/secret/</code>.


## Ajouter et valider les modifications avec Git

| Tags |
|------|
| `Git` `git add` `git commit` `Chiffrement` |

Après avoir modifié le fichier `.gitattributes`, ajoutez-le et validez les modifications :

```bash
git add .gitattributes
git commit -m "Configure git-crypt"
```

Ajoutez ensuite les fichiers à chiffrer (s'ils sont déjà présents, ils doivent être ajoutés à nouveau) :

```bash
git add secrets.txt config/secret/
git commit -m "Add encrypted files"
```


## Verrouillage et déverrouillage des fichiers avec git-crypt

| Tags |
|------|
| `git-crypt` `sécurité` `chiffrement` `verrouillage` `déverrouillage` |

*   Pour **verrouiller** les fichiers (les chiffrer), utilisez :

    ```bash
    git-crypt lock
    ```

*   Pour **déverrouiller** les fichiers (les déchiffrer), assurez-vous d'avoir accès à la clé de chiffrement et exécutez :

    ```bash
    git-crypt unlock
    ```


## Partage de la clé de chiffrement Git-Crypt

| Tags |
|------|
| `git-crypt` `chiffrement` `sécurité` `GPG` |

Si une collaboration est requise sur des fichiers chiffrés, la clé de chiffrement <code>git-crypt</code> doit être partagée de manière sécurisée. <code>git-crypt</code> permet d'ajouter des utilisateurs autorisés à déchiffrer les fichiers en utilisant leurs clés GPG.


## Sécurité et bonnes pratiques Git-Crypt

| Tags |
|------|
| `git-crypt` `sécurité` `Git` `chiffrement` |

*   N'ajoutez jamais la clé de chiffrement à votre dépôt Git.
*   Assurez-vous de sauvegarder la clé de chiffrement en lieu sûr.
*   L'utilisation de `git-crypt` ajoute une couche de sécurité pour les données sensibles, mais soyez conscient des meilleures pratiques de sécurité et de gestion des clés.

En suivant ces étapes, vous pouvez gérer efficacement les fichiers sensibles dans votre dépôt Git en utilisant `git-crypt`.


## Chiffrement de fichiers secrets après commit

| Tags |
|------|
| `git-crypt` `Git` `sécurité` `chiffrement` |

Si des fichiers en clair ont été commis dans votre dépôt Git et que vous souhaitez maintenant les chiffrer avec <code>git-crypt</code>, une procédure spécifique doit être suivie. Cette procédure implique la suppression de l'historique des fichiers en clair avant de les chiffrer. En effet, une fois qu'un fichier a été commis dans un dépôt Git, il persiste dans l'historique, même s'il est supprimé ou modifié dans des commits ultérieurs. Voici les étapes à suivre :


## Sauvegarde du dépôt

| Tags |
|------|
| `Git` `Sauvegarde` `Dépôt` |

Avant d'effectuer des modifications importantes, telles que la suppression de fichiers dans l'historique de votre dépôt, il est recommandé de réaliser une sauvegarde complète de votre dépôt.


## Suppression des fichiers de l'historique Git

| Tags |
|------|
| `Git` `filter-branch` `BFG Repo-Cleaner` `sécurité` |

Vous devez supprimer les fichiers à chiffrer de l'historique de votre dépôt. Utilisez <code>git filter-branch</code> ou un outil comme BFG Repo-Cleaner.

Pour supprimer un fichier spécifique de l'historique avec <code>git filter-branch</code> :

```bash
git filter-branch --force --index-filter "git rm --cached --ignore-unmatch CHEMIN_DU_FICHIER" --prune-empty --tag-name-filter cat -- --all
```

Remplacez <code>CHEMIN_DU_FICHIER</code> par le chemin du fichier à supprimer.


## Vérification de la suppression des fichiers

| Tags |
|------|
| `Git` `Suppression` `Historique` |

Après l'exécution de la commande de suppression, confirmez la disparition des fichiers de l'historique. Cela peut être fait en recherchant le contenu du fichier dans les anciens commits.


## Chiffrement des fichiers avec git-crypt

| Tags |
|------|
| `git-crypt` `sécurité` `chiffrement` `git` |

Après avoir supprimé les fichiers de l'historique, initialisez <code>git-crypt</code> dans votre dépôt si ce n'est pas déjà fait :

```bash
git-crypt init
```

Configurez ensuite les fichiers à chiffrer en ajoutant les règles appropriées dans le fichier <code>.gitattributes</code>, comme décrit précédemment.


## Ajouter et valider les fichiers chiffrés

| Tags |
|------|
| `git-crypt` `git` `chiffrement` `sécurité` |

Ajoutez les fichiers chiffrés au dépôt :

```bash
git add .
git commit -m "Add encrypted files"
```


## Forcer le push vers le dépôt distant

| Tags |
|------|
| `Git` `push` `filter-branch` |

Après le chiffrement et le commit, forcez le push vers le dépôt distant pour écraser l'historique modifié par `git filter-branch`.

```bash
git push origin --force --all
```


## Avertissements relatifs au forçage du push Git

| Tags |
|------|
| `Git` `push force` `collaboration` `sécurité` |

*   Forcer le push (<code>git push --force</code>) peut perturber les autres utilisateurs du dépôt. La coordination avec tous les collaborateurs est essentielle.
*   Tous les collaborateurs doivent comprendre qu'ils devront cloner à nouveau le dépôt ou gérer soigneusement la fusion des historiques en cas de travaux en cours.

En suivant ces étapes, vous pouvez chiffrer les fichiers qui ont été précédemment commis en clair dans votre dépôt Git. Cette opération modifie l'historique de votre dépôt. Procédez avec prudence et assurez-vous que tous les collaborateurs sont informés des changements.


## Résolution de l'erreur "Cannot rewrite branches"

| Tags |
|------|
| `Git` `Erreur` `Réécriture` `Branches` |

L'erreur "Cannot rewrite branches: You have unstaged changes" se produit lors de l'exécution de commandes Git modifiant l'historique, comme <code>git filter-branch</code> ou <code>git rebase</code>, en présence de modifications non validées. Plusieurs solutions sont possibles :


## Stasher les modifications Git

| Tags |
|------|
| `Git` `stash` `version control` |

Vous pouvez mettre de côté vos modifications avec `git stash`. Cela permet de sauvegarder vos modifications en cours dans une pile à part, où elles peuvent être récupérées plus tard, vous permettant ainsi de continuer avec votre opération d'historique.

```bash
git stash push -m "Mes modifications temporaires"
```

Après avoir terminé l'opération qui modifie l'historique, vous pouvez récupérer vos modifications avec :

```bash
git stash pop
```


## Commiter les modifications
| Tags |
|------|
| `git` `commit` `versionning` |

Une alternative consiste à commiter les modifications. Cela permet de conserver les changements dans l'historique du dépôt.

```bash
git add .
git commit -m "Description de mes modifications"
```

Après avoir commité les modifications, il est possible de réessayer l'opération qui modifie l'historique.


## Annulation des modifications Git

| Tags |
|------|
| `Git` `checkout` `reset` `version control` |

Si les modifications en cours ne sont pas nécessaires, vous pouvez les annuler. Pour les modifications non staged :

```bash
git checkout -- <fichier>
```

Pour les modifications staged (ajoutées à l'index, mais non commitées) :

```bash
git reset HEAD <fichier>
git checkout -- <fichier>
```

Remplacez `<fichier>` par le nom du fichier à annuler. Pour annuler toutes les modifications dans le dépôt :

```bash
git reset --hard
```

**Attention :** `git reset --hard` supprimera toutes les modifications non commitées dans votre dépôt. À utiliser avec précaution.


## Vérification de l'état du dépôt Git

| Tags |
|------|
| `git` `état` `status` `répertoire de travail` |

Avant de tenter à nouveau l'opération, il est recommandé de vérifier l'état du dépôt :

```bash
git status
```

Si la commande <code>git status</code> indique que le répertoire de travail est propre, l'opération de modification de l'historique peut être poursuivie.


## Gestion de la clé Git-Crypt

| Tags |
|------|
| `git-crypt` `sécurité` `chiffrement` `GPG` |

Dans `git-crypt`, la clé de chiffrement est gérée en interne. Elle n'est pas directement exposée aux utilisateurs sous forme de fichier. L'accès au dépôt chiffré peut être partagé en utilisant les clés GPG des utilisateurs ou en exportant la clé principale de `git-crypt`.


## Exporter la clé de chiffrement git-crypt

| Tags |
|------|
| `git-crypt` `sécurité` `chiffrement` `git` |

Pour partager l'accès chiffré à un dépôt sans utiliser GPG, exportez la clé de chiffrement `git-crypt` et fournissez-la de manière sécurisée. Voici comment procéder :

1.  **Exporter la clé** :

    ```bash
    git-crypt export-key /chemin/vers/destination-de-la-cle
    ```

    Remplacez `/chemin/vers/destination-de-la-cle` par le chemin complet de destination du fichier de clé exporté. Cette commande crée un fichier contenant la clé de chiffrement.

2.  **Partager la clé** :
    Partagez le fichier de clé exporté avec l'utilisateur qui doit accéder aux fichiers chiffrés. Utilisez une méthode de partage sécurisée, comme un partage de fichiers chiffré ou un transfert physique sécurisé.


## Importer une clé de chiffrement git-crypt

| Tags |
|------|
| `git-crypt` `sécurité` `chiffrement` `git` |

Pour importer une clé de chiffrement `git-crypt`, suivez ces étapes :

1.  **Placement de la clé** : Placez le fichier de clé fourni dans un répertoire sécurisé de votre choix.

2.  **Déverrouillage du dépôt** : Naviguez dans le répertoire de votre dépôt Git et exécutez la commande suivante :

    ```bash
    git-crypt unlock /chemin/vers/la-cle
    ```

    Remplacez `/chemin/vers/la-cle` par le chemin d'accès réel au fichier de clé.


## Gestion de la sécurité avec Git-Crypt

| Tags |
|------|
| `git-crypt` `sécurité` `chiffrement` `clés` |

*   **Sécurité des clés** : La clé de chiffrement `git-crypt` est critique. Sa compromission expose les fichiers chiffrés. Partager la clé uniquement de manière sécurisée et avec des personnes de confiance.
*   **Stockage sécurisé** : Stockez la clé de chiffrement dans un endroit sûr. Utilisez un gestionnaire de mots de passe ou un dispositif de stockage sécurisé.
*   **Contrôle d'accès** : Restreignez l'accès aux utilisateurs autorisés pour minimiser les risques de fuite de données.

En suivant ces instructions, gérez la clé de chiffrement `git-crypt` pour partager l'accès aux fichiers chiffrés ou pour accéder à un dépôt chiffré.
