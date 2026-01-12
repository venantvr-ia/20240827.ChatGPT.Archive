## Changer la version PHP d'Apache

| Tags |
|------|
| `Apache` `PHP` `Configuration` |

Pour changer la version de PHP utilisée par Apache, suivez les étapes suivantes. Ce guide est applicable pour [OS] et nécessite un accès root.

**1. Identifier les versions PHP installées**

Utilisez la commande suivante pour lister les versions PHP installées sur votre système :

```bash
ls /etc/php/*/apache2/
```

Cette commande listera les fichiers de configuration Apache pour chaque version PHP installée.

**2. Désactiver le module PHP actuel**

Désactivez le module PHP actuel en utilisant la commande `a2dismod` :

```bash
sudo a2dismod php[VERSION_ACTUELLE]
```

Remplacez `[VERSION_ACTUELLE]` par la version actuellement activée (par exemple, `7.4`).

**3. Activer le nouveau module PHP**

Activez le module PHP que vous souhaitez utiliser avec la commande `a2enmod` :

```bash
sudo a2enmod php[NOUVELLE_VERSION]
```

Remplacez `[NOUVELLE_VERSION]` par la version que vous souhaitez activer (par exemple, `8.0`).

**4. Redémarrer Apache**

Redémarrez Apache pour appliquer les modifications de configuration :

```bash
sudo systemctl restart apache2
```

**5. Vérification**

Créez un fichier `info.php` dans le répertoire racine de votre serveur web (par exemple, `/var/www/html/`) avec le contenu suivant :

```php
<?php
phpinfo();
?>
```

Accédez à ce fichier via votre navigateur (par exemple, `http://[IP]/info.php`) et vérifiez la version de PHP affichée.

**6. Dépannage**

*   **Erreurs de permissions :** Assurez-vous que les permissions des fichiers et répertoires sont correctement configurées pour l'utilisateur Apache.
*   **Modules manquants :** Si votre application dépend de certains modules PHP, assurez-vous qu'ils sont installés pour la nouvelle version de PHP. Vous pouvez les installer avec `apt install php[NOUVELLE_VERSION]-[MODULE]`.
*   **Conflits de configuration :** Vérifiez les fichiers de configuration Apache pour éviter d'éventuels conflits.
*   **Logs :** Consultez les logs Apache (généralement situés dans `/var/log/apache2/`) pour identifier d'éventuelles erreurs.

**Contact**

Pour toute question, contactez [NOM] à [EMAIL].


## Migration Apache de PHP 7

| Tags |
|------|
| `Apache` `PHP` `Migration` `Linux` |

Pour migrer d'une version de PHP vers une autre, comme de PHP 7.4 à PHP 8.3 sur un serveur Apache, plusieurs étapes sont nécessaires pour gérer les différentes versions de PHP installées sur votre système. Ce guide est conçu pour un environnement Linux standard et s'applique généralement aux distributions utilisant Apache comme serveur web.


## Vérification des versions de PHP installées

| Tags |
|------|
| `PHP` `version` `installation` |

Avant de commencer, confirmez que les versions de PHP cibles sont installées sur votre système. Utilisez la commande suivante pour vérifier la version PHP par défaut :

```bash
php -v
```

Pour lister toutes les versions PHP installées, exécutez :

```bash
update-alternatives --list php
```


## Changer de version PHP pour Apache

| Tags |
|------|
| `PHP` `Apache` `a2enmod` |

Utilisez <code>a2enmod</code> pour désactiver l'ancienne version de PHP et activer la nouvelle. Par exemple, pour passer de PHP 7.4 à PHP 8.3, procédez comme suit :

```bash
sudo a2dismod php7.4
sudo a2enmod php8.3
```

Cela désactive le module pour PHP 7.4 et active celui pour PHP 8.3.


## Redémarrage d'Apache

| Tags |
|------|
| `Apache` `systemctl` `redémarrage` |

Après avoir modifié les modules, redémarrez Apache pour appliquer les modifications :

```bash
sudo systemctl restart apache2
```


## Vérification de la version active de PHP
| Tags |
|------|
| `PHP` `Apache` `Configuration` |

Après le redémarrage d'Apache, vérifiez que la nouvelle version de PHP est active en créant un fichier PHP temporaire. Par exemple, créez un fichier <code>info.php</code> dans le répertoire racine de votre serveur web (habituellement <code>/var/www/html/</code>) avec le contenu suivant :

```php
<?php
phpinfo();
?>
```

Accédez à ce fichier via votre navigateur en naviguant vers <code>http://[NOM]/info.php</code>. Cela devrait afficher les informations de configuration de PHP.


## Changer la version PHP CLI

| Tags |
|------|
| `PHP` `CLI` `update-alternatives` |

Si vous souhaitez modifier la version de PHP utilisée dans la ligne de commande, utilisez la commande `update-alternatives` :

```bash
sudo update-alternatives --set php /usr/bin/php8.3
```

Ceci configure PHP 8.3 comme version par défaut pour la CLI.


## Revenir à une version PHP antérieure
| Tags |
|------|
| `PHP` `Apache` `a2dismod` `a2enmod` |

Pour rétrograder vers PHP 7.4, les étapes sont similaires, mais inversées. Désactivez PHP 8.3 et réactivez PHP 7.4 en utilisant les commandes <code>a2dismod</code> et <code>a2enmod</code>, puis redémarrez le serveur Apache. Ces opérations permettent de basculer entre les différentes versions de PHP configurées sur le serveur Apache.


## Dépannage : Apache démarre, mais PHP ne charge pas

| Tags |
|------|
| `Apache` `PHP` `Configuration` `Dépannage` |

Si Apache démarre correctement, mais que PHP n'est pas chargé, plusieurs problèmes de configuration ou d'installation peuvent en être la cause. Voici quelques étapes pour diagnostiquer et résoudre ce problème :


## Vérification de l'installation de PHP

| Tags |
|------|
| `PHP` `Installation` `Terminal` |

Assurez-vous que PHP est correctement installé. Pour vérifier l'installation, exécutez la commande suivante dans le terminal :

```bash
php -v
```

Si cette commande ne renvoie pas la version de PHP, PHP n'est probablement pas installé correctement. Réinstallez-le.


## Vérification du Module PHP pour Apache

| Tags |
|------|
| `Apache` `PHP` `Module` `Configuration` |

Assurez-vous que le module PHP correspondant est activé pour Apache. Vérifiez les modules actifs à l'aide de la commande suivante :

```bash
apache2ctl -M
```

Recherchez une entrée similaire à <code>php7_module</code> ou <code>php8_module</code> dans la liste. Si le module PHP est absent, activez-le. Par exemple, pour activer PHP 8.3 :

```bash
sudo a2enmod php8.3
```


## Configuration de PHP dans Apache

| Tags |
|------|
| `PHP` `Apache` `Configuration` `Module` |

Vérifiez la configuration d'Apache pour vous assurer que PHP est configuré correctement. Recherchez une ligne qui charge le module PHP, généralement dans <code>php.conf</code> ou dans le fichier de configuration de votre site.  Cette ligne ressemblera à :

```apache
LoadModule php8_module /usr/lib/apache2/modules/libphp8.3.so
```

Vérifiez que le chemin et le nom du module sont corrects.


## Vérification du fichier .htaccess

| Tags |
|------|
| `Apache` `htaccess` `configuration` `PHP` |

Si un fichier <code>.htaccess</code> est utilisé pour des configurations spécifiques au site, il faut s'assurer qu'il ne contient aucune règle susceptible d'entraver l'exécution de PHP. Des règles incorrectes relatives à la gestion des types MIME ou des directives inappropriées peuvent engendrer des dysfonctionnements.


## Droits d'accès et propriétaire des fichiers

| Tags |
|------|
| `Apache` `PHP` `droits d'accès` `sécurité` |

Vérifiez que les fichiers de configuration et les modules PHP disposent des droits d'accès et appartiennent aux utilisateurs et groupes appropriés. Utiliser la commande suivante :

```bash
ls -l /etc/apache2/mods-available/php*.load
```

Les fichiers doivent généralement appartenir à root.


## Redémarrage d'Apache

| Tags |
|------|
| `Apache` `systemctl` `redémarrage` |

Après avoir effectué les modifications, redémarrez Apache pour appliquer les changements :

```bash
sudo systemctl restart apache2
```


## Dépannage PHP : Consulter les logs d'erreur

| Tags |
|------|
| `PHP` `Apache` `Logs` `Dépannage` |

Si PHP ne se charge toujours pas, consultez les logs d'erreur d'Apache pour identifier la source du problème :

```bash
sudo tail -f /var/log/apache2/error.log
```

Cette commande affiche les erreurs en temps réel lors de l'accès aux pages PHP.


## Erreur FCGI Apache : "No such file or directory"

| Tags |
|------|
| `Apache` `FCGI` `PHP-FPM` `Socket` `Error` |

Pourquoi est-ce que vous rencontrez l'erreur suivante dans les logs Apache : « [Thu Apr 25 14:30:18.689667 2024] [proxy:error] [pid 2448707] (2)No such file or directory: AH02454: FCGI: attempt to connect to Unix domain socket /run/php/php8.3-fpm.sock (*) failed » ?


## Résolution d'erreur de connexion PHP-FPM

| Tags |
|------|
| `Apache` `PHP-FPM` `FastCGI` `Unix Socket` `Configuration` |

L'erreur dans les logs Apache signale une tentative de connexion d'Apache au socket Unix de PHP-FPM, mais ce dernier est introuvable. Cette situation résulte généralement d'une configuration PHP-FPM incorrecte ou d'un service PHP-FPM non démarré. La procédure de résolution est la suivante :


## Vérification et Démarrage de PHP-FPM

| Tags |
|------|
| `PHP-FPM` `systemctl` `Bash` `PHP` |

<ol>
<li>
<p><strong>Vérification de l'état de PHP-FPM :</strong></p>
<pre><code class="language-bash">sudo systemctl status php8.3-fpm
</code></pre>
</li>
<li>
<p><strong>Démarrage de PHP-FPM (si arrêté) :</strong></p>
<pre><code class="language-bash">sudo systemctl start php8.3-fpm
</code></pre>
</li>
<li>
<p><strong>Installation de PHP-FPM (si absent) :</strong></p>
<pre><code class="language-bash">sudo apt install php8.3-fpm
</code></pre>
</li>
</ol>


## Vérification de la configuration PHP-FPM

| Tags |
|------|
| `PHP-FPM` `PHP 8.3` `Configuration` `Socket Unix` |

<ol>
<li>
<p><strong>Accéder au fichier de configuration PHP-FPM pour PHP 8.3</strong>. Le fichier principal se situe généralement à :</p>
<pre><code class="language-bash">/etc/php/8.3/fpm/pool.d/www.conf
</code></pre>
</li>
<li>
<p><strong>Localiser la ligne définissant le chemin du socket Unix</strong>. Exemple :</p>
<pre><code>listen = /run/php/php8.3-fpm.sock
</code></pre>
</li>
<li>
<p><strong>Vérifier que le chemin spécifié est correct et que le dossier <code>/run/php/</code> existe</strong>. Commande de vérification :</p>
<pre><code class="language-bash">ls -l /run/php/
</code></pre>
</li>
</ol>


## Vérification de la configuration Apache

| Tags |
|------|
| `Apache` `PHP-FPM` `Configuration` `Serveur Web` |

<ol>
<li>
<p><strong>Vérifiez la configuration d'Apache pour l'utilisation de PHP-FPM</strong>. La configuration spécifique à un site se trouve généralement dans le fichier de configuration du site, sous <code>/etc/apache2/sites-available/</code>, ou dans un fichier de configuration global.</p>
</li>
<li>
<p><strong>La directive de configuration doit être similaire à l'exemple suivant</strong> :</p>
<pre><code class="language-apache">&lt;FilesMatch &quot;\.php$&quot;&gt;
    SetHandler &quot;proxy:unix:/run/php/php8.3-fpm.sock|fcgi://localhost/&quot;
&lt;/FilesMatch&gt;
</code></pre>
</li>
<li>
<p><strong>Vérifiez que le chemin du socket correspond à celui spécifié dans la configuration de PHP-FPM</strong>.</p>
</li>
</ol>


## Redémarrage des services PHP-FPM et Apache

| Tags |
|------|
| `PHP-FPM` `Apache` `systemctl` `configuration` |

<ol>
<li>
<strong>Redémarrez PHP-FPM et Apache pour appliquer les changements</strong> :
<pre><code class="language-bash">sudo systemctl restart php8.3-fpm
sudo systemctl restart apache2
</code></pre>
</li>
</ol>


## Vérification des logs pour les erreurs

| Tags |
|------|
| `Apache` `PHP-FPM` `logs` `dépannage` |

<ol>
<li>
<strong>Après avoir redémarré les services, examinez de nouveau les logs d'erreur d'Apache</strong> pour déterminer si le problème persiste :
<pre><code class="language-bash">sudo tail /var/log/apache2/error.log
</code></pre>
</li>
</ol>
<p>En suivant ces étapes, vous devriez être en mesure de résoudre l'erreur de connexion au socket PHP-FPM et de vous assurer que PHP est correctement chargé par Apache.</p>


## Dépannage du démarrage de php8.3-fpm

| Tags |
|------|
| `PHP-FPM` `systemctl` `dépannage` `configuration` |

Si le service <code>php8.3-fpm</code> est chargé mais reste inactif après une tentative de démarrage, cela indique généralement un problème avec la configuration de PHP-FPM ou une autre condition qui empêche le service de démarrer correctement. Voici quelques étapes pour diagnostiquer et résoudre ce problème :


## Dépannage du service : Vérification de l'état du service

| Tags |
|------|
| `PHP` `systemctl` `dépannage` `Linux` |

La première étape consiste à obtenir des détails sur la raison pour laquelle le service ne démarre pas. Cela peut être fait en vérifiant l'état du service :

```bash
sudo systemctl status php8.3-fpm
```

Examinez les messages d'erreur dans l'état. Les erreurs courantes peuvent inclure des problèmes de configuration, des fichiers manquants ou des problèmes de permissions.


## Vérification des logs PHP-FPM

| Tags |
|------|
| `PHP-FPM` `logs` `journalctl` |

PHP-FPM utilise un système de journalisation pour fournir des informations sur les problèmes potentiels. Les logs pertinents sont consultables via la commande suivante :

```bash
sudo journalctl -u php8.3-fpm
```

Examinez les entrées de log pour détecter les erreurs. Ces erreurs peuvent identifier des problèmes spécifiques, tels que des erreurs de syntaxe dans les fichiers de configuration ou des problèmes liés aux extensions PHP.


## Configuration de PHP-FPM : Examen et vérification

| Tags |
|------|
| `PHP-FPM` `configuration` `syntaxe` `fichiers de configuration` |

Un problème de configuration est une cause fréquente d'échec de démarrage de PHP-FPM. Examinez le fichier de configuration principal et les fichiers de pool associés :

```bash
sudo nano /etc/php/8.3/fpm/php-fpm.conf
sudo nano /etc/php/8.3/fpm/pool.d/www.conf
```

Vérifiez les erreurs de syntaxe et les valeurs incorrectes. Assurez-vous que le fichier de configuration est correctement structuré et que les chemins de fichiers et sockets sont corrects et existants.


## Permissions et propriétaires de fichiers PHP-FPM

| Tags |
|------|
| `PHP-FPM` `permissions` `configuration` |

Assurez-vous que les fichiers de configuration et les répertoires utilisés par PHP-FPM disposent des permissions adéquates et appartiennent aux utilisateurs appropriés. Des problèmes de permission peuvent empêcher le démarrage correct de PHP-FPM.

Vérifiez et ajustez les permissions comme suit :

