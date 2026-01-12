## Bloquer les uploads HTML

| Tags |
|------|
| `sécurité` `upload` `HTML` `Apache` |

Pour empêcher l'upload de fichiers HTML, vous pouvez configurer votre serveur web Apache en utilisant un fichier `.htaccess`. Cela peut être particulièrement utile pour améliorer la sécurité et empêcher des uploads malveillants.

Voici une configuration exemple :

```apache
<FilesMatch "\.html$">
  Order Allow,Deny
  Deny from all
</FilesMatch>
```

Ce code, placé dans un fichier `.htaccess` à la racine du répertoire que vous souhaitez protéger, bloque l'accès à tous les fichiers avec l'extension `.html`.

Pour l'implémenter :

1.  **Créez ou modifiez le fichier `.htaccess`** : Si le fichier n'existe pas, créez-le dans le répertoire cible. Sinon, ouvrez-le pour y ajouter les directives.
2.  **Ajoutez le code** : Copiez et collez le bloc de code ci-dessus dans le fichier `.htaccess`.
3.  **Enregistrez le fichier** : Assurez-vous d'enregistrer les modifications apportées au fichier `.htaccess`.

**Points importants :**

*   Ce code bloque l'accès aux fichiers HTML via le serveur web. Les utilisateurs ne pourront pas visualiser ou accéder aux fichiers HTML via une requête HTTP.
*   Assurez-vous que le serveur Apache est configuré pour autoriser l'utilisation des fichiers `.htaccess`. Cela se fait généralement dans le fichier de configuration principal d'Apache (souvent `httpd.conf` ou `apache2.conf`). Recherchez et assurez-vous que la directive `AllowOverride` est définie sur `All` pour le répertoire concerné.
*   Testez votre configuration en essayant d'accéder à un fichier HTML via votre navigateur après avoir mis en place les directives. Vous devriez obtenir une erreur "Accès refusé" ou similaire.

**Exemple de configuration `httpd.conf` (extrait):**

```apache
<Directory "/var/www/html">
    Options Indexes FollowSymLinks
    AllowOverride All
    Require all granted
</Directory>
```

Dans cet exemple, `AllowOverride All` permet l'utilisation de fichiers `.htaccess` pour configurer le répertoire `/var/www/html`. Remplacez `/var/www/html` par le chemin de votre répertoire.


## Bloquer l'upload de fichiers HTML dans WordPress

| Tags |
|------|
| `WordPress` `Sécurité` `Upload` `PHP` |

Pour empêcher l'upload de fichiers HTML dans WordPress, plusieurs méthodes sont possibles. La méthode suivante combine code personnalisé et configuration WordPress :

```php
<?php
add_filter( 'upload_mimes', 'restrict_html_uploads' );
function restrict_html_uploads( $mimes ) {
  unset( $mimes['htm'] );
  unset( $mimes['html'] );
  return $mimes;
}
?>
```

Ce code, ajouté au fichier `functions.php` de votre thème enfant, supprime les types de fichiers HTML (`htm` et `html`) de la liste des extensions autorisées pour les uploads.

**Instructions d'implémentation :**

1.  **Accéder à votre site WordPress :** Connectez-vous à votre tableau de bord WordPress ([NOM].com/wp-admin/).
2.  **Accéder à l'éditeur de fichiers :** Naviguez vers "Apparence" -> "Éditeur de fichiers" dans le menu d'administration.
3.  **Sélectionner `functions.php` :** Dans la liste des fichiers de thème sur le côté droit, sélectionnez `functions.php` du thème enfant actif. Si vous n'avez pas de thème enfant, créez-en un.
4.  **Coller le code :** Collez le code PHP fourni à la fin du fichier `functions.php`.
5.  **Mettre à jour le fichier :** Cliquez sur le bouton "Mettre à jour le fichier" pour enregistrer les modifications.

**Considérations supplémentaires :**

*   **Sécurité :** Bien que cette méthode réduise le risque, elle ne garantit pas une sécurité absolue. Il est important de maintenir WordPress, les plugins et le thème à jour.
*   **Alternatives :** Pour une protection plus robuste, envisagez d'utiliser des plugins de sécurité WordPress.
*   **Tests :** Après avoir implémenté ces modifications, testez la fonctionnalité d'upload pour vous assurer que les fichiers HTML ne peuvent plus être téléchargés.
*   **Contacter un expert :** Pour une configuration plus avancée ou en cas de doute, consultez un expert en sécurité WordPress ou un développeur.
*   **Autres configurations :** Vérifiez les paramètres de votre serveur et les éventuels pare-feux pour vous assurer qu'ils ne permettent pas l'accès aux fichiers HTML.
*   **Contact :** Si vous avez des questions, contactez le support technique de [NOM] à [EMAIL] ou joignez [NOM] au [IP].


## Bloquer l'upload de fichiers via functions.php

| Tags |
|------|
| `WordPress` `PHP` `functions.php` `Sécurité` `Upload` |

Vous pouvez utiliser le fichier `functions.php` de votre thème WordPress pour filtrer les types de fichiers autorisés lors de l'upload. Le code suivant bloque spécifiquement les fichiers HTML.

```php
function my_custom_mime_types($mimes) {
    // Supprimer l'extension HTML des types de fichiers autorisés
    unset($mimes['html']);
    unset($mimes['htm']);
    return $mimes;
}
add_filter('upload_mimes', 'my_custom_mime_types');
```


## Sécurisation des uploads via plugin WordPress

| Tags |
|------|
| `WordPress` `Sécurité` `Plugin` `Wordfence` `iThemes` `All In One WP Security` |

Il est possible de configurer des plugins de sécurité WordPress pour restreindre les types de fichiers téléchargeables. Voici quelques plugins populaires offrant cette fonctionnalité :

*   **Wordfence Security** : Permet de configurer diverses règles de sécurité, incluant les restrictions sur les types de fichiers.
*   **iThemes Security** : Offre des options pour restreindre l'upload de certains types de fichiers.
*   **All In One WP Security &amp; Firewall** : Inclut des fonctionnalités pour bloquer l'upload de certains types de fichiers, comme les fichiers HTML.


## Bloquer l'accès aux fichiers HTML via .htaccess

| Tags |
|------|
| `htaccess` `sécurité` `apache` `HTML` |

