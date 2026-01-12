## Blocage de l'accès aux fichiers Apache

| Tags |
|------|
| `Apache` `Configuration` `Sécurité` |

Pour bloquer l'accès à des fichiers spécifiques dans Apache, plusieurs méthodes peuvent être utilisées. Cette section décrit les approches courantes et fournit des exemples de configuration.

**1. Utilisation de `.htaccess`**

Le fichier `.htaccess` permet de définir des directives de configuration au niveau du répertoire. Pour bloquer l'accès à un fichier, utilisez la directive `Require`:

```apache
<Files "fichier_sensible.txt">
  Require all denied
</Files>
```

Cette configuration, placée dans le fichier `.htaccess` du répertoire contenant `fichier_sensible.txt`, refusera l'accès à ce fichier.

**2. Configuration du VirtualHost**

La configuration du VirtualHost dans le fichier de configuration Apache (souvent `apache2.conf` ou un fichier dans `/etc/apache2/sites-available/`) permet un contrôle plus fin :

```apache
<VirtualHost *:80>
    ServerName [NOM].example.com
    DocumentRoot /var/www/html

    <Directory "/var/www/html">
        <Files "fichier_sensible.txt">
            Require all denied
        </Files>
    </Directory>
</VirtualHost>
```

Cette configuration bloque l'accès au fichier `fichier_sensible.txt` pour le VirtualHost spécifié.  Assurez-vous de redémarrer Apache après toute modification de la configuration.

**3. Blocage par type de fichier (extension)**

Il est possible de bloquer l'accès à tous les fichiers d'une extension spécifique :

```apache
<FilesMatch "\.(log|bak)$">
    Require all denied
</FilesMatch>
```

Cette directive, également applicable dans `.htaccess` ou la configuration du VirtualHost, bloque l'accès à tous les fichiers avec les extensions `.log` et `.bak`.

**4. Sécurité renforcée**

Pour une sécurité accrue, il est recommandé de :

*   Placer les fichiers sensibles en dehors du répertoire racine du serveur web.
*   Utiliser des directives `Require` avec des restrictions basées sur l'adresse IP (par exemple, `Require ip [IP]`) ou le nom d'hôte.
*   Mettre en place une authentification (via `.htaccess` et `mod_auth`) pour les répertoires sensibles.
*   Garder Apache et ses modules à jour pour corriger les failles de sécurité.

**Exemple de blocage par adresse IP:**

```apache
<Files "fichier_sensible.txt">
  Require ip [IP]
</Files>
```

Cela autorisera l'accès uniquement depuis l'adresse IP spécifiée.


## Création d'un fichier .htaccess

| Tags |
|------|
| `Apache` `htaccess` `configuration` `sécurité` |

Pour créer un fichier `.htaccess` bloquant l'accès aux fichiers, suivez ces étapes :

1.  **Ouvrez un éditeur de texte** : Utilisez un éditeur tel que Notepad, Vim, ou Nano.

2.  **Écrivez les directives** : Insérez les directives suivantes dans le fichier :

    ```apache
    Order deny,allow
    Deny from all
    ```

    Cette configuration utilise `Order`, `Deny`, et `Allow` pour contrôler l'accès. `Order deny,allow` refuse par défaut l'accès, sauf si une règle `Allow` est spécifiée. `Deny from all` bloque l'accès à tous les utilisateurs.

3.  **Enregistrez le fichier** : Nommez le fichier `.htaccess` sans extension.

4.  **Placez le fichier** : Placez `.htaccess` dans le répertoire racine de votre site ou dans le dossier à protéger. Apache appliquera les règles à ce répertoire et à ses sous-répertoires.

5.  **Testez la configuration** : Vérifiez que l'accès au site ou aux fichiers est refusé.

6.  **Vérifiez la configuration d'Apache** : Assurez-vous que votre serveur Apache est configuré pour lire les fichiers `.htaccess`. La directive `AllowOverride` doit être réglée sur `All` ou au moins `FileInfo` pour le répertoire concerné. Cette configuration se trouve dans le fichier principal d'Apache (par exemple, `httpd.conf` ou `apache2.conf`).

7.  **Redémarrez Apache** : Redémarrez le serveur Apache pour appliquer les modifications.

Notez que l'utilisation de `.htaccess` peut impacter les performances. Pour une performance optimale, configurez directement dans les fichiers de configuration principaux d'Apache et désactivez `.htaccess`, surtout pour les sites à fort trafic.
