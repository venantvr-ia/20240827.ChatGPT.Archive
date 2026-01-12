## Gérer les cookies dans WordPress

| Tags |
|------|
| `WordPress` `cookies` `PHP` |

WordPress utilise des cookies pour diverses fonctions, notamment l'authentification des utilisateurs et le suivi des sessions. Les développeurs doivent comprendre comment ces cookies fonctionnent pour les gérer efficacement.

### Définir un cookie

Pour définir un cookie en PHP dans WordPress, utilisez la fonction `setcookie()`.

```php
<?php
setcookie("nom_du_cookie", "valeur_du_cookie", time() + (86400 * 30), "/"); // Durée de vie d'un jour
?>
```

*   `nom_du_cookie` : Le nom du cookie.
*   `valeur_du_cookie` : La valeur à stocker dans le cookie.
*   `time() + (86400 * 30)` : Le délai d'expiration du cookie (ici, 30 jours).
*   `/` : Le chemin du cookie (ici, pour tout le site).

### Récupérer un cookie

Pour récupérer la valeur d'un cookie, utilisez la variable superglobale `$_COOKIE`.

```php
<?php
if (isset($_COOKIE["nom_du_cookie"])) {
  $cookie_valeur = $_COOKIE["nom_du_cookie"];
  echo "La valeur du cookie est : " . $cookie_valeur;
}
?>
```

### Supprimer un cookie

Pour supprimer un cookie, utilisez `setcookie()` avec un délai d'expiration dans le passé.

```php
<?php
setcookie("nom_du_cookie", "", time() - 3600, "/");
?>
```

### Considérations importantes

*   **Sécurité :** Utilisez HTTPS pour sécuriser la transmission des cookies.  Protégez les cookies contre les attaques XSS et CSRF.
*   **Confidentialité :** Informez les utilisateurs de l'utilisation des cookies et obtenez leur consentement si nécessaire, conformément aux réglementations sur la confidentialité (par exemple, le RGPD).
*   **Durée de vie :** Définissez des durées de vie de cookies appropriées.
*   **Chemin et domaine :** Spécifiez correctement le chemin et le domaine des cookies pour limiter leur portée.

### Exemple concret

Voici un exemple d'implémentation pour un plugin simple.

```php
<?php
/**
 * Plugin Name: Cookie Example
 * Description: Démonstration de l'utilisation des cookies dans WordPress.
 * Version: 1.0.0
 * Author: [NOM]
 */

// Définir un cookie lors de l'activation du plugin
function cookie_example_plugin_activation() {
  setcookie("cookie_exemple", "Valeur de l'exemple", time() + (86400 * 30), COOKIEPATH, COOKIE_DOMAIN, false, true); // HttpOnly et Secure
}
register_activation_hook( __FILE__, 'cookie_example_plugin_activation' );

// Afficher la valeur du cookie
function cookie_example_display_cookie() {
  if (isset($_COOKIE["cookie_exemple"])) {
    echo "<p>Cookie Example : " . $_COOKIE["cookie_exemple"] . "</p>";
  }
}
add_action('wp_footer', 'cookie_example_display_cookie');

// Supprimer le cookie lors de la désactivation du plugin
function cookie_example_plugin_deactivation() {
  setcookie("cookie_exemple", "", time() - 3600, COOKIEPATH, COOKIE_DOMAIN, false, true);
}
register_deactivation_hook( __FILE__, 'cookie_example_plugin_deactivation' );
?>
```

Ce code définit un cookie lors de l'activation du plugin, affiche sa valeur dans le pied de page et le supprime lors de la désactivation du plugin.  Il utilise également les constantes `COOKIEPATH` et `COOKIE_DOMAIN` de WordPress pour assurer la compatibilité.

**Note :** Toujours valider et nettoyer les données des cookies avant de les utiliser, et utilisez des mesures de sécurité appropriées pour protéger les informations sensibles.


