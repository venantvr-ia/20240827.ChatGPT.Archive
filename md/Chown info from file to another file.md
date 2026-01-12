## Modification des informations Chown d'un fichier

| Tags |
|------|
| `chown` `linux` `permissions` `command-line` |

La commande `chown` permet de modifier le propriétaire et/ou le groupe d'un fichier ou d'un répertoire. Cette section explique comment utiliser cette commande.

**Syntaxe:**

```bash
chown [options] utilisateur[:groupe] fichier...
```

*   `utilisateur` : Nom d'utilisateur (ou UID).
*   `groupe` : Nom du groupe (ou GID).  Optionnel, si omis seul l'utilisateur est modifié.
*   `fichier` : Le fichier ou le répertoire sur lequel appliquer les changements.

**Exemples:**

1.  **Changer le propriétaire d'un fichier:**

    Pour changer le propriétaire du fichier `fichier.txt` à l'utilisateur `[NOM]`, utilisez :

    ```bash
    chown [NOM] fichier.txt
    ```

2.  **Changer le propriétaire et le groupe d'un fichier:**

    Pour changer le propriétaire et le groupe du fichier `fichier.txt` à l'utilisateur `[NOM]` et au groupe `[GROUPE]`, utilisez :

    ```bash
    chown [NOM]:[GROUPE] fichier.txt
    ```

3.  **Changer récursivement les propriétaires et groupes d'un répertoire et ses contenus:**

    L'option `-R` permet d'appliquer les changements de manière récursive.  Par exemple, pour changer le propriétaire et le groupe du répertoire `dossier` et de tous ses fichiers et sous-répertoires :

    ```bash
    chown -R [NOM]:[GROUPE] dossier
    ```

4.  **Utilisation des UID et GID:**

    Au lieu des noms d'utilisateur et de groupe, vous pouvez utiliser leurs identifiants numériques (UID et GID).  Ceci peut être utile dans les scripts ou lorsque les noms ne sont pas disponibles.

    ```bash
    chown 1001:1002 fichier.txt
    ```

    Dans cet exemple, l'utilisateur avec l'UID 1001 et le groupe avec le GID 1002 sont définis.

**Conseils:**

*   **Permissions:**  Vous devez avoir les permissions appropriées (généralement être l'utilisateur root ou posséder le fichier) pour utiliser `chown`.
*   **Sécurité:**  Soyez prudent lors de l'utilisation de `chown -R`, car des changements incorrects peuvent rendre votre système instable.
*   **Vérification:**  Après avoir utilisé `chown`, vérifiez les changements avec la commande `ls -l` pour confirmer que les permissions ont été modifiées comme prévu.
*   **Documentation:** Consultez la page de manuel de `chown` pour plus d'informations : `man chown`.


## Copier les informations chown d'un fichier

| Tags |
|------|
| `chown` `stat` `Linux` `Unix` `propriété` |

Pour copier les informations `chown` (propriétaire et groupe) d'un fichier source vers un fichier de destination, utilisez les commandes `stat` et `chown`.

1.  Obtenez les informations de propriété du fichier source :

```bash
stat -c "%U:%G" fichier_source
```

Cette commande affiche le propriétaire (`%U`) et le groupe (`%G`) du fichier source.

2.  Appliquez ces informations au fichier de destination :

```bash
chown $(stat -c "%U" fichier_source):$(stat -c "%G" fichier_source) fichier_destination
```

Remplacez `fichier_source` et `fichier_destination` par les chemins d'accès appropriés.

Exécutez ces commandes avec les privilèges nécessaires. La syntaxe peut varier légèrement selon le système d'exploitation.
