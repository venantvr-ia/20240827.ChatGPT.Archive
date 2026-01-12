## Masques de sous-réseau IP

| Tags |
|------|
| `IP` `réseau` `sous-réseau` `masque` |

Un masque de sous-réseau est une adresse IP de 32 bits utilisée pour distinguer l'adresse réseau et l'adresse de l'hôte au sein d'une adresse IP. Il "masque" une partie de l'adresse IP, permettant d'identifier la partie réseau et la partie hôte.

Les masques de sous-réseau sont généralement écrits en notation décimale pointée, comme les adresses IP.

**Fonctionnement**

Le masque de sous-réseau utilise une série de 1 et de 0 pour identifier la partie réseau et la partie hôte de l'adresse IP. Les 1 indiquent la partie réseau, tandis que les 0 indiquent la partie hôte.

Par exemple, le masque de sous-réseau 255.255.255.0 :

*   **255.255.255.0** en binaire est **11111111.11111111.11111111.00000000**.
*   Ce masque divise l'adresse IP en une partie réseau (les 24 premiers bits) et une partie hôte (les 8 derniers bits).

**Exemple**

Considérons l'adresse IP [IP] et le masque de sous-réseau 255.255.255.0 :

*   Adresse IP : [IP] (en binaire : [BINAIRE IP])
*   Masque de sous-réseau : 255.255.255.0 (en binaire : 11111111.11111111.11111111.00000000)

En effectuant une opération ET logique entre l'adresse IP et le masque de sous-réseau, on obtient l'adresse réseau :

```
[BINAIRE IP]
ET 11111111.11111111.11111111.00000000
-----------------------------------------
[ADRESSE RESEAU BINAIRE]  (correspondant à l'adresse réseau)
```

**Classes d'adresses IP (Historique)**

Dans le passé, les adresses IP étaient classées en classes (A, B, C, D et E). Chaque classe avait un masque de sous-réseau par défaut :

*   **Classe A :** 255.0.0.0
*   **Classe B :** 255.255.0.0
*   **Classe C :** 255.255.255.0

Les classes d'adresses IP sont désormais obsolètes. Le CIDR (Classless Inter-Domain Routing) est utilisé pour la gestion moderne des adresses IP.

**CIDR (Classless Inter-Domain Routing)**

CIDR permet de diviser un réseau en sous-réseaux de taille variable. Il utilise la notation CIDR, qui indique le nombre de bits utilisés pour la partie réseau de l'adresse IP.

Par exemple :

*   192.168.1.0/24 : L'adresse IP est 192.168.1.0 et le masque de sous-réseau est /24 (255.255.255.0).
*   192.168.1.0/16 : L'adresse IP est 192.168.1.0 et le masque de sous-réseau est /16 (255.255.0.0).

**Calcul du nombre d'hôtes**

Le nombre d'hôtes disponibles dans un sous-réseau se calcule comme suit :

`2^(nombre de bits hôtes) - 2`

*   Le -2 représente l'adresse réseau et l'adresse de diffusion (broadcast), qui ne peuvent pas être attribuées à des hôtes.

**Exemples**

*   /24 (255.255.255.0) : 8 bits pour l'hôte -> 2^8 - 2 = 254 hôtes
*   /16 (255.255.0.0) : 16 bits pour l'hôte -> 2^16 - 2 = 65 534 hôtes


## Masque de sous-réseau pour l'adresse IP 192.168.0.0

| Tags |
|------|
| `IP` `subnet mask` `network` |

The subnet mask for the IP address 192.168.0.0 is contingent on the network class and subnet division. IP addresses commencing with 192.168 generally denote Class C addresses, with a default subnet mask of 255.255.255.0. This mask accommodates 256 addresses within the subnet, with 254 available for host assignment (the first address represents the network, and the last is reserved for broadcast).

However, the subnet mask can vary if subnetting is employed. This technique is often used for efficient IP address range utilization within an organization or for segmenting networks for security or performance gains.

For instance, to divide the network into smaller subnets, masks such as 255.255.255.192 or 255.255.255.128 may be used. These masks reduce the number of hosts per subnet but increase the number of individual subnets.

Subnetting knowledge is crucial in ethical hacking, network engineering, and cybersecurity, as it influences network structure and security. In ethical hacking, subnetting comprehension aids in network mapping and vulnerability identification.


## Comparaison des masques réseau /24 et /32

| Tags |
|------|
| `réseau` `subnet mask` `adressage IP` |

Pour l'adresse IP [IP], les masques de sous-réseau /24 et /32 peuvent être utilisés, mais ils ont des objectifs différents :

1.  **/24 (255.255.255.0)** : C'est le masque de sous-réseau le plus courant pour un réseau de classe C tel que [IP]. Il prend en charge jusqu'à 256 adresses IP.