## Contrôle des cookies WordPress selon l'authentification

| Tags |
|------|
| `WordPress` `PHP` `JavaScript` `Cookies` `Authentification` |

Pour implémenter la gestion des cookies en fonction de l'état d'authentification d'un utilisateur sous WordPress, utilisez du code JavaScript en conjonction avec des fonctions PHP.

1.  **Vérification de l'authentification en PHP** : Ajoutez le code suivant à votre fichier `functions.php` :

    ```php
    function is_user_authenticated() {
        if ( is_user_logged_in() ) {
            wp_enqueue_script('your-js-file', 'path/to/your/js/file.js');
            wp_localize_script('your-js-file', 'userAuth', array('authenticated' => true));
        } else {
            wp_enqueue_script('your-js-file', 'path/to/your/js/file.js');
            wp_localize_script('your-js-file', 'userAuth', array('authenticated' => false));
        }
    }
    add_action('wp_enqueue_scripts', 'is_user_authenticated');
    ```

2.  **Gestion des cookies en JavaScript** : Dans votre fichier JavaScript (`your-js-file.js`), intégrez le code suivant :

    ```javascript
    document.addEventListener("DOMContentLoaded", function(){
        // Vérifie si l'utilisateur est authentifié
        if (!userAuth.authenticated) {
            // Votre code pour afficher la pop-up de cookies ici

            // Écouteur pour le bouton 'Accepter'
            document.getElementById("acceptCookies").addEventListener("click", function() {
                // Stocker les cookies
            });

            // Écouteur pour le bouton 'Refuser'
            document.getElementById("refuseCookies").addEventListener("click", function() {
                // Supprimer ou empêcher les cookies
                document.cookie.split(";").forEach(function(c) {
                  document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/");
                });
            });
        }
    });
    ```

    Assurez-vous que les identifiants des boutons correspondent à votre code HTML.

3.  **Intégration avec le plugin** : Il est possible que vous deviez désactiver la gestion des cookies du plugin pour intégrer votre propre logique.

Cette approche permet un contrôle complet sur la gestion des cookies en fonction de l'état d'authentification de l'utilisateur.


## Empêcher la création de cookies en JavaScript

| Tags |
|------|
| `JavaScript` `Cookies` `Gestion des cookies` `Sécurité` |

Pour empêcher la création de cookies, il faut utiliser une variable globale ou un indicateur pour déterminer si l'utilisateur a accepté les cookies. Chaque tentative de création de cookie doit vérifier cet indicateur.

Par exemple :

1.  **JavaScript pour gérer les cookies** :

    ```javascript
    var canSetCookies = true; // Une variable globale

    document.addEventListener("DOMContentLoaded", function(){
        // Vérifie si l'utilisateur est authentifié
        if (!userAuth.authenticated) {
            // Votre code pour afficher la pop-up de cookies ici

            // Écouteur pour le bouton 'Accepter'
            document.getElementById("acceptCookies").addEventListener("click", function() {
                canSetCookies = true;
                // Stocker un cookie pour se rappeler que l'utilisateur a accepté
                document.cookie = "cookiesAccepted=true; path=/";
            });

            // Écouteur pour le bouton 'Refuser'
            document.getElementById("refuseCookies").addEventListener("click", function() {
                canSetCookies = false;
                // Supprimer tous les cookies
                document.cookie.split(";").forEach(function(c) {
                  document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/");
                });
            });
        }
    });
    ```

2.  **Ensuite, chaque fois que vous essayez de créer un cookie** :

    ```javascript
    if (canSetCookies) {
        // Créez le cookie ici
        document.cookie = "yourCookie=value; path=/";
    }
    ```

Ce code exige que chaque script tentant de créer un cookie vérifie la variable `canSetCookies` avant de le faire. Intégrer cette vérification dans une fonction utilitaire pour la création de cookies peut simplifier la gestion.


## Configuration d'un bouton de consentement aux cookies

