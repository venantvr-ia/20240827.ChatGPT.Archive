## Docker pour le Pivotement Réseaux

| Tags |
|------|
| `Docker` `Réseau` `Sécurité` `Pivotement` |

Le pivotement réseau est une technique utilisée pour accéder à des ressources internes d'un réseau compromis. Docker peut être utilisé pour faciliter et améliorer ce processus. Cette section explore l'utilisation de Docker pour le pivotement réseau.

### Configuration de l'environnement Docker

Pour commencer, assurez-vous que Docker est installé et configuré correctement.

1.  **Installation de Docker :** Suivez les instructions d'installation de Docker pour votre système d'exploitation.

2.  **Vérification de l'installation :** Exécutez la commande suivante pour vérifier que Docker est correctement installé :

    ```bash
    docker --version
    ```

### Création d'une image Docker

Créez une image Docker qui inclut les outils nécessaires au pivotement réseau. Un exemple de Dockerfile pourrait ressembler à ceci :

```dockerfile
FROM ubuntu:latest
RUN apt-get update && apt-get install -y --no-install-recommends \
    netcat \
    openssh-client \
    proxychains \
    && rm -rf /var/lib/apt/lists/*
```

Construisez l'image :

```bash
docker build -t pivot-tools .
```

### Exécution du conteneur Docker

Exécutez le conteneur Docker avec les outils nécessaires.  Voici comment exécuter le conteneur et configurer le réseau :

```bash
docker run -it --rm --network host pivot-tools
```

L'option `--network host` permet au conteneur d'utiliser le réseau de l'hôte, ce qui est souvent nécessaire pour le pivotement réseau.

### Utilisation des outils de pivotement

Une fois dans le conteneur, vous pouvez utiliser les outils installés pour le pivotement réseau.  Par exemple, pour utiliser `netcat` pour établir une connexion :

```bash
nc [IP] [PORT]
```

Ou, pour utiliser `ssh` :

```bash
ssh [UTILISATEUR]@[IP]
```

### Configuration de Proxychains

Pour utiliser Proxychains, modifiez le fichier `/etc/proxychains.conf` dans le conteneur et configurez les proxies.  Voici un exemple de configuration :

```
strict_chain
proxy_dns
tcp_connect_timeout 5000
[proxy_list]
socks4  127.0.0.1 1080
```

Ensuite, vous pouvez utiliser Proxychains pour acheminer le trafic à travers les proxies.  Par exemple :

```bash
proxychains ssh [UTILISATEUR]@[IP]
```

### Exemples de pivotement réseau

1.  **Pivotement SSH :** Si vous avez accès à un serveur via SSH, vous pouvez l'utiliser comme point de pivot pour accéder à d'autres ressources sur le réseau interne.

2.  **Pivotement SOCKS :** Configurez un serveur SOCKS sur le serveur compromis et utilisez-le pour acheminer le trafic vers les ressources internes.

### Sécurité

*   **Gestion des accès :** Limitez l'accès au conteneur Docker uniquement aux utilisateurs autorisés.
*   **Mises à jour :** Mettez régulièrement à jour l'image Docker avec les dernières correctifs de sécurité.
*   **Surveillance :** Surveillez l'activité du conteneur et du réseau pour détecter toute activité suspecte.

### Conclusion

Docker offre un environnement flexible et reproductible pour le pivotement réseau. En utilisant Docker, vous pouvez facilement déployer et gérer les outils nécessaires pour le pivotement réseau tout en assurant un certain niveau d'isolation et de reproductibilité.


## Solution Docker pour le pivotement réseau

| Tags |
|------|
| `Docker` `PivotSuite` `Pentesting` `Réseau` |

Pour simuler le pivotement réseau en tests d'intrusion, l'outil Docker PivotSuite est une solution portable. Elle permet l'exposition de sous-réseaux internes et l'exécution d'attaques de type man-in-the-middle.

Pour l'installer et l'exécuter avec Docker :

1.  Cloner le dépôt GitHub :

    ```bash
    git clone https://github.com/RedTeamOperations/PivotSuite.git
    ```

2.  Accéder au répertoire :

    ```bash
    cd PivotSuite
    ```

3.  Construire l'image Docker :

    ```bash
    docker build -t pivotsuite .
    ```

4.  Exécuter le conteneur Docker :

    ```bash
    docker run -it pivotsuite
    ```

Cette configuration permet de tester les techniques de pivotement réseau dans un environnement isolé. Elle est utile pour évaluer les défenses de réseau, en accord avec les normes ISO 27001 et GDPR.

La documentation complète de PivotSuite est disponible sur le dépôt GitHub. Ces pratiques sont importantes pour la compréhension des vulnérabilités et des meilleures pratiques en pentesting.


## Metasploit avec Docker : Exemple de pivot

| Tags |
|------|
| `Metasploit` `Docker` `Pivot` `Pentesting` `Sécurité` |

Bien sûr, une autre approche possible est d'utiliser Metasploit avec un conteneur Docker. Metasploit, un framework de tests d'intrusion largement reconnu, supporte diverses techniques de pivotement. L'exécution dans un conteneur Docker facilite et accélère le déploiement.

Voici les étapes pour installer Metasploit dans Docker :

1.  Cloner le dépôt GitHub Metasploit :

    ```bash
    git clone https://github.com/rapid7/metasploit-framework.git
    ```

2.  Naviguer vers le répertoire :

    ```bash
    cd metasploit-framework
    ```

3.  Construire l'image Docker :

    ```bash
    docker build -t metasploit .
    ```

4.  Exécuter le conteneur Docker :

    ```bash
    docker run -it metasploit
    ```

Après le lancement de Metasploit, utilisez des modules spécifiques pour les tests de pivotement réseau, comme <code>route</code>, <code>post/multi/manage/shell_to_meterpreter</code>, et d'autres.

Cela constitue une ressource pertinente pour la formation en éthique hacking et en ingénierie de la sécurité, permettant de simuler des attaques dans un environnement contrôlé.  L'intégration de cette méthode dans les services de pentesting permet de tester des scénarios de pivotement sur les réseaux clients, offrant ainsi une valeur ajoutée.

La documentation de Metasploit fournit des informations détaillées et des exemples d'utilisation.


## Configuration d'une solution de pentesting

| Tags |
|------|
| `Docker` `Docker Compose` `Pentesting` `Metasploit` `Pivot` `Sécurité` |

