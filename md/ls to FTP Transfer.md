## Transfert via FTP avec la commande `ls`

| Tags |
|------|
| `FTP` `ls` `Shell` `Scripting` |

Le but de ce document est d'expliquer comment utiliser la commande `ls` pour lister des fichiers et les transférer via FTP.

```bash
#!/bin/bash
# Script pour transférer des fichiers via FTP

# Variables de configuration
FTP_SERVER="[NOM]"
FTP_USER="[NOM]"
FTP_PASSWORD="[MOT DE PASSE]"
LOCAL_DIR="/chemin/vers/dossier/local"
REMOTE_DIR="/chemin/vers/dossier/distant"

# Connexion FTP et transfert
ftp -n $FTP_SERVER <<EOF
user $FTP_USER $FTP_PASSWORD
cd $REMOTE_DIR
lcd $LOCAL_DIR
ls -l | awk '{print "put " $9}' | ftp -n $FTP_SERVER
bye
EOF

echo "Transfert terminé."
```

Ce script effectue les actions suivantes :

1.  **Configuration des variables :** Définit le serveur FTP, l'utilisateur, le mot de passe, le répertoire local et le répertoire distant.  Ces valeurs doivent être personnalisées pour votre environnement.
2.  **Connexion FTP :**  Utilise la commande `ftp` pour se connecter au serveur FTP.  L'option `-n` désactive le mode de connexion automatique.
3.  **Authentification :** Envoie les commandes `user` pour l'authentification.
4.  **Changement de répertoire :** `cd` et `lcd` changent respectivement les répertoires distants et locaux.
5.  **Lister et transférer les fichiers :**
    *   `ls -l` liste les fichiers dans le répertoire local.
    *   `awk '{print "put " $9}'` extrait le nom du fichier (9e colonne de la sortie `ls -l`) et prépare la commande `put`.
    *   La sortie d'`awk` est ensuite redirigée vers une autre instance de la commande `ftp` pour effectuer le transfert.  Chaque fichier est transféré individuellement.
6.  **Déconnexion :** La commande `bye` ferme la connexion FTP.
7.  **Message de confirmation :** Affiche un message de fin.

**Note :** Ce script effectue un transfert de chaque fichier trouvé. La gestion des erreurs et des conflits de noms de fichiers n'est pas implémentée.  Il est fortement recommandé d'ajouter des contrôles supplémentaires pour une utilisation en production.  De plus, l'utilisation de mot de passe en clair dans un script est déconseillée ; il est préférable d'utiliser des méthodes d'authentification plus sécurisées (SSH keys, etc.).


## Redirection de `ls` vers un serveur FTP

| Tags |
|------|
| `ls` `FTP` `Redirection` `Terminal` |

