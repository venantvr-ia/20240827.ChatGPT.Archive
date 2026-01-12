## Création d'une route réseau

| Tags |
|------|
| `réseau` `route` `configuration` `Linux` |

Pour créer une route réseau, utilisez la commande `ip route`.  Voici quelques exemples :

Pour ajouter une route par défaut (gateway) :

```bash
ip route add default via [IP]
```

Pour ajouter une route spécifique :

```bash
ip route add [ADRESSE_RESEAU]/[MASQUE_RESEAU] via [IP]
```

Exemple concret :  ajouter une route vers le réseau 192.168.1.0/24 via la passerelle [IP] :

```bash
ip route add 192.168.1.0/24 via [IP]
```

Pour supprimer une route :

```bash
ip route del [ADRESSE_RESEAU]/[MASQUE_RESEAU]
```

Pour afficher la table de routage :

```bash
ip route show
```

Attention, ces modifications sont généralement non persistantes et perdues au redémarrage.  Pour rendre les routes persistantes, il faut les configurer dans le fichier de configuration réseau approprié, selon votre distribution Linux ([NOM] a des exemples).  Par exemple, sur Debian/Ubuntu, cela peut se faire dans `/etc/network/interfaces`.  Sur CentOS/RHEL, cela se fait dans des fichiers spécifiques dans `/etc/sysconfig/network-scripts/`. Consultez la documentation de votre distribution pour plus de détails.  N'oubliez pas de redémarrer le service réseau après modification, ou d'appliquer la configuration avec la commande appropriée (e.g. `sudo ifdown eth0 && sudo ifup eth0`).  En cas de problème, vérifiez la configuration de votre pare-feu ([NOM]) et assurez-vous de la bonne communication entre les différents éléments du réseau.  Pour le débogage, utilisez des outils comme `tcpdump` et `traceroute`.  Pour plus d'informations, reportez-vous aux manuels (`man ip`, `man route`).  Contactez [NOM] à [EMAIL] en cas de besoin.


## Routage statique entre deux réseaux

| Tags |
|------|
| `réseau` `routage statique` `routeur` `IP` |

Pour créer une route entre deux réseaux distincts, le routage statique peut être utilisé afin d'indiquer à chaque routeur comment atteindre l'autre réseau. Les étapes générales sont les suivantes, bien que les détails puissent varier en fonction du matériel et du logiciel de votre routeur.


## Configuration de routage statique

| Tags |
|------|
| `réseau` `routage` `routeur` `IP` |

1.  Accédez à l'interface de configuration Web du routeur.
2.  Localisez la section de routage statique (exemple : "Paramètres avancés").
3.  Créez une nouvelle route statique :
    *   Réseau de destination : 192.168.3.0
    *   Masque de sous-réseau : 255.255.255.0 (ou /24)
    *   Passerelle : [IP] (exemple : 192.168.3.1)


## Configuration de la route statique sur 192.168.3.1

| Tags |
|------|
| `Routage statique` `Réseau` `Configuration` `Sécurité réseau` |

1.  Accéder à l'interface de configuration Web du routeur.
2.  Naviguer vers la section de routage statique.
3.  Ajouter une nouvelle route statique avec les paramètres suivants :

    *   Réseau de destination : 192.168.1.0
    *   Masque de sous-réseau : 255.255.255.0 (ou /24)
    *   Passerelle : Adresse IP du routeur du réseau 192.168.1.0/24 (par exemple, 192.168.1.1)

Une fois ces configurations terminées, la communication entre les deux réseaux devrait être possible.

Cette opération est couramment utilisée en pentesting et en sécurité réseau, particulièrement lors de projets nécessitant une séparation des réseaux tout en autorisant des communications spécifiques.

Pour approfondir vos connaissances, consultez des ouvrages tels que « Computer Networking: A Top-Down Approach » de James Kurose et Keith Ross.


## Exécution de commandes en ligne de commande

| Tags |
|------|
| `Ligne de commande` `Routage statique` `Système d'exploitation` |

En ligne de commande, diverses commandes permettent de configurer le routage statique, en fonction du système d'exploitation ou de l'équipement utilisé. Voici quelques exemples :


## Ajout de routes statiques sur Linux/Unix

| Tags |
|------|
| `Linux` `Unix` `réseau` `route` `route statique` |

Pour ajouter une route statique temporaire :

```bash
sudo route add -net 192.168.3.0 netmask 255.255.255.0 gw 192.168.1.1
```

Pour les routes permanentes, utiliser un script de démarrage ou modifier les fichiers de configuration, tels que <code>/etc/network/interfaces</code> ou <code>/etc/sysconfig/network-scripts/route-ethX</code>.


## Configuration d'une route statique Cisco

| Tags |
|------|
| `Cisco` `Routage` `Configuration` `Route statique` |

En mode de configuration (<code>config terminal</code>), la commande suivante peut être utilisée :

