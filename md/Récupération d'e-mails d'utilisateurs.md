## Récupération des adresses e-mail des utilisateurs

| Tags |
|------|
| `e-mail` `récupération` `sécurité` |


## Récupération des emails depuis une requête

| Tags |
|------|
| `PHP` `WordPress` `get_users` `emails` |

Pour extraire les adresses e-mail des utilisateurs à partir du résultat de la fonction `get_users()`, vous pouvez itérer sur le tableau d'objets utilisateurs et récupérer la propriété `user_email` de chaque utilisateur. Voici comment procéder :

```php
<?php
$users = get_users(['role' => ConcilioRoles::MANAGER]);
$emails = [];

foreach ($users as $user) {
    $emails[] = $user->user_email;
}

// $emails maintenant contient un tableau d'adresses e-mail
?>
```

Dans cet exemple :

1.  `$users = get_users(['role' => ConcilioRoles::MANAGER]);` : Récupère les utilisateurs avec le rôle spécifié.
2.  `$emails = [];` : Initialise un tableau pour stocker les adresses e-mail.
3.  La boucle `foreach` itère sur chaque objet utilisateur dans `$users`.
4.  `$emails[] = $user->user_email;` : Ajoute l'adresse e-mail de l'utilisateur actuel au tableau `$emails`.

Le tableau `$emails` contient désormais une liste des adresses e-mail des utilisateurs correspondants.


## Extraction des emails d'utilisateurs PHP

| Tags |
|------|
| `PHP` `array` `email` `get_users` |

Pour extraire les adresses e-mail des utilisateurs à partir de la fonction `get_users()`, il faut itérer à travers le tableau résultant et récupérer les adresses. Le code suivant suppose PHP et que chaque élément du tableau `$users` représente un utilisateur avec un attribut email.

Exemple si chaque utilisateur est un objet :

```php
$emails = [];
foreach ($users as $user) {
    if (isset($user->email)) { // Vérifie l'existence de l'email
        $emails[] = $user->email;
    }
}
```

Exemple si chaque utilisateur est un tableau associatif :

```php
$emails = [];
foreach ($users as $user) {
    if (isset($user['email'])) { // Vérifie l'existence de l'email
        $emails[] = $user['email'];
    }
}
```

Dans les deux cas, `$emails` contient un tableau des adresses e-mail des utilisateurs. Il est crucial de vérifier si l'e-mail est défini en utilisant `isset()` pour éviter les erreurs.


## Récupération des emails des utilisateurs WordPress par rôle

| Tags |
|------|
| `WordPress` `PHP` `WP_User_Query` `WP_User` `Rôle utilisateur` |

Dans WordPress, l'objet <code>WP_User</code> gère les données utilisateurs. La classe <code>WP_User_Query</code> permet de requêter les utilisateurs en fonction de divers critères, y compris leur rôle.

Pour récupérer les emails des utilisateurs ayant le rôle 'manager', créez une requête <code>WP_User_Query</code> avec le rôle approprié, puis itérez sur les résultats pour extraire l'adresse email de chaque utilisateur.

Exemple de code PHP :

```php
// Requête pour les utilisateurs avec le rôle 'manager'
$user_query = new WP_User_Query(array(
    'role' => 'Manager', // Vérifier l'exactitude du nom du rôle
));

// Vérification de l'existence d'utilisateurs
if (!empty($user_query->get_results())) {
    $emails = array();

    // Itération sur chaque utilisateur et extraction de l'email
    foreach ($user_query->get_results() as $user) {
        $emails[] = $user->user_email;
    }

    // $emails contient maintenant les adresses email des utilisateurs 'manager'
} else {
    echo 'Aucun utilisateur trouvé avec le rôle spécifié.';
}
```

Ce code utilise <code>WP_User_Query</code> pour obtenir les utilisateurs avec le rôle 'Manager'.  La méthode <code>get_results()</code> retourne les utilisateurs trouvés. L'email de chaque utilisateur est accessible via la propriété <code>user_email</code> de l'objet <code>WP_User</code>.

Assurez-vous que le rôle spécifié dans la requête (<code>'role' => 'Manager'</code>) correspond exactement au rôle défini dans votre installation WordPress. Les noms de rôle sont sensibles à la casse.


## Lister les rôles WordPress avec une requête SQL

| Tags |
|------|
| `WordPress` `SQL` `Base de données` `Rôles` |

Pour lister les rôles d'utilisateur dans WordPress en utilisant une requête SQL, interrogez la table `wp_options` de votre base de données WordPress. WordPress stocke les rôles d'utilisateur dans cette table sous la clé `wp_user_roles`. Voici les étapes et la requête SQL nécessaire :

1.  Connectez-vous à votre base de données WordPress, via phpMyAdmin, un client MySQL, ou tout autre outil de gestion de base de données.

2.  Exécutez la requête SQL suivante :

    ```sql
    SELECT option_value FROM wp_options WHERE option_name = 'wp_user_roles';
    ```

    Remplacez `wp_` par le préfixe de table réel si vous utilisez un préfixe différent pour vos tables WordPress.

3.  Le résultat de cette requête est une chaîne de caractères sérialisée représentant un tableau associatif des rôles et de leurs capacités.

4.  Désérialisez cette chaîne pour la lire. En PHP, utilisez la fonction `unserialize()`. Exemple de code :

    ```php
    $roles_serialized = '...'; // Remplacez ceci par la chaîne obtenue de la requête SQL
    $roles = unserialize($roles_serialized);
    print_r($roles); // Affiche la liste des rôles et leurs capacités
    ```

L'interaction directe avec la base de données WordPress pour des tâches comme celle-ci est généralement déconseillée, en raison de problèmes potentiels de compatibilité et de changements futurs dans WordPress. Utilisez de préférence les fonctions API de WordPress. Cependant, pour des requêtes SQL spécifiques et des manipulations de données directes, la méthode décrite ci-dessus fonctionne.
