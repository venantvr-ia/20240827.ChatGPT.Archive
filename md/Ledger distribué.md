## Ledger distribué

| Tags |
|------|
| `Ledger` `Blockchain` `Sécurité` |
Le registre distribué (DLT) est un type de base de données partagées et synchronisées sur plusieurs sites, géographiquement dispersés, ou avec plusieurs participants. Contrairement aux bases de données traditionnelles, il n'existe pas d'administration centrale ou d'entrepôt de données.

Chaque participant du réseau possède une copie identique du registre. Les modifications apportées au registre sont enregistrées sous forme de blocs. Chaque nouveau bloc est ensuite cryptographiquement lié au bloc précédent, formant une chaîne. Cette structure en chaîne, associée à l'utilisation de la cryptographie, garantit l'intégrité et la sécurité des données.

**Fonctionnement général :**

1.  **Transaction :** Une transaction est initiée par un participant.
2.  **Diffusion :** La transaction est diffusée à l'ensemble du réseau.
3.  **Validation :** Les participants valident la transaction en fonction de règles prédéfinies (consensus).
4.  **Bloc :** Une fois validée, la transaction est regroupée avec d'autres transactions pour former un bloc.
5.  **Ajout :** Le bloc est ajouté à la chaîne de blocs après consensus.
6.  **Mise à jour :** Chaque participant met à jour sa copie du registre.

**Avantages principaux :**

*   **Sécurité améliorée :** La nature distribuée et la cryptographie rendent les données très résistantes aux manipulations et à la censure.
*   **Transparence :** Toutes les transactions sont généralement visibles par les participants (selon les permissions).
*   **Efficacité :** Supprime le besoin d'intermédiaires, réduisant les coûts et les délais.
*   **Résilience :** En l'absence d'un point de défaillance unique, le réseau est plus résilient aux pannes.

**Cas d'utilisation courants :**

*   **Cryptomonnaies :** Bitcoin, Ethereum, etc.
*   **Gestion de la chaîne d'approvisionnement :** Suivi des produits de leur origine à leur destination finale.
*   **Vote électronique :** Sécurisation et transparence des processus de vote.
*   **Gestion d'identité :** Stockage sécurisé des informations d'identité.

**Technologies associées :**

*   **Blockchain :** Le type de DLT le plus connu, utilisant une structure de données en chaîne de blocs.
*   **Cryptographie :** Hashage, signatures numériques, cryptographie asymétrique.
*   **Consensus :** Mécanismes pour valider les transactions (preuve de travail, preuve d'enjeu, etc.).
*   **Contrats intelligents :** Code auto-exécutable stocké sur le DLT.

**Exemple de code (Python simplifié) :**

```python
import hashlib
import json
from time import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = json.dumps({'index': self.index, 'timestamp': self.timestamp, 'data': self.data, 'previous_hash': self.previous_hash}, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time(), "Genesis Block", "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(previous_block.index + 1, time(), data, previous_block.hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

# Exemple d'utilisation
blockchain = Blockchain()
blockchain.add_block({"amount": 100, "sender": "[NOM]", "receiver": "[NOM]"})
blockchain.add_block({"amount": 50, "sender": "[NOM]", "receiver": "[NOM]"})

print(json.dumps([block.__dict__ for block in blockchain.chain], indent=2))
print("La blockchain est-elle valide?", blockchain.is_valid())
```

Ce code est une illustration simplifiée. Les vraies implémentations de DLT sont plus complexes et incluent des mécanismes de consensus et de sécurité plus élaborés.


## Distributed Ledger : Définition et Fonctionnement

| Tags |
|------|
| `Distributed Ledger` `Blockchain` `Décentralisation` |

Un distributed ledger, également connu sous le nom de registre distribué, est une technologie permettant de stocker, gérer et synchroniser des données sur un réseau décentralisé. Il s'agit d'un système de base de données partagé entre plusieurs nœuds.

La principale caractéristique d'un distributed ledger est l'absence d'autorité centrale pour maintenir et valider les transactions. Les participants du réseau, appelés "nœuds", collaborent pour valider et enregistrer les transactions de manière transparente et sécurisée.

La technologie du distributed ledger est souvent associée à la blockchain, qui est un type spécifique de distributed ledger. La blockchain utilise la cryptographie pour créer une chaîne de blocs contenant les transactions validées, formant un historique immuable et transparent des activités du réseau.

Le distributed ledger peut être utilisé dans divers domaines : transactions financières, gestion de la chaîne d'approvisionnement, gouvernance des données, registres fonciers, soins de santé, etc. Il offre des avantages tels que la transparence, l'immutabilité, la sécurité et la réduction des coûts en éliminant les intermédiaires tiers.

Le terme "distributed ledger" englobe différentes technologies et implémentations. Outre la blockchain, il existe d'autres types de distributed ledgers, tels que les directed acyclic graphs (DAG) et les registres distribués basés sur d'autres architectures.