```bash
sudo chown -R www-data:www-data /var/lib/php/sessions
sudo chown -R www-data:www-data /var/lib/php/wsdlcache
```


## Redémarrage du service

| Tags |
|------|
| `PHP` `systemctl` `fpm` |

Après avoir effectué les modifications nécessaires, redémarrez le service :

```bash
sudo systemctl restart php8.3-fpm
```


## Vérification du statut PHP-FPM après redémarrage

| Tags |
|------|
| `PHP-FPM` `systemctl` `démarrage` `statut` |

Après le redémarrage, vérifiez le statut du service pour confirmer son activation :

```bash
sudo systemctl status php8.3-fpm
```

Si le service est toujours inactif, examinez les journaux système pour identifier la cause ou vérifiez la configuration de démarrage automatique.


## Résolution d'un problème de compatibilité Xdebug

| Tags |
|------|
| `Xdebug` `PHP` `Zend Engine` `Compatibilité` |

Le service php-fpm8.3 a généré le message d'erreur suivant le 25 avril à 14:26:48 sur la machine rvv-GE62VR-7RF : "Xdebug requires Zend Engine API version 420200930. The Zend Engine API version 420230831 which is installed, is newer. Contact Derick Rethans at https://xdebug.org/docs/faq#api for a later version of Xdebug."

Ce message indique une incompatibilité entre la version installée de Xdebug et la version de Zend Engine présente sur le système. La version de Xdebug installée est plus ancienne que la version de Zend Engine, ce qui entraîne le dysfonctionnement.

Pour résoudre ce problème, il est nécessaire de mettre à jour Xdebug vers une version compatible avec la version de Zend Engine installée. La documentation de Xdebug fournit des informations sur la compatibilité des versions. Veuillez consulter la FAQ de Xdebug à l'adresse suivante : https://xdebug.org/docs/faq#api.

La mise à jour de Xdebug peut se faire via le gestionnaire de paquets utilisé sur le système. Par exemple, sous Debian/Ubuntu, on pourrait utiliser :

```bash
sudo apt update
sudo apt install php-xdebug
```

Ou, si une version spécifique est requise :

```bash
sudo pecl install xdebug
```

Après l'installation ou la mise à jour, redémarrer le service php-fpm8.3 pour appliquer les changements.


## Erreur de compatibilité Xdebug et PHP-FPM

| Tags |
|------|
| `PHP` `Xdebug` `PHP-FPM` `Compatibilité` `Débogage` |

L'erreur rencontrée avec PHP-FPM signale une incompatibilité entre la version de Xdebug installée et la version de PHP utilisée (PHP 8.3). Explication et résolution :


## Erreur Xdebug et incompatibilité PHP

| Tags |
|------|
| `Xdebug` `PHP` `API` `Compatibilité` |

L'erreur indique une incompatibilité entre la version de Xdebug et la version de PHP utilisée.

*   **Xdebug requires Zend Engine API version 420200930**: Xdebug est compilé pour une ancienne version de PHP (probablement PHP 8.0).
*   **The Zend Engine API version 420230831 which is installed, is newer**: La version de PHP en cours d'utilisation (PHP 8.3) utilise une version plus récente de l'API Zend Engine.
*   **Contact Derick Rethans at [URL] for a later version of Xdebug**: Il est recommandé de vérifier si une version plus récente de Xdebug, compatible avec PHP 8.3, est disponible.


## Résolution du Problème

| Tags |
|------|
| `dépannage` `solutions` `configuration` |

Voici quelques solutions possibles pour résoudre le problème rencontré :

1.  **Vérification de la connectivité réseau**

    Assurez-vous que votre appareil est correctement connecté au réseau. Vérifiez les points suivants :

    *   Câblage : Assurez-vous que les câbles réseau sont correctement branchés sur votre appareil et sur le routeur.
    *   Wi-Fi : Si vous utilisez une connexion Wi-Fi, assurez-vous d'être connecté au bon réseau et que le signal est suffisamment fort.
    *   Adresse IP : Vérifiez que votre appareil possède une adresse IP valide. Vous pouvez utiliser la commande `ipconfig` (Windows) ou `ifconfig` (Linux/macOS) pour vérifier votre configuration réseau. Si vous n'avez pas d'adresse IP, essayez de redémarrer votre routeur et votre appareil.

2.  **Vérification des paramètres du pare-feu**

    Un pare-feu mal configuré peut bloquer l'accès à certaines applications ou services. Vérifiez les points suivants :

    *   Règles du pare-feu : Assurez-vous que le pare-feu n'empêche pas les applications ou services concernés de communiquer.
    *   Exceptions : Ajoutez des exceptions pour les applications ou services qui ont besoin d'accéder à Internet.

3.  **Vérification des paramètres DNS**

    Les problèmes de résolution de noms de domaine peuvent empêcher l'accès à certains sites web. Vérifiez les points suivants :

    *   Serveurs DNS : Assurez-vous que votre appareil utilise des serveurs DNS valides. Vous pouvez utiliser les serveurs DNS de votre fournisseur d'accès Internet, ou des serveurs DNS publics tels que ceux de Google (8.8.8.8 et 8.8.4.4) ou Cloudflare (1.1.1.1 et 1.0.0.1).
    *   Cache DNS : Videz le cache DNS de votre appareil pour vous assurer qu'il utilise les dernières informations. Pour vider le cache DNS sous Windows, vous pouvez utiliser la commande `ipconfig /flushdns`.

4.  **Vérification des paramètres du proxy**

    Si vous utilisez un serveur proxy, assurez-vous qu'il est correctement configuré. Vérifiez les points suivants :

    *   Configuration : Vérifiez les paramètres du proxy dans les paramètres de votre navigateur ou de votre système d'exploitation.
    *   Authentification : Si le proxy nécessite une authentification, assurez-vous d'utiliser les informations d'identification correctes.

5.  **Recherche de logiciels malveillants**

    Les logiciels malveillants peuvent causer des problèmes de connectivité réseau. Effectuez une analyse complète de votre système avec un logiciel antivirus à jour.

6.  **Contact du support technique**

    Si les solutions ci-dessus ne fonctionnent pas, contactez le support technique de votre fournisseur d'accès Internet ou de l'application concernée. Fournissez-leur autant d'informations que possible sur le problème, y compris les messages d'erreur et les étapes que vous avez déjà essayées.

    Vous pouvez contacter [NOM] à [EMAIL] ou [IP].


## Mise à jour de Xdebug pour PHP 8.3

| Tags |
|------|
| `Xdebug` `PHP 8.3` `pecl` `Configuration` |

La première étape consiste à vérifier et, si nécessaire, à mettre à jour Xdebug pour garantir la compatibilité avec PHP 8.3. Utilisez <code>pecl</code>, le gestionnaire de paquets PHP, pour l'installation ou la mise à jour :

```bash
sudo pecl install xdebug
```

Après l'installation, confirmez que la configuration de Xdebug est correcte dans votre fichier <code>php.ini</code> ou dans un fichier de configuration dédié à Xdebug situé dans <code>/etc/php/8.3/fpm/conf.d/</code>.


## Vérification de la configuration Xdebug

| Tags |
|------|
| `Xdebug` `PHP` `Configuration` `Debug` |

Après la mise à jour, vérifiez la configuration de Xdebug. Consulter le fichier de configuration (généralement <code>20-xdebug.ini</code>) :

```bash
cat /etc/php/8.3/fpm/conf.d/20-xdebug.ini
```

La configuration doit inclure :

```ini
zend_extension=xdebug.so
```


## Redémarrer PHP-FPM

| Tags |
|------|
| `PHP-FPM` `Xdebug` `Configuration` |

Après la mise à jour et la configuration de Xdebug, redémarrez PHP-FPM pour appliquer les modifications :

```bash
sudo systemctl restart php8.3-fpm
```


## Vérification du fonctionnement de PHP-FPM

| Tags |
|------|
| `PHP-FPM` `systemctl` `PHP` |

Vérifiez l'état de PHP-FPM :

```bash
sudo systemctl status php8.3-fpm
```


## Tester l'installation de Xdebug

| Tags |
|------|
| `Xdebug` `PHP` `Test` |

Pour vérifier le bon fonctionnement de Xdebug, créez un script PHP contenant la fonction `phpinfo();`. L'exécution de ce script doit afficher les informations relatives à Xdebug.


## Désactivation Temporaire de Xdebug

| Tags |
|------|
| `Xdebug` `PHP-FPM` `PHP` `Configuration` |

Si Xdebug n'est pas immédiatement requis, et pour assurer le bon fonctionnement de PHP-FPM, désactivez temporairement Xdebug :

```bash
sudo phpdismod xdebug
sudo systemctl restart php8.3-fpm
```

Ceci permet à PHP-FPM de démarrer sans charger Xdebug, contournant l'erreur jusqu'à ce qu'une version compatible de Xdebug soit installée.


## Suppression des versions PHP obsolètes

| Tags |
|------|
| `PHP` `APT` `Linux` `Gestion des paquets` `Ubuntu` `Debian` |