Si vous recherchez une solution plus complète impliquant plusieurs conteneurs Docker et des réseaux vulnérables pour pratiquer le pivotement, vous pouvez essayer "Docker Pwnbox". Cette solution peut inclure plusieurs machines vulnérables (comme Metasploitable, WebGoat, etc.) et des outils de pentesting (comme Metasploit, Burp Suite, etc.) dans un environnement Docker.

Voici comment configurer une telle plateforme :

<ol>
<li>
<strong>Docker Compose</strong>: Créez un fichier <code>docker-compose.yml</code> qui détaille toutes les machines vulnérables et les outils de pentest que vous souhaitez inclure.
<pre><code class="language-yaml">version: &#x27;3&#x27;
services:
  metasploitable:
    image: tleemcjr/metasploitable2
    networks: 
      - vulnerable_network
  webgoat:
    image: webgoat/webgoat-8.0
    networks:
      - vulnerable_network
  metasploit:
    image: metasploitframework/metasploit-framework
    networks:
      - vulnerable_network
networks:
  vulnerable_network:
    driver: bridge
</code></pre>
</li>
<li>
<strong>Lancer les conteneurs</strong>: Exécutez <code>docker-compose up -d</code> pour lancer tous les conteneurs en arrière-plan.
</li>
<li>
<strong>Interconnexion</strong>: Vous pouvez ensuite accéder au conteneur Metasploit et effectuer des attaques sur les autres machines du même réseau Docker.
<pre><code>docker exec -it [CONTAINER_ID_FOR_METASPLOIT] /bin/bash
</code></pre>
</li>
<li>
<strong>Pratique du pivotement</strong>: Utilisez Metasploit pour exploiter une des machines vulnérables et ensuite utilisez cette machine comme un pivot pour accéder aux autres.
</li>
</ol>

Cet environnement vous permettra de pratiquer des scénarios réalistes de pivotement et d'exploitation de vulnérabilités, ce qui sera très utile pour votre entreprise en pentesting et pour votre compréhension des meilleures pratiques en matière de sécurité.

Cette mise en pratique sera alignée avec les standards ISO 27001 et GDPR, en vous offrant un environnement sûr pour tester les mesures de protection des données et des informations.


## Remerciements et conseils

| Tags |
|------|
| `remerciements` `conseils` `pentesting` |

Je suis heureux que cela ait été utile. N'hésitez pas à poser d'autres questions ou à demander des éclaircissements supplémentaires. Bonne chance avec votre entreprise de pentesting et votre formation en ingénierie de la sécurité !


## Configuration Réseau Avancée avec Docker Compose

| Tags |
|------|
| `Docker` `Réseau` `Compose` `Pentesting` `Sécurité` |

Dans un environnement complexe, l'extension du fichier <code>docker-compose.yml</code> permet de définir plusieurs réseaux et d'affecter des conteneurs à ces réseaux.

Exemple :

```yaml
version: '3'
services:
  metasploitable:
    image: tleemcjr/metasploitable2
    networks: 
      - internal_network
    ports:
      - "2222:22"
  webgoat:
    image: webgoat/webgoat-8.0
    networks:
      - dmz_network
  metasploit:
    image: metasploitframework/metasploit-framework
    networks:
      - internal_network
      - dmz_network
    ports:
      - "4444:4444"
  gateway:
    image: alpine
    networks:
      - internal_network
      - dmz_network
    entrypoint: /bin/sh -c "trap 'exit 0' INT; while :; do sleep 1; done"

networks:
  internal_network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
  dmz_network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.29.0.0/16
```

Dans cet exemple :

*   <code>internal_network</code> représente un réseau interne.
*   <code>dmz_network</code> représente une zone démilitarisée (DMZ).
*   <code>gateway</code> simule une passerelle entre les deux réseaux.

La machine Metasploit est connectée à deux réseaux, simulant des attaques pivotantes à travers la passerelle.

Cette configuration est adaptée à la pratique du pivotement en utilisant Metasploit. Adaptez cet exemple à vos propres scénarios.


## Configuration de tests en "boîte noire"

| Tags |
|------|
| `Metasploit` `Docker` `Pentesting` `Sécurité` `Réseau` |

Effectivement, dans un scénario de test d'intrusion en "boîte noire", le testeur n'a pas d'informations préalables sur l'infrastructure réseau ou les systèmes cibles. Pour simuler cela, vous pourriez configurer Metasploit de manière à ce qu'il ne soit pas directement connecté aux réseaux cibles dans le fichier `docker-compose.yml`. Vous pourriez alors utiliser une machine "attaquante" distincte, également en conteneur, qui serait la seule à avoir accès à Metasploit et à une partie des autres réseaux.

Exemple de configuration :

```yaml
version: '3'
services:
  metasploitable:
    image: tleemcjr/metasploitable2
    networks: 
      - internal_network
  webgoat:
    image: webgoat/webgoat-8.0
    networks:
      - dmz_network
  metasploit:
    image: metasploitframework/metasploit-framework
    networks:
      - attacker_network
  attacker_machine:
    image: kali
    networks:
      - attacker_network
      - dmz_network
    ports:
      - "4444:4444"
  gateway:
    image: alpine
    networks:
      - internal_network
      - dmz_network
    entrypoint: /bin/sh -c "trap 'exit 0' INT; while :; do sleep 1; done"

networks:
  internal_network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
  dmz_network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.29.0.0/16
  attacker_network:
    driver: bridge
    ipam:
      config:
        - subnet: 172.30.0.0/16
```

Dans cette configuration :

*   **attacker\_machine** représente votre machine attaquante, équipée d'outils de pentesting.
*   **metasploit** est sur un réseau isolé (`attacker_network`) et peut seulement être accessible via la machine attaquante.
*   **gateway** et les autres machines vulnérables ne sont pas directement accessibles par la machine Metasploit, simulant un environnement de "boîte noire".

Cela vous permettrait de tester des techniques de découverte, d'exploitation et de pivotement dans un contexte où vous avez un accès très limité aux informations sur la cible, ce qui est plus proche d'un véritable scénario de boîte noire.


## Configuration du réseau Docker

| Tags |
|------|
| `Docker` `Réseau` `Pivot` `Pentesting` `Docker Compose` |

Pour créer un environnement comprenant trois machines vulnérables et deux passerelles, où chaque machine vulnérable est interposée entre deux passerelles, la configuration <code>docker-compose.yml</code> suivante peut être utilisée :