Pour transférer la sortie de la commande `ls` vers un serveur FTP via le terminal (en supposant que l'accès au serveur FTP est configuré), redirigez la sortie vers un fichier temporaire, puis utilisez une commande FTP pour envoyer ce fichier au serveur.

Exemple :

1.  Exécutez la commande `ls` en redirigeant la sortie vers un fichier temporaire :

    ```bash
    ls > liste_fichiers.txt
    ```

2.  Utilisez une commande FTP pour envoyer ce fichier vers le serveur FTP. Exemple :

    ```bash
    ftp -n [IP] <<EOF
    user [NOM] [PASSWORD]
    put liste_fichiers.txt
    quit
    EOF
    ```

    Remplacez `[IP]`, `[NOM]` et `[PASSWORD]` par les informations correctes du serveur FTP. Assurez-vous que la commande FTP est installée.

Note : L'utilisation de FTP n'est pas sécurisée, car les données sont envoyées en clair. Utilisez SFTP (SSH File Transfer Protocol) ou d'autres méthodes sécurisées si possible.


## Exemple de "One-liner" Python

| Tags |
|------|
| `Python` `one-liner` `commande` `ls` `FTP` |

Voici un exemple de commande en une ligne pour lister les fichiers avec la commande "ls" et envoyer la sortie vers un serveur FTP :

```bash
ls | ftp -n [IP] <<EOF; user [NOM] [PASSWORD]; put - liste_fichiers.txt; quit; EOF
```

Remplacez "[IP]", "[NOM]" et "[PASSWORD]" par les informations correctes pour votre serveur FTP. Cette commande exécutera la commande "ls", enverra la liste des fichiers via FTP vers le serveur et quittera automatiquement le FTP après l'opération.


## Envoyer la sortie de "ls" via curl vers FTP

| Tags |
|------|
| `curl` `FTP` `Bash` `ls` |

Si vous préférez une autre méthode, utilisez la commande `curl` pour envoyer directement la sortie de la commande `ls` vers un serveur FTP avec l'option `--upload-file` :

```bash
ls | curl -T - ftp://username:password@server_ip/path/liste_fichiers.txt
```

Remplacez "username", "password", "server_ip" et le chemin du répertoire distant ("path") par les informations correctes pour votre serveur FTP.


## Utilisation de la commande `ls` pour l'envoi d'e-mails

| Tags |
|------|
| `ls` `mail` `bash` `command-line` |

Pour envoyer la liste des fichiers générée par la commande `ls` par e-mail, utilisez les commandes `mail` ou `mailx`, si elles sont installées. Voici un exemple :

```bash
ls | mail -s "Liste des fichiers" [EMAIL]
```

Remplacez "[EMAIL]" par l'adresse e-mail du destinataire. Cette commande enverra le résultat de `ls` sans formatage. Pour un formatage ou des détails supplémentaires, redirigez la sortie vers un fichier, formatez-le, puis utilisez `mail` pour envoyer ce fichier par e-mail.


## Partager un dossier NFS sous Debian

| Tags |
|------|
| `NFS` `Debian` `partage` `serveur` |

Pour créer un partage NFS (Network File System) sous Debian, suivez ces étapes :

1.  **Installer les paquets nécessaires :** Assurez-vous que le serveur NFS est installé sur votre système. Si ce n'est pas le cas, installez les paquets nécessaires avec la commande :

    ```bash
    sudo apt-get update
    sudo apt-get install nfs-kernel-server
    ```

2.  **Configurer les dossiers à partager :** Choisissez le dossier que vous souhaitez partager via NFS. Par exemple, supposons que vous souhaitez partager le dossier `/chemin/vers/dossier`.

3.  **Configurer les autorisations :** Assurez-vous que les autorisations appropriées sont définies sur le dossier que vous partagez. Utilisez les commandes `chmod` et `chown` pour ajuster les autorisations et le propriétaire du dossier selon vos besoins.

4.  **Configurer le partage NFS :** Ouvrez le fichier de configuration NFS `/etc/exports` en édition avec un éditeur de texte :

    ```bash
    sudo nano /etc/exports
    ```

    Ajoutez une ligne pour définir le partage, par exemple :

    ```
    /chemin/vers/dossier    [IP](rw,sync,no_subtree_check)
    ```

    Remplacez `[IP]` par l'adresse IP du client qui sera autorisé à accéder au partage. Vous pouvez utiliser `*` pour autoriser tous les clients, mais cela n'est pas recommandé pour des raisons de sécurité.

    Dans l'exemple ci-dessus, les options `rw` (lecture/écriture), `sync` (écritures synchrones) et `no_subtree_check` (désactivation de la vérification des sous-arborescences) sont utilisées.

5.  **Redémarrer le service NFS :** Une fois le fichier de configuration modifié, redémarrez le service NFS pour prendre en compte les changements :

    ```bash
    sudo systemctl restart nfs-kernel-server
    ```

6.  **Configurer le pare-feu :** Assurez-vous que les ports nécessaires pour NFS sont ouverts dans le pare-feu, généralement les ports TCP 2049 et UDP 2049.

7.  **Accéder au partage NFS depuis le client :** Sur le client, montez le partage NFS avec la commande :

    ```bash
    sudo mount [IP]:/chemin/vers/dossier /chemin/de/montage
    ```

    Remplacez `[IP]` par l'adresse IP du serveur et `/chemin/de/montage` par le chemin local où vous souhaitez monter le partage.

Assurez-vous de consulter la documentation officielle pour toute information plus détaillée ou les configurations spécifiques à votre cas.
