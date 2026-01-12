## Capturer les sondes WiFi avec Python

| Tags |
|------|
| `Python` `WiFi` `Réseau` `Sécurité` |

Le script Python suivant utilise la bibliothèque scapy pour capturer les trames de sonde WiFi. Il affiche les adresses MAC sources détectées.

```python
#!/usr/bin/env python
import scapy.all as scapy
import argparse

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface réseau à utiliser")
    options = parser.parse_args()
    if not options.interface:
        parser.error("[-] Veuillez spécifier une interface, utilisez --help pour plus d'informations.")
    return options

def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(scapy.Dot11ProbeReq):
        try:
            mac_address = packet.addr2
            print("[+] Adresse MAC de la sonde : " + mac_address)
        except:
            pass

options = get_arguments()
sniff(options.interface)
```

Pour utiliser ce script :

1.  **Enregistrez le script :** Sauvegardez le code dans un fichier, par exemple `wifi_probe_sniffer.py`.
2.  **Exécutez le script avec l'interface réseau :** Remplacez `wlan0` par le nom de votre interface WiFi.

    ```bash
    sudo python wifi_probe_sniffer.py -i wlan0
    ```

**Important :**

*   L'utilisation de ce script à des fins malveillantes est illégale. Il est conçu à des fins d'apprentissage et de recherche.
*   Assurez-vous d'avoir installé scapy (`pip install scapy`).
*   L'exécution de ce script nécessite des privilèges root (sudo).
*   L'adresse IP de l'utilisateur est : [IP].
*   L'adresse email de l'utilisateur est : [EMAIL].
*   Le nom de l'utilisateur est : [NOM].


## Manipuler Aircrack-ng avec Python

| Tags |
|------|
| `Aircrack-ng` `Python` `subprocess` `airodump-ng` `réseau sans fil` |

Aircrack-ng est un ensemble d'outils pour l'analyse de sécurité des réseaux sans fil. L'interaction avec Aircrack-ng depuis Python est possible via le module <code>subprocess</code>. Cela permet d'automatiser des tâches, telles que la capture de paquets WiFi.

L'exemple suivant illustre l'utilisation de <code>airodump-ng</code>, un composant d'Aircrack-ng, pour capturer du trafic réseau :

```python
import subprocess

# Remplacer 'interface' par le nom de votre interface sans fil en mode moniteur
interface = "mon0"

# Commencer la capture avec airodump-ng
try:
    subprocess.run(["airodump-ng", interface], check=True)
except subprocess.CalledProcessError as e:
    print(f"Une erreur s'est produite: {e}")
```

Prérequis pour l'exécution du script :

1.  Aircrack-ng doit être installé.
2.  Des droits d'exécution suffisants (généralement superutilisateur) sont requis.
3.  L'interface sans fil doit être en mode moniteur (configuration possible via <code>airmon-ng</code>).

Avertissement : L'interception de trafic réseau sans autorisation peut être illégale. Conformez-vous aux lois et réglementations en vigueur, notamment le GDPR, et respectez la confidentialité des données.

Pour des tâches plus complexes (analyse des données capturées), envisagez l'écriture de scripts Python qui traitent les fichiers de sortie d'<code>airodump-ng</code> ou l'utilisation de bibliothèques Python spécialisées dans la manipulation des réseaux sans fil.

Pour approfondir, consultez la documentation d'Aircrack-ng, familiarisez-vous avec les options de ligne de commande et explorez l'utilisation du module <code>subprocess</code> pour l'automatisation.


## Utiliser Scapy comme alternative à Aircrack-ng

| Tags |
|------|
| `Scapy` `Python` `Réseau` `WiFi` `Capture de paquets` |

Pour interagir avec Aircrack-ng en Python, une alternative à l'utilisation de la librairie <code>subprocess</code> est d'employer <code>Scapy</code>. Cette librairie Python est conçue pour la manipulation de paquets réseau, offrant des fonctionnalités pour la capture et l'analyse des paquets WiFi, tels que les sondes.

Scapy permet de générer, modifier, envoyer et intercepter des paquets réseau à travers une interface Python simplifiée. Un exemple basique d'utilisation pour capturer des sondes WiFi est présenté ci-dessous :

```python
from scapy.all import *

# Fonction pour afficher le résumé de chaque paquet
def packet_handler(pkt):
    if pkt.haslayer(Dot11ProbeReq):  # Filtrer les paquets qui sont des Probe Requests
        print(pkt.summary())

# Démarrez la capture sur l'interface spécifique
sniff(iface="wlan0mon", prn=packet_handler, store=False)
```