```yaml
version: '3'
services:
  vuln_machine1:
    image: tleemcjr/metasploitable2
    networks: 
      - net1
      - net2
  vuln_machine2:
    image: webgoat/webgoat-8.0
    networks: 
      - net2
      - net3
  vuln_machine3:
    image: vulnerables/web-dvwa
    networks: 
      - net3
      - net4
  gateway1:
    image: alpine
    networks:
      - net1
      - net2
    entrypoint: /bin/sh -c &quot;trap &#x27;exit 0&#x27; INT; while :; do sleep 1; done&quot;
  gateway2:
    image: alpine
    networks:
      - net3
      - net4
    entrypoint: /bin/sh -c &quot;trap &#x27;exit 0&#x27; INT; while :; do sleep 1; done&quot;
  attacker_machine:
    image: kali
    networks:
      - net1
    ports:
      - &quot;4444:4444&quot;

networks:
  net1:
    driver: bridge
  net2:
    driver: bridge
  net3:
    driver: bridge
  net4:
    driver: bridge
```

Dans cette configuration :

*   <code>vuln_machine1</code>, <code>vuln_machine2</code> et <code>vuln_machine3</code> représentent les machines vulnérables.
*   <code>gateway1</code> et <code>gateway2</code> agissent comme passerelles.
*   Chaque machine vulnérable est connectée à deux réseaux distincts. Par exemple, <code>vuln_machine1</code> est accessible via <code>net1</code> et <code>net2</code>.
*   <code>attacker_machine</code>, positionnée sur le réseau <code>net1</code>, sert de point d'entrée pour les attaques.

Cet environnement permet de simuler le pivotement, où une machine vulnérable est exploitée pour servir de tremplin pour attaquer la suivante via la passerelle, et ainsi de suite. Ceci facilite l'apprentissage et le développement des compétences en pentesting réseau.


## Configuration des machines du réseau

| Tags |
|------|
| `réseau` `Docker` `sécurité` |


## Scénario de Pentesting : Réseaux Isolés et Pivoting

| Tags |
|------|
| `Docker` `Pentesting` `Réseaux` `Sécurité` `Escalade de privilèges` |

Pour créer un scénario où chaque machine vulnérable est sur son propre réseau, et où vous devez passer par des passerelles vulnérables pour atteindre les autres machines, vous pouvez configurer votre <code>docker-compose.yml</code> comme ceci :

```yaml
version: '3'
services:
  vuln_machine1:
    image: tleemcjr/metasploitable2
    networks: 
      - net1
  vuln_machine2:
    image: webgoat/webgoat-8.0
    networks: 
      - net2
  vuln_machine3:
    image: vulnerables/web-dvwa
    networks: 
      - net3
  gateway1:
    image: vulnerables/cowrie
    networks:
      - net1
      - net2
  gateway2:
    image: vulnerables/cowrie
    networks:
      - net2
      - net3
  attacker_machine:
    image: kali
    networks:
      - net1
    ports:
      - "4444:4444"

networks:
  net1:
    driver: bridge
  net2:
    driver: bridge
  net3:
    driver: bridge
```

Dans cette configuration :

*   <code>vuln_machine1</code>, <code>vuln_machine2</code>, et <code>vuln_machine3</code> sont vos machines vulnérables, chacune sur son propre réseau.
*   <code>gateway1</code> et <code>gateway2</code> servent de passerelles vulnérables et sont des images Docker simulant des routeurs vulnérables. J'utilise l'image <code>vulnerables/cowrie</code> comme un exemple; vous pouvez choisir des images qui simulent des routeurs vulnérables.
*   L'<code>attacker_machine</code> est sur <code>net1</code>, ce qui signifie qu'elle ne peut accéder qu'à <code>vuln_machine1</code> directement.

Vous commencez par exploiter <code>vuln_machine1</code>, puis utilisez cette machine pour exploiter <code>gateway1</code>, et ainsi de suite, pour atteindre les autres réseaux et machines.

Ce scénario est idéal pour pratiquer des compétences avancées en pentesting, y compris l'escalade de privilèges et le pivotement à travers des routeurs et passerelles vulnérables.


## Présentation de l'image Cowrie

| Tags |
|------|
| `Cowrie` `SSH` `Telnet` `Honeypot` `Docker` `Pentest` |

Cowrie est un honeypot SSH/Telnet interactif conçu pour enregistrer les tentatives d'attaque. Il simule un système SSH et/ou Telnet, capturant les tentatives d'attaque et les commandes des attaquants. Dans un environnement de pentest, Cowrie peut simuler une passerelle vulnérable, permettant l'analyse des types d'attaques potentielles.

Dans la configuration Docker proposée, l'image Docker `vulnerables/cowrie` est utilisée pour simuler ces passerelles vulnérables. Ces "passerelles" sont les seuls points d'accès aux réseaux et machines vulnérables. Cowrie offre un contrôle précis des interactions et aide à comprendre comment un attaquant pourrait exploiter une passerelle vulnérable pour accéder au réseau.

Cowrie est couramment utilisé dans la recherche en sécurité et en production pour piéger les attaquants. Il constitue également un outil précieux dans un laboratoire de pentest pour la pratique et le développement des compétences.


## Images Docker de routeurs vulnérables ?

| Tags |
|------|
| `Docker` `Routeur` `Vulnérabilité` `Sécurité` `GNS3` |

À ma connaissance, jusqu'à septembre 2021, il est peu courant de trouver des images Docker spécifiquement conçues pour simuler des routeurs vulnérables. Docker est principalement orienté vers les applications et les services, et moins souvent vers la simulation d'appareils réseau tels que les routeurs ou les commutateurs. Les fonctionnalités de bas niveau d'un routeur, comme le routage des paquets IP, sont souvent mieux simulées en utilisant des émulateurs réseau plus spécialisés tels que GNS3 ou des environnements de virtualisation comme VMware, capables d'exécuter des systèmes d'exploitation de routeur réels.

Cependant, il est possible de créer des images Docker personnalisées simulant des routeurs vulnérables. Cela peut être réalisé en exécutant des services réseau courants et en les configurant de manière intentionnellement non sécurisée. Par exemple, il est possible de configurer un serveur SSH avec des mots de passe faibles, d'activer des services obsolètes, ou d'installer des logiciels connus pour leurs vulnérabilités.

Pour des simulations plus réalistes, des outils tels que GNS3 permettent l'intégration d'images réelles de systèmes d'exploitation de routeurs (par exemple, Cisco), qui peuvent être configurés pour exposer des vulnérabilités.