Une méthode consiste à utiliser le fichier `.htaccess` pour bloquer l'accès aux fichiers HTML potentiellement téléversés. Cette approche n'empêche pas le téléversement, mais interdit l'exécution des fichiers HTML sur le serveur.

Insérez le code suivant dans votre fichier `.htaccess` :

```apache
<FilesMatch "\.(html|htm)$">
    Order Allow,Deny
    Deny from all
</FilesMatch>
```


## Configuration des permissions serveur

| Tags |
|------|
| `Sécurité` `Serveur` `Apache` `Nginx` `Permissions` |

Vous pouvez configurer les permissions sur votre serveur pour empêcher l'upload ou l'exécution de fichiers HTML. Cette configuration dépend du type de serveur utilisé (Apache, Nginx, etc.). Par exemple, sur un serveur Apache, vous pouvez définir des règles dans le fichier <code>.htaccess</code> ou directement dans la configuration du serveur.


## Validation côté client

| Tags |
|------|
| `JavaScript` `Validation` `Frontend` |

Même si elle n'est pas la plus sécurisée (car contournable), une validation JavaScript côté client peut empêcher les utilisateurs de sélectionner des fichiers HTML lors de l'upload. Cette méthode doit toujours être utilisée en complément des techniques de validation côté serveur.


## Sécurisation WordPress : Prévention des uploads HTML

| Tags |
|------|
| `WordPress` `sécurité` `HTML` `upload` |

En combinant ces méthodes, vous pouvez protéger votre site WordPress contre l'upload de fichiers HTML, réduisant ainsi les risques d'attaques et d'exécution de code malveillant. Il est fortement conseillé d'associer ces mesures à un plugin de sécurité complet pour une protection optimale.


## Blocage des fonctions PHP sensibles

| Tags |
|------|
| `PHP` `Sécurité` `Fonctions` `WordPress` |

Pour bloquer l'utilisation de certaines fonctions PHP telles que <code>phpinfo()</code>, il est possible de les désactiver via la directive <code>disable_functions</code>. Cette configuration s'effectue dans le fichier de configuration PHP (<code>php.ini</code>) ou, dans certains cas, via le fichier <code>.htaccess</code>. La modification ne s'effectue pas directement dans <code>wp-config.php</code>.


## Désactivation de fonctions PHP via php.ini

| Tags |
|------|
| `PHP` `php.ini` `Sécurité` `Fonctions` |

Si vous avez accès à la configuration de votre serveur PHP, la méthode la plus efficace consiste à ajouter les fonctions que vous souhaitez désactiver dans le fichier `php.ini`.

Procédure :

1.  Accédez à votre fichier `php.ini`.
2.  Recherchez la directive `disable_functions`.
3.  Ajoutez `phpinfo` à la liste des fonctions désactivées.

Exemple :

```ini
disable_functions = phpinfo, exec, shell_exec, system, passthru
```

Après avoir ajouté cette ligne, redémarrez votre serveur pour appliquer les changements.


## Désactivation de fonctions PHP via .htaccess

| Tags |
|------|
| `PHP` `htaccess` `sécurité` `php.ini` |

Si l'accès au fichier <code>php.ini</code> n'est pas possible, la désactivation des fonctions PHP peut être tentée via le fichier <code>.htaccess</code>. Cette méthode est spécifique au serveur et peut ne pas être applicable sur tous les environnements d'hébergement.

Ajouter la directive suivante dans le fichier <code>.htaccess</code> :

```apache
php_value disable_functions phpinfo,exec,shell_exec,system,passthru
```

Si cette méthode ne fonctionne pas, il faudra utiliser l'accès à <code>php.ini</code> ou contacter l'hébergeur.


## Désactiver phpinfo() via wp-config.php

| Tags |
|------|
| `WordPress` `phpinfo()` `wp-config.php` `Sécurité` |

Bien que la désactivation directe de <code>phpinfo()</code> via <code>wp-config.php</code> ne soit pas possible, il est possible de mettre en œuvre du code pour empêcher son exécution. Cela peut se faire en utilisant des crochets, des filtres, ou en redéfinissant la fonction elle-même.

Voici un exemple de redéfinition de la fonction <code>phpinfo()</code> dans le fichier <code>wp-config.php</code> :

```php
if (!function_exists('phpinfo')) {
    function phpinfo() {
        // Rediriger ou afficher un message si quelqu'un tente d'appeler phpinfo()
        error_log('Tentative d\'appel à phpinfo() bloquée');
        die('Cette fonction a été désactivée pour des raisons de sécurité.');
    }
}
```

Ce code redéfinit la fonction <code>phpinfo()</code> pour qu'elle n'effectue aucune action ou affiche un message en cas de tentative d'appel. Cette méthode est utile pour bloquer l'utilisation spécifique de <code>phpinfo()</code> dans WordPress, mais n'empêche pas les autres scripts PHP du serveur de l'appeler.


## Blocage des fonctions PHP

| Tags |
|------|
| `PHP` `php.ini` `WordPress` |

La méthode la plus sûre pour bloquer des fonctions PHP telles que <code>phpinfo()</code> est de les désactiver directement dans la configuration PHP via <code>php.ini</code>. Si l'accès à ce fichier est impossible, des alternatives existent : utiliser <code>.htaccess</code> ou, en dernier recours, des solutions spécifiques dans <code>wp-config.php</code> pour redéfinir ou bloquer ces fonctions dans votre installation WordPress.


## Empêcher l'interprétation HTML

| Tags |
|------|
| `HTML` `sécurité` `échappement` `sanitisation` |

Pour empêcher l'interprétation et l'exécution du code HTML soumis via un formulaire, il est impératif d'**échapper** ou de **sanitiser** ce code avant son affichage sur une page web. Cette pratique protège contre l'exécution de scripts malveillants et l'affichage indésirable de code HTML.


## Sécurisation XSS avec htmlspecialchars() en PHP

| Tags |
|------|
| `PHP` `HTML` `XSS` `htmlspecialchars` |

La fonction `htmlspecialchars()` est une méthode courante pour prévenir les attaques Cross-Site Scripting (XSS) en PHP. Elle convertit les caractères spéciaux en entités HTML, empêchant leur exécution par le navigateur.