Dans ce script :

*   Remplacez `"wlan0mon"` par le nom de votre interface sans fil en mode moniteur.
*   `Dot11ProbeReq` représente la classe Scapy pour les requêtes de sonde (Probe Requests). Ce filtre peut être adapté pour capturer d'autres types de paquets.
*   La fonction `sniff` de Scapy permet de capturer les paquets. L'argument `prn` spécifie une fonction de rappel qui s'exécute pour chaque paquet capturé, tandis que `store=False` empêche Scapy de stocker les paquets en mémoire.

Conditions d'utilisation de Scapy :

*   Exécution du script en tant que superutilisateur (root).
*   Installation de Scapy (<code>pip install scapy</code>).
*   Configuration de la carte sans fil en mode moniteur (via <code>airmon-ng</code> ou un autre outil).

L'avantage de Scapy réside dans son interface de programmation riche et flexible, supérieure à l'exécution de commandes terminal via <code>subprocess</code>. Avec Scapy, l'analyse approfondie des paquets, la création de statistiques et le développement d'outils de sécurité personnalisés sont possibles.

Il est impératif de respecter les réglementations locales concernant la capture de trafic réseau et d'obtenir les autorisations nécessaires lorsque vous travaillez sur des réseaux qui ne vous appartiennent pas.


## Sortie du code Python

| Tags |
|------|
| `Python` `fonction` `addition` |

```python
def addition(a, b):
    return a + b

print(addition(3, 4))
```


## Sortie du script Scapy et résumé des paquets

| Tags |
|------|
| `Scapy` `Probe Request` `Réseau` |

Le script Scapy fourni n'affiche pas de sortie formatée au sens traditionnel. Il affiche plutôt un résumé de chaque paquet de demande de sonde (Probe Request) capturé sur l'interface réseau spécifiée.

Lorsqu'un paquet de demande de sonde est détecté, la fonction `packet_handler` est appelée, et `pkt.summary()` est exécuté, affichant un résumé du paquet.  Ce résumé peut se présenter comme suit :

```
RadioTap / 802.11 Probe Request 1L <SSID=YourSSID> / Dot11ProbeReq <SSID=YourSSID>
```

Ce résumé indique qu'il s'agit d'un paquet de demande de sonde et affiche des informations comme l'identifiant de l'ensemble de services (SSID) recherché par la station.

Le comportement et la sortie du script dépendent de l'environnement d'exécution et des paquets capturés. Il fournit des informations de base pour chaque demande de sonde détectée par la carte réseau en mode moniteur.


## Détails des Probe Requests avec Scapy

| Tags |
|------|
| `Scapy` `Probe Request` `Python` `WiFi` `Réseau` |

Pour obtenir plus de détails sur les Probe Requests capturés avec Scapy, la fonction `packet_handler` peut être étendue pour extraire et afficher des informations supplémentaires. Les Probe Requests contiennent des informations telles que l'adresse MAC de l'émetteur, le SSID recherché et d'autres paramètres.

Voici une version modifiée de la fonction `packet_handler` qui affiche des détails supplémentaires pour chaque Probe Request :

```python
from scapy.all import *

def packet_handler(pkt):
    if pkt.haslayer(Dot11ProbeReq):
        # Obtenir l'adresse MAC de l'émetteur
        mac_address = pkt.addr2
        # Obtenir le nom du SSID
        ssid = pkt.info.decode('utf-8')
        # Obtenir la force du signal, si présente
        signal_strength = pkt.getlayer(RadioTap).dBm_AntSignal

        print(f"Probe Request Captured:")
        print(f"MAC Address: {mac_address}")
        print(f"SSID: {ssid}")
        print(f"Signal Strength: {signal_strength} dBm")
        print("-" * 30)  # Séparation visuelle des paquets

# Démarrer la capture sur l'interface spécifique
sniff(iface="wlan0mon", prn=packet_handler, store=False)
```

En exécutant ce script, pour chaque Probe Request détecté, les informations suivantes seront affichées :

*   **MAC Address:** L'adresse MAC de la station émettrice.
*   **SSID:** Le SSID recherché par la station, qui peut être vide pour les requêtes "wildcard".
*   **Signal Strength:** La force du signal du paquet en dBm.

Il est important de noter que la capture de la force du signal (RSSI) dépend de la prise en charge par la carte réseau.

Pour que ce script fonctionne, Scapy doit être installé et l'interface réseau doit être configurée en mode moniteur. De plus, le script doit être exécuté avec des privilèges suffisants (généralement en tant que superutilisateur) pour capturer les paquets réseau.