| Tags |
|------|
| `WordPress` `REST API` `PHP` `JavaScript` |

Pour implémenter cette fonctionnalité dans WordPress, utilisez l'API REST pour créer un endpoint personnalisé qui gère les préférences de l'utilisateur concernant les cookies. Côté serveur, l'identifiant de session détermine si les cookies doivent être envoyés.

1.  **Création d'un endpoint personnalisé dans `functions.php`**:

    ```php
    function set_cookie_preference( $request ) {
        $session_id = $request['session_id'];
        $preference = $request['preference']; // Accepté ou refusé
        // Stocker la préférence dans la session ou la base de données
        // ...
        return new WP_REST_Response("Preference set", 200);
    }

    add_action('rest_api_init', function () {
      register_rest_route('custom', '/set-cookie-preference', [
        'methods' => 'POST',
        'callback' => 'set_cookie_preference',
      ]);
    });
    ```

2.  **JavaScript pour envoyer une requête POST suite au clic sur le bouton**:

    ```javascript
    document.addEventListener("DOMContentLoaded", function(){
        const sessionId = // Obtenez l'identifiant de session (côté serveur ou JS)

        document.getElementById("acceptCookies").addEventListener("click", function() {
            fetch("/wp-json/custom/set-cookie-preference", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ session_id: sessionId, preference: 'accepted' })
            });
        });

        document.getElementById("refuseCookies").addEventListener("click", function() {
            fetch("/wp-json/custom/set-cookie-preference", {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ session_id: sessionId, preference: 'refused' })
            });
        });
    });
    ```

3.  **Gestion des cookies côté serveur dans WordPress selon la préférence de l'utilisateur**:

    Avant de définir un cookie, vérifiez la préférence de l'utilisateur pour cette session.

    ```php
    function maybe_set_cookies() {
        $session_id = // Obtenez l'identifiant de session
        $preference = // Récupérez la préférence de l'utilisateur depuis la session ou la base de données

        if ($preference !== 'refused') {
            // Définissez les cookies
        }
    }

    add_action('init', 'maybe_set_cookies');
    ```

Cette approche envoie une requête POST à un endpoint personnalisé de l'API REST de WordPress suite au clic sur un bouton. Le serveur enregistre la préférence de l'utilisateur via son identifiant de session, et vérifie cette préférence avant de définir des cookies.


## Gestion des cookies avec WordPress

| Tags |
|------|
| `WordPress` `PHP` `cookies` |

WordPress permet de gérer les cookies grâce à la fonction PHP native `setcookie()` et à la superglobale `$_COOKIE`.

### Création d'un cookie

La fonction `setcookie()` est utilisée pour créer un cookie. Il est recommandé d'utiliser les hooks `init` ou `wp_loaded` pour insérer le code avant l'envoi des en-têtes HTTP.

Exemple :

```php
add_action('init', 'my_set_cookie');
function my_set_cookie() {
    if(!is_user_logged_in()) { // Vérifier que l'utilisateur n'est pas authentifié
        setcookie('my_cookie', 'my_value', time() + 3600, COOKIEPATH, COOKIE_DOMAIN);
    }
}
```

### Lecture d'un cookie

Les valeurs des cookies sont accessibles via la superglobale `$_COOKIE`.

Exemple :

```php
$my_cookie_value = $_COOKIE['my_cookie'] ?? 'default_value';
```

### Suppression d'un cookie

Pour supprimer un cookie, `setcookie()` doit être appelé avec une date d'expiration dans le passé.

Exemple :

```php
add_action('init', 'my_remove_cookie');
function my_remove_cookie() {
    if(is_user_logged_in()) { // Seulement pour les utilisateurs authentifiés
        setcookie('my_cookie', '', time() - 3600, COOKIEPATH, COOKIE_DOMAIN);
    }
}
```

`COOKIEPATH` et `COOKIE_DOMAIN` sont des constantes WordPress qui définissent le chemin et le domaine du cookie.