Exemple :

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_input = $_POST['user_input'];

    // Échapper le contenu avant l'affichage
    echo htmlspecialchars($user_input, ENT_QUOTES, 'UTF-8');
}
?>
```

Dans cet exemple, si l'utilisateur soumet <code>&lt;script&gt;alert(&#x27;XSS&#x27;);&lt;/script&gt;</code>, le navigateur affichera <code>&amp;lt;script&amp;gt;alert(&#x27;XSS&#x27;);&amp;lt;/script&amp;gt;</code>, évitant l'exécution du script.


## Utilisation de htmlentities()

| Tags |
|------|
| `PHP` `htmlentities` `Sécurité` `HTML` |

Une autre fonction similaire est `htmlentities()`, qui convertit tous les caractères applicables en entités HTML, contrairement à `htmlspecialchars()`.

Exemple :

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_input = $_POST['user_input'];

    // Convertir tous les caractères spéciaux en entités HTML
    echo htmlentities($user_input, ENT_QUOTES, 'UTF-8');
}
?>
```


## Validation et nettoyage des entrées utilisateur

| Tags |
|------|
| `PHP` `sécurité` `validation` `strip_tags` `htmlspecialchars` |

Il est fortement conseillé de valider et de nettoyer les entrées utilisateur pour prévenir l'injection de code malveillant ou de balises HTML indésirables. La fonction PHP <code>strip_tags()</code> permet de supprimer toutes les balises HTML et PHP.

Exemple :

```php
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user_input = $_POST['user_input'];

    // Supprimer toutes les balises HTML
    $clean_input = strip_tags($user_input);

    echo htmlspecialchars($clean_input, ENT_QUOTES, 'UTF-8');
}
?>
```


## Protection avec un WAF ou un plugin de sécurité

| Tags |
|------|
| `WAF` `WordPress` `Sécurité` `Plugin` |

Pour les sites WordPress ou les applications web plus complexes, l'utilisation d'un <strong>Web Application Firewall (WAF)</strong> ou d'un plugin de sécurité peut aider à protéger contre les injections de scripts et autres attaques liées à l'interprétation du code HTML.


## Sécurité des entrées utilisateurs et XSS

| Tags |
|------|
| `XSS` `Sécurité` `htmlspecialchars()` `htmlentities()` |

Échapper et nettoyer les entrées utilisateurs avant affichage est essentiel pour prévenir les attaques de type <strong>Cross-Site Scripting (XSS)</strong> et autres vulnérabilités. Les fonctions <code>htmlspecialchars()</code> et <code>htmlentities()</code>, associées à une validation des données efficace, assurent la sécurité du site et la gestion appropriée des entrées HTML.


## Extensions de fichiers à surveiller pour la sécurité

| Tags |
|------|
| `PHP` `Sécurité` `Apache` `Extensions` |

Lors de la gestion des fichiers uploadés sur un serveur Apache avec PHP, plusieurs extensions de fichiers peuvent être problématiques car elles peuvent contenir du code exécutable ou potentiellement nuisible. Voici une liste des principales extensions que vous devriez surveiller et éventuellement bloquer pour éviter les risques de sécurité :


## Extensions de fichiers PHP

| Tags |
|------|
| `PHP` `fichiers` `extensions` |

Les fichiers PHP peuvent contenir du code serveur exécuté par Apache/PHP :

*   ` .php`
*   ` .php3`
*   ` .php4`
*   ` .php5`
*   ` .php7`
*   ` .phtml`
*   ` .phps` (code source PHP)


## Extensions de scripts système

| Tags |
|------|
| `shell` `script` `sécurité` `système` |

Ces fichiers peuvent contenir des commandes système qui, si elles sont exécutées, peuvent compromettre la sécurité du serveur :

*   `.sh` (Shell script)
*   `.bash` (Bash script)
*   `.csh` (C shell script)
*   `.bat` (Batch file pour Windows)
*   `.cmd` (Command file pour Windows)


## Extensions Python et Perl

| Tags |
|------|
| `Python` `Perl` `script` `extension` |

Ces fichiers peuvent exécuter du code Python ou Perl sur le serveur :

*   `.py` (script Python)
*   `.pl` (script Perl)
*   `.cgi` (script Common Gateway Interface, souvent écrit en Perl)


## Extensions JavaScript côté serveur
| Tags |
|------|
| `JavaScript` `Serveur` `Fichier` |

JavaScript peut être utilisé côté serveur dans les configurations suivantes :

*   `.js` (JavaScript)
*   `.jsp` (Java Server Pages)
*   `.jspx` (Java Server Pages XML)
*   `.htc` (HTML Components)


## Extensions de fichiers clients et code malveillant

| Tags |
|------|
| `HTML` `Scripts` `Sécurité` `XML` |

Ces extensions peuvent être associées à des fichiers de configuration ou de script côté client et sont susceptibles de contenir du code malveillant :

*   `.html` ou `.htm` (fichiers HTML)
*   `.shtml` (Server-side include HTML)
*   `.xhtml` (Extensible HTML)
*   `.xml` (Extensible Markup Language)
*   `.svg` (Scalable Vector Graphics - peut contenir des scripts malveillants)


## Extensions de fichiers exécutables

| Tags |
|------|
| `exécutable` `Windows` `sécurité` |

Ces fichiers peuvent être exécutés sur le serveur ou le client, causant potentiellement des dommages :

*   `.exe` (Windows executable)
*   `.dll` (Windows dynamic link library)
*   `.com` (Command file pour DOS)
*   `.scr` (Screensaver pour Windows, mais peut contenir du code exécutable)
*   `.msi` (Microsoft Installer)


## Extensions de fichiers de scripts et d'automatisation

| Tags |
|------|
| `scripting` `automatisation` `sécurité` |

Ces fichiers sont susceptibles d'exécuter des tâches automatisées. Leur compromission peut engendrer des risques :

*   `vbs` (VBScript)
*   `wsf` (Windows Script File)
*   `hta` (HTML Application)


## Extensions de fichiers compressés et archivés

| Tags |
|------|
| `Compression` `Archive` `Sécurité` |

Ces fichiers peuvent contenir d'autres fichiers potentiellement nuisibles une fois décompressés :

*   `.zip`
*   `.rar`
*   `.tar`
*   `.gz`
*   `.7z`


## Extensions spécifiques au serveur Apache

