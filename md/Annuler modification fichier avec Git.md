## Annuler les modifications d'un fichier avec Git

| Tags |
|------|
| `Git` `version control` `rollback` |

Il existe plusieurs façons d'annuler les modifications apportées à un fichier avec Git. Voici les méthodes les plus courantes :

### Annuler les modifications non préparées

Si vous avez modifié un fichier, mais que vous ne l'avez pas préparé à l'aide de `git add`, vous pouvez annuler les modifications à l'aide de la commande suivante :

```bash
git checkout -- <nom_fichier>
```

Cette commande remplace le fichier modifié par la dernière version validée. Toutes les modifications locales seront perdues.

### Annuler les modifications préparées

Si vous avez préparé les modifications à l'aide de `git add`, mais que vous ne les avez pas encore validées, vous pouvez annuler les modifications préparées en exécutant les commandes suivantes :

```bash
git reset HEAD <nom_fichier>
git checkout -- <nom_fichier>
```

La première commande annule la préparation des modifications. La seconde commande annule les modifications du fichier dans le répertoire de travail.

### Annuler la dernière validation

Si vous avez validé les modifications, mais que vous souhaitez annuler la dernière validation, vous pouvez utiliser la commande suivante :

```bash
git reset --hard HEAD^
```

Cette commande réinitialisera votre branche à l'état de la validation précédente. **Attention :** cette commande supprimera toutes les modifications de la dernière validation et toutes les modifications ultérieures non validées.

Si vous souhaitez annuler une validation spécifique, vous pouvez utiliser la commande suivante :

```bash
git revert <hash_de_validation>
```

Cette commande créera une nouvelle validation qui annule les modifications apportées par la validation spécifiée. Cela préserve l'historique de votre projet.

### Exemples supplémentaires

Voici quelques exemples plus spécifiques :

*   Pour annuler toutes les modifications apportées à un fichier nommé `example.txt` :

```bash
git checkout -- example.txt
```

*   Pour annuler les modifications préparées pour un fichier nommé `example.txt` :

```bash
git reset HEAD example.txt
git checkout -- example.txt
```

*   Pour annuler la dernière validation et supprimer les modifications locales :

```bash
git reset --hard HEAD^
```

*   Pour annuler une validation spécifique avec le hash `abcdef1234567890` :

```bash
git revert abcdef1234567890
```

### Autres ressources

Pour plus d'informations, consultez les ressources suivantes :

*   Documentation Git : [https://git-scm.com/doc](https://git-scm.com/doc)
*   Tutoriel Git : [NOM] [EMAIL]


## Annuler des modifications de fichiers Git

| Tags |
|------|
| `Git` `commande` `rollback` `reset` `checkout` |

Pour annuler une modification de fichier avec Git en ligne de commande, plusieurs options sont disponibles en fonction de l'état actuel des modifications et du résultat souhaité. Voici différents scénarios :

1.  **Modifications non ajoutées (non staged)**

    Pour restaurer un fichier à son état lors du dernier commit :

    ```bash
    git checkout -- <fichier>
    ```

    Cette commande remplace les modifications du fichier par la dernière version committée.
2.  **Modifications ajoutées (staged) mais non commises**

    Pour annuler l'ajout (staging) et restaurer le fichier à son état lors du dernier commit :

    ```bash
    git reset HEAD <fichier>
    git checkout -- <fichier>
    ```

    La première commande (<code>git reset</code>) retire le fichier de la zone de staging. La seconde (<code>git checkout</code>) restaure le fichier à son état précédent.
3.  **Modifications commises**

    *   **Annuler le dernier commit tout en conservant les modifications :**

        ```bash
        git reset --soft HEAD^
        ```

    *   **Annuler le dernier commit et les modifications :**

        ```bash
        git reset --hard HEAD^
        ```

        <code>HEAD^</code> fait référence au commit précédent. <code>--soft</code> conserve les modifications comme "non staged", tandis que <code>--hard</code> les supprime.
4.  **Revenir à un état spécifique d'un commit antérieur**

    ```bash
    git checkout <commit_hash> -- <fichier>
    ```

    Où <code>&lt;commit_hash&gt;</code> est le hash du commit de référence.

**Important:** Les commandes avec <code>--hard</code> peuvent entraîner la perte de modifications. Il est recommandé de sauvegarder les fichiers importants avant d'utiliser ces commandes.