En résumé, si l'objectif est de pratiquer le pentesting dans un environnement simulant fidèlement des routeurs réels, des solutions spécialisées comme GNS3 ou des environnements virtuels complets peuvent être plus appropriées que Docker.


## Reformater des phrases

| Tags |
|------|
| `markdown` `rédaction technique` `reformulation` |

Je vais reformater les phrases en corrigeant la ponctuation et l'orthographe, tout en préservant les blocs de code et les informations techniques. Voici un exemple :

Texte original : « comment je peux utiliser la fonction print() en python pour afficher du texte à l'écran. »

Question reformulée : « Comment puis-je utiliser la fonction print() en Python pour afficher du texte à l'écran ? »

Fournissez-moi d'autres phrases à reformater.


## Configuration d'un environnement de test avec GNS3

| Tags |
|------|
| `GNS3` `Réseau` `Pentest` `Routeur` `Vulnérabilité` |

Bien sûr, voici un exemple simplifié pour configurer un environnement de test avec GNS3, qui simule un réseau contenant des routeurs et des machines vulnérables. L'exemple suppose que vous avez déjà installé GNS3 et que vous avez accès à des images d'IOS Cisco pour la simulation de routeurs.

<ol>
<li>
<strong>Ouvrez GNS3 et créez un nouveau projet.</strong>
</li>
<li>
<strong>Ajoutez des routeurs virtuels :</strong>
<ul>
<li>Faites glisser quelques routeurs Cisco depuis le panneau latéral vers l'espace de travail.</li>
</ul>
</li>
<li>
<strong>Ajoutez des machines virtuelles vulnérables :</strong>
<ul>
<li>Vous pouvez intégrer des VM comme Metasploitable, WebGoat, etc., dans GNS3.</li>
</ul>
</li>
<li>
<strong>Connectez les nœuds :</strong>
<ul>
<li>Utilisez l'outil de connexion pour connecter les routeurs entre eux et les routeurs aux machines virtuelles.</li>
</ul>
</li>
<li>
<strong>Configurez les routeurs pour être vulnérables :</strong>
<ul>
<li>Double-cliquez sur un routeur pour ouvrir la console et accéder à l'interface de ligne de commande.</li>
<li>Configurez des services inutiles, des mots de passe faibles, etc.</li>
<li>
Par exemple, pour activer le Telnet avec un mot de passe faible :
<pre><code class="language-shell">conf t
line vty 0 4
password weakpassword
login
exit
</code></pre>
</li>
</ul>
</li>
<li>
<strong>Démarrez les nœuds :</strong>
<ul>
<li>Cliquez droit sur chaque nœud et choisissez &quot;Démarrer&quot; pour lancer les machines virtuelles et les routeurs.</li>
</ul>
</li>
<li>
<strong>Ajoutez une machine attaquante :</strong>
<ul>
<li>Vous pouvez utiliser une machine Kali Linux comme poste d'attaque. Connectez cette machine à l'un des routeurs.</li>
</ul>
</li>
<li>
<strong>Testez la vulnérabilité :</strong>
<ul>
<li>Utilisez votre machine attaquante pour identifier et exploiter les vulnérabilités dans les routeurs et les machines virtuelles.</li>
</ul>
</li>
<li>
<strong>Pivotez :</strong>
<ul>
<li>Une fois que vous avez compromis un appareil, utilisez-le pour attaquer les autres appareils dans le réseau, en pratiquant des techniques de pivotement.</li>
</ul>
</li>
</ol>
GNS3 vous permet d'émuler un environnement réseau très proche de la réalité, y compris les vulnérabilités et les faiblesses que vous pouvez rencontrer dans un véritable environnement de production. Vous pouvez donc pratiquer toutes sortes de scénarios de pentesting et d'escalade de privilèges.


## GNS3 : Gratuité et modèles économiques

| Tags |
|------|
| `GNS3` `réseau` `simulation` `open-source` `licence` |

GNS3 (Graphical Network Simulator-3) est un logiciel open-source, dont la version de base est gratuite. Il permet de simuler des réseaux complexes sans frais. Cependant, plusieurs points sont à considérer :

1.  **Images de routeur/systèmes d'exploitation** : GNS3 fournit le framework de simulation, mais les images de routeurs (ex : Cisco IOS) ne sont généralement pas gratuites. Un accès légal à ces images est requis, souvent via un abonnement ou une licence du fabricant.

2.  **Support et fonctionnalités avancées** : GNS3 propose une version payante (abonnement), la GNS3 VM, incluant support technique et fonctionnalités avancées. Cette version est adaptée aux entreprises et environnements de formation professionnelle.

3.  **Ressources système** : Bien que gratuit, le logiciel nécessite un matériel robuste et peut consommer des ressources système importantes, selon la complexité du réseau simulé.

4.  **Services cloud** : GNS3 offre des services cloud payants pour exécuter les simulations, solution pratique si le matériel local est insuffisant.

En résumé, GNS3 est utilisable gratuitement pour les besoins de base, mais certaines fonctionnalités et ressources peuvent être payantes ou sous licence.


## Alternatives à GNS3 pour la simulation réseau

| Tags |
|------|
| `GNS3` `simulation réseau` `tests de pénétration` `EVE-NG` `Packet Tracer` `VIRL` `NetSim` `VirtualBox` `VMware` `Cloonix` `Mininet` |

Oui, plusieurs alternatives à GNS3 existent pour la simulation réseau et les tests de pénétration :

1.  **EVE-NG (Emulated Virtual Environment - Next Generation)** : Une plateforme de virtualisation puissante, supportant divers dispositifs (routeurs, commutateurs, pare-feu). Versions gratuite et professionnelle.

2.  **Packet Tracer** : Développé par Cisco, plus limité que GNS3 mais facile d'utilisation pour les débutants. Principalement utilisé à des fins éducatives.

3.  **VIRL (Virtual Internet Routing Lab)** : Cisco propose VIRL, avec des fonctionnalités avancées (payant), ciblant un public professionnel.

4.  **NetSim** : Simulateur réseau payant, axé sur la formation et la certification. Prend en charge différents dispositifs Cisco, souvent utilisé dans l'enseignement.

5.  **VirtualBox/VMware avec des VMs personnalisées** : Création de laboratoires de test via des machines virtuelles. Cette méthode offre un contrôle total sur les dispositifs et topologies, mais demande plus de configuration manuelle.

6.  **Cloonix** : Simulateur réseau open-source capable de simuler des réseaux complexes.

