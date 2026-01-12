## Gestion des paquets avec apt

| Tags |
|------|
| `apt` `debian` `ubuntu` `paquets` `gestion` |

L'outil `apt` (Advanced Package Tool) est un gestionnaire de paquets utilisé par les distributions Debian et Ubuntu. Il simplifie l'installation, la mise à jour et la suppression de logiciels.

**Mise à jour de la liste des paquets :**

Avant d'installer ou de mettre à jour des paquets, il est nécessaire de rafraîchir la liste des paquets disponibles.

```bash
sudo apt update
```

**Installation d'un paquet :**

Pour installer un paquet, utilisez la commande suivante :

```bash
sudo apt install <nom_du_paquet>
```

Par exemple, pour installer le paquet `nano` :

```bash
sudo apt install nano
```

**Recherche d'un paquet :**

Pour rechercher un paquet spécifique, utilisez la commande `apt search`.

```bash
apt search <terme_de_recherche>
```

**Mise à jour des paquets installés :**

Pour mettre à jour tous les paquets installés, utilisez la commande :

```bash
sudo apt upgrade
```

Pour mettre à jour une version spécifique d'un paquet :

```bash
sudo apt install --only-upgrade <nom_du_paquet>
```

**Suppression d'un paquet :**

Pour supprimer un paquet, utilisez la commande :

```bash
sudo apt remove <nom_du_paquet>
```

Pour supprimer un paquet et ses fichiers de configuration, utilisez :

```bash
sudo apt purge <nom_du_paquet>
```


## Fonction apt\_get en Ruby

| Tags |
|------|
| `Ruby` `apt-get` `Open3` `Gestion de paquets` |

```ruby
def apt_get(action)
  cmd = ['apt-get', action]
  cmd << '-y' if ['upgrade', 'dist-upgrade', 'autoremove'].include?(action)
  stdout, stderr, status = Open3.capture3(*cmd)
  raise Puppet::Error, stderr if status != 0
  { status: stdout.strip }
end
```


```markdown
## Fonction Ruby apt_get pour la gestion des paquets

| Tags |
|------|
| `Ruby` `apt-get` `gestion de paquets` `Debian` |

Ce code définit une fonction `apt_get` en Ruby. Elle accepte une action (chaîne de caractères) pour la gestion des paquets sur un système basé sur Debian (ex: Ubuntu). La fonction utilise la commande `apt-get` pour effectuer différentes actions telles que la mise à jour, la mise à niveau de la distribution, ou la suppression des paquets inutilisés.

Description des étapes :

1.  La fonction construit une commande `cmd` basée sur l'action fournie. Elle commence par `'apt-get'` et ajoute l'action spécifiée.
2.  Si l'action est `'upgrade'`, `'dist-upgrade'`, ou `'autoremove'`, elle ajoute l'option `-y` à la commande. Cette option exécute la commande sans confirmation.
3.  La méthode `Open3.capture3` exécute la commande et capture la sortie standard (`stdout`), la sortie d'erreur standard (`stderr`), et le statut de la commande.
4.  Si le statut n'est pas 0 (erreur), une exception `Puppet::Error` est levée avec le message d'erreur de `stderr`.
5.  En cas de succès, la fonction retourne un dictionnaire contenant le statut, qui est la sortie standard sans espaces en début et fin de chaîne.

Note : Ce code nécessite les bibliothèques appropriées (ex: Open3) et les permissions pour exécuter `apt-get`.
```

## Gestion des erreurs sans exceptions

| Tags |
|------|
| `Ruby` `exceptions` `error handling` |

Dans l'exemple suivant, la gestion des erreurs est assurée sans lever d'exceptions. La fonction retourne une structure de données contenant l'état de l'opération et un message descriptif.

```ruby
def apt_get(action)
  cmd = ['apt-get', action]
  cmd << '-y' if ['upgrade', 'dist-upgrade', 'autoremove'].include?(action)
  stdout, stderr, status = Open3.capture3(*cmd)
  if status != 0
    { status: 'error', message: stderr.strip }
  else
    { status: 'success', message: stdout.strip }
  end
end
```

La fonction `apt_get` exécute une commande `apt-get`. Si le statut de la commande est différent de 0, indiquant une erreur, la fonction retourne un hash avec le statut `'error'` et le message d'erreur extrait de `stderr`. En cas de succès, elle retourne un hash avec le statut `'success'` et la sortie standard de `stdout`.