Pour supprimer les versions PHP non désirées tout en conservant PHP 7.4 et 8.3, suivez ces étapes. Cette procédure nettoiera votre environnement et garantira que seules les versions spécifiées sont actives. Ce guide est conçu pour les systèmes Linux utilisant APT (commun sur des distributions telles qu'Ubuntu ou Debian).


## Lister les versions de PHP installées
| Tags |
|------|
| `PHP` `installation` `dpkg` `ligne de commande` |

Pour commencer, identifiez les versions de PHP installées sur votre système. Utilisez la commande suivante pour afficher les paquets PHP installés :

```bash
dpkg -l | grep php
```


## Suppression des versions PHP obsolètes

| Tags |
|------|
| `PHP` `apt-get` `suppression` |

Ensuite, employez la commande <code>apt-get remove</code> pour désinstaller les versions non désirées. Veillez à conserver les versions 7.4 et 8.3. Par exemple, pour supprimer PHP 7.2 et PHP 7.3, utilisez :

```bash
sudo apt-get purge php7.2*
sudo apt-get purge php7.3*
```

Ces commandes suppriment les paquets associés aux versions PHP spécifiées. Le caractère générique <code>*</code> assure la suppression de tous les paquets liés.


## Vérification des versions PHP actives pour Apache

| Tags |
|------|
| `PHP` `Apache` `Configuration` |

Si Apache est utilisé, vérifier que seules les versions PHP 7.4 et 8.3 sont activées :

```bash
sudo a2dismod php7.2 php7.3  # Désactivez les anciennes versions
sudo a2enmod php7.4 php8.3  # Activez les versions que vous souhaitez conserver
```


## Redémarrer Apache

| Tags |
|------|
| `Apache` `systemctl` `serveur` |

Après avoir modifié la configuration d'Apache, redémarrez le serveur pour appliquer les changements :

```bash
sudo systemctl restart apache2
```


## Nettoyage des dépendances inutilisées

| Tags |
|------|
| `APT` `Linux` `Dépendances` `Gestion des paquets` |

Après la suppression des paquets, utilisez la commande suivante pour nettoyer les dépendances inutilisées et libérer de l'espace disque :

```bash
sudo apt-get autoremove
```


## Vérification des versions PHP installées
| Tags |
|------|
| `PHP` `CLI` `FPM` `version` |

Après le nettoyage du système, vérifiez les versions de PHP installées :

```bash
php -v  # Vérifiez la version de la CLI de PHP
```

Pour chaque version de FPM conservée, vérifiez :

```bash
php7.4 -v
php8.3 -v
```

Ces vérifications permettent de confirmer l'installation et le fonctionnement des versions PHP.


## Vérification de l'extension PHP mysqli

| Tags |
|------|
| `PHP` `mysqli` `extension` `configuration` |

Pour vérifier si l'extension <code>mysqli</code> pour PHP est installée et activée sur votre système, suivez les étapes suivantes. Ces instructions permettent de confirmer la disponibilité et le bon fonctionnement de l'extension pour différentes versions de PHP, notamment PHP 7.4 et PHP 8.3.


## Vérification de l'installation de MySQLi avec phpinfo()

| Tags |
|------|
| `PHP` `MySQLi` `phpinfo()` `Serveur Web` |

<ol>
<li>
<p><strong>Création du fichier de test PHP</strong>:
Créez un fichier nommé <code>test.php</code> dans le répertoire racine de votre serveur web (généralement <code>/var/www/html/</code>) avec le code suivant :</p>
<pre><code class="language-php">&lt;?php
phpinfo();
?&gt;
</code></pre>
</li>
<li>
<p><strong>Accès au fichier via un navigateur web</strong>:
Ouvrez un navigateur et accédez à l'URL suivante : <code>http://localhost/test.php</code> ou <code>http://[IP]/test.php</code>. Remplacez <code>[IP]</code> par l'adresse IP de votre serveur.</p>
</li>
<li>
<p><strong>Recherche de MySQLi</strong>:
Utilisez la fonction de recherche de votre navigateur (Ctrl + F ou Cmd + F) et recherchez "mysqli".  Si l'extension est installée, une section dédiée à <code>mysqli</code> affichera les informations de configuration et les chemins d'accès.</p>
</li>
</ol>


## Vérification de l'installation via la CLI

| Tags |
|------|
| `PHP` `MySQLi` `CLI` |

<ol>
<li>
<p><strong>Exécution d'une commande PHP</strong> :</p>
<p>Utilisez la commande suivante dans votre terminal pour vérifier si l'extension mysqli est chargée :</p>
<pre><code class="language-bash">php -m | grep mysqli
</code></pre>
<p>Si mysqli est installé et actif, la commande affichera <code>mysqli</code> dans la sortie.</p>
</li>
</ol>


## Vérification de la configuration PHP par version

| Tags |
|------|
| `PHP` `configuration` `mysqli` `PHP 7.4` `PHP 8.3` |

Si des versions spécifiques de PHP doivent être vérifiées (ex : PHP 7.4, PHP 8.3), utilisez les commandes suivantes :

```bash
php7.4 -m | grep mysqli
php8.3 -m | grep mysqli
```


## Installation/Activation de mysqli

| Tags |
|------|
| `PHP` `MySQLi` `Installation` `Configuration` |

Si <code>mysqli</code> n'est pas installé ou activé :

1.  **Installer mysqli pour PHP** : Installer <code>mysqli</code> avec <code>apt</code> pour les distributions Debian :

    ```bash
    sudo apt-get install php7.4-mysqli php8.3-mysqli
    ```

2.  **Activer l'extension** : Si l'extension est installée mais non activée, modifier le fichier de configuration PHP (ex: <code>/etc/php/7.4/cli/php.ini</code> ou <code>/etc/php/8.3/cli/php.ini</code>) et s'assurer que la ligne suivante est décommentée :

    ```ini
    extension=mysqli
    ```

3.  **Redémarrer le serveur web** : Redémarrer le serveur web pour appliquer les changements :

    ```bash
    sudo systemctl restart apache2
    ```


## Tester la connexion MySQLi

| Tags |
|------|
| `PHP` `MySQLi` `Connexion` `Base de données` |

Après avoir vérifié l'installation et l'activation, testez <code>mysqli</code> avec un script PHP simple. Cet exemple tente de se connecter à une base de données MySQL :

```php
<?php
$mysqli = new mysqli("localhost", "mon_utilisateur", "mon_mot_de_passe", "nom_de_ma_base");

if ($mysqli->connect_error) {
    die("Échec de la connexion : " . $mysqli->connect_error);
} else {
    echo "Connexion réussie.";
}
?>
```

Remplacez <code>"mon_utilisateur"</code>, <code>"mon_mot_de_passe"</code> et <code>"nom_de_ma_base"</code> par vos identifiants. Un message "Connexion réussie" indique que <code>mysqli</code> fonctionne.


## Résoudre l'erreur "sudo: pecl : commande introuvable"

| Tags |
|------|
| `PECL` `PHP` `Debian` `Ubuntu` `sudo` |

Si l'erreur <code>sudo: pecl : commande introuvable</code> s'affiche, cela indique que l'outil <code>pecl</code> n'est pas installé. PECL (PHP Extension Community Library) est nécessaire pour installer les extensions PHP.

Voici comment installer et configurer PECL sur les systèmes basés sur Debian ou Ubuntu.


## Installation des prérequis

| Tags |
|------|
| `PHP` `PECL` `Installation` |

Pour installer PECL, installez le paquet <code>php-pear</code> et <code>php-dev</code>. Ce dernier contient les fichiers nécessaires à la compilation des extensions PHP. Assurez-vous également d'avoir les outils de développement et le compilateur C installés :

```bash
sudo apt-get update
sudo apt-get install php-pear php-dev build-essential
```


## Installer PECL (si nécessaire)

| Tags |
|------|
| `PECL` `PHP` `installation` `command-line` |

Normalement, l'installation de <code>php-pear</code> installe également PECL. Pour vérifier l'installation de PECL, exécutez la commande suivante :

```bash
pecl version
```

Si la commande n'est pas reconnue et qu'aucune version n'est retournée, vérifiez le chemin d'installation ou tentez une liaison manuelle de PECL :

```bash
sudo ln -s /usr/bin/pecl /usr/local/bin/pecl
```


## Vérification de la configuration PHP

| Tags |
|------|
| `PHP` `php.ini` `PECL` |

Après l'installation, confirmez que PHP est configuré pour charger les extensions installées via PECL. Vérifiez le fichier <code>php.ini</code> pour vous assurer que le répertoire des extensions est correctement configuré.

Exécutez la commande suivante pour déterminer le chemin :

```bash
php -i | grep extension_dir
```


## Installation d'extensions PHP avec PECL

| Tags |
|------|
| `PHP` `PECL` `Xdebug` `Extension` |

Avec PECL installé, vous pouvez installer des extensions PHP. Par exemple, pour installer l'extension Xdebug, utilisez la commande suivante :

```bash
sudo pecl install xdebug
```


## Configuration PHP pour l'extension installée

| Tags |
|------|
| `PHP` `PECL` `php.ini` `Xdebug` |

Après l'installation d'une extension via PECL, il est nécessaire de l'ajouter au fichier <code>php.ini</code>. Pour l'extension Xdebug, la ligne suivante est ajoutée :

```ini
zend_extension=xdebug.so
```


## Redémarrage du serveur web

| Tags |
|------|
| `Apache` `Nginx` `Serveur web` `PHP` |

Pour appliquer les changements, redémarrez le serveur web.

Exemple pour Apache :
```bash
sudo systemctl restart apache2
```

Exemple pour Nginx :
```bash
sudo systemctl restart nginx
```

Ces étapes permettent d'installer PECL et d'utiliser ses extensions avec la configuration PHP.


## Installation de Xdebug pour PHP 7

| Tags |
|------|
| `Xdebug` `PHP 7` `PECL` `Extension` |

Pour installer Xdebug pour PHP 7.4 et 8.3 via PECL, suivez les étapes suivantes pour configurer chaque version de PHP avec la version appropriée de l'extension Xdebug.


## Préparation du système

| Tags |
|------|
| `PHP` `installation` `environnement` |

Avant de commencer, installez les outils nécessaires à la compilation des extensions PHP et les paquets <code>php-dev</code> spécifiques à chaque version de PHP :

```bash
sudo apt-get update
sudo apt-get install php-pear php-dev build-essential
sudo apt-get install php7.4-dev php8.3-dev
```


## Installation de Xdebug par version PHP

| Tags |
|------|
| `Xdebug` `PHP` `PECL` `Installation` |

PECL facilite l'installation d'extensions PHP, en spécifiant le chemin vers les binaires <code>phpize</code> et <code>php-config</code>. L'installation de Xdebug est nécessaire pour chaque version de PHP.

1.  **Pour PHP 7.4 :**

    ```bash
    sudo pecl install xdebug-2.9.8  # Cette version est compatible avec PHP 7.4
    ```

2.  **Pour PHP 8.3 :**

    ```bash
    sudo pecl install xdebug  # Cela installera la dernière version compatible avec PHP 8.3
    ```

Lors de l'installation via PECL, il est important d'utiliser les bons <code>phpize</code> et <code>php-config</code> si l'invite le demande. Le chemin correct peut être spécifié pour chaque version :

*   Pour PHP 7.4 :

    ```bash
    sudo pecl -d php_suffix=7.4 install xdebug-2.9.8
    ```

*   Pour PHP 8.3 :

    ```bash
    sudo pecl -d php_suffix=8.3 install xdebug
    ```


## Activer Xdebug dans les configurations PHP

| Tags |
|------|
| `Xdebug` `PHP` `php.ini` `Configuration` |

Après l'installation de Xdebug, configurez <code>php.ini</code> pour chaque version de PHP afin de charger Xdebug :

1.  **Pour PHP 7.4** :
    Ajoutez la ligne suivante à votre <code>php.ini</code> (généralement <code>/etc/php/7.4/apache2/php.ini</code> et <code>/etc/php/7.4/cli/php.ini</code>) :

    ```ini
    zend_extension=xdebug.so
    ```

2.  **Pour PHP 8.3** :
    Ajoutez la même ligne aux fichiers <code>php.ini</code> pour PHP 8.3 (par exemple, <code>/etc/php/8.3/apache2/php.ini</code> et <code>/etc/php/8.3/cli/php.ini</code>) :

    ```ini
    zend_extension=xdebug.so
    ```


## Configuration de base de Xdebug

| Tags |
|------|
| `Xdebug` `PHP` `Configuration` `Débogage` |

Vous pouvez configurer Xdebug pour le débogage à distance. Ajoutez les lignes suivantes à vos fichiers <code>php.ini</code>, sous les sections Xdebug, pour chaque version :

```ini
xdebug.mode = debug
xdebug.start_with_request = yes
xdebug.client_host = "127.0.0.1"
xdebug.client_port = 9003  # Assurez-vous que ce port est libre et adapté à vos besoins
```


## Redémarrage du serveur web

| Tags |
|------|
| `Apache` `serveur web` `redémarrage` |

Une fois la configuration terminée, redémarrez le serveur web pour appliquer les changements :

```bash
sudo systemctl restart apache2
```


## Vérification de l'installation de Xdebug

| Tags |
|------|
| `Xdebug` `PHP` `Configuration` `Vérification` |

Pour vérifier la bonne installation et configuration de Xdebug, créez un fichier PHP contenant la fonction `phpinfo()` et accédez-y via votre navigateur. Recherchez la section Xdebug pour confirmer que l'extension est chargée et correctement configurée.


## Xdebug non affiché dans phpinfo()

| Tags |
|------|
| `Xdebug` `PHP` `phpinfo` `configuration` `extension` |

Si Xdebug n'est pas visible dans la sortie de <code>phpinfo()</code> après l'installation et la configuration, cela suggère un problème avec l'installation, la configuration, ou le chargement de l'extension par PHP. Voici quelques étapes de diagnostic et de résolution :


## Vérification de l'installation de Xdebug

| Tags |
|------|
| `Xdebug` `PHP` `installation` `pecl` |

<ol>
<li>
<p><strong>Vérifier l'installation de Xdebug :</strong> Utilisez la commande <code>pecl list</code> pour confirmer que Xdebug est une extension installée.</p>
</li>
<li>
<p><strong>Identifier le chemin d'accès de l'extension Xdebug :</strong> Exécutez <code>php-config --extension-dir</code> pour localiser le répertoire d'installation des extensions PHP.</p>
<pre><code class="language-bash">php-config --extension-dir
</code></pre>
<p>Vérifiez que Xdebug se trouve dans ce répertoire.</p>
</li>
</ol>


## Vérification du fichier php.ini

| Tags |
|------|
| `PHP` `php.ini` `Xdebug` |

<ol>
<li>
<p><strong>Vérification du fichier php.ini utilisé :</strong>
Dans le fichier <code>phpinfo()</code>, vérifiez la valeur de <code>Loaded Configuration File</code> pour vous assurer que le fichier <code>php.ini</code> modifié est le bon.</p>
</li>
<li>
<p><strong>Vérification de la directive zend_extension :</strong>
Assurez-vous que la ligne suivante est présente et correctement formatée dans le fichier <code>php.ini</code> :</p>
<pre><code class="language-ini">zend_extension=/chemin_complet/xdebug.so
</code></pre>
<p>Remplacez <code>/chemin_complet/</code> par le chemin correct vers le fichier <code>xdebug.so</code>.</p>
</li>
<li>
<p><strong>Vérification des erreurs de syntaxe ou de chemin :</strong>
Inspectez le fichier <code>php.ini</code> pour toute erreur de syntaxe ou de chemin, car celles-ci peuvent empêcher le chargement de l'extension.</p>
</li>
</ol>


## Redémarrage du Serveur Web

| Tags |
|------|
| `Apache` `systemctl` `php.ini` `Serveur Web` |

<ol>
<li>
<strong>Redémarrez votre serveur web</strong> :
Après avoir effectué des modifications sur <code>php.ini</code> ou autre, assurez-vous de redémarrer votre serveur web pour appliquer les changements.
<pre><code class="language-bash">sudo systemctl restart apache2
</code></pre>
</li>
</ol>


## Vérification de la version de PHP

| Tags |
|------|
| `PHP` `Xdebug` `Version` |

<ol>
<li>
<strong>Vérification de la version de PHP :</strong>
S'assurer que la version de PHP utilisée est celle pour laquelle Xdebug a été configuré.  Effectuer cette vérification via la commande suivante :
<pre><code class="language-bash">php -v
</code></pre>
ou
<pre><code class="language-bash">php7.4 -v
php8.3 -v
</code></pre>
</li>
</ol>


## Vérification des Logs d'Erreur

| Tags |
|------|
| `PHP` `Apache` `Logs` `Dépannage` |

<ol>
<li>
<strong>Consulter les logs d'erreur PHP et Apache</strong> : Les logs peuvent aider à identifier les causes d'un problème de chargement d'extension.

<pre><code class="language-bash">sudo tail -f /var/log/apache2/error.log
</code></pre>
ou pour les erreurs PHP spécifiques :
<pre><code class="language-bash">sudo tail -f /var/log/php7.4-fpm.log
sudo tail -f /var/log/php8.3-fpm.log
</code></pre>
</li>
</ol>


## Tester Xdebug avec un script PHP

| Tags |
|------|
| `Xdebug` `PHP` `Test` |

<ol>
<li>
<strong>Création d'un script de test pour Xdebug :</strong>
Créez un script PHP simple pour vérifier l'activation de Xdebug :
</li>
</ol>
```php
<?php
var_dump(function_exists('xdebug_info'));
xdebug_info();
```

Exécutez ce script pour confirmer l'état de Xdebug.


## Dépannage Xdebug : Guide de résolution

| Tags |
|------|
| `Xdebug` `PHP` `Debugging` `Configuration` |

En suivant ces étapes, vous devriez être en mesure de diagnostiquer la raison pour laquelle Xdebug ne s'affiche pas dans votre configuration PHP et de résoudre le problème. Assurez-vous que chaque étape est soigneusement vérifiée pour éliminer toutes les causes possibles.


## Désinstallation complète de Xdebug

| Tags |
|------|
| `Xdebug` `PHP` `PECL` `php.ini` `Désinstallation` |

Pour supprimer complètement Xdebug de votre système, suivez ces étapes :

1.  **Désinstaller l'extension via PECL**

    Utilisez la commande PECL pour désinstaller l'extension Xdebug.  Ouvrez votre terminal et exécutez la commande suivante :

    ```bash
    pecl uninstall xdebug
    ```

2.  **Supprimer la configuration de `php.ini`**

    Ouvrez votre fichier `php.ini`. L'emplacement de ce fichier dépend de votre environnement PHP. Vous pouvez trouver son emplacement en utilisant la fonction `phpinfo()`. Recherchez toutes les lignes contenant `xdebug` et supprimez-les. Cela inclut, par exemple :

    ```ini
    zend_extension=xdebug.so
    xdebug.mode=debug
    xdebug.start_upon_error=yes
    xdebug.client_host=[IP]
    xdebug.client_port=9003
    ```

3.  **Redémarrer le serveur web**

    Pour que les modifications prennent effet, redémarrez votre serveur web. La méthode de redémarrage dépend de votre serveur (Apache, Nginx, etc.). Par exemple, pour Apache sous Linux, vous pourriez utiliser :

    ```bash
    sudo service apache2 restart
    ```

    Ou, pour Nginx :

    ```bash
    sudo service nginx restart
    ```

    Après le redémarrage, vérifiez que Xdebug n'est plus chargé en utilisant `phpinfo()` dans un script PHP, ou en vérifiant les logs de votre serveur.

## Désinstallation de Xdebug avec PECL

| Tags |
|------|
| `Xdebug` `PECL` `PHP` `Désinstallation` |

Vous pouvez désinstaller Xdebug en utilisant la commande `pecl` :

```bash
sudo pecl uninstall xdebug
```


## Désactivation de Xdebug dans php.ini

| Tags |
|------|
| `PHP` `Xdebug` `php.ini` `Apache` `CLI` |

1.  **Localisation des fichiers <code>php.ini</code> :**

    *   **Pour Apache :**
        Utilisez les commandes suivantes pour éditer les fichiers <code>php.ini</code> pour vos versions PHP :
        ```bash
        sudo nano /etc/php/7.4/apache2/php.ini
        sudo nano /etc/php/8.3/apache2/php.ini
        ```

    *   **Pour CLI :**
        Utilisez les commandes suivantes pour éditer les fichiers <code>php.ini</code> pour vos versions PHP :
        ```bash
        sudo nano /etc/php/7.4/cli/php.ini
        sudo nano /etc/php/8.3/cli/php.ini
        ```

2.  **Suppression ou mise en commentaire des configurations Xdebug :**

    Ouvrez chaque fichier <code>php.ini</code> et identifiez les lignes relatives à Xdebug. Mettez-les en commentaire en préfixant chaque ligne avec un point-virgule (<code>;</code>) ou supprimez-les. Les configurations typiques à identifier sont :

    ```ini
    zend_extension=xdebug.so
    xdebug.remote_enable=1
    xdebug.remote_connect_back=1
    xdebug.remote_port=9000
    xdebug.idekey="votre_idekey"
    ```


## Redémarrage du Serveur Web

| Tags |
|------|
| `Apache` `PHP-FPM` `systemctl` |

Après avoir effectué les modifications, redémarrez le serveur web pour appliquer les changements. Instructions pour Apache et PHP-FPM :

*   **Redémarrer Apache** :

```bash
sudo systemctl restart apache2
```

*   **Redémarrer PHP-FPM** (si utilisé) :

```bash
sudo systemctl restart php7.4-fpm
sudo systemctl restart php8.3-fpm
```


## Vérification de la Désinstallation de Xdebug

| Tags |
|------|
| `Xdebug` `PHP` `Désinstallation` `phpinfo` `Module PHP` |

Après le redémarrage du serveur web, vérifiez la suppression complète de Xdebug :

*   **Vérification des modules PHP chargés :**

    Exécutez les commandes suivantes :

    ```bash
    php -m | grep xdebug
    php7.4 -m | grep xdebug
    php8.3 -m | grep xdebug
    ```

    Si `grep` ne retourne aucun résultat, Xdebug n'est plus chargé.

*   **Vérification via `phpinfo()` :**

    Créez un fichier PHP (par exemple `info.php`) avec le code suivant :

    ```php
    <?php
    phpinfo();
    ?>
    ```

    Accédez à ce fichier via votre navigateur pour confirmer l'absence de Xdebug.

En suivant ces étapes, la suppression de Xdebug est confirmée.


## Réinstallation de Xdebug pour PHP 8

| Tags |
|------|
| `Xdebug` `PHP` `PHP 8` `Debian` `Ubuntu` |

Pour réinstaller Xdebug pour PHP 8.3 sur votre serveur, suivez les étapes ci-dessous. Celles-ci supposent que vous utilisez un système basé sur Debian ou Ubuntu. Si vous utilisez une autre distribution Linux, les commandes peuvent varier légèrement.


## Installer les Prérequis

| Tags |
|------|
| `PHP` `Xdebug` `Installation` `PHP 8.3` `apt-get` |

Avant d'installer Xdebug, il est nécessaire d'installer PHP 8.3, ainsi que les outils de développement et les fichiers d'en-tête PHP requis pour la compilation des extensions :

```bash
sudo apt-get update
sudo apt-get install php8.3 php8.3-dev php-pear build-essential
```


## Installation de Xdebug avec PECL

| Tags |
|------|
| `Xdebug` `PECL` `PHP` `Installation` |

Utilisez PECL pour installer Xdebug. Cette méthode assure l'installation de la dernière version compatible avec PHP 8.3 :

```bash
sudo pecl install xdebug
```

Pour les environnements avec plusieurs versions de PHP, spécifiez le binaire PHP à utiliser :

```bash
sudo pecl -d php_suffix=8.3 install xdebug
```


## Configuration de PHP pour Xdebug

| Tags |
|------|
| `PHP` `Xdebug` `php.ini` `Configuration` |

Après l'installation, configurez PHP pour charger l'extension Xdebug.  Cela implique d'ajouter une configuration au fichier `php.ini` ou à un fichier spécifique de configuration Xdebug dans le répertoire de configuration PHP.

1.  **Localisation du fichier `php.ini` approprié.**  Pour PHP 8.3 avec Apache, le fichier peut être :

    ```bash
    sudo nano /etc/php/8.3/apache2/php.ini
    ```

    Pour l'interface en ligne de commande (CLI) :

    ```bash
    sudo nano /etc/php/8.3/cli/php.ini
    ```

2.  **Ajout de la configuration Xdebug** à la fin du fichier `php.ini`.  Spécifiez le chemin complet du fichier `.so` de Xdebug, généralement installé dans `/usr/lib/php/20200930` ou `/usr/lib/php/20210902`.  Déterminez le chemin avec :

    ```bash
    find /usr/lib/php/ -name 'xdebug.so'
    ```

    Ajoutez ensuite la configuration suivante dans `php.ini` :

    ```ini
    [Xdebug]
    zend_extension=/chemin/vers/xdebug.so
    xdebug.mode=debug
    xdebug.start_with_request=yes
    xdebug.client_host=127.0.0.1
    xdebug.client_port=9003
    ```


## Redémarrage du Serveur Web

| Tags |
|------|
| `Apache` `PHP-FPM` `systemctl` `redémarrage` |

Pour appliquer les modifications, redémarrez le serveur web :

*   Pour Apache :

```bash
sudo systemctl restart apache2
```

*   Pour PHP-FPM :

```bash
sudo systemctl restart php8.3-fpm
```


## Vérification de l'installation de Xdebug

| Tags |
|------|
| `Xdebug` `PHP` `Configuration` `Serveur Web` |

Pour vérifier l'installation et la configuration de Xdebug, créez le fichier `info.php` suivant dans le répertoire racine de votre serveur web :

```php
<?php
phpinfo();
?>
```

Accédez à ce fichier via un navigateur web en naviguant vers `http://[VOTRE_DOMAINE]/info.php`. Vérifiez la présence de 'Xdebug' dans la sortie de `phpinfo()` pour confirmer l'installation et la configuration réussies.


## Installer cURL pour PHP 7

| Tags |
|------|
| `PHP` `cURL` `Debian` `Ubuntu` `Extension` |

Pour installer l'extension PHP cURL pour PHP 7.4 et PHP 8.3 sur un système basé sur Debian ou Ubuntu, les étapes varient selon la version de PHP.


## Mise à jour de la liste des paquets

| Tags |
|------|
| `apt-get` `Linux` `paquets` `terminal` |

Ouvrez un terminal et mettez à jour la liste des paquets pour obtenir les dernières versions disponibles :

```bash
sudo apt-get update
```


## Installation de cURL pour PHP

| Tags |
|------|
| `PHP` `cURL` `installation` `apt-get` |

Pour installer le module cURL pour chaque version de PHP, exécutez les commandes suivantes :

*   **Pour PHP 7.4 :**

```bash
sudo apt-get install php7.4-curl
```

*   **Pour PHP 8.3 :**

```bash
sudo apt-get install php8.3-curl
```
Ces commandes installent les modules cURL spécifiques à chaque version de PHP.


## Vérification de l'installation de cURL

| Tags |
|------|
| `cURL` `PHP` `Installation` `Vérification` |

Après l'installation, confirmez que l'extension cURL est correctement installée en utilisant la commande <code>php -m</code>. Cette commande liste tous les modules PHP chargés. Exécutez cette vérification pour chaque version de PHP installée :

*   **Pour PHP 7.4** :

```bash
php7.4 -m | grep curl
```

*   **Pour PHP 8.3** :

```bash
php8.3 -m | grep curl
```

Si <code>curl</code> apparaît dans la liste des modules, l'extension est installée avec succès pour la version de PHP spécifiée.


## Redémarrage du serveur web

| Tags |
|------|
| `Apache` `Nginx` `PHP` `systemctl` |

Si vous utilisez PHP avec un serveur web comme Apache ou Nginx, redémarrez le serveur pour charger les nouvelles extensions :

*   **Pour Apache** :

```bash
sudo systemctl restart apache2
```

*   **Pour Nginx avec PHP-FPM** :

```bash
sudo systemctl restart php7.4-fpm
sudo systemctl restart php8.3-fpm
```


## Tester l'extension cURL

| Tags |
|------|
| `cURL` `PHP` `Test` `HTTP` |

Pour vérifier le bon fonctionnement de cURL, créez un script PHP simple. Par exemple, sauvegardez le code suivant dans un fichier nommé <code>test_curl.php</code> :

```php
<?php
$ch = curl_init("http://example.com");
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$data = curl_exec($ch);
curl_close($ch);
echo $data;
?>
```

Placez ce fichier dans le répertoire racine de votre serveur web. Accédez à ce fichier via votre navigateur. Si le contenu de "http://example.com" s'affiche, l'installation de cURL est réussie.


## Prévention des ReflectionException

| Tags |
|------|
| `PHP` `Reflection` `Exception` `__construct` |

L'exception `ReflectionException: Method Pods\Integrations\Polylang::__construct() does not exist` est levée.  Le code en cause est le suivant :

```php
try {
    $constructorReflection = new ReflectionMethod($className, '__construct');
} catch (ReflectionException $e) {
    static::$constructorParametersCache[$className] = [];
    // No constructor method, no args.
    return [];
}
```


## Résolution ReflectionException avec ReflectionMethod

| Tags |
|------|
| `PHP` `Reflection` `Exception` `__construct` |

L'exception `ReflectionException` est levée lorsque `ReflectionMethod` est utilisé pour une classe sans constructeur. L'erreur indique que la classe cible (`Pods\Integrations\Polylang`) n'a pas de méthode constructeur (`__construct()`).

Pour éviter cette exception, vérifiez l'existence du constructeur avant d'instancier `ReflectionMethod`. Voici une modification possible :


## Analyse de code PHP : Gestion des constructeurs

| Tags |
|------|
| `PHP` `Reflection` `constructeur` `exception` |

```php
try {
    if (method_exists($className, '__construct')) {
        $constructorReflection = new ReflectionMethod($className, '__construct');
    } else {
        throw new ReflectionException("Method {$className}::__construct() does not exist");
    }
} catch (ReflectionException $e) {
    static::$constructorParametersCache[$className] = [];
    // No constructor method, no args.
    return [];
}
```


## Modification du code : Explication détaillée

| Tags |
|------|
| `PHP` `Reflection` `Exception Handling` |

<ol>
<li>
<p><strong>Vérification du constructeur :</strong> Le code vérifie si la méthode <code>__construct()</code> existe dans la classe spécifiée en utilisant <code>method_exists()</code> avant d'instancier <code>ReflectionMethod</code>. Cette fonction retourne <code>true</code> si la méthode existe, et <code>false</code> sinon.</p>
</li>
<li>
<p><strong>Gestion des exceptions :</strong> Si la méthode <code>__construct()</code> n'existe pas, une <code>ReflectionException</code> est explicitement lancée avec un message personnalisé. Cette exception est capturée dans le bloc <code>catch</code> suivant.</p>
</li>
<li>
<p><strong>Bloc Catch :</strong> Le bloc <code>catch</code> gère l'erreur en définissant le cache des paramètres du constructeur à un tableau vide. Cela indique qu'aucun paramètre de constructeur n'est nécessaire pour cette classe, permettant au script de continuer sans interruption.</p>
</li>
</ol>


## Avantages de la Vérification des Méthodes

| Tags |
|------|
| `programmation` `robustesse` `gestion des erreurs` |

*   **Robustesse Améliorée :** Vérifier l'existence d'une méthode avant de l'appeler diminue le risque d'exceptions imprévues, améliorant la robustesse du code.

*   **Gestion des Erreurs :** La gestion explicite des cas où une méthode est absente permet de contrôler la réaction de l'application (journalisation, mesures correctives).


## Conclusion de la Réflexion PHP Améliorée

| Tags |
|------|
| `PHP` `réflexion` `gestion des erreurs` |

Cette approche améliore la fiabilité du traitement de la réflexion en PHP, en garantissant que les tentatives de réflexion ne provoquent pas d'exceptions non gérées. Elle permet également une gestion d'erreur plus souple et adaptable selon les exigences de votre application.


## Gestion globale des exceptions PHP
| Tags |
|------|
| `PHP` `Exceptions` `Gestion d'erreurs` |

Pour gérer les exceptions de manière globale dans votre application PHP, afin d'empêcher l'interruption du flux d'exécution par des exceptions telles que <code>ReflectionException</code>, plusieurs stratégies architecturales sont possibles. Cela inclut l'implémentation d'un gestionnaire d'exceptions global et l'utilisation de mécanismes de middleware dans les frameworks supportant cette approche.


## Gestion des exceptions globales en PHP

| Tags |
|------|
| `PHP` `exceptions` `set_exception_handler` |

PHP offre la possibilité de configurer un gestionnaire d'exceptions global qui traitera les exceptions non gérées. La fonction <code>set_exception_handler()</code> permet de définir ce gestionnaire. Voici un exemple :

```php
function exception_handler($exception) {
    echo "Exception non capturée: " , $exception->getMessage(), "\n";
    // Logique supplémentaire pour gérer l'exception
}

set_exception_handler('exception_handler');

// Votre code habituel ici
```


## Utilisation de Middleware dans les Frameworks

| Tags |
|------|
| `middleware` `framework` `gestion d'erreurs` |

Si votre application utilise un framework supportant les middlewares, il est possible d'insérer un middleware de gestion d'erreurs. Ce dernier agit comme un filtre pour toutes les requêtes. Les frameworks modernes tels que Laravel, Symfony (via des composants), ou Slim, offrent la possibilité de créer des middlewares pour intercepter et gérer les exceptions de manière appropriée.


## Gestion des exceptions avec Symfony

| Tags |
|------|
| `Symfony` `PHP` `Event Listener` `kernel.exception` |

Dans Symfony, un Event Listener ou un Event Subscriber peut être utilisé pour écouter l'événement `kernel.exception`. Voici un exemple de configuration :

```php
namespace App\EventListener;

use Symfony\Component\HttpKernel\Event\ExceptionEvent;
use Symfony\Component\HttpFoundation\Response;

class ExceptionListener
{
    public function onKernelException(ExceptionEvent $event)
    {
        $exception = $event->getThrowable();
        $message = sprintf(
            'Erreur de l\'application: %s avec le code: %s',
            $exception->getMessage(),
            $exception->getCode()
        );

        // Envoyer une réponse personnalisée
        $response = new Response();
        $response->setContent($message);
        $event->setResponse($response);
    }
}
```


## Avantages des gestionnaires et middlewares

| Tags |
|------|
| `gestion des erreurs` `middleware` `PHP` |

<ol>
<li>
<p><strong>Centralisation de la gestion des erreurs :</strong> Les gestionnaires et middlewares centralisent la gestion des erreurs, simplifiant la maintenance et assurant une gestion cohérente des exceptions.</p>
</li>
<li>
<p><strong>Séparation des préoccupations :</strong> Ces approches séparent la gestion des erreurs du code métier, améliorant la lisibilité et la maintenabilité.</p>
</li>
<li>
<p><strong>Réponse cohérente :</strong> Elles garantissent une réponse uniforme en cas d'erreur, essentiel pour les API avec des formats de réponse spécifiques.</p>
</li>
</ol>
<p>En utilisant ces stratégies, les exceptions telles que <code>ReflectionException</code> peuvent être gérées, évitant ainsi leur remontée inattendue dans le pipeline PHP. Cela permet un contrôle précis sur le flux d'exécution de l'application.</p>


## Installation locale de SonarQube

| Tags |
|------|
| `SonarQube` `Installation` `Linux` `Java` |
<p>L'installation locale de SonarQube permet d'analyser la qualité du code source. Ce guide présente l'installation étape par étape de SonarQube sur un système Linux. La présence de Java est requise pour le fonctionnement de SonarQube.</p>


## Installation de Java

| Tags |
|------|
| `Java` `SonarQube` `Installation` |

SonarQube requiert Java pour fonctionner. La version recommandée pour les versions récentes de SonarQube est Java 11.

Pour l'installer :

```bash
sudo apt update
sudo apt install openjdk-11-jdk
```

Vérification de l'installation :

```bash
java -version
```


## Téléchargement de SonarQube

| Tags |
|------|
| `SonarQube` `téléchargement` `installation` |

<ol>
<li>
<p>Téléchargez la dernière version de SonarQube sur le site officiel : <a href="https://www.sonarqube.org/downloads/">https://www.sonarqube.org/downloads/</a>.</p>
</li>
<li>
<p>Décompressez l'archive :</p>
</li>
</ol>
<pre><code class="language-bash">cd /opt
sudo wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.x.x.zip
sudo unzip sonarqube-9.x.x.zip
sudo mv sonarqube-9.x.x sonarqube
</code></pre>
<p>Remplacez <code>9.x.x</code> par la version téléchargée.</p>


## Configuration de SonarQube

| Tags |
|------|
| `SonarQube` `configuration` `sonar.properties` |

Les fichiers de configuration se trouvent dans <code>/opt/sonarqube/conf/</code>. Le fichier principal à configurer est <code>sonar.properties</code>.

**Configuration de la base de données** (Optionnel):

Par défaut, SonarQube utilise une base de données H2 intégrée, déconseillée en production. Pour les tests locaux, la configuration par défaut est suffisante. Pour une utilisation plus poussée, il est recommandé de configurer une connexion à une base de données externe telle que PostgreSQL.


## Lancement de SonarQube

| Tags |
|------|
| `SonarQube` `Sécurité` `Utilisateur` `Installation` |

<ol>
<li>
<p><strong>Droits d'utilisateur</strong> :
Pour des raisons de sécurité, SonarQube ne doit pas être exécuté en tant que root. Il est recommandé de créer un utilisateur dédié :</p>
<pre><code class="language-bash">sudo groupadd sonar
sudo useradd -c &quot;User for SonarQube&quot; -d /opt/sonarqube -g sonar -s /bin/bash sonar
sudo chown -R sonar:sonar /opt/sonarqube
</code></pre>
</li>
<li>
<p><strong>Démarrage de SonarQube</strong> :
Commutez vers l'utilisateur créé et démarrez SonarQube :</p>
<pre><code class="language-bash">sudo su - sonar
/opt/sonarqube/bin/linux-x86-64/sonar.sh start
</code></pre>
</li>
</ol>


## Accéder à SonarQube

| Tags |
|------|
| `SonarQube` `accès` `web` |

Ouvrez un navigateur web et accédez à <code>http://localhost:9000</code>. Les identifiants par défaut sont <code>admin</code> pour le nom d'utilisateur et <code>admin</code> pour le mot de passe.


## Analyser un Projet avec SonarQube

| Tags |
|------|
| `SonarQube` `analyse de code` `qualité du code` |

Pour analyser un projet, configurez le scanner SonarQube pour votre environnement de développement ou utilisez le scanner accessible via le portail web SonarQube. Reportez-vous à la documentation SonarQube pour des instructions spécifiques à votre environnement.

En suivant ces étapes, vous devriez pouvoir installer et configurer SonarQube localement pour l'analyse de la qualité du code. Consultez la documentation officielle de SonarQube pour des informations détaillées et les configurations spécifiques à votre environnement.


## Suppression complète d'un conteneur Docker SonarQube

| Tags |
|------|
| `Docker` `SonarQube` `conteneurs` `volumes` `images` |

Pour supprimer complètement un conteneur Docker exécutant SonarQube, ainsi que toutes les données associées (volumes, images, réseaux), suivez ces étapes. Cette approche est utile pour réinitialiser l'installation de SonarQube ou libérer des ressources sur le système.

**1. Arrêter et supprimer le conteneur**

Arrêtez le conteneur SonarQube en cours d'exécution et supprimez-le :

```bash
docker stop <container_id_or_name>
docker rm <container_id_or_name>
```

Remplacez `<container_id_or_name>` par l'ID ou le nom du conteneur SonarQube.  Vous pouvez trouver l'ID ou le nom en utilisant la commande `docker ps -a`.

**2. Supprimer le volume persistant**

Si vous avez utilisé un volume Docker pour persister les données de SonarQube (recommandé pour conserver les données entre les redémarrages), supprimez ce volume :

```bash
docker volume ls # pour lister les volumes
docker volume rm <volume_name>
```

Remplacez `<volume_name>` par le nom du volume utilisé par SonarQube.  Vous pouvez lister les volumes avec `docker volume ls` et identifier celui utilisé par SonarQube grâce à la commande `docker inspect <container_id_or_name>`.  Recherchez la section "Mounts".

**3. Supprimer l'image Docker**

Supprimez l'image Docker SonarQube.  Cela supprimera l'image téléchargée depuis le registre Docker :

```bash
docker images # pour lister les images
docker rmi <image_id_or_name>
```

Remplacez `<image_id_or_name>` par l'ID ou le nom de l'image SonarQube. Vous pouvez lister les images avec `docker images`.

**4. Supprimer le réseau (si applicable)**

Si SonarQube utilisait un réseau Docker spécifique, supprimez-le :

```bash
docker network ls # pour lister les réseaux
docker network rm <network_name>
```

Remplacez `<network_name>` par le nom du réseau utilisé par SonarQube.

**Exemple complet**

Supposons que le conteneur s'appelle `sonarqube-instance`, que le volume se nomme `sonarqube_data`, et que l'image s'appelle `sonarqube:latest`. Voici un exemple de commandes :

```bash
docker stop sonarqube-instance
docker rm sonarqube-instance
docker volume ls
docker volume rm sonarqube_data
docker images
docker rmi sonarqube:latest
```

**Note importante :** Cette procédure supprimera définitivement toutes les données associées à SonarQube.  Assurez-vous de sauvegarder les données importantes avant de procéder si nécessaire.


## Identifier le conteneur SonarQube

| Tags |
|------|
| `Docker` `SonarQube` `conteneur` |

Pour identifier le conteneur Docker exécutant SonarQube, utilisez la commande suivante :

```bash
docker ps
```

Cette commande liste les conteneurs en cours d'exécution. Si le conteneur SonarQube est arrêté, utilisez la commande suivante pour lister tous les conteneurs :

```bash
docker ps -a
```

Recherchez le <code>CONTAINER ID</code> ou le <code>NAME</code> de votre conteneur SonarQube.


## Arrêt du conteneur SonarQube

| Tags |
|------|
| `Docker` `SonarQube` `Conteneur` |

Avant de supprimer le conteneur, arrêtez-le. Utilisez le <code>CONTAINER ID</code> ou le <code>NAME</code> que vous avez identifié précédemment :

```bash
docker stop [CONTAINER ID ou NAME]
```


## Suppression d'un conteneur Docker

| Tags |
|------|
| `Docker` `Conteneur` `Suppression` |

Après l'arrêt d'un conteneur, utilisez la commande suivante pour le supprimer :

```bash
docker rm [CONTAINER ID ou NAME]
```


## Suppression des volumes Docker

| Tags |
|------|
| `Docker` `Volumes` `SonarQube` |

Si des volumes Docker ont été créés pour la persistance des données SonarQube, il est recommandé de les supprimer pour un nettoyage complet. Commencez par identifier les volumes :

```bash
docker volume ls
```

Identifiez les volumes associés à SonarQube, en vous basant notamment sur leurs noms, puis supprimez-les :

```bash
docker volume rm [VOLUME NAME]
```


## Suppression de l'image Docker SonarQube

| Tags |
|------|
| `Docker` `SonarQube` `Image` `rmi` |

Si vous souhaitez supprimer l'image Docker de SonarQube, identifiez l'image :

```bash
docker images
```

Recherchez l'image SonarQube dans la liste et utilisez l'<code>IMAGE ID</code> ou <code>REPOSITORY:TAG</code> pour la supprimer :

```bash
docker rmi [IMAGE ID ou REPOSITORY:TAG]
```


## Nettoyage des ressources Docker

| Tags |
|------|
| `Docker` `Conteneurs` `Nettoyage` |

Pour nettoyer les ressources Docker inutilisées (réseaux, images, conteneurs arrêtés, volumes), utiliser :

```bash
docker system prune
```

Pour inclure également les volumes non utilisés dans le nettoyage :

```bash
docker system prune --volumes
```


## Suppression de SonarQube et de ses données

| Tags |
|------|
| `SonarQube` `Docker` `Suppression` `Données` |

Ces étapes permettent la suppression complète de SonarQube et de ses données associées d'un environnement Docker. Cette procédure est utile lors de mises à jour majeures, de réinstallations ou pour libérer de l'espace disque.

Il est impératif de sauvegarder toutes les données importantes avant de procéder à la suppression, en particulier en environnement de production.


## Installation de SonarQube sur Debian/Ubuntu

| Tags |
|------|
| `SonarQube` `Debian` `Ubuntu` `Installation` `apt` |

Installer SonarQube directement via <code>apt</code> sur un système Debian ou Ubuntu n'est pas possible en utilisant les dépôts officiels, car SonarQube n'est pas disponible dans les dépôts standards de ces systèmes d'exploitation. Cependant, vous pouvez installer SonarQube sur un système Linux en suivant une série d'étapes qui impliquent le téléchargement manuel du package depuis le site officiel de SonarQube, l'installation de Java, et la configuration de SonarQube. Voici comment procéder :


## Installation de Java

| Tags |
|------|
| `Java` `SonarQube` `Installation` `OpenJDK` |

SonarQube requiert Java pour fonctionner. L'installation de Java 11 est recommandée via <code>apt</code> :

```bash
sudo apt update
sudo apt install openjdk-11-jdk
```

Vérification de l'installation :

```bash
java -version
```


## Installation de SonarQube

| Tags |
|------|
| `SonarQube` `Installation` `Community Edition` `Linux` |

<ol>
<li>
<p><strong>Téléchargement de SonarQube</strong></p>
<ul>
<li>Téléchargez la dernière version de la Community Edition de SonarQube depuis le site officiel : <a href="https://www.sonarqube.org/downloads/">https://www.sonarqube.org/downloads/</a>.</li>
</ul>
</li>
<li>
<p><strong>Décompression de l'archive</strong></p>
<ul>
<li>Placez le fichier téléchargé dans un répertoire approprié, tel que <code>/opt</code> :</li>
</ul>
<pre><code class="language-bash">sudo mv chemin/vers/sonarqube-*.zip /opt/
cd /opt
sudo unzip sonarqube-*.zip
sudo mv sonarqube-* sonarqube
</code></pre>
</li>
<li>
<p><strong>Modification des permissions</strong></p>
<ul>
<li>Pour des raisons de sécurité, exécutez SonarQube avec un utilisateur dédié plutôt que root. Créez un utilisateur et attribuez-lui les fichiers :</li>
</ul>
<pre><code class="language-bash">sudo adduser sonarqube
sudo chown -R sonarqube:sonarqube /opt/sonarqube
</code></pre>
</li>
</ol>


## Configuration de SonarQube

| Tags |
|------|
| `SonarQube` `configuration` `sonar.properties` `mémoire` |

<ol>
<li>
<p><strong>Modification de la configuration</strong> :</p>
<ul>
<li>Modifier le fichier de configuration de SonarQube pour personnaliser les paramètres :</li>
</ul>
<pre><code class="language-bash">sudo nano /opt/sonarqube/conf/sonar.properties
</code></pre>
<ul>
<li>Exemple de configuration : paramétrer une base de données autre que H2, ou configurer les paramètres du serveur.</li>
</ul>
</li>
<li>
<p><strong>Limitation de l'utilisation de la mémoire</strong> (recommandé) :</p>
<ul>
<li>Ajuster les paramètres de mémoire Java pour SonarQube dans le script de démarrage :</li>
</ul>
<pre><code class="language-bash">sudo nano /opt/sonarqube/bin/linux-x86-64/sonar.sh
</code></pre>
<ul>
<li>Modifier les lignes contenant <code>SONARQUBE_OPTS</code>.</li>
</ul>
</li>
</ol>


## Démarrage de SonarQube

| Tags |
|------|
| `SonarQube` `démarrage` `script` `bash` |

<ol>
<li>
<strong>Utiliser le script de démarrage pour lancer SonarQube :</strong>
<ul>
<li>En tant qu'utilisateur <code>sonarqube</code> :</li>
</ul>
<pre><code class="language-bash">sudo su sonarqube
/opt/sonarqube/bin/linux-x86-64/sonar.sh start
</code></pre>
</li>
</ol>


## Accès à SonarQube

| Tags |
|------|
| `SonarQube` `Installation` `Configuration` |

Accédez à l'interface web de SonarQube en ouvrant votre navigateur et en accédant à l'adresse suivante : `http://[IP]:9000`.

Connectez-vous avec les identifiants par défaut : `admin/admin`. Suivez ensuite les instructions pour sécuriser votre installation.

Cette procédure illustre l'installation de SonarQube sur un système Linux en téléchargeant et en configurant manuellement l'application, sans utiliser `apt` pour une installation directe.


## Téléchargement SonarQube avec `wget`

| Tags |
|------|
| `SonarQube` `wget` `téléchargement` `installation` |

Il semble que le lien de téléchargement utilisé pour SonarQube ne soit pas directement fonctionnel car il contient une version générique (`9.x.x`) qui n'existe pas en tant qu'URL directe. Il est nécessaire de remplacer `9.x.x` par le numéro de version spécifique souhaité.


## Téléchargement de la Version SonarQube

| Tags |
|------|
| `SonarQube` `Installation` `Téléchargement` |

<ol>
<li>
<p><strong>Accéder au lien de téléchargement officiel</strong> : Visitez le site web officiel de SonarQube pour obtenir le lien de téléchargement direct de la version désirée.</p>
<ul>
<li>Naviguez vers la page <a href="https://www.sonarqube.org/downloads/">SonarQube Downloads</a>.</li>
</ul>
</li>
<li>
<p><strong>Sélectionner la version</strong> : Choisissez la version appropriée, telle que la dernière version stable de la Community Edition.</p>
</li>
<li>
<p><strong>Copier le lien de téléchargement</strong> : Copiez le lien de téléchargement direct de la version sélectionnée.</p>
</li>
</ol>


## Téléchargement de SonarQube avec wget

| Tags |
|------|
| `SonarQube` `wget` `téléchargement` `installation` |

Une fois le lien correct obtenu, utilisez <code>wget</code> pour télécharger le fichier :

```bash
sudo wget [lien_direct_du_fichier_zip]
```

Par exemple, si la dernière version est la <code>9.5</code>, le lien sera quelque chose comme :

```bash
sudo wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.5.0.56709.zip
```

Remplacez l'URL ci-dessus par l'URL exacte trouvée sur le site de SonarQube.


## Décompression et installation de SonarQube

| Tags |
|------|
| `SonarQube` `Installation` `Bash` |

Après le téléchargement, procéder à la décompression et à l'installation :

```bash
sudo unzip sonarqube-9.5.0.56709.zip -d /opt/
sudo mv /opt/sonarqube-9.5.0.56709 /opt/sonarqube
```

Ajuster le nom du répertoire en fonction de la version téléchargée.


## Configuration et Vérification SonarQube

| Tags |
|------|
| `SonarQube` `configuration` `sonar.properties` |

Continuez la configuration de SonarQube comme précédemment décrit, en incluant la configuration du fichier `sonar.properties`, la création d'un utilisateur système et le démarrage du service.


## Conclusion de l'utilisation de wget

| Tags |
|------|
| `wget` `téléchargement` `URL` |

Assurez-vous d'utiliser le lien exact correspondant à la version souhaitée pour le téléchargement. Les liens génériques ou mal formés ne fonctionneront pas avec <code>wget</code> ou d'autres outils de téléchargement.


## Emplacement des logs SonarQube

| Tags |
|------|
| `SonarQube` `Logs` `Dépannage` |

Les logs de SonarQube sont cruciaux pour le diagnostic des problèmes et la surveillance du fonctionnement de l'application. Par défaut, SonarQube stocke ses fichiers de log dans un répertoire spécifique à l'installation.  Voici les emplacements courants :


## Emplacement des Logs SonarQube

| Tags |
|------|
| `SonarQube` `Logs` `Configuration` |

<ol>
<li>
<p><strong>Dossier des logs</strong> :</p>
<ul>
<li>Les logs de SonarQube sont stockés dans le dossier <code>logs</code>, situé dans le répertoire d'installation de SonarQube.</li>
<li>
Si l'installation a suivi les instructions typiques (par exemple, dans <code>/opt/sonarqube</code>), les logs se trouvent dans :
<pre><code>/opt/sonarqube/logs
</code></pre>
</li>
</ul>
</li>
<li>
<p><strong>Fichiers de log importants</strong> :</p>
<ul>
<li><strong>sonar.log</strong> : Journalise les messages généraux et les erreurs liées au démarrage de SonarQube.</li>
<li><strong>web.log</strong> : Journalise les activités de l'application web de SonarQube.</li>
<li><strong>ce.log</strong> : Contient des informations sur les tâches de traitement en arrière-plan (Compute Engine).</li>
<li><strong>es.log</strong> : Fournit les logs d'Elasticsearch, utilisé pour la recherche et l'indexation des données.</li>
<li><strong>access.log</strong> : Trace les requêtes HTTP accédant à SonarQube.</li>
</ul>
</li>
</ol>
<p>Les logs permettent d'identifier les erreurs de configuration, les problèmes de performance, ou les défaillances système. Pour les problèmes de démarrage, consulter <code>sonar.log</code> et <code>web.log</code>.</p>


## Accès aux fichiers logs

| Tags |
|------|
| `logs` `terminal` `tail` `SonarQube` |

Pour accéder aux fichiers log, utilisez les commandes terminal telles que <code>cat</code>, <code>less</code>, ou <code>tail</code>.  Pour suivre les dernières entrées du fichier <code>web.log</code> en temps réel, utilisez :

```bash
tail -f /opt/sonarqube/logs/web.log
```

Cette commande est utile pour surveiller les logs lors du démarrage de SonarQube ou lors de l'exécution d'analyses.


## Sécurité et Rotation des Logs SonarQube

| Tags |
|------|
| `SonarQube` `Logs` `Sécurité` `Rotation` |

*   **Sécurité** : Configurez les permissions des fichiers de logs afin d'empêcher tout accès non autorisé.
*   **Rotation des logs** : SonarQube implémente la rotation des logs pour éviter une croissance excessive des fichiers de logs. Les paramètres de rotation des logs sont configurables.

La connaissance des emplacements et des rôles des fichiers de logs facilite la gestion et le dépannage de l'installation SonarQube.


## Installation de Java (Ubuntu)

| Tags |
|------|
| `Java` `Ubuntu` `Installation` |

Pour installer Java sur Ubuntu, il est important de noter que la version <code>61.0</code> n'est pas une version standard. Si vous souhaitez installer une version spécifique de Java (Java 11 ou une autre version LTS), suivez les instructions appropriées.


## Installation d'OpenJDK sur Ubuntu

| Tags |
|------|
| `OpenJDK` `Java` `Ubuntu` `apt` |

OpenJDK est l'implémentation open source de la plateforme Java, disponible dans les dépôts officiels d'Ubuntu.

**Étape 1 : Mettre à jour la liste des paquets**

```bash
sudo apt update
```

**Étape 2 : Installer Java**

Pour installer Java 11, une version LTS (Long Term Support) courante, exécutez :

```bash
sudo apt install openjdk-11-jdk
```

**Étape 3 : Vérifier l'installation**

Après l'installation, vérifiez la version de Java :

```bash
java -version
```

Cela affichera la version, la distribution, et d'autres informations sur l'installation de Java.


## Installation d'Oracle JDK

| Tags |
|------|
| `Java` `JDK` `Oracle` `Linux` |

Si vous préférez utiliser Oracle JDK au lieu de OpenJDK pour des raisons spécifiques, vous pouvez télécharger et installer la version la plus récente directement depuis le site web d'Oracle. Voici comment procéder :

**Étape 1 : Télécharger Oracle JDK**

1.  Visitez le [site officiel d'Oracle](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) pour télécharger le JDK.
2.  Acceptez l'accord de licence.
3.  Téléchargez le fichier `.tar.gz` approprié pour les systèmes basés sur Linux.

**Étape 2 : Extraire le fichier téléchargé**

Supposons que vous ayez téléchargé le fichier dans votre dossier `~/Downloads`.

```bash
cd ~/Downloads
tar -xzf jdk-11.x.x_linux-x64_bin.tar.gz
```

Remplacez `jdk-11.x.x_linux-x64_bin.tar.gz` par le nom exact du fichier que vous avez téléchargé.

**Étape 3 : Installer Java**

1.  Déplacez le dossier JDK extrait vers `/usr/lib/jvm/` :

```bash
sudo mkdir -p /usr/lib/jvm
sudo mv jdk-11.x.x /usr/lib/jvm/oraclejdk11
```

2.  Configurez cette installation comme alternative par défaut pour Java :

```bash
sudo update-alternatives --install /usr/bin/java java /usr/lib/jvm/oraclejdk11/bin/java 100
sudo update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/oraclejdk11/bin/javac 100
```

**Étape 4 : Sélectionner la version par défaut**

Si vous avez plusieurs installations de Java, vous pouvez sélectionner la version par défaut avec :

```bash
sudo update-alternatives --config java
sudo update-alternatives --config javac
```

Suivez les instructions à l'écran pour choisir la version par défaut de Java.


## Installation de Java sur Ubuntu

| Tags |
|------|
| `Java` `Ubuntu` `OpenJDK` `Oracle JDK` `Installation` |

Installer Java sur Ubuntu est une tâche simple, que ce soit via les dépôts officiels pour OpenJDK ou directement depuis le site d'Oracle pour Oracle JDK. Choisissez la version appropriée en fonction de vos besoins de développement ou de production.


## Résolution de l'erreur Java UnsupportedClassVersionError

| Tags |
|------|
| `Java` `Ubuntu` `UnsupportedClassVersionError` `JVM` `JDK` |

L'erreur `java.lang.UnsupportedClassVersionError` se produit lorsque la version de la machine virtuelle Java (JVM) utilisée pour exécuter une application est antérieure à la version de la compilation de l'application. Dans ce cas, l'application `org/sonar/application/App` a été compilée avec la version 61.0 des fichiers de classe (Java 17), tandis que la JVM en cours d'utilisation ne prend en charge que jusqu'à la version 55.0 (Java 11).

Pour résoudre ce problème sous Ubuntu, suivez les étapes suivantes :

**1. Identifier la version actuelle de Java**

Vérifiez la version de Java installée sur votre système :

```bash
java -version
```

Le résultat affichera des informations sur la version de Java installée. Par exemple :

```
java version "1.8.0_312"
Java(TM) SE Runtime Environment (build 1.8.0_312-b07)
Java HotSpot(TM) 64-Bit Server VM (build 25.312-b07, mixed mode)
```

**2. Installer une version de Java compatible (JDK 17 ou plus récente)**

Si votre version de Java est trop ancienne, installez une version plus récente (JDK 17 ou ultérieure).  Plusieurs options sont possibles :

*   **Utiliser `apt` (recommandé):**

    Mettez à jour la liste des paquets et installez une version récente de Java :

    ```bash
    sudo apt update
    sudo apt install openjdk-17-jdk
    ```

    Si vous avez besoin d'une autre version, remplacez `openjdk-17-jdk` par `openjdk-21-jdk` par exemple.

*   **Installer manuellement:**

    Téléchargez le JDK depuis le site officiel d'Oracle ou d'OpenJDK.  Installez-le et configurez les variables d'environnement `JAVA_HOME` et `PATH`.

**3.  Configurer la version Java par défaut (si plusieurs sont installées)**

Si vous avez plusieurs versions de Java installées, configurez la version par défaut à utiliser :

```bash
sudo update-alternatives --config java
```

Sélectionnez le numéro correspondant à la version JDK 17 (ou plus récente) que vous avez installée.  Faites de même pour `javac` si nécessaire :

```bash
sudo update-alternatives --config javac
```

**4. Vérifier la nouvelle version de Java**

Après avoir installé et configuré la nouvelle version de Java, vérifiez à nouveau la version pour confirmer que la mise à jour a réussi :

```bash
java -version
```

L'erreur `UnsupportedClassVersionError` devrait être résolue si la JVM utilisée correspond à la version du JDK avec laquelle l'application a été compilée ou est plus récente.

**Exemple de résolution du problème pour [NOM] :**

[NOM] a rencontré cette erreur lors de l'exécution de SonarQube sur Ubuntu. En suivant ces étapes, [NOM] a installé et configuré OpenJDK 17, résolvant ainsi l'erreur et permettant le bon fonctionnement de SonarQube.  [EMAIL] peut être contacté pour plus d'informations. L'adresse IP était [IP].


## Résoudre l'erreur java.lang.UnsupportedClassVersionError

| Tags |
|------|
| `Java` `SonarQube` `UnsupportedClassVersionError` `Ubuntu` |

L'erreur <code>java.lang.UnsupportedClassVersionError</code> signale que l'application SonarQube a été compilée avec une version de Java plus récente que celle disponible sur le système. Dans ce cas, le fichier de classe a été compilé pour Java 17 (version 61.0), alors que la version installée est Java 11 (version 55.0). La solution consiste à installer Java 17 et à configurer le système pour l'utiliser.


## Installation de Java 17

| Tags |
|------|
| `Java` `Java 17` `Ubuntu` `Installation` |

Java 17, une version LTS (Long Term Support), est recommandée pour la stabilité et le support à long terme. Procédez comme suit pour installer Java 17 depuis le dépôt officiel d'Ubuntu :

1.  **Ajouter le PPA pour les versions récentes de Java** (si pas déjà fait) :

    ```bash
    sudo add-apt-repository ppa:linuxuprising/java
    sudo apt update
    ```

2.  **Installer Java 17** :

    ```bash
    sudo apt install oracle-java17-installer oracle-java17-set-default
    ```

    Cette commande installe Java 17 et configure le système pour utiliser Java 17 par défaut.


## Vérification de la version Java

| Tags |
|------|
| `Java` `Installation` `Version` |

Après l'installation, vérifiez la version de Java :

```bash
java -version
```

La sortie attendue doit indiquer Java 17.


## Redémarrage de SonarQube

| Tags |
|------|
| `SonarQube` `Java 17` `Démarrage` `Linux` |

Une fois Java 17 installé, redémarrez SonarQube :

```bash
# Naviguez au dossier où SonarQube est installé
cd /chemin/vers/sonarqube

# Utilisez les scripts fournis pour démarrer SonarQube
./bin/linux-x86-64/sonar.sh start
```


## Vérification de l'état de SonarQube

| Tags |
|------|
| `SonarQube` `démarrage` `vérification` |

Après le démarrage de SonarQube, accédez à son interface web pour confirmer son bon fonctionnement. L'interface est accessible par défaut à l'adresse <code>http://localhost:9000</code>.


## Configuration Java 17

| Tags |
|------|
| `Java` `Environnement` `Compatibilité` `SonarQube` |

<ul>
<li>
<p><strong>Variables d'environnement</strong> : Définissez correctement les variables d'environnement Java, notamment <code>JAVA_HOME</code>, pour cibler Java 17.</p>
<pre><code class="language-bash">export JAVA_HOME=/usr/lib/jvm/java-17-oracle
export PATH=$JAVA_HOME/bin:$PATH
</code></pre>
<p>Ajoutez ces lignes à <code>~/.bashrc</code> ou <code>~/.profile</code> pour une configuration persistante.</p>
</li>
<li>
<p><strong>Compatibilité</strong> : Assurez-vous de la compatibilité de l'application avec la version Java utilisée. Certaines applications requièrent des versions spécifiques.</p>
</li>
</ul>
<p>Ces étapes permettent de résoudre l'erreur <code>UnsupportedClassVersionError</code> en utilisant une version Java compatible avec les fichiers classe de SonarQube.</p>


## Diagnostic d'Elasticsearch arrêté pour SonarQube

| Tags |
|------|
| `Elasticsearch` `SonarQube` `Démarrage` `Erreur` `Diagnostic` |

Le message d'erreur "Process[ElasticSearch] is stopped" signale un arrêt du processus Elasticsearch, crucial pour le fonctionnement de SonarQube. Ce problème peut résulter de diverses causes, allant des configurations erronées aux limitations de ressources. Voici des étapes pour diagnostiquer et résoudre ce problème.


## Vérification des logs ElasticSearch

| Tags |
|------|
| `Elasticsearch` `Logs` `SonarQube` |

La première étape pour diagnostiquer le problème consiste à consulter les logs d'ElasticSearch. Ces logs se trouvent généralement dans le dossier <code>logs</code> de votre installation SonarQube :

```
/chemin/vers/sonarqube/logs/es.log
```

Ouvrez ce fichier et recherchez les messages d'erreur. Ces informations peuvent indiquer pourquoi ElasticSearch ne démarre pas, notamment les problèmes de mémoire, les erreurs de configuration ou les problèmes de permissions.


## Vérification de la Configuration d'Elasticsearch

| Tags |
|------|
| `Elasticsearch` `Configuration` `Paramètres système` |

Elasticsearch requiert une configuration spécifique pour fonctionner correctement, notamment en ce qui concerne la mémoire et certains paramètres du noyau. Les points suivants doivent être vérifiés :

*   **Mémoire allouée** : La quantité de mémoire allouée à Elasticsearch doit être suffisante.

*   **Paramètre `vm.max_map_count`** : Ce paramètre du noyau doit être au moins égal à 262144. Pour vérifier la valeur actuelle, exécutez la commande suivante :

    ```bash
    sysctl vm.max_map_count
    ```

    Pour modifier ce paramètre, utilisez la commande suivante (nécessite des privilèges d'administrateur) :

    ```bash
    sudo sysctl -w vm.max_map_count=262144
    ```

    Pour rendre la modification permanente, ajoutez la ligne `vm.max_map_count=262144` au fichier `/etc/sysctl.conf`.


## Vérification des Ressources Système

| Tags |
|------|
| `Elasticsearch` `Ressources` `Performance` |

Elasticsearch peut échouer au démarrage en raison de ressources système insuffisantes. Il est essentiel de vérifier les éléments suivants :

*   **Mémoire disponible** : s'assurer que le système dispose de suffisamment de mémoire RAM libre pour le fonctionnement d'Elasticsearch.
*   **Espace disque** : vérifier que l'espace disque disponible est suffisant pour éviter tout problème de fonctionnement.


## Redémarrage d'Elasticsearch

| Tags |
|------|
| `Elasticsearch` `SonarQube` `redémarrage` `bash` |

Une fois les configurations vérifiées et ajustées, redémarrez Elasticsearch. La procédure implique généralement le redémarrage de SonarQube :

```bash
/chemin/vers/sonarqube/bin/linux-x86-64/sonar.sh stop
/chemin/vers/sonarqube/bin/linux-x86-64/sonar.sh start
```


## Dépannage SonarQube : Documentation

| Tags |
|------|
| `SonarQube` `Elasticsearch` `Documentation` `Dépannage` |

Si les problèmes persistent, consultez la documentation officielle de SonarQube pour des instructions détaillées et des configurations spécifiques à votre version de SonarQube et d'Elasticsearch.

En suivant ces étapes, vous devriez être en mesure d'identifier et de corriger les problèmes empêchant Elasticsearch de démarrer dans votre installation SonarQube.


## Pourquoi l'erreur "java.lang.RuntimeException" ?

| Tags |
|------|
| `Java` `Elasticsearch` `Sécurité` `Linux` |

L'erreur <code>java.lang.RuntimeException: can not run Elasticsearch as root</code> survient lors de l'exécution d'Elasticsearch sous l'utilisateur root sur un système Linux. Cette restriction est implémentée pour des raisons de sécurité, car l'exécution d'Elasticsearch avec les privilèges root peut engendrer des vulnérabilités importantes.

Pour corriger cette erreur, il faut configurer Elasticsearch pour qu'il s'exécute avec un utilisateur non privilégié.


## Création d'un utilisateur non privilégié

| Tags |
|------|
| `Elasticsearch` `Sécurité` `Utilisateur` `Linux` |

<ol>
<li>
<p><strong>Créer un nouvel utilisateur</strong> dédié à Elasticsearch. Exemple :</p>
<pre><code class="language-bash">sudo adduser --disabled-login --gecos "" elasticsearch
</code></pre>
<p>Cette commande crée un utilisateur sans droits d'ouverture de session.</p>
</li>
<li>
<p><strong>Attribuer la propriété des dossiers Elasticsearch</strong> au nouvel utilisateur :</p>
<pre><code class="language-bash">sudo chown -R elasticsearch:elasticsearch /chemin/vers/sonarqube/elasticsearch
</code></pre>
<p>Remplacer <code>/chemin/vers/sonarqube/elasticsearch</code> par le chemin d'installation réel d'Elasticsearch.</p>
</li>
</ol>


## Modification des Scripts de Démarrage d'Elasticsearch

| Tags |
|------|
| `Elasticsearch` `Démarrage` `Scripts` `Linux` |

Pour garantir l'exécution d'Elasticsearch avec l'utilisateur approprié, les scripts de démarrage doivent être modifiés.

1.  **Ouvrez le script de démarrage d'Elasticsearch :**

    ```bash
    sudo nano /chemin/vers/sonarqube/elasticsearch/bin/elasticsearch
    ```

2.  **Ajoutez la commande de changement d'utilisateur :** Insérez cette commande au début du script, avant le démarrage d'Elasticsearch :

    ```bash
    su - elasticsearch -c "/chemin/vers/sonarqube/elasticsearch/bin/elasticsearch"
    ```

    Vérifiez que le chemin vers le script `elasticsearch` est correct.


## Redémarrage de SonarQube et Elasticsearch

| Tags |
|------|
| `SonarQube` `Elasticsearch` `redémarrage` `configuration` |

Après les modifications, redémarrez SonarQube et Elasticsearch :

```bash
sudo -u elasticsearch /chemin/vers/sonarqube/elasticsearch/bin/elasticsearch
```


## Vérification du Démarrage d'Elasticsearch

| Tags |
|------|
| `Elasticsearch` `Démarrage` `Logs` `curl` |

Après le redémarrage, confirmez le bon fonctionnement :

1.  **Vérifiez les logs d'Elasticsearch** afin de détecter toute erreur de démarrage.
2.  **Vérifiez le statut d'Elasticsearch** : utilisez <code>curl</code> pour vérifier la réponse du service :

    ```bash
    curl -X GET "localhost:9200/"
    ```

    Cette commande doit retourner les informations de base du cluster Elasticsearch, confirmant son bon fonctionnement.


## Résolution de l'erreur "Unable to create shared memory"

| Tags |
|------|
| `shared memory` `erreur` `ressources système` `permissions` |

L'erreur "Unable to create shared memory" se produit généralement lorsqu'une application ne peut pas allouer un segment de mémoire partagée. Les causes possibles incluent des ressources système insuffisantes, des problèmes de permissions ou des erreurs de configuration. Ce guide explique comment résoudre ce problème, notamment pour les applications utilisant la mémoire partagée, comme les bases de données ou les serveurs web (par exemple, PostgreSQL, Apache).


## Vérification des ressources système

| Tags |
|------|
| `système` `ressources` `mémoire` `disque` |

<ol>
<li>
<p><strong>Vérification de la mémoire disponible :</strong></p>
<ul>
<li>Utiliser la commande <code>free -m</code> pour vérifier la mémoire disponible. Si la mémoire disponible est faible, envisager de fermer d'autres programmes ou d'ajouter de la RAM.</li>
</ul>
</li>
<li>
<p><strong>Vérification de l'espace disque :</strong></p>
<ul>
<li>Utiliser <code>df -h</code> pour s'assurer qu'il y a suffisamment d'espace disque. Certaines applications utilisent l'espace disque pour la pagination ou le stockage temporaire.</li>
</ul>
</li>
</ol>


## Dépannage des problèmes de permissions

| Tags |
|------|
| `permissions` `Linux` `sécurité` |

<ol>
<li>
<p><strong>Permissions utilisateur :</strong></p>
<ul>
<li>S'assurer que l'utilisateur exécutant l'application dispose des permissions nécessaires pour créer et gérer la mémoire partagée. Cela peut impliquer des permissions pour accéder à certains répertoires ou exécuter des commandes.</li>
</ul>
</li>
<li>
<p><strong>Politiques de sécurité :</strong></p>
<ul>
<li>Sous Linux, vérifier si SELinux ou AppArmor est activé et pourrait empêcher l'application de créer de la mémoire partagée. Il peut être nécessaire de configurer ces modules de sécurité pour autoriser les opérations nécessaires.</li>
</ul>
</li>
</ol>


## Paramètres de configuration

| Tags |
|------|
| `Linux` `shmmax` `shmall` `mémoire partagée` `sysctl` |

<ol>
<li>
<p><strong>Limites du système :</strong></p>
<ul>
<li>
Les paramètres <code>shmmax</code> et <code>shmall</code> sous Linux contrôlent la taille maximale de la mémoire partagée. Il peut être nécessaire d'augmenter ces valeurs :
<ul>
<li>
Vérifiez les valeurs actuelles avec :
<pre><code class="language-bash">sysctl -a | grep shm
</code></pre>
</li>
<li>
Pour les modifier temporairement :
<pre><code class="language-bash">sudo sysctl -w kernel.shmmax=2147483648  # Définir à une valeur raisonnable pour vos besoins
sudo sysctl -w kernel.shmall=524288      # Ajuster également si nécessaire
</code></pre>
</li>
<li>
Pour rendre ces modifications permanentes, ajoutez-les à <code>/etc/sysctl.conf</code> :
<pre><code class="language-plaintext">kernel.shmmax=2147483648
kernel.shmall=524288
</code></pre>
</li>
<li>Rechargez les configurations avec <code>sudo sysctl -p</code>.</li>
</ul>
</li>
</ul>
</li>
<li>
<p><strong>Paramètres de mémoire partagée spécifiques aux applications :</strong></p>
<ul>
<li>Certaines applications vous permettent de configurer l'utilisation de la mémoire partagée dans leurs propres fichiers de configuration (par exemple, <code>postgresql.conf</code> de PostgreSQL pour les tampons partagés).</li>
</ul>
</li>
</ol>


## Dépannage et journaux

| Tags |
|------|
| `journaux` `dépannage` `système` |

<ol>
<li>
<p><strong>Vérification des journaux d'application :</strong></p>
<ul>
<li>Consultez les journaux d'application pour obtenir des messages d'erreur plus spécifiques qui pourraient donner des indications sur ce qui ne va pas.</li>
</ul>
</li>
<li>
<p><strong>Journaux système :</strong></p>
<ul>
<li>Vérifiez les journaux système (<code>/var/log/syslog</code> ou <code>journalctl</code> pour les systèmes systemd) pour tout message pertinent concernant la mémoire partagée ou les limites de ressources.</li>
</ul>
</li>
</ol>


## Guides Spécifiques aux Logiciels

| Tags |
|------|
| `documentation` `logiciel` `mémoire partagée` |

Si vous rencontrez ce problème avec un logiciel spécifique (par exemple, une base de données ou un serveur web), consultez la documentation officielle ou les forums de la communauté pour obtenir des conseils sur les problèmes de mémoire partagée propres à ce logiciel.


## PostgreSQL Shared Memory Issue Resolution

| Tags |
|------|
| `PostgreSQL` `shared memory` `configuration` `Linux` |

If you're running PostgreSQL and encounter shared memory issues, adjust your PostgreSQL configuration:

1.  **Edit the PostgreSQL Configuration File (<code>postgresql.conf</code>):**

    *   Adjust the <code>shared_buffers</code> setting if necessary.

2.  **Reconfigure Linux Shared Memory Limits:**

    *   Follow the steps to adjust <code>shmmax</code> and <code>shmall</code>.

3.  **Restart PostgreSQL:**

    *   Restart the PostgreSQL service after making changes:

    ```bash
    sudo systemctl restart postgresql
    ```

By following these steps, you should be able to diagnose and fix "Unable to create shared memory" errors, ensuring that your applications have sufficient resources and permissions to function correctly.


## Cause d'erreur : FileNotFoundException

| Tags |
|------|
| `Java` `SonarQube` `Permissions` `FileNotFoundException` |

L'erreur <code>java.io.FileNotFoundException: /opt/sonarqube/temp/sharedmemory (Permission non accordée)</code> signifie que le processus exécutant SonarQube n'a pas les permissions requises pour accéder ou créer un fichier dans le répertoire spécifié. Cela peut être dû à des permissions de fichier restrictives, à des problèmes de propriété ou à des politiques de sécurité restreignant l'accès. Voici comment résoudre ce problème :


## Vérification des droits et permissions d'accès

| Tags |
|------|
| `SonarQube` `permissions` `chown` `chmod` `Linux` |

<ol>
<li>
<p><strong>Vérification de la propriété :</strong></p>
<ul>
<li>
S'assurer que le répertoire <code>/opt/sonarqube</code> et ses sous-répertoires appartiennent à l'utilisateur sous lequel SonarQube s'exécute. Si SonarQube s'exécute sous un utilisateur spécifique (par exemple, <code>sonar</code>), modifier la propriété avec :<pre><code class="language-bash">sudo chown -R sonar:sonar /opt/sonarqube
</code></pre>
</li>
<li>Remplacer <code>sonar:sonar</code> par le nom d'utilisateur et de groupe appropriés sous lesquels SonarQube fonctionne.</li>
</ul>
</li>
<li>
<p><strong>Vérification et définition des permissions :</strong></p>
<ul>
<li>
S'assurer que l'utilisateur dispose des permissions en lecture et en écriture sur le répertoire <code>/opt/sonarqube/temp</code>. Définir ces permissions avec :<pre><code class="language-bash">sudo chmod -R 775 /opt/sonarqube/temp
</code></pre>
</li>
<li>Cette commande accorde à l'utilisateur propriétaire et au groupe des permissions complètes (lecture, écriture, exécution) et aux autres utilisateurs des permissions de lecture et d'exécution.</li>
</ul>
</li>
</ol>


## Vérification des permissions effectives

| Tags |
|------|
| `Permissions` `Linux` `namei` `Sécurité` |

*   Utiliser la commande <code>namei</code> pour lister les permissions pour chaque répertoire menant au fichier :

```bash
namei -l /opt/sonarqube/temp/sharedmemory
```

*   Cette commande permet d'identifier les répertoires du chemin qui pourraient ne pas avoir les permissions correctes.


## Vérification des contextes de sécurité

| Tags |
|------|
| `SELinux` `Sécurité` `Linux` |

Si vous utilisez SELinux ou des outils de sécurité similaires, ils peuvent bloquer l'accès au répertoire :

1.  **Vérification de l'état de SELinux :**

    *   Exécutez `sestatus` pour vérifier si SELinux est activé et en mode d'application.
    *   Si c'est le cas, vérifiez s'il y a des refus qui pourraient être liés à SonarQube :

    ```bash
    sudo ausearch -m avc -ts recent
    ```

2.  **Ajustement des politiques SELinux :**

    *   Si SELinux est à l'origine du refus d'accès, vous pouvez soit définir le contexte correct pour le répertoire, soit temporairement définir SELinux en mode permissif pour tester si cela résout le problème :

    ```bash
    sudo setenforce 0  # Définit SELinux en mode permissif
    ```

    *   Pour modifier le contexte du répertoire de manière permanente, utilisez :

    ```bash
    sudo semanage fcontext -a -t httpd_sys_rw_content_t '/opt/sonarqube/temp(/.*)?'
    sudo restorecon -Rv /opt/sonarqube/temp
    ```

    *   Remplacez `httpd_sys_rw_content_t` par le type de contexte approprié requis par votre application.


## Redémarrer SonarQube

| Tags |
|------|
| `SonarQube` `restart` `systemd` `administration` |

Après avoir effectué ces modifications, redémarrez SonarQube pour les appliquer :

```bash
sudo systemctl restart sonarqube
```

Ou utilisez la commande appropriée si vous n’utilisez pas systemd.


## Étape 5 : Vérification de la résolution

| Tags |
|------|
| `SonarQube` `permissions` `logs` `configuration` |

Après le redémarrage, vérifiez que le problème est résolu en consultant les journaux ou en essayant d'accéder à l'application. Si le problème persiste, vérifiez à nouveau les configurations et assurez-vous qu'il n'y a pas de fautes de frappe ou de paramètres oubliés.

En suivant ces étapes, vous devriez être en mesure de résoudre les problèmes d'autorisation empêchant SonarQube d'accéder au répertoire nécessaire sur votre serveur.


## Accès Initial à SonarQube

| Tags |
|------|
| `SonarQube` `Installation` `Sécurité` |

Pour accéder à l'interface web SonarQube après une nouvelle installation, les identifiants par défaut sont :

*   **Username :** `admin`
*   **Password :** `admin`

Après la connexion, SonarQube invitera l'utilisateur à modifier le mot de passe pour des raisons de sécurité. Il est vivement conseillé de choisir un mot de passe fort et unique pour sécuriser l'instance.

Si ces identifiants ne fonctionnent pas, contacter l'administrateur qui a configuré SonarQube ou réinitialiser le mot de passe via la base de données ou les fichiers de configuration, en suivant les recommandations de SonarQube, si l'accès au serveur et à la base de données est disponible.


## Ajout d'un projet local à SonarQube

| Tags |
|------|
| `SonarQube` `Analyse de code` `SonarScanner` |

Pour ajouter un projet local à SonarQube et analyser votre code, plusieurs étapes sont nécessaires. Cela inclut la configuration du projet dans SonarQube et l'utilisation du SonarScanner pour analyser le projet et transmettre les résultats au serveur SonarQube. Procédez comme suit :


## Configuration initiale du projet SonarQube

| Tags |
|------|
| `SonarQube` `configuration` `projet` `token` |

<ol>
<li>
<p><strong>Se connecter à SonarQube.</strong></p>
<ul>
<li>Accéder à l'instance SonarQube via l'URL (ex: <code>http://localhost:9000</code>) et s'authentifier avec les identifiants utilisateur.</li>
</ul>
</li>
<li>
<p><strong>Créer un nouveau projet :</strong></p>
<ul>
<li>Dans le tableau de bord SonarQube, cliquer sur <strong>Create new project</strong>.</li>
<li>Définir une <strong>Project key</strong> et un <strong>Display name</strong>.</li>
<li>Cliquer sur <strong>Set Up</strong>.</li>
</ul>
</li>
<li>
<p><strong>Générer un token d'authentification :</strong></p>
<ul>
<li>Lors de la configuration du projet, générer un token d'authentification pour l'authentification de SonarScanner.</li>
<li>Nommer le token et cliquer sur <strong>Generate</strong>.</li>
<li>Conserver le token en lieu sûr, celui-ci ne sera plus accessible après la fermeture de la fenêtre.</li>
</ul>
</li>
</ol>


## Installation de SonarScanner

| Tags |
|------|
| `SonarScanner` `SonarQube` `Analyse statique` |

SonarScanner est utilisé pour analyser le code source et envoyer les résultats à SonarQube.

1.  **Télécharger SonarScanner :**

    *   Téléchargez la version appropriée de SonarScanner pour votre système d'exploitation à partir de la [page de téléchargement de SonarScanner](https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/).
2.  **Décompresser SonarScanner :**

    *   Décompressez le fichier téléchargé dans le répertoire souhaité.
3.  **Configurer le chemin (facultatif) :**

    *   Ajoutez le chemin du répertoire `bin` de SonarScanner à votre variable d'environnement `PATH`. Cela permet d'exécuter SonarScanner depuis n'importe quel répertoire.


## Configuration de SonarScanner

| Tags |
|------|
| `SonarScanner` `SonarQube` `configuration` `propriétés` |

<ol>
<li>
<strong>Modification du fichier de configuration SonarScanner :</strong>
<ul>
<li>Ouvrez le fichier <code>conf/sonar-scanner.properties</code> dans le répertoire d'installation de SonarScanner.</li>
<li>
Configurez <code>sonar.host.url</code> pour cibler votre serveur SonarQube :
<pre><code class="language-properties">sonar.host.url=http://localhost:9000
</code></pre>
</li>
<li>
Optionnellement, configurez votre jeton d'authentification :
<pre><code class="language-properties">sonar.login=your_generated_token
</code></pre>
</li>
</ul>
</li>
</ol>


## Exécution de SonarScanner

| Tags |
|------|
| `SonarScanner` `analyse statique` `SonarQube` `ligne de commande` |

<ol>
<li>
<p><strong>Ouvrez un terminal ou une invite de commande.</strong></p>
</li>
<li>
<p><strong>Naviguez vers le répertoire de votre projet source.</strong></p>
</li>
<li>
<p><strong>Exécutez SonarScanner :</strong></p>
<pre><code class="language-bash">sonar-scanner \
-Dsonar.projectKey=your_project_key \
-Dsonar.sources=. \
-Dsonar.host.url=http://localhost:9000 \
-Dsonar.login=your_generated_token
</code></pre>
<p>Remplacez <code>your_project_key</code>, <code>http://localhost:9000</code>, et <code>your_generated_token</code> par vos informations.</p>
</li>
</ol>


## Vérification des résultats de l'analyse SonarQube

| Tags |
|------|
| `SonarQube` `analyse de code` `interface utilisateur` |

*   Retournez à votre interface utilisateur SonarQube.
*   Naviguez vers la page de votre projet pour visualiser l'analyse de votre code.

En suivant ces étapes, vous pourrez configurer, analyser et visualiser les résultats de l'analyse de votre projet local dans SonarQube.


## Intégration de SonarScanner à une instance locale

| Tags |
|------|
| `SonarQube` `SonarScanner` `Analyse de code` |

Pour intégrer SonarScanner à votre instance locale de SonarQube et analyser votre code source, suivez ces étapes :


## Installation de SonarScanner

| Tags |
|------|
| `SonarScanner` `SonarQube` `Installation` `Environnement` |

<ol>
<li>
<p><strong>Téléchargement de SonarScanner</strong> :</p>
<ul>
<li>Téléchargez SonarScanner depuis la <a href="https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/">page de téléchargement</a>. Sélectionnez la version appropriée à votre système d'exploitation.</li>
</ul>
</li>
<li>
<p><strong>Extraction de SonarScanner</strong> :</p>
<ul>
<li>Extrayez le fichier téléchargé dans un répertoire de votre choix.</li>
</ul>
</li>
<li>
<p><strong>Ajout de SonarScanner au PATH</strong> (recommandé) :</p>
<ul>
<li>Pour un accès facile depuis le terminal, ajoutez le répertoire <code>bin</code> de SonarScanner à la variable d'environnement <code>PATH</code>.</li>
<li>
Sur Linux ou macOS :
<pre><code class="language-bash">export PATH=$PATH:/chemin/vers/sonar-scanner/bin
</code></pre>
</li>
<li>Sur Windows, ajoutez le chemin via les paramètres système (Paramètres &gt; Système &gt; Informations système &gt; Paramètres système avancés &gt; Variables d'environnement).</li>
</ul>
</li>
</ol>


## Configuration de SonarScanner

| Tags |
|------|
| `SonarScanner` `SonarQube` `properties` `configuration` |

<ol>
<li>
<strong>Configuration du fichier <code>sonar-scanner.properties</code></strong> (facultatif) :
<ul>
<li>Naviguez dans le répertoire de SonarScanner, puis dans le sous-dossier <code>conf</code> et ouvrez le fichier <code>sonar-scanner.properties</code>.</li>
<li>
Configurez les propriétés de base :
<pre><code class="language-properties">sonar.host.url=http://localhost:9000
sonar.login=le_token_d_authentification
</code></pre>
</li>
<li><code>sonar.host.url</code> doit pointer vers votre instance locale de SonarQube.</li>
<li><code>sonar.login</code> est le token d'authentification généré dans SonarQube.</li>
</ul>
</li>
</ol>


## Génération d'un Token d'Authentification SonarQube

| Tags |
|------|
| `SonarQube` `token` `authentification` |

<ol>
<li>
<p><strong>Connectez-vous à SonarQube</strong> :</p>
<ul>
<li>Accédez à l'instance SonarQube via l'URL (par exemple, <code>http://localhost:9000</code>) et authentifiez-vous avec vos identifiants. Les identifiants par défaut sont <code>admin/admin</code>.</li>
</ul>
</li>
<li>
<p><strong>Générez un token</strong> :</p>
<ul>
<li>Accédez à votre profil en sélectionnant « My Account » après avoir cliqué sur votre nom d'utilisateur.</li>
<li>Naviguez vers l'onglet « Security ». Dans la section « Tokens », attribuez un nom à votre token et cliquez sur « Generate ».</li>
<li>Copiez et conservez en lieu sûr le token généré.</li>
</ul>
</li>
</ol>


## Exécution de l'analyse avec SonarScanner

| Tags |
|------|
| `SonarScanner` `analyse statique` `SonarQube` `intégration continue` |

<ol>
<li><strong>Naviguez vers le répertoire source de votre projet.</strong></li>
<li>
<strong>Exécutez SonarScanner :</strong>
<ul>
<li>
Ouvrez un terminal et exécutez la commande suivante :
<pre><code class="language-bash">sonar-scanner \
  -Dsonar.projectKey=nom_du_projet \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=le_token_d_authentification
</code></pre>
</li>
<li>Remplacez <code>nom_du_projet</code> par un identifiant unique pour votre projet et <code>le_token_d_authentification</code> par le token d'authentification généré.</li>
</ul>
</li>
</ol>


## Vérification des Résultats de l'Analyse

| Tags |
|------|
| `SonarQube` `SonarScanner` `analyse de code` |

Après l'exécution de SonarScanner, accédez à votre instance SonarQube pour consulter les résultats de l'analyse.

Consultez le tableau de bord du projet pour une analyse détaillée.

Ces étapes permettent d'intégrer SonarScanner à votre instance SonarQube locale, pour une analyse automatisée et régulière de la qualité du code.


## Installation et configuration de SonarScanner sur Ubuntu

| Tags |
|------|
| `SonarScanner` `SonarQube` `Ubuntu` `Analyse de code` |

Pour installer et configurer SonarScanner sur Ubuntu et l'intégrer avec une instance locale de SonarQube, suivez les instructions détaillées ci-dessous. Ces instructions vous guideront à travers le processus de téléchargement, d'installation, et de configuration de SonarScanner pour qu'il puisse communiquer avec SonarQube.


## Installation de SonarScanner

| Tags |
|------|
| `SonarScanner` `Linux` `Installation` `SonarQube` `Bash` |

<ol>
<li>
<p><strong>Télécharger SonarScanner</strong> pour Linux à partir du <a href="https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/">site officiel de SonarQube</a> :</p>
<pre><code class="language-bash">cd /tmp
wget https://binaries.sonarsource.com/Distribution/sonar-scanner-cli/sonar-scanner-cli-4.6.2.2472-linux.zip
</code></pre>
</li>
<li>
<p><strong>Décompresser le fichier téléchargé</strong> :</p>
<pre><code class="language-bash">sudo apt install unzip
unzip sonar-scanner-cli-4.6.2.2472-linux.zip -d /opt
</code></pre>
</li>
<li>
<p><strong>Renommer le dossier pour simplifier son utilisation</strong> :</p>
<pre><code class="language-bash">sudo mv /opt/sonar-scanner-4.6.2.2472-linux /opt/sonar-scanner
</code></pre>
</li>
<li>
<p><strong>Ajouter SonarScanner au PATH du système</strong> :</p>
<ul>
<li>
Ouvrir le fichier <code>.bashrc</code> ou <code>.profile</code> dans le répertoire personnel pour ajouter le chemin du scanner à la variable d'environnement PATH :
<pre><code class="language-bash">nano ~/.bashrc
</code></pre>
</li>
<li>
Ajouter la ligne suivante à la fin du fichier :
<pre><code class="language-bash">export PATH=&quot;$PATH:/opt/sonar-scanner/bin&quot;
</code></pre>
</li>
<li>
Sourcer le fichier pour appliquer les modifications :
<pre><code class="language-bash">source ~/.bashrc
</code></pre>
</li>
</ul>
</li>
</ol>


## Configuration de SonarScanner

| Tags |
|------|
| `SonarScanner` `SonarQube` `configuration` `properties` |

<ol>
<li>
<strong>Configuration du fichier <code>sonar-scanner.properties</code></strong> (facultatif) :
<ul>
<li>
Édition du fichier de configuration :
<pre><code class="language-bash">nano /opt/sonar-scanner/conf/sonar-scanner.properties
</code></pre>
</li>
<li>
Configuration de l'URL de l'instance SonarQube et du token d'authentification (si nécessaire) :
<pre><code class="language-properties">sonar.host.url=http://localhost:9000
sonar.login=your_generated_token
</code></pre>
</li>
</ul>
</li>
</ol>


## Génération d'un Token d'Authentification

| Tags |
|------|
| `SonarQube` `token` `authentification` |

<ol>
<li>
<p><strong>Connectez-vous à l'instance SonarQube</strong> :</p>
<ul>
<li>Naviguez vers <code>http://localhost:9000</code> et authentifiez-vous.</li>
</ul>
</li>
<li>
<p><strong>Générez un token</strong> :</p>
<ul>
<li>Accédez à votre profil utilisateur, puis à la section « Security ».</li>
<li>Nommez votre token et cliquez sur « Generate ». Copiez et conservez ce token de manière sécurisée.</li>
</ul>
</li>
</ol>


## Analyser un Projet avec SonarScanner

| Tags |
|------|
| `SonarScanner` `SonarQube` `Analyse statique` `Bash` |

<ol>
<li>
<p>Ouvrez un terminal dans le répertoire source de votre projet.</p>
</li>
<li>
<p>Exécutez SonarScanner avec les paramètres suivants :</p>
<pre><code class="language-bash">sonar-scanner \
  -Dsonar.projectKey=nom_du_projet \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=your_generated_token
</code></pre>
</li>
</ol>
<p>Ces étapes permettent d'installer, de configurer et d'utiliser SonarScanner sur Ubuntu pour analyser vos projets avec une instance locale de SonarQube.</p>


## Résolution de l'erreur SonarScanner Java

| Tags |
|------|
| `SonarScanner` `Java` `UnsupportedClassVersionError` `Java Runtime` |

L'erreur "java.lang.UnsupportedClassVersionError: org/sonar/batch/bootstrapper/EnvironmentInformation has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 55.0" indique une incompatibilité de version Java lors de l'exécution de SonarScanner.  SonarScanner a été compilé avec une version de Java plus récente que celle utilisée pour l'exécuter.

Pour résoudre ce problème, suivez ces étapes :

1.  **Vérifiez la version de Java utilisée par SonarScanner.**  Vous pouvez généralement le faire en exécutant `sonar-scanner -v` ou en consultant la documentation SonarScanner.

2.  **Identifiez la version de Java requise par SonarScanner.** La documentation de SonarScanner ou les messages d'erreur indiqueront la version minimale de Java requise.

3.  **Mettez à jour la version de Java.**  Assurez-vous que la version de Java utilisée pour exécuter SonarScanner correspond à la version requise. Si vous avez plusieurs versions de Java installées, configurez l'environnement pour utiliser la version correcte.

    *   **Configuration de la variable d'environnement JAVA_HOME :**
        Définissez la variable d'environnement `JAVA_HOME` pour pointer vers le répertoire d'installation de la version de Java correcte.  Par exemple:

        ```bash
        export JAVA_HOME=/usr/lib/jvm/jdk17
        export PATH=$JAVA_HOME/bin:$PATH
        ```

        Remplacez `/usr/lib/jvm/jdk17` par le chemin d'accès correct à votre installation Java.

    *   **Modification des paramètres de SonarScanner :**
        Dans certains cas, vous devrez peut-être modifier les paramètres de SonarScanner pour spécifier explicitement le chemin d'accès à l'exécutable Java. Consultez la documentation de SonarScanner pour des instructions spécifiques.

4.  **Vérifiez la configuration de l'environnement.**  Après avoir modifié la version de Java, vérifiez que SonarScanner utilise la nouvelle version en exécutant à nouveau `sonar-scanner -v` ou en consultant les logs d'exécution.

5.  **Exemple de modification du fichier de configuration SonarScanner.properties:**

    Si la variable `JAVA_HOME` n'est pas prise en compte, vous pouvez forcer l'utilisation de la bonne version en modifiant le fichier `sonar-scanner.properties`.

    ```properties
    # Force l'utilisation d'une version spécifique de Java
    # sonar.java.source=17  # Décommentez et définissez la version source si nécessaire
    # sonar.java.target=17  # Décommentez et définissez la version cible si nécessaire
    ```

6.  **Redémarrez l'environnement (si nécessaire).**  Après avoir modifié les variables d'environnement, il est parfois nécessaire de redémarrer votre terminal ou votre environnement de développement pour que les changements soient pris en compte.

**Exemple de résolution avec une version de Java non-supportée:**

Si l'erreur persiste, cela peut être dû à une version de Java trop ancienne pour SonarScanner.

```
SonarScanner 4.x
java.lang.UnsupportedClassVersionError: org/sonar/batch/bootstrapper/EnvironmentInformation has been compiled by a more recent version of the Java Runtime (class file version 61.0), this version of the Java Runtime only recognizes class file versions up to 55.0
```

Dans cet exemple, la classe `EnvironmentInformation` a été compilée avec Java 17 (class file version 61.0), mais l'environnement d'exécution ne reconnaît que les versions jusqu'à Java 11 (class file version 55.0). La solution consiste à installer et à configurer Java 17 ou une version plus récente compatible avec SonarScanner et à mettre à jour la variable `JAVA_HOME`.


## Résolution de l'erreur java.lang.UnsupportedClassVersionError

| Tags |
|------|
| `Java` `SonarScanner` `java.lang.UnsupportedClassVersionError` `Ubuntu` |

L'erreur <code>java.lang.UnsupportedClassVersionError</code> signale que SonarScanner a été compilé avec une version de Java plus récente que celle installée sur votre système. En l'occurrence, la classe a été compilée avec Java 17 (version du fichier de classe 61.0), alors que votre environnement d'exécution Java actuel ne supporte que Java 11 au maximum (version du fichier de classe 55.0). La solution consiste à installer Java 17, qui est compatible avec la version de SonarScanner en cours d'utilisation.

Voici comment installer Java 17 sur Ubuntu :


## Installer Java 17 sur Ubuntu

| Tags |
|------|
| `Java` `OpenJDK` `Ubuntu` `apt` |

1.  **Mettre à jour la liste des paquets :**

    ```bash
    sudo apt update
    ```
2.  **Installer Java 17 :**

    ```bash
    sudo apt install openjdk-17-jdk
    ```
3.  **Vérifier l'installation :**

    ```bash
    java -version
    ```

    La commande ci-dessus doit afficher la version 17 de Java.


## Configurer Java 17 comme version par défaut

| Tags |
|------|
| `Java` `Java 17` `update-alternatives` `javac` `Configuration` |

Si plusieurs versions de Java sont installées, configurez Java 17 comme version par défaut :

1.  **Configurer les alternatives pour Java** :

    ```bash
    sudo update-alternatives --config java
    ```

    Sélectionnez Java 17 dans la liste des versions disponibles.

2.  **Configurer les alternatives pour javac (le compilateur Java)** :

    ```bash
    sudo update-alternatives --config javac
    ```

    Sélectionnez la version 17 de `javac`.


## Redémarrage de SonarScanner

| Tags |
|------|
| `SonarScanner` `Java` `SonarQube` |

Après la mise à jour de Java, redémarrez SonarScanner pour appliquer les modifications. Exécutez la commande suivante depuis votre répertoire de projet :

```bash
sonar-scanner \
  -Dsonar.projectKey=nom_du_projet \
  -Dsonar.sources=. \
  -Dsonar.host.url=http://localhost:9000 \
  -Dsonar.login=your_generated_token
```


## Vérification du fonctionnement

| Tags |
|------|
| `SonarQube` `SonarScanner` `Java` `Ubuntu` |

Si l'erreur `UnsupportedClassVersionError` n'apparaît plus, l'analyse démarre et s'exécute sans problème. Les résultats sont consultables sur l'instance SonarQube via navigateur.

L'installation de Java 17 et sa configuration comme version par défaut résolvent les problèmes d'incompatibilité de version, permettant à SonarScanner de fonctionner correctement sur Ubuntu.