7.  **Mininet** : Spécialisé dans la simulation des réseaux SDN (Software-Defined Networking).
    Idéal pour les personnes intéressées par ce domaine.

Chaque outil possède ses propres avantages, inconvénients et cas d'utilisation. Le choix dépendra des besoins spécifiques en matière de formation et de tests de pénétration.


## Outils gratuits pour l'intégration Docker et simulation réseau

| Tags |
|------|
| `Docker` `Docker Compose` `Mininet` `Réseau simulé` `Pentesting` |

Si vous recherchez une solution gratuite pour l'utilisation de conteneurs Docker, envisagez d'utiliser <strong>Docker Compose</strong> en combinaison avec <strong>Mininet</strong> pour la création d'un environnement de réseau simulé.

<ol>
<li>
<strong>Docker Compose</strong> : Définissez et exécutez vos conteneurs Docker. Utilisez un fichier <code>docker-compose.yml</code> pour spécifier les images Docker, les réseaux et autres configurations.
</li>
<li>
<strong>Mininet</strong> : Outil open-source pour simuler des réseaux SDN (Software-Defined Networking). Bien que principalement utilisé pour les réseaux SDN, Mininet permet de créer des topologies de réseau standards.
</li>
<li>
Utilisez Docker Compose pour créer des conteneurs Docker représentant des machines vulnérables, des serveurs, etc.
</li>
<li>
Utilisez Mininet pour créer une topologie de réseau simulé. Intégrez vos conteneurs Docker dans cette topologie en utilisant des scripts ou des commandes CLI.
</li>
<li>
Connectez les conteneurs Docker à Mininet pour qu'ils fassent partie de la topologie de réseau simulée.
</li>
</ol>

Cette combinaison permet de créer un environnement réseau complexe pour les tests de pénétration, tout en utilisant des conteneurs Docker pour les machines cibles. C'est une solution gratuite pour simuler des scénarios réseau pour le pentesting.


## Ports des machines vulnérables dans le script Docker

| Tags |
|------|
| `Docker` `Sécurité` `Ports` |

Dans le script Docker précédent, l'absence de spécification explicite des ports expose implicitement les ports par défaut des conteneurs. Sans configuration spécifique, Docker expose tous les ports nécessaires au fonctionnement des applications. Pour une attaque, il est donc essentiel d'identifier et de cibler les services exposés sur ces ports. Il est fortement recommandé d'examiner attentivement la configuration du conteneur et les services qui y sont déployés pour déterminer les ports ouverts et les vulnérabilités potentielles.


## Exposer les ports Docker Compose

| Tags |
|------|
| `Docker` `Docker Compose` `Ports` `YAML` |

Dans un fichier Docker Compose, l'absence de spécification de ports implique que ces derniers ne sont ni exposés ni mappés à l'hôte. L'utilisation de la clé `ports` dans le fichier `docker-compose.yml` permet d'exposer des ports spécifiques.

Exemple :

```yaml
services:
  vulnerable-machine-1:
    image: vuln-image-1
    ports:
      - "8080:8080"
      - "22:22"
  vulnerable-machine-2:
    image: vuln-image-2
    ports:
      - "9090:9090"
      - "23:23"
```

Dans l'exemple ci-dessus :

*   Pour `vulnerable-machine-1`, le port 8080 du conteneur est mappé au port 8080 de l'hôte, et le port 22 du conteneur est mappé au port 22 de l'hôte.
*   Pour `vulnerable-machine-2`, le port 9090 du conteneur est mappé au port 9090 de l'hôte, et le port 23 du conteneur est mappé au port 23 de l'hôte.

Il est ainsi possible d'attaquer ces machines en ciblant les ports spécifiés depuis la machine attaquante.


## Modifier le réseau Docker dans le script `compose`

| Tags |
|------|
| `Docker` `Compose` `Réseau` `Conteneurs` |

Si vous souhaitez restreindre l'accès aux ports des machines vulnérables à leur propre réseau, utilisez la fonctionnalité de réseau interne de Docker. Avec cette méthode, les ports ne seront pas exposés à l'hôte, mais resteront accessibles aux autres conteneurs du même réseau.

Pour ce faire, modifiez le fichier `docker-compose.yml` comme suit :

```yaml
version: '3'

services:
  cowrie:
    image: cowrie/cowrie
    networks:
      - my_internal_network
  vulnerable-machine-1:
    image: vuln-image-1
    networks:
      - my_internal_network
  vulnerable-machine-2:
    image: vuln-image-2
    networks:
      - my_internal_network
  vulnerable-machine-3:
    image: vuln-image-3
    networks:
      - my_internal_network

networks:
  my_internal_network:
    internal: true
```

Dans cet exemple, une nouvelle section `networks` définit un réseau interne nommé `my_internal_network`. Cette information réseau est également ajoutée à chaque service, permettant aux conteneurs de communiquer entre eux au sein de ce réseau sans être exposés à l'hôte ou à d'autres réseaux.

Notez que, avec un réseau interne, les ports du conteneur ne sont accessibles que par d'autres conteneurs du même réseau. Par conséquent, une machine attaquante doit également être un conteneur sur le même réseau interne pour atteindre les machines vulnérables.


## Exemple de script Docker Compose pour Mininet

| Tags |
|------|
| `Docker` `Docker Compose` `Mininet` `Réseau` |

```yaml
version: '3'
services:
  mininet:
    image: mininet/mininet
    container_name: mininet
    privileged: true
    networks:
      - mininet_network
    volumes:
      - /lib/modules:/lib/modules
      - /lib/x86_64-linux-gnu:/lib/x86_64-linux-gnu

  vulnerable-machine-1:
    image: vuln-image-1
    networks:
      - mininet_network

  vulnerable-machine-2:
    image: vuln-image-2
    networks:
      - mininet_network

  vulnerable-machine-3:
    image: vuln-image-3
    networks:
      - mininet_network

networks:
  mininet_network:
    driver: bridge
```

Explication des éléments clés:

*   `privileged: true`: Pour Mininet, exécuter le conteneur en mode privilégié permet d'utiliser certaines fonctionnalités du réseau que Mininet pourrait nécessiter.
*   `volumes`: Montage des modules du noyau et des bibliothèques nécessaires pour Mininet.
*   `networks`: Tous les conteneurs sont sur le même réseau ponté, appelé `mininet_network`.

Pour utiliser Mininet avec Docker, vous devez généralement avoir accès aux privilèges supplémentaires pour permettre à Mininet de manipuler les interfaces réseau dans le conteneur. D'où l'option `privileged: true`.

