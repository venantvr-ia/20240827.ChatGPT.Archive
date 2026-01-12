## Installation de PHP 8.3 sur Ubuntu

| Tags |
|------|
| `PHP` `Ubuntu` `Installation` `APT` |

Pour installer PHP 8.3 sur Ubuntu, suivez les étapes suivantes :

**1. Mettre à jour les paquets:**

```bash
sudo apt update
```

**2. Ajouter le dépôt Ondřej Surý (PPA):**

Ce PPA fournit des versions PHP récentes et maintenues.

```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
```

**3. Installer PHP 8.3 et les extensions courantes:**

```bash
sudo apt install php8.3 php8.3-cli php8.3-common php8.3-mysql php8.3-xml php8.3-json php8.3-opcache php8.3-gd php8.3-curl php8.3-mbstring php8.3-zip
```

**4. Vérifier l'installation:**

```bash
php -v
```

La sortie devrait afficher la version de PHP installée (8.3).

**5. Configuration (optionnel):**

Les fichiers de configuration de PHP se trouvent généralement dans `/etc/php/8.3/`.  Vous pouvez éditer `php.ini` pour ajuster les paramètres selon vos besoins.  Par exemple, pour augmenter la limite de mémoire :

```bash
sudo nano /etc/php/8.3/cli/php.ini
```

Modifiez la directive `memory_limit`.

**6. Redémarrer le serveur web (si applicable):**

Si vous utilisez PHP avec un serveur web comme Apache ou Nginx, redémarrez-le pour que les changements soient pris en compte.

*   **Apache:** `sudo systemctl restart apache2`
*   **Nginx:** `sudo systemctl restart nginx`

**Note:**  Remplacez [EMAIL] par votre propre adresse email. Pour toute question, contactez [NOM] à [EMAIL] ou visitez [IP].


## Installation de PHP 8.3 sur Ubuntu

| Tags |
|------|
| `PHP` `Ubuntu` `WordPress` `Apache` `Nginx` |

Pour installer PHP 8.3 pour WordPress sur Ubuntu, assurez-vous que votre système est à jour.

1.  **Mise à jour du système** :
    Exécutez les commandes suivantes dans le terminal :

    ```bash
    sudo apt update
    sudo apt upgrade
    ```

2.  **Ajout du dépôt PPA pour PHP** :
    Utilisez un PPA tiers pour obtenir la dernière version de PHP. Ondřej Surý maintient un PPA populaire.

    ```bash
    sudo apt install software-properties-common
    sudo add-apt-repository ppa:ondrej/php
    sudo apt update
    ```

3.  **Installation de PHP 8.3** :
    Installez PHP 8.3 et les modules courants pour WordPress.

    ```bash
    sudo apt install php8.3 php8.3-cli php8.3-fpm php8.3-mysql php8.3-xml php8.3-curl php8.3-gd php8.3-mbstring
    ```

4.  **Vérification de l'installation de PHP** :
    Vérifiez l'installation.

    ```bash
    php -v
    ```

5.  **Configuration de PHP pour votre serveur web** :

    *   **Pour Apache** : Activez le module PHP et redémarrez le service.

        ```bash
        sudo a2enmod php8.3
        sudo systemctl restart apache2
        ```

    *   **Pour Nginx** : Configurez le fichier de configuration de votre site pour utiliser le socket PHP-FPM approprié (e.g., `/etc/nginx/sites-available`).

        ```nginx
        location ~ \.php$ {
           include snippets/fastcgi-php.conf;
           fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
        }
        ```

        Redémarrez Nginx.

        ```bash
        sudo systemctl restart nginx
        ```

6.  **Installation de WordPress** :
    Téléchargez et configurez WordPress. Assurez-vous que votre base de données et votre utilisateur MySQL sont configurés.
