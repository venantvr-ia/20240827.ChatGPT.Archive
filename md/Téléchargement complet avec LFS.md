## Téléchargement complet avec Git LFS

| Tags |
|------|
| `Git` `LFS` `téléchargement` `performance` |

Pour télécharger un dépôt Git contenant des fichiers gérés par Git LFS (Large File Storage), vous devez vous assurer que Git LFS est installé et configuré correctement. Voici les étapes à suivre et les commandes à utiliser :

**1. Installation de Git LFS :**

Si Git LFS n'est pas déjà installé, vous devez l'installer sur votre système. Les instructions d'installation varient selon le système d'exploitation. Consulter la documentation officielle de Git LFS : [https://git-lfs.github.com/](https://git-lfs.github.com/)

**2. Initialisation de Git LFS dans le dépôt :**

Après l'installation, dans le répertoire de votre dépôt Git, exécutez :

```bash
git lfs install
```

Cela configure Git pour utiliser Git LFS.

**3. Téléchargement du dépôt :**

Utilisez la commande `git clone` pour cloner le dépôt. Git LFS téléchargera automatiquement les fichiers gérés par LFS.

```bash
git clone [URL du dépôt]
```

Remplacez `[URL du dépôt]` par l'URL de votre dépôt Git.

**4. Vérification du téléchargement :**

Après le clonage, vous pouvez vérifier que les fichiers LFS ont été téléchargés correctement.  Dans le répertoire du dépôt, utilisez la commande suivante pour lister les fichiers gérés par LFS et leurs informations :

```bash
git lfs ls-files
```

Vous pouvez également vérifier le contenu des fichiers téléchargés pour vous assurer de leur intégrité.

**5. Gestion des erreurs de téléchargement (si nécessaire) :**

Si vous rencontrez des problèmes lors du téléchargement, comme des erreurs de connexion ou d'authentification, vérifiez les points suivants :

*   **Authentification :** Assurez-vous d'avoir les droits d'accès au dépôt et que vos identifiants sont corrects.  Si le dépôt est privé, vous devrez peut-être vous authentifier avec votre nom d'utilisateur et mot de passe ou un jeton d'accès.
*   **URL du dépôt :** Vérifiez que l'URL du dépôt est correcte.
*   **Connexion réseau :** Assurez-vous d'avoir une connexion réseau stable.
*   **Git LFS configuration :** Vérifiez la configuration de Git LFS.  En particulier, vérifiez que `git config -l | grep lfs` contient les informations de configuration attendues.  Vérifiez aussi les paramètres de proxy si vous en utilisez un.
*   **Proxy :** Si vous utilisez un proxy, configurez les paramètres de proxy Git :

```bash
git config --global http.proxy [adresse du proxy]
git config --global https.proxy [adresse du proxy]
```

**Exemple :**

```bash
git clone https://[NOM]@git.example.com/mon-depot.git
cd mon-depot
git lfs ls-files
```

Si des erreurs persistent, consultez la documentation de Git LFS ou contactez l'administrateur du dépôt. Pour plus d'informations sur Git LFS, visitez [https://git-lfs.github.com/](https://git-lfs.github.com/). Pour signaler un problème, vous pouvez contacter [NOM] à [EMAIL]. Pour des problèmes de réseau, contactez [NOM] à [EMAIL] ou [NOM] à [EMAIL]. Le serveur est situé sur [IP].


## Télécharger un dataset complet depuis Hugging Face

| Tags |
|------|
| `Hugging Face` `datasets` `Git LFS` `téléchargement` |

Pour télécharger un dataset complet, y compris les fichiers stockés avec Git Large File Storage (LFS) sur Hugging Face, suivez les étapes suivantes :

1.  **Installation des Dépendances :**
    Assurez-vous d'avoir installé Git LFS et la bibliothèque `datasets` de Hugging Face. Vous pouvez les installer via pip si ce n'est pas déjà fait :

    ```bash
    pip install git-lfs datasets
    ```

2.  **Clonage du Dépôt de Données :**
    Trouvez l'URL du dépôt de l'ensemble de données sur Hugging Face. En général, vous pouvez le trouver sur la page de l'ensemble de données sous l'onglet "Data Files". Ensuite, clonez le dépôt en utilisant Git :

    ```bash
    git clone https://huggingface.co/datasets/<organisation>/<nom_du_dataset>
    ```

    Remplacez `<organisation>` et `<nom_du_dataset>` par les valeurs appropriées pour l'ensemble de données que vous souhaitez télécharger.

3.  **Téléchargement des Fichiers LFS :**
    Après avoir cloné le dépôt, naviguez dans le dossier du dépôt cloné, et lancez la commande suivante pour récupérer les fichiers LFS :

    ```bash
    git lfs pull
    ```

4.  **Vérification des Données :**
    Vérifiez que tous les fichiers nécessaires sont présents et complets dans le répertoire local. Vous pouvez explorer le dossier et ses sous-dossiers pour vous assurer que tout est téléchargé.

Ces étapes devraient vous permettre de récupérer l'ensemble de l'ensemble de données, y compris les fichiers volumineux stockés avec LFS. Si vous rencontrez des problèmes avec l'une de ces étapes, assurez-vous que votre configuration Git LFS est correctement effectuée et que vous avez les permissions nécessaires pour accéder aux données.


## Annuler les modifications Git d'un dépôt local

| Tags |
|------|
| `Git` `versionning` `rollback` `reset` `revert` |

Pour annuler les modifications dans un dépôt Git local, plusieurs options sont disponibles en fonction de l'état des modifications et de l'objectif. Voici les méthodes courantes :


## Annulation des modifications non mises en stage

| Tags |
|------|
| `git` `checkout` `restore` `unstaged changes` |

Si vous avez des fichiers modifiés non ajoutés à la zone de mise en scène, utilisez :

```bash
git checkout -- <nom_de_fichier>
```

Remplacez `<nom_de_fichier>` par le nom du fichier à réinitialiser. Pour réinitialiser tous les fichiers modifiés :

```bash
git checkout -- .
```

Depuis Git version 2.23, vous pouvez aussi utiliser `git restore` :

```bash
git restore <nom_de_fichier>
```

Pour restaurer tous les fichiers dans le répertoire de travail :

```bash
git restore .
```


## Désindexer des modifications mises en stage

| Tags |
|------|
| `Git` `reset` `staging` |

Si vous avez mis des modifications en zone de staging et souhaitez les désindexer (tout en conservant les modifications dans les fichiers) :

```bash
git reset HEAD <nom_de_fichier>
```

Pour désindexer tous les fichiers :

```bash
git reset HEAD .
```


## Annuler les modifications et revenir à un commit

| Tags |
|------|
| `Git` `reset` `commit` `versionning` |

Si vous souhaitez annuler toutes les modifications et revenir à un commit précis :

```bash
git reset --hard &lt;commit_hash&gt;
```

Remplacez `&lt;commit_hash&gt;` par le hash du commit spécifique auquel vous souhaitez revenir. Soyez prudent avec cette commande, car elle efface toutes les modifications non commitées.


## Annulation d'un commit récent

| Tags |
|------|
| `Git` `commit` `reset` |

Pour annuler un commit tout en conservant les modifications dans votre répertoire de travail :
```bash
git reset --soft HEAD^
```

Pour annuler le dernier commit et supprimer toutes les modifications :
```bash
git reset --hard HEAD^
```

Utilisez `HEAD^` pour revenir d'un commit, ou `HEAD~2` pour revenir de deux commits, etc.


## Git Revert : Annuler un commit spécifique

| Tags |
|------|
| `Git` `revert` `commit` `versioning` |

Si l'objectif est d'annuler un commit précis et de générer un nouveau commit annulant les modifications introduites par celui-ci, la commande suivante peut être utilisée :

```bash
git revert <commit_hash>
```

Cette méthode est particulièrement pertinente lorsque les modifications ont déjà été poussées vers un dépôt distant, évitant ainsi la réécriture de l'historique.


## Choisir la méthode appropriée pour l'annulation

| Tags |
|------|
| `Git` `Annulation` `Historique` |

Chaque méthode présente des cas d'utilisation spécifiques, selon que vous souhaitez conserver les modifications après l'annulation, ou que vos changements ont déjà été poussés et que d'autres dépendent de votre historique public. Il est crucial de comprendre les effets de chaque commande avant de l'exécuter pour éviter la perte de données.