Une fois que tout est configuré, vous pouvez exécuter des scripts Mininet pour configurer la topologie du réseau comme vous le souhaitez, en utilisant Mininet CLI ou des scripts Python. Vous pourrez ainsi simuler le comportement du réseau entre vos machines vulnérables.

N'oubliez pas que vous devez toujours faire preuve de prudence lorsque vous manipulez des machines vulnérables et des environnements potentiellement dangereux, surtout en accordant des privilèges supplémentaires à des conteneurs. Assurez-vous que votre environnement est isolé et sécurisé pour éviter tout risque.


## Script pour machines vulnérables et Mininet

| Tags |
|------|
| `Mininet` `Docker Compose` `réseau` `sécurité` `script` |

Pour configurer un environnement complexe avec des machines vulnérables isolées sur leurs propres réseaux et Mininet comme passerelle, on utilise Docker Compose pour les machines vulnérables et un script Mininet pour la topologie réseau. On suppose ici que des images de routeurs vulnérables sont disponibles, nommées <code>vuln-router</code>.


## Docker Compose Configuration

| Tags |
|------|
| `Docker` `docker-compose` `YAML` `Containers` |

```yaml
version: '3'
services:
  vulnerable-machine-1:
    image: vuln-image-1
    container_name: vuln1
    networks:
      - network1

  vulnerable-machine-2:
    image: vuln-image-2
    container_name: vuln2
    networks:
      - network2

  vulnerable-machine-3:
    image: vuln-image-3
    container_name: vuln3
    networks:
      - network3

networks:
  network1:
    driver: bridge
  network2:
    driver: bridge
  network3:
    driver: bridge
```


## Script Mininet pour la Topologie Réseau

| Tags |
|------|
| `Mininet` `Python` `Réseau` `Docker` |

```python
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.cli import CLI

net = Mininet()

# Create nodes
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')

r1 = net.addHost('r1', image="vuln-router")
r2 = net.addHost('r2', image="vuln-router")

# Create links
net.addLink(h1, r1)
net.addLink(r1, r2)
net.addLink(r2, h2)
net.addLink(r2, h3)

# Build network
net.build()

# Start Mininet CLI
CLI(net)
```

Le script <code>topology.py</code> configure une topologie réseau dans Mininet. Il définit trois hôtes (h1, h2, h3) et deux routeurs vulnérables (r1, r2).  Les liens entre les nœuds simulent une infrastructure réseau. L'intégration de conteneurs Docker dans cette topologie nécessite des ajustements réseau spécifiques.  Les conteneurs vulnérables sont censés être sur leurs propres réseaux (network1, network2, network3) dans <code>docker-compose.yml</code>.


## Docker Compose et Mininet : Établir la connexion

| Tags |
|------|
| `Docker` `Docker Compose` `Mininet` `Réseau` |

Le lien entre Docker Compose et Mininet peut être complexe, car il nécessite une manipulation de bas niveau des interfaces réseau. Voici une méthode générale pour lier les deux :


## Identification des interfaces réseau Docker
| Tags |
|------|
| `Docker` `Réseau` `Conteneurs` |

Après le lancement des conteneurs via Docker Compose, il est nécessaire d'identifier leurs interfaces réseau. Utiliser la commande suivante :

```bash
docker inspect <CONTAINER_ID>
```

Localiser la section <code>"Networks"</code> pour obtenir l'adresse IP et le nom du réseau.


## Ajout d'hôtes existants avec l'API Mininet

| Tags |
|------|
| `Mininet` `API` `Docker` `Réseau` |

Vous pouvez utiliser l'API Mininet pour ajouter des hôtes représentant des conteneurs Docker. Lors de l'ajout du lien, vous devez spécifier l'interface réseau.


## Création de liens pair-à-pair (vETH)

| Tags |
|------|
| `Docker` `Mininet` `vETH` `Réseau` |

Vous pouvez établir des liens pair-à-pair (vETH) entre des conteneurs Docker et des hôtes Mininet. Ces liens vETH simulent un "câble virtuel" entre le conteneur et l'hôte Mininet.


## Configuration du routage

| Tags |
|------|
| `Mininet` `Routage` `Réseau` |

Une fois les hôtes connectés, configurez le routage sur les routeurs Mininet (ou les hôtes qui agissent comme des routeurs) pour permettre la communication entre les différents réseaux.


## Tester la connectivité réseau

| Tags |
|------|
| `réseau` `ping` `traceroute` `connectivité` |

Utilisez des outils comme <code>ping</code> ou <code>traceroute</code> pour vérifier que le routage fonctionne comme prévu.


## Script Mininet : Ajouter un hôte existant

| Tags |
|------|
| `Mininet` `Python` `Réseau` `Hôte` `Docker` |

```python
from mininet.net import Mininet
from mininet.node import Host

net = Mininet()

# Ajoutez le contrôleur et les commutateurs comme d'habitude
c0 = net.addController('c0')
s1 = net.addSwitch('s1')

# Ajoutez un hôte Mininet avec une interface spécifique
h1 = net.addHost('h1', cls=Host, ip='192.168.1.2/24', mac='00:00:00:00:00:01')
net.addLink(h1, s1)

# Ajoutez un conteneur Docker en tant qu'hôte
d1 = net.addHost('d1', cls=Host, ip='192.168.1.3/24', mac='00:00:00:00:00:02')
net.addLink(d1, s1)

# Vous devrez configurer manuellement le conteneur pour utiliser la nouvelle interface

net.start()
net.pingAll()
net.stop()
```

Cette méthode est avancée et requiert une compréhension des concepts de réseau. Elle est particulièrement utile pour un contrôle précis du comportement réseau.


## Automatisation de tâches avec Python

| Tags |
|------|
| `Python` `Docker Compose` `Mininet` `subprocess` `CLI` |

Ce projet vise à automatiser la création d'un environnement complexe intégrant Docker Compose et Mininet en Python. La bibliothèque `subprocess` est utilisée pour exécuter des commandes shell, gérant ainsi les conteneurs Docker et la topologie Mininet.

L'exemple suivant illustre l'intégration :

**1. Configuration Docker Compose**

Un fichier `docker-compose.yml` est défini comme suit :

```yaml
# docker-compose.yml content
version: '3'
services:
  vulnerable-machine-1:
    image: vuln-image-1
    networks:
      - network1
  # ... autres machines vulnérables et réseaux

networks:
  network1:
    driver: bridge
  # ... autres réseaux
```

**2. Script Python**