| Tags |
|------|
| `Apache` `configuration` `.htaccess` `.htpasswd` |

Certains fichiers spécifiques à la configuration d'Apache peuvent poser problème s'ils sont mal configurés :

*   `.htaccess` (fichier de configuration Apache)
*   `.htpasswd` (fichier de mot de passe Apache)


## Extensions serveur associées

| Tags |
|------|
| `ASP` `JSP` `Certificats` |

*   `.asp` ou `.aspx` (Active Server Pages)
*   `.jsp` (Java Server Pages)
*   `.cer` ou `.crt` (Certificate file, potentiellement utilisés de manière malveillante dans certaines configurations)


## Sécurisation des uploads de fichiers

| Tags |
|------|
| `sécurité` `upload` `Apache` `PHP` `WordPress` |

Pour sécuriser votre serveur, limitez l'upload aux types de fichiers nécessaires, tels que les images (<code>.jpg</code>, <code>.png</code>, <code>.gif</code>) et les documents (<code>.pdf</code>, <code>.docx</code>, <code>.xlsx</code>). Configurez des règles dans Apache (via <code>.htaccess</code> ou <code>httpd.conf</code>), dans PHP (via <code>php.ini</code>), ou utilisez des plugins de sécurité WordPress pour bloquer l'upload de fichiers dangereux.

Validez et nettoyez toutes les entrées utilisateurs. Limitez également les permissions d'exécution sur les répertoires de stockage des fichiers uploadés.


## Création d'une liste d'extensions PHP et regex

| Tags |
|------|
| `PHP` `regex` `sécurité` `file` |

```php
<?php
// Liste des extensions problématiques
$dangerous_extensions = [
    'php', 'php3', 'php4', 'php5', 'php7', 'phtml', 'phps',
    'sh', 'bash', 'csh', 'bat', 'cmd',
    'py', 'pl', 'cgi',
    'js', 'jsp', 'jspx', 'htc',
    'html', 'htm', 'shtml', 'xhtml', 'xml', 'svg',
    'exe', 'dll', 'com', 'scr', 'msi',
    'vbs', 'wsf', 'hta',
    'zip', 'rar', 'tar', 'gz', '7z',
    'asp', 'aspx',
    'cer', 'crt',
    'htaccess', 'htpasswd'
];

// Création d'une regex pour détecter ces extensions
$dangerous_extensions_regex = '/\.(' . implode('|', $dangerous_extensions) . ')$/i';

// Exemple d'utilisation
$uploaded_file = 'example.php';

if (preg_match($dangerous_extensions_regex, $uploaded_file)) {
    echo "Le fichier est potentiellement dangereux.";
} else {
    echo "Le fichier est sûr.";
}
?>
```


## Comprendre le filtrage des extensions de fichiers

| Tags |
|------|
| `PHP` `regex` `sécurité` `validation` |