```bash
ip route 192.168.3.0 255.255.255.0 192.168.1.1
```


## Ajout d'une route statique sur Windows

| Tags |
|------|
| `Windows` `Routage` `Réseau` |

Pour ajouter une route statique :

```cmd
route add 192.168.3.0 mask 255.255.255.0 192.168.1.1
```

Cette commande crée une route statique. Elle indique que le trafic destiné au réseau `192.168.3.0/24` doit être acheminé via la passerelle `192.168.1.1`.

La compréhension du routage est essentielle, notamment pour la segmentation du réseau et la sécurité des données, en accord avec les normes comme ISO 27001.

Pour une étude approfondie de l'administration réseau, le livre "TCP/IP Network Administration" de Craig Hunt est recommandé.


## Installer la commande 'route' sous Ubuntu

| Tags |
|------|
| `Ubuntu` `route` `ip` `net-tools` `réseau` |

La commande `route` est obsolète et a été remplacée par `ip` sur les systèmes Linux modernes, comme Ubuntu. Pour installer `route` :

```bash
sudo apt update
sudo apt install net-tools
```

Après installation, la commande `route` est disponible.

Il est recommandé d'utiliser la commande `ip` pour la gestion des routes, car elle est plus complète et standard. Exemple d'ajout d'une route :

```bash
sudo ip route add 192.168.3.0/24 via 192.168.1.1
```

La maîtrise de ces outils est cruciale, en particulier pour les activités de pentesting. Ils sont des compétences fondamentales en manipulation de réseau, utiles pour les audits de sécurité et la conformité aux normes comme ISO 27001.

Pour plus d'informations sur le routage sous Linux, le livre "Linux IP Stacks Commentary: Guide to Gaining Network Control" de Nicholas Wells est une excellente ressource.


## Ajouter une route sous Android

| Tags |
|------|
| `Android` `réseau` `routing` `ip` `root` |

Sous Android, l'ajout d'une route statique requiert généralement un accès root, car les commandes de modification du routage nécessitent des privilèges administratifs. Voici comment ajouter une route si votre appareil Android est rooté :

1.  **Ouvrez un terminal** sur votre appareil Android. Une application de terminal peut être téléchargée depuis le Google Play Store.

2.  **Accédez aux droits super-utilisateur** en entrant la commande `su`.

3.  **Ajoutez la route** en utilisant la commande `ip`. Par exemple, pour ajouter une route vers le réseau 192.168.3.0/24 via la passerelle 192.168.1.1, utilisez la commande suivante :

    ```bash
    ip route add 192.168.3.0/24 via 192.168.1.1 dev [interface]
    ```

    Remplacez `[interface]` par l'interface réseau à utiliser, comme `wlan0` pour le Wi-Fi.

Ces modifications seront perdues après un redémarrage de l'appareil. Pour les rendre permanentes, créez un script de démarrage qui exécute ces commandes à chaque démarrage.

L'ajout de routes sur les appareils mobiles est rarement recommandé en dehors des tests ou configurations spécifiques, en particulier en raison des exigences de sécurité liées aux normes telles que ISO 27001 ou GDPR. Comprenez les implications en matière de sécurité avant de procéder.

Pour approfondir les compétences en sécurité mobile, consultez le livre "Android Hacker's Handbook" de Joshua J. Drake et al.


## Alternatives à l'ajout de routes statiques sur Android

| Tags |
|------|
| `Android` `Réseau` `VPN` `Routage` |

Sans accès root sur Android, voici des alternatives pour configurer le routage :

1.  **VPN**: Utiliser un service VPN permettant de définir des routes statiques pour diriger le trafic via une passerelle spécifique.
2.  **Applications de routage spécifiques**: Certaines applications tierces prétendent offrir des fonctionnalités de routage sans root, bien que leur efficacité puisse être limitée.
3.  **Configuration réseau avancée**: Certains réseaux Wi-Fi d'entreprise offrent des options pour définir des routes statiques via des configurations de profil réseau avancées. Cela dépend du matériel et des logiciels réseau.
4.  **Proxy**: Utiliser un proxy sur votre réseau pour rediriger le trafic. Cela nécessite une configuration côté serveur.
5.  **Réglages du routeur**: Configurer le routage directement sur le routeur pour rediriger le trafic en fonction des besoins, affectant tous les appareils connectés au réseau.

Soyez prudent lors de la manipulation des routes ou de l'utilisation de VPN, en particulier dans les domaines soumis à des réglementations strictes telles que la GDPR ou ISO 27001. Ces actions peuvent avoir des implications en matière de sécurité des données et de conformité.

Pour plus d'informations, consultez des documents spécialisés sur la sécurité des réseaux mobiles. "Mobile Device Security: A Comprehensive Guide to Securing Your Information in a Moving World" par [NOM] est un point de départ.