Le script Python réalise les actions suivantes :

```python
import subprocess
import time
from mininet.net import Mininet
from mininet.node import RemoteController, Host
from mininet.cli import CLI

# Lancer les conteneurs Docker avec Docker Compose
subprocess.run(["docker-compose", "up", "-d"])

# Laisser le temps aux conteneurs de démarrer
time.sleep(10)

# Initialisation de Mininet
net = Mininet(controller=RemoteController)

# Ajouter un contrôleur
c0 = net.addController('c0', port=6633)

# Ajouter des commutateurs
s1 = net.addSwitch('s1')

# Ajouter des hôtes (machines vulnérables)
h1 = net.addHost('h1')
h2 = net.addHost('h2')
h3 = net.addHost('h3')

# Ajouter des routeurs (en supposant que vous avez des images Docker pour des routeurs vulnérables)
r1 = net.addHost('r1', ip='10.0.0.1')
r2 = net.addHost('r2', ip='10.0.0.2')

# Connecter les nœuds
net.addLink(h1, r1)
net.addLink(r1, s1)
net.addLink(s1, r2)
net.addLink(r2, h2)
net.addLink(r2, h3)

# Démarrer le réseau
net.build()
net.start()

# Ouvrir l'interface CLI de Mininet pour des tests
CLI(net)

# Arrêt du réseau et des conteneurs
net.stop()
subprocess.run(["docker-compose", "down"])
```

**Fonctionnement du script:**

1.  Lance les conteneurs Docker via Docker Compose.
2.  Initialise un réseau Mininet avec un commutateur, trois hôtes et deux routeurs.
3.  Connecte les hôtes et les routeurs.
4.  Ouvre l'interface CLI de Mininet pour les tests.
5.  Arrête le réseau et les conteneurs après la fermeture de l'interface CLI de Mininet.

Ce script est une base. Pour une utilisation en production, des fonctionnalités telles que le routage dynamique et la configuration des pare-feu seraient nécessaires. L'intégration des ID des conteneurs Docker en tant qu'hôtes Mininet est une extension possible, nécessitant une gestion fine des interfaces réseau.


## Intégration de la commande `inspect` dans le script

| Tags |
|------|
| `Docker` `docker inspect` `Mininet` `Python` `Réseau` |

Vous avez raison. La section concernant l'utilisation de `docker inspect` pour obtenir les informations réseau des conteneurs Docker et les intégrer dans Mininet manquait. Voici comment incorporer cette étape dans le script Python :

1.  Après le démarrage des conteneurs avec Docker Compose, utilisez `docker ps` pour récupérer les ID des conteneurs.
2.  Ensuite, utilisez `docker inspect` avec ces ID pour obtenir les informations réseau.
3.  Transmettez ces informations à Mininet pour configurer les hôtes.

Voici un exemple de code Python illustrant ces étapes :

```python
import subprocess
import json
import time
from mininet.net import Mininet
from mininet.node import Host
from mininet.cli import CLI

# Lancer les conteneurs Docker avec Docker Compose
subprocess.run(["docker-compose", "up", "-d"])

# Laisser le temps aux conteneurs de démarrer
time.sleep(5)

# Obtenir la liste des conteneurs en cours d'exécution
result = subprocess.run(["docker", "ps", "-q"], stdout=subprocess.PIPE)
container_ids = result.stdout.decode('utf-8').strip().split("\n")

# Obtenir les informations réseau des conteneurs
container_network_info = {}
for container_id in container_ids:
    result = subprocess.run(["docker", "inspect", container_id], stdout=subprocess.PIPE)
    container_info = json.loads(result.stdout.decode('utf-8'))[0]
    ip_address = container_info['NetworkSettings']['Networks']['network1']['IPAddress']
    container_network_info[container_id] = ip_address

# Initialisation de Mininet
net = Mininet()

# Ajouter un commutateur et des hôtes en utilisant les informations de l'étape précédente
s1 = net.addSwitch('s1')
for container_id, ip_address in container_network_info.items():
    net.addHost(container_id[:5], cls=Host, ip=f"{ip_address}/24")
    net.addLink(container_id[:5], s1)

# Démarrer le réseau
net.start()

# Ouvrir l'interface CLI de Mininet pour des tests
CLI(net)

# Arrêter le réseau
net.stop()

# Arrêter les conteneurs Docker
subprocess.run(["docker-compose", "down"])
```

Ce script suppose que tous les conteneurs partagent le même réseau Docker (dans cet exemple, nommé `network1`). Adaptez ce script selon vos besoins spécifiques.


## Images de routeurs manquantes dans Mininet ?

| Tags |
|------|
| `Mininet` `Docker` `Réseau` `Routeur` `Python` `Namespace` |

Oui, l'exemple initial utilise des hôtes standards de Mininet à la place des routeurs, ce qui est moins adapté pour tester des scénarios de sécurité. Mininet ne supporte pas directement les conteneurs Docker comme routeurs, mais il existe des solutions.

Une méthode consiste à créer des conteneurs Docker simulant des routeurs vulnérables, puis à utiliser les "namespaces" Linux pour les intégrer à la topologie Mininet.

Une autre approche consiste à lancer des routeurs vulnérables comme conteneurs Docker séparés. Ensuite, Mininet peut être configuré pour utiliser ces "routeurs" comme hôtes, en ajoutant manuellement des règles de routage pour simuler le comportement réseau souhaité.

Voici un exemple simplifié d'intégration d'un conteneur Docker dans une topologie Mininet :

```python
from mininet.net import Mininet
from mininet.node import Node
from mininet.cli import CLI

class DockerRouter(Node):
    def config(self, **params):
        super(DockerRouter, self).config(**params)
        self.cmd('sysctl -w net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl -w net.ipv4.ip_forward=0')
        super(DockerRouter, self).terminate()

net = Mininet()

# Ajout d'un commutateur
s1 = net.addSwitch('s1')

# Ajout d'hôtes vulnérables
h1 = net.addHost('h1')
h2 = net.addHost('h2')

# Ajout d'un routeur (ici, il s'agirait d'un conteneur Docker agissant en tant que routeur)
r1 = net.addHost('r1', cls=DockerRouter)

# Connexion des noeuds
net.addLink(h1, s1)
net.addLink(h2, s1)
net.addLink(r1, s1)

# Démarrage du réseau
net.start()

# Configuration du routage (à adapter)
r1.cmd('ip route add default via 10.0.0.1 dev r1-eth0')

CLI(net)
net.stop()
```