<ol>
<li>
<p><strong>Liste des extensions dangereuses</strong> :</p>
<ul>
<li>La liste <code>$dangerous_extensions</code> contient les extensions de fichiers considérées comme dangereuses. L'ajout ou la suppression d'extensions dans cette liste est personnalisable selon les exigences.</li>
</ul>
</li>
<li>
<p><strong>Construction de l'expression régulière</strong> :</p>
<ul>
<li>La fonction <code>implode(&#x27;|&#x27;, $dangerous_extensions)</code> crée une chaîne où chaque extension est séparée par le caractère <code>|</code>, l'opérateur "ou" en regex.</li>
<li>
L'expression régulière résultante est ensuite incluse dans <code>/\.(extension1|extension2)$/i</code>, ce qui signifie :<ul>
<li><code>\.</code> : Correspond au caractère littéral &quot;.&quot; précédant l'extension.</li>
<li><code>extension1|extension2</code> : Correspond à l'une des extensions de la liste.</li>
<li><code>$</code> : Assure que l'extension est à la fin du nom du fichier.</li>
<li><code>i</code> : Indique une recherche insensible à la casse (par exemple, pour détecter <code>.PHP</code>).</li>
</ul>
</li>
</ul>
</li>
<li>
<p><strong>Application de l'expression régulière</strong> :</p>
<ul>
<li>La fonction <code>preg_match()</code> vérifie si le nom de fichier correspond à l'une des extensions dangereuses. Si une correspondance est trouvée, un message d'avertissement est affiché.</li>
</ul>
</li>
</ol>


## Sécurisation des fichiers uploadés

| Tags |
|------|
| `sécurité` `upload` `expression régulière` |

Ce script permet de filtrer les fichiers uploadés en fonction de leur extension. Une expression régulière est utilisée pour vérifier si le nom de fichier se termine par l'une des extensions potentiellement dangereuses. L'objectif est de sécuriser le traitement des fichiers uploadés sur votre serveur.


## Bloquer les types de fichiers avec `upload_mimes`

| Tags |
|------|
| `WordPress` `PHP` `upload_mimes` `Sécurité` |

Le hook `upload_mimes` de WordPress permet de contrôler les types de fichiers autorisés lors de l'upload. Pour interdire certaines extensions de fichiers potentiellement dangereuses, ce hook peut être utilisé pour filtrer les types MIME correspondants.

Voici un exemple de code à ajouter dans le fichier `functions.php` de votre thème ou dans un plugin personnalisé pour bloquer les extensions problématiques :

```php
function block_dangerous_mime_types($mimes) {
    // Liste des extensions à bloquer
    $dangerous_extensions = [
        'php', 'php3', 'php4', 'php5', 'php7', 'phtml', 'phps',
        'sh', 'bash', 'csh', 'bat', 'cmd',
        'py', 'pl', 'cgi',
        'js', 'jsp', 'jspx', 'htc',
        'html', 'htm', 'shtml', 'xhtml', 'xml', 'svg',
        'exe', 'dll', 'com', 'scr', 'msi',
        'vbs', 'wsf', 'hta',
        'zip', 'rar', 'tar', 'gz', '7z',
        'asp', 'aspx',
        'cer', 'crt',
        'htaccess', 'htpasswd'
    ];

    // Parcourir la liste des extensions et les supprimer des types MIME autorisés
    foreach ($dangerous_extensions as $ext) {
        if (isset($mimes[$ext])) {
            unset($mimes[$ext]);
        }
    }

    return $mimes;
}
add_filter('upload_mimes', 'block_dangerous_mime_types');
```


## Explications du code de blocage d'extensions

| Tags |
|------|
| `WordPress` `sécurité` `PHP` `upload_mimes` |

<ol>
<li>
<p><strong>Liste des extensions bloquées</strong> :</p>
<ul>
<li>La variable <code>$dangerous_extensions</code> contient la liste des extensions de fichiers à bloquer lors des uploads sur le site WordPress.</li>
</ul>
</li>
<li>
<p><strong>Filtrage des types MIME</strong> :</p>
<ul>
<li>La fonction <code>block_dangerous_mime_types()</code> reçoit un tableau <code>$mimes</code> en paramètre, représentant les types MIME autorisés.</li>
<li>Pour chaque extension de <code>$dangerous_extensions</code>, la fonction vérifie sa présence dans <code>$mimes</code> et la supprime en utilisant <code>unset()</code> si elle est trouvée.</li>
</ul>
</li>
<li>
<p><strong>Intégration du hook <code>upload_mimes</code></strong> :</p>
<ul>
<li>Le filtre <code>upload_mimes</code> est utilisé pour appliquer la fonction <code>block_dangerous_mime_types()</code>, bloquant ainsi les extensions non désirées.</li>
</ul>
</li>
</ol>


## Sécurisation des téléchargements WordPress

| Tags |
|------|
| `WordPress` `Sécurité` `PHP` |

En intégrant ce code à votre site WordPress, vous empêchez les utilisateurs de télécharger des fichiers avec des extensions potentiellement à risque. Ceci renforce la sécurité en limitant les types de fichiers autorisés à ceux qui ne présentent pas de risque d'exécution de code malveillant.

Le code est adaptable ; vous pouvez ajouter ou supprimer des extensions de la liste <code>$dangerous_extensions</code> selon vos besoins.


## Récupération du JSON d'une requête POST en PHP

| Tags |
|------|
| `PHP` `JSON` `POST` `file_get_contents` `json_decode` |

Pour récupérer les données JSON envoyées via une requête POST en PHP, utilisez la fonction <code>file_get_contents('php://input')</code> pour lire le flux de données brutes, puis décodez le JSON en un tableau ou un objet PHP à l'aide de <code>json_decode()</code>.

Voici un exemple de code :

```php
<?php
// Lire le contenu brut de la requête POST
$json_data = file_get_contents('php://input');

// Décoder le JSON en un tableau associatif PHP
$data = json_decode($json_data, true);

// Vérifier si le JSON a été décodé correctement
if (json_last_error() === JSON_ERROR_NONE) {
    // Utiliser les données JSON décodées
    print_r($data); // Par exemple, afficher le tableau

    // Accéder à une valeur spécifique
    if (isset($data['key'])) {
        echo "La valeur de 'key' est : " . $data['key'];
    }
} else {
    // Gérer l'erreur si le JSON est mal formé
    echo "Erreur dans le format JSON : " . json_last_error_msg();
}
?>
```


## Analyse du Code : Lecture et Traitement JSON

| Tags |
|------|
| `PHP` `JSON` `HTTP` `file_get_contents` `json_decode` |

<ol>
<li>
<p><strong>Lecture des données brutes</strong> :</p>
<ul>
<li><code>file_get_contents('php://input')</code> : Lit le corps brut d'une requête HTTP POST, principalement utilisé pour les données JSON.</li>
</ul>
</li>
<li>
<p><strong>Décodage JSON</strong> :</p>
<ul>
<li><code>json_decode($json_data, true)</code> : Convertit une chaîne JSON en un tableau associatif PHP.  Sans le second paramètre <code>true</code>, un objet PHP est renvoyé.</li>
</ul>
</li>
<li>
<p><strong>Gestion des erreurs JSON</strong> :</p>
<ul>
<li><code>json_last_error()</code> : Vérifie les erreurs survenues pendant le décodage JSON.</li>
<li><code>json_last_error_msg()</code> : Fournit un message d'erreur descriptif en cas d'erreur de format JSON.</li>
</ul>
</li>
<li>
<p><strong>Utilisation des données JSON</strong> :</p>
<ul>
<li>Accès aux valeurs du tableau ou de l'objet PHP après le décodage JSON.</li>
</ul>
</li>
</ol>


## Gestion des erreurs de décodage JSON

| Tags |
|------|
| `JSON` `API REST` `Gestion des erreurs` |


## Simplification du code PHP WPML

| Tags |
|------|
| `PHP` `WPML` `Traduction` |

```php
<?php

include_once('class.concilio-wpml.php');

try {
    if (isset($_GET['wpml'])) {
        $wpml = $_GET['wpml'];
        $string = $_GET['string'] ?? '';
        $to = $_GET['to'] ?? 'fr';
        $domain = $_GET['domain'] ?? '';

        if ($wpml == 1 && $string && $to && $domain) {
            define('ICL_LANGUAGE_CODE', $to);
            global $bypass_all_plugins;
            $bypass_all_plugins = [
                "sitepress-multilingual-cms/sitepress.php",
                // 19/04/2024 "wpml-string-translation/plugin.php"
            ];
            include($_SERVER['DOCUMENT_ROOT'] . '/wp-blog-header.php');
            http_response_code(200);
            echo json_encode((new concilio_wpml())->retrieve_translation($string, '', $to, $domain));
        } elseif ($wpml == 2) {
            $json_data = file_get_contents('php://input');
            $data = json_decode($json_data, true);
            $to = $_GET['to'] ?? 'fr';
            $domain = $data['domain'] ?? '';
            $string = $data['string'] ?? '';

            if ($to && $domain && $string) {
                define('ICL_LANGUAGE_CODE', $to);
                global $bypass_all_plugins;
                $bypass_all_plugins = [
                    "sitepress-multilingual-cms/sitepress.php",
                    // 19/04/2024 "wpml-string-translation/plugin.php"
                ];
                include($_SERVER['DOCUMENT_ROOT'] . '/wp-blog-header.php');
                http_response_code(200);
                echo json_encode((new concilio_wpml())->retrieve_translation($string, '', $to, $domain));
            } else {
                http_response_code(200);
                echo json_encode($string);
            }
        } else {
            http_response_code(200);
            echo json_encode($string);
        }
    }
} catch (Exception $e) {
    $string = $_GET['string'] ?? '';
    http_response_code(200);
    echo json_encode($string);
}
?>
```


## Amélioration du Code PHP pour la Traduction WPML

| Tags |
|------|
| `PHP` `WPML` `Traduction` `API` |

```php
<?php

include_once('class.concilio-wpml.php');

function handle_translation($string, $to, $domain) {
    define('ICL_LANGUAGE_CODE', $to);
    global $bypass_all_plugins;
    $bypass_all_plugins = array(
        "sitepress-multilingual-cms/sitepress.php",
        // 19/04/2024 "wpml-string-translation/plugin.php"
    );
    include($_SERVER['DOCUMENT_ROOT'] . '/wp-blog-header.php');
    http_response_code(200);
    echo json_encode((new concilio_wpml())->retrieve_translation($string, '', $to, $domain));
}

try {
    if (isset($_GET['wpml'])) {
        $to = $_GET['to'] ?? 'fr';
        if ($to == 'undefined') {
            $to = 'fr';
        }

        $string = $_GET['string'] ?? '';
        $domain = $_GET['domain'] ?? '';

        if ($_GET['wpml'] == 1 && isset($_GET['string'], $_GET['to'], $_GET['domain'])) {
            handle_translation($string, $to, $domain);
        } elseif ($_GET['wpml'] == 2) {
            $json_data = file_get_contents('php://input');
            $data = json_decode($json_data, true);
            if (isset($data['string'], $data['domain'])) {
                $string = $data['string'];
                $domain = $data['domain'];
                handle_translation($string, $to, $domain);
            } else {
                http_response_code(200);
                echo json_encode($string);
            }
        } else {
            http_response_code(200);
            echo json_encode($string);
        }
    }
} catch (Exception $e) {
    $string = $_GET['string'] ?? '';
    http_response_code(200);
    echo json_encode($string);
}
```


## Améliorations de code

| Tags |
|------|
| `refactoring` `PHP` `code simplification` |

<ol>
<li>
<p><strong>Fonction <code>handle_translation</code></strong> : La logique de traduction redondante a été encapsulée dans une fonction, simplifiant ainsi le code et réduisant la duplication.</p>
</li>
<li>
<p><strong>Opérateur null coalescent <code>??</code></strong> : L'utilisation de cet opérateur permet de définir des valeurs par défaut lors de l'accès aux éléments des tableaux <code>$_GET</code> et <code>$data</code>.</p>
</li>
<li>
<p><strong>Réduction des redondances</strong> : Le traitement des erreurs et des réponses par défaut a été simplifié pour éviter les répétitions inutiles.</p>
</li>
</ol>
<p>Cette version améliorée offre une meilleure lisibilité et maintenabilité, tout en préservant les fonctionnalités du code original.</p>


## Implémentation d'un Switch Case avec $_GET['wpml']

| Tags |
|------|
| `PHP` `$_GET` `switch` `WPML` |

```php
<?php

include_once('class.concilio-wpml.php');

function handle_translation($string, $to, $domain) {
    define('ICL_LANGUAGE_CODE', $to);
    global $bypass_all_plugins;
    $bypass_all_plugins = array(
        "sitepress-multilingual-cms/sitepress.php",
        // 19/04/2024 "wpml-string-translation/plugin.php"
    );
    include($_SERVER['DOCUMENT_ROOT'] . '/wp-blog-header.php');
    http_response_code(200);
    echo json_encode((new concilio_wpml())->retrieve_translation($string, '', $to, $domain));
}

try {
    $wpml = $_GET['wpml'] ?? null;
    $string = $_GET['string'] ?? '';
    $to = $_GET['to'] ?? 'fr';
    if ($to == 'undefined') {
        $to = 'fr';
    }
    $domain = $_GET['domain'] ?? '';

    switch ($wpml) {
        case 1: // GET request handling
            if (isset($_GET['string'], $_GET['to'], $_GET['domain'])) {
                handle_translation($string, $to, $domain);
            } else {
                http_response_code(200);
                echo json_encode($string);
            }
            break;

        case 2: // POST request handling
            $json_data = file_get_contents('php://input');
            $data = json_decode($json_data, true);
            if (isset($data['string'], $data['domain'])) {
                $string = $data['string'];
                $domain = $data['domain'];
                handle_translation($string, $to, $domain);
            } else {
                http_response_code(200);
                echo json_encode($string);
            }
            break;

        default:
            http_response_code(200);
            echo json_encode($string);
            break;
    }
} catch (Exception $e) {
    http_response_code(200);
    echo json_encode($string);
}
```

## Améliorations de l'implémentation

| Tags |
|------|
| `PHP` `switch` `GET` `POST` `null coalescent` |

<ol>
<li>
<p><strong>Implémentation Switch Case</strong> :</p>
<ul>
<li>Le code utilise une instruction <code>switch</code> pour gérer la valeur de <code>$_GET[&#x27;wpml&#x27;]</code>, améliorant la lisibilité du flux de contrôle.</li>
<li>Les cas <code>1</code> et <code>2</code> traitent respectivement les requêtes GET et POST, avec des opérations spécifiques pour chacune.</li>
</ul>
</li>
<li>
<p><strong>Définition des valeurs par défaut</strong> :</p>
<ul>
<li>Les valeurs par défaut pour <code>$_GET[&#x27;string&#x27;]</code>, <code>$_GET[&#x27;to&#x27;]</code>, et <code>$_GET[&#x27;domain&#x27;]</code> sont établies via l'opérateur null coalescent (<code>??</code>).</li>
</ul>
</li>
<li>
<p><strong>Rationalisation des blocs conditionnels</strong> :</p>
<ul>
<li>L'instruction <code>switch</code> simplifie la structure en regroupant logiquement les différentes conditions basées sur <code>$_GET[&#x27;wpml&#x27;]</code>.</li>
<li>Le bloc <code>default</code> gère les cas où <code>$_GET[&#x27;wpml&#x27;]</code> ne correspond à aucune des valeurs définies, offrant un comportement par défaut.</li>
</ul>
</li>
</ol>
<p>Ce code optimisé offre une meilleure lisibilité et maintenabilité, tout en conservant les fonctionnalités de la version précédente.</p>


## Code de réponse

| Tags |
|------|
| `code` `réponse` `exemple` |

Pour être certain que le code de réponse


## Vérification du code d'erreur HTTP avec jQuery.ajax

| Tags |
|------|
| `JavaScript` `jQuery` `AJAX` `HTTP` `Erreur` |

Pour vérifier le code d'erreur HTTP dans votre requête `jQuery.ajax`, vous devez utiliser l'option `statusCode`. Cette option vous permet de gérer les différents codes de statut HTTP renvoyés par le serveur.

Voici comment modifier votre code pour inclure la vérification du code d'erreur 200 :

```javascript
jQuery.ajax({
    type: "POST",
    url: wpml_url_api(),
    data: {
        "domain": "concilio-js",
        "string": afternoonQuery.text(),
    },
    statusCode: {
        200: function(result) {
            var output = jQuery.parseJSON(result);
            jQuery('#afternoon-button').text(output.translated);
        },
        // Gérer les autres codes d'erreur si nécessaire
        400: function() {
            // Gérer les erreurs 400 (Bad Request)
            console.error("Erreur 400 : Requête incorrecte.");
        },
        500: function() {
            // Gérer les erreurs 500 (Internal Server Error)
            console.error("Erreur 500 : Erreur interne du serveur.");
        }
    }
});
```

Dans ce code :

*   L'option `statusCode` est utilisée pour définir des fonctions de rappel pour différents codes de statut HTTP.
*   `200` est le code de statut "OK".  La fonction définie sera exécutée si la requête réussit et renvoie le code 200. Le traitement des données se fait de la même manière que dans votre code initial.
*   Des fonctions de rappel supplémentaires sont ajoutées pour gérer d'autres codes d'erreur (400, 500, etc.).  Vous devriez adapter ces fonctions pour traiter les erreurs spécifiques selon les besoins de votre application. Cela peut inclure l'affichage de messages d'erreur à l'utilisateur, la journalisation des erreurs, ou toute autre action appropriée.

En utilisant `statusCode`, vous pouvez spécifiquement gérer le cas où le code d'erreur est 200 et également prendre des mesures en cas d'autres codes d'erreur, améliorant ainsi la robustesse de votre code.


## Vérification du code d'erreur HTTP avec jQuery

| Tags |
|------|
| `jQuery` `AJAX` `HTTP` `statusCode` `complete` |

Pour s'assurer que le code d'erreur est 200 avant de traiter la réponse, utilisez les fonctions <code>complete</code> ou <code>statusCode</code> dans les requêtes AJAX jQuery. Ces fonctions permettent de vérifier le code de statut HTTP retourné par le serveur avant l'exécution du traitement de la réponse.

Exemple de modification du code pour vérifier le code de statut HTTP :


## Vérification du statut HTTP avec `statusCode`

| Tags |
|------|
| `JavaScript` `jQuery` `Ajax` `statusCode` `HTTP` |

Vous pouvez utiliser l'option `statusCode` pour vérifier que le code de statut est 200 avant de traiter la réponse :

```javascript
jQuery.ajax({
    type: "POST",
    url: wpml_url_api(),
    data: {
        "domain": "concilio-js",
        "string": afternoonQuery.text(),
    },
    statusCode: {
        200: function(result) {
            var output = jQuery.parseJSON(result);
            jQuery('#afternoon-button').text(output.translated);
        }
    },
    error: function(jqXHR, textStatus, errorThrown) {
        console.log("Erreur : " + textStatus + ", " + errorThrown);
        // Vous pouvez ajouter ici un traitement d'erreur
    }
});
```


## Vérification du statut HTTP avec `complete`

| Tags |
|------|
| `JavaScript` `jQuery` `Ajax` `HTTP` `Statut` |

Une autre méthode consiste à utiliser l'option `complete` pour vérifier le code de statut de la réponse avant de traiter la donnée :

```javascript
jQuery.ajax({
    type: "POST",
    url: wpml_url_api(),
    data: {
        "domain": "concilio-js",
        "string": afternoonQuery.text(),
    },
    complete: function(jqXHR, textStatus) {
        if (jqXHR.status === 200) {
            var output = jQuery.parseJSON(jqXHR.responseText);
            jQuery('#afternoon-button').text(output.translated);
        } else {
            console.log("Erreur : code de statut HTTP " + jqXHR.status);
            // Vous pouvez gérer d'autres codes de statut ici
        }
    },
    error: function(jqXHR, textStatus, errorThrown) {
        console.log("Erreur : " + textStatus + ", " + errorThrown);
        // Traitement supplémentaire des erreurs si nécessaire
    }
});
```


## Gestion des réponses HTTP

| Tags |
|------|
| `HTTP` `statusCode` `error` `complete` |

<ol>
<li>
<p><strong><code>statusCode</code></strong> :</p>
<ul>
<li>Définit des callbacks spécifiques pour chaque code de statut HTTP. Le traitement est effectué uniquement si le serveur retourne un code 200.</li>
</ul>
</li>
<li>
<p><strong><code>complete</code></strong> :</p>
<ul>
<li>Exécute une fonction une fois la requête terminée, quelle que soit la réponse. Le code de statut (<code>jqXHR.status</code>) peut être vérifié manuellement avant de traiter la réponse.</li>
</ul>
</li>
<li>
<p><strong><code>error</code></strong> :</p>
<ul>
<li>Gère les erreurs réseau ou les codes de statut HTTP autres que 200.</li>
</ul>
</li>
</ol>
<p>Ces méthodes garantissent que la logique s'exécute uniquement en cas de code 200, assurant le traitement d'une réponse réussie.</p>


## Requête AJAX et réception des données

| Tags |
|------|
| `JavaScript` `jQuery` `AJAX` `POST` `PHP` |

```javascript
jQuery.ajax({
    type: "POST",
    url: wpml_url_api(),
    data: {
        "domain": "concilio-js",
        "string": morningQuery.text(),
    },
    statusCode: {
        200: function (result) {
            var output = jQuery.parseJSON(result);
            jQuery('#morning-button').text(output.translated);
        }
    },
    error: function (jqXHR, textStatus, errorThrown) {
        jQuery('#morning-button').text(morningQuery.text());
    }
});
```

Les données sont reçues par le point de terminaison PHP comme une QueryString. La configuration ci-dessus présente-t-elle des lacunes ?


## Envoyer des données JSON avec jQuery AJAX

| Tags |
|------|
| `jQuery` `AJAX` `JSON` `POST` |

Lorsque vous envoyez des données via une requête POST avec jQuery AJAX, les données sont, par défaut, envoyées en tant que `application/x-www-form-urlencoded`. Ce format est similaire à une chaîne de requête. Pour que le serveur traite les données comme du JSON, vous devez les formater correctement et ajuster les en-têtes HTTP.

Voici les étapes à suivre :


## Envoi de données JSON via requêtes AJAX

| Tags |
|------|
| `JSON` `AJAX` `JavaScript` `jQuery` `API` |

Pour envoyer des données au format JSON, convertissez votre objet en chaîne JSON et spécifiez l'en-tête `Content-Type` comme `application/json` :

```javascript
jQuery.ajax({
    type: "POST",
    url: wpml_url_api(),
    data: JSON.stringify({
        "domain": "concilio-js",
        "string": morningQuery.text(),
    }),
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    statusCode: {
        200: function (result) {
            jQuery('#morning-button').text(result.translated);
        }
    },
    error: function (jqXHR, textStatus, errorThrown) {
        jQuery('#morning-button').text(morningQuery.text());
    }
});
```


## Explications concernant les requêtes JSON

| Tags |
|------|
| `JSON` `JavaScript` `Serveur` |

<ol>
<li>
<p><strong><code>JSON.stringify()</code></strong> :</p>
<ul>
<li>Convertit un objet JavaScript en une chaîne JSON. Cette opération assure que les données sont transmises au serveur au format JSON.</li>
</ul>
</li>
<li>
<p><strong><code>contentType: &quot;application/json; charset=utf-8&quot;</code></strong> :</p>
<ul>
<li>Informe le serveur que les données reçues sont au format JSON.</li>
</ul>
</li>
<li>
<p><strong><code>dataType: &quot;json&quot;</code></strong> :</p>
<ul>
<li>Spécifie que la réponse attendue du serveur est en JSON. Bien que pas toujours obligatoire si le serveur renvoie correctement du JSON, il est recommandé pour une meilleure pratique.</li>
</ul>
</li>
</ol>


## Solution 2 : Traitement des données URL-encodées en PHP

| Tags |
|------|
| `PHP` `$_POST` `URL-encoding` |

Si les données sont conservées sous forme URL-encodée, le code PHP doit être configuré pour traiter correctement ces données.  Utilisez la variable `$_POST` pour récupérer les données. Assurez-vous que le point d'accès PHP est configuré pour traiter `$_POST` plutôt que `php://input`.

Exemple de code PHP pour récupérer les données :

```php
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $domain = $_POST['domain'];
    $string = $_POST['string'];

    // Traitement des données...
}
```


## Conclusion : Choix de la méthode d'envoi de données

| Tags |
|------|
| `JSON` `PHP` `$_POST` `URL Encoding` |

La méthode à privilégier dépend des exigences spécifiques. L'utilisation du format JSON pour l'envoi de données et leur traitement natif en PHP requiert la première approche. Dans le cas contraire, si l'encodage URL par défaut est souhaité, il est impératif que PHP traite correctement la variable <code>$_POST</code>.


## Factorisation des appels jQuery.ajax

| Tags |
|------|
| `JavaScript` `jQuery` `Ajax` `Factorisation` |

```javascript
function callAjax(queryString, buttonId) {
    jQuery.ajax({
        type: "POST",
        url: wpml_url_api(),
        data: JSON.stringify({
            "domain": "concilio-js",
            "string": queryString.text(),
        }),
        contentType: "application/json; charset=utf-8",
        statusCode: {
            200: function (result) {
                var output = jQuery.parseJSON(result);
                jQuery('#' + buttonId).text(output.translated);
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            jQuery('#' + buttonId).text(queryString.text());
        }
    });
}

callAjax(morningQuery, 'morning-button');
callAjax(afternoonQuery, 'afternoon-button');
callAjax(eveningQuery, 'evening-button');
```


## Fonction générique pour requêtes AJAX

| Tags |
|------|
| `JavaScript` `AJAX` `Fonction` `jQuery` |

Pour factoriser le code, une fonction générique peut gérer les appels AJAX avec des paramètres spécifiques pour chaque requête.

```javascript
function sendTranslationRequest(queryElement, buttonElement) {
    jQuery.ajax({
        type: "POST",
        url: wpml_url_api(),
        data: JSON.stringify({
            "domain": "concilio-js",
            "string": queryElement.text(),
        }),
        contentType: "application/json; charset=utf-8",
        statusCode: {
            200: function (result) {
                var output = jQuery.parseJSON(result);
                jQuery(buttonElement).text(output.translated);
            }
        },
        error: function (jqXHR, textStatus, errorThrown) {
            jQuery(buttonElement).text(queryElement.text());
        }
    });
}

// Utilisation de la fonction générique pour chaque bouton
sendTranslationRequest(morningQuery, '#morning-button');
sendTranslationRequest(afternoonQuery, '#afternoon-button');
sendTranslationRequest(eveningQuery, '#evening-button');
```


## Rationalisation du code de traduction

| Tags |
|------|
| `JavaScript` `AJAX` `Fonctions` `Refactoring` |

1.  **Fonction <code>sendTranslationRequest</code> :**

    *   Cette fonction prend deux paramètres : <code>queryElement</code> et <code>buttonElement</code>.
    *   <code>queryElement</code> est l'élément contenant le texte à traduire.
    *   <code>buttonElement</code> est l'élément DOM où le texte traduit sera affiché.

2.  **Appels AJAX Factorisés :**

    *   Le corps de la fonction contient l'appel AJAX, désormais générique et réutilisable.
    *   Les données sont récupérées de <code>queryElement.text()</code> et injectées dans l'appel AJAX.
    *   Le résultat de l'appel met à jour <code>buttonElement</code>.

3.  **Appel de la fonction pour chaque bouton :**

    *   La fonction est appelée pour chaque combinaison d'élément de texte et de bouton, remplaçant les appels AJAX redondants.

    Cette approche améliore la concision, la maintenabilité et élimine la duplication de code. Les modifications futures (URL, paramètres de requête) requièrent seulement une mise à jour dans la fonction <code>sendTranslationRequest</code>.