La classe `DockerRouter`, héritant de `Node`, active le routage IP. Cette classe peut être étendue pour des opérations plus complexes, telles que le chargement de configurations de routeur ou le démarrage de services.

Pour des utilisations avancées, une intégration plus étroite entre Docker et Mininet est conseillée, potentiellement via des techniques comme Docker-in-Docker ou la manipulation directe des namespaces réseau Linux.


## Exemple Mininet avec Docker en Python

| Tags |
|------|
| `Mininet` `Docker` `Python` `Réseau` |

Créer un environnement de test complet avec des routeurs et des hôtes vulnérables en utilisant Mininet et Docker est assez complexe. Cependant, je peux vous donner un exemple simplifié où Mininet crée des commutateurs et des hôtes, puis utilise des scripts Python pour configurer les routeurs en utilisant des conteneurs Docker.

Notez que cet exemple est très basique et n'inclut pas de vulnérabilités spécifiques. Pour des scénarios de test plus réalistes, vous devrez utiliser des images Docker qui simulent des routeurs avec des vulnérabilités connues ou configurer des services vulnérables vous-même.

Tout d'abord, installez les dépendances nécessaires :

```bash
pip install mininet
```

Vous aurez également besoin de Docker et Docker Compose installés sur votre système.

Ensuite, voici le script Python :

```python
import subprocess
from mininet.net import Mininet
from mininet.node import Node
from mininet.cli import CLI
from mininet.log import setLogLevel

class DockerRouter(Node):
    def config(self, **params):
        super(DockerRouter, self).config(**params)
        self.cmd('sysctl -w net.ipv4.ip_forward=1')

    def terminate(self):
        self.cmd('sysctl -w net.ipv4.ip_forward=0')
        super(DockerRouter, self).terminate()

def run():
    # Initiate Mininet
    net = Mininet()

    # Add hosts and switches
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    s1 = net.addSwitch('s1')
    r1 = net.addHost('r1', cls=DockerRouter, ip='10.0.0.3/24')

    # Add links
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(r1, s1)

    # Start the network
    net.start()

    # Start Docker container as a router
    subprocess.run(['docker', 'run', '--rm', '--privileged', '--name=router', 'alpine:latest'])

    # Attach Docker container to Mininet
    subprocess.run(['docker', 'exec', 'router', 'brctl', 'addbr', 'br0'])
    subprocess.run(['docker', 'exec', 'router', 'ifconfig', 'br0', '10.0.0.3/24', 'up'])

    # Enable IP forwarding in the Docker container
    subprocess.run(['docker', 'exec', 'router', 'sysctl', '-w', 'net.ipv4.ip_forward=1'])

    # Run Mininet CLI for testing
    CLI(net)

    # Stop network and clean up
    net.stop()
    subprocess.run(['docker', 'stop', 'router'])

if __name__ == '__main__':
    setLogLevel('info')
    run()
```

Ce script utilise Mininet pour créer un réseau simple composé de deux hôtes (`h1` et `h2`), un commutateur (`s1`), et un routeur (`r1`). Le routeur est en fait un conteneur Docker exécutant une image Alpine Linux minimale.

Après avoir démarré le réseau Mininet, le script exécute plusieurs commandes Docker pour configurer le conteneur en tant que routeur. En particulier, il crée un pont réseau dans le conteneur et configure son adresse IP. Il active également le transfert IP pour permettre le routage des paquets.

Enfin, le script lance l'interface CLI de Mininet pour vous permettre de tester le réseau.

Cet exemple est très simplifié mais il devrait vous donner une bonne base pour créer des environnements de test plus complexes.


## Interfaces graphiques pour Mininet

| Tags |
|------|
| `Mininet` `GUI` `MiniEdit` `ONOS` |

Oui, plusieurs interfaces graphiques (GUI) sont disponibles pour Mininet afin de simplifier la création et la gestion de topologies réseau.

MiniEdit est l'une des interfaces les plus utilisées, souvent incluse dans les distributions Mininet. Elle permet de concevoir, modifier et visualiser les topologies Mininet grâce à une interface intuitive. Il est possible d'ajouter des hôtes, des commutateurs et des liaisons, de configurer leurs propriétés, et d'exécuter la topologie directement à partir de l'interface.

Pour démarrer MiniEdit, exécutez la commande <code>miniedit</code> dans le terminal, à condition qu'il soit installé et configuré correctement.

ONOS (Open Network Operating System) est une autre option offrant une interface utilisateur plus complète avec des fonctionnalités supplémentaires. Cependant, cela peut être superflu pour des tests de topologies simples.

Le choix de l'interface dépend des besoins spécifiques et des préférences de l'utilisateur.


## Création d'un fichier Docker Compose

| Tags |
|------|
| `Docker` `Docker Compose` `YAML` `Réseau` `IP` |

Pour créer une configuration Docker Compose avec trois images Docker vulnérables, chacune sur un réseau différent et avec des adresses IP spécifiques, utilisez un fichier `docker-compose.yml` tel que celui-ci :

```yaml
version: '3'
services:
  vulnerable1:
    image: vuln-image1
    networks:
      network1:
        ipv4_address: 192.168.1.2

  vulnerable2:
    image: vuln-image2
    networks:
      network2:
        ipv4_address: 192.168.2.2

  vulnerable3:
    image: vuln-image3
    networks:
      network3:
        ipv4_address: 192.168.3.2

networks:
  network1:
    ipam:
      config:
        - subnet: 192.168.1.0/24

  network2:
    ipam:
      config:
        - subnet: 192.168.2.0/24

  network3:
    ipam:
      config:
        - subnet: 192.168.3.0/24
```

Ce fichier définit :

*   Trois services Docker : `vulnerable1`, `vulnerable2`, et `vulnerable3`. Chaque service utilise une image vulnérable spécifique (`vuln-image1`, `vuln-image2`, `vuln-image3`).
*   Chaque service est associé à un réseau différent : `network1`, `network2`, et `network3`.
*   Les adresses IP pour chaque service sont spécifiées sur leurs réseaux respectifs : `192.168.1.2`, `192.168.2.2`, et `192.168.3.2`.
*   Les plages de sous-réseaux pour chaque réseau sont définies dans la section `networks`.

Après avoir créé ce fichier, lancez les conteneurs et les réseaux avec la commande `docker-compose up`. Remplacez `vuln-image1`, `vuln-image2`, et `vuln-image3` par les noms des images Docker vulnérables que vous souhaitez utiliser.