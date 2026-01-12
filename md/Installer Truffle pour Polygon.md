## Installation de Truffle pour Polygon

| Tags |
|------|
| `Truffle` `Polygon` `Blockchain` `Ethereum` |

Pour installer Truffle pour Polygon, suivez les étapes suivantes :

1.  **Prérequis** : Assurez-vous d'avoir installé Node.js et npm sur votre système.

2.  **Installation de Truffle** : Utilisez npm pour installer Truffle globalement :

    ```bash
    npm install -g truffle
    ```

3.  **Création d'un projet Truffle** : Créez un nouveau projet Truffle :

    ```bash
    truffle init my-polygon-project
    cd my-polygon-project
    ```

4.  **Configuration pour Polygon** : Modifiez le fichier `truffle-config.js` pour inclure les paramètres de connexion à Polygon :

    ```javascript
    module.exports = {
      networks: {
        polygon: {
          provider: () => new HDWalletProvider({
            mnemonic: {
              phrase: "[MNEMONIC]"
            },
            providerOrUrl: "https://polygon-rpc.com",
            chainId: 137
          }),
          network_id: 137,
          gas: 5500000,
          confirmations: 2,
          timeoutBlocks: 200,
          skipDryRun: true
        }
      },
      compilers: {
        solc: {
          version: "0.8.19",
          settings: {
            optimizer: {
              enabled: true,
              runs: 200
            }
          }
        }
      }
    };
    ```

    Remplacez `[MNEMONIC]` par votre phrase secrète de portefeuille.  Vous pouvez également configurer le réseau de test Polygon (par exemple, Mumbai) en utilisant les paramètres appropriés.

5.  **Déploiement de contrats** : Déployez vos contrats intelligents sur Polygon en utilisant la commande :

    ```bash
    truffle migrate --network polygon
    ```

    Assurez-vous d'avoir des tokens MATIC dans votre portefeuille pour payer les frais de gaz.

6.  **Vérification des contrats (optionnel)** : Vous pouvez vérifier vos contrats sur un explorateur de blocs Polygon (tel que Polygonscan) :

    ```bash
    truffle run verify ContractName --network polygon
    ```


## Installer Truffle pour Polygon

| Tags |
|------|
| `Truffle` `Polygon` `Smart Contracts` `Node.js` `NPM` |

Pour installer Truffle et le configurer pour Polygon, suivez ces étapes :

1.  **Installer Node.js et NPM** : Assurez-vous d'avoir Node.js et NPM installés. Vous pouvez les télécharger sur [NOM]. Choisissez la version LTS.
2.  **Installer Truffle** : Ouvrez un terminal et exécutez la commande :

    ```bash
    npm install -g truffle
    ```

3.  **Créer un nouveau projet Truffle** : Créez un répertoire pour votre projet et accédez-y :

    ```bash
    mkdir mon-projet-polygon
    cd mon-projet-polygon
    ```

    Initialisez le projet Truffle :

    ```bash
    truffle init
    ```

4.  **Configurer Truffle pour Polygon** : Ouvrez <code>truffle-config.js</code> et ajoutez les informations de configuration pour Polygon. Vous aurez besoin d'un fournisseur d'API (Infura ou QuickNode) et d'un compte Ethereum avec des clés privées.

    ```javascript
    const HDWalletProvider = require("@truffle/hdwallet-provider");
    const privateKey = "votre_clé_privée";
    const apiKey = "votre_api_key";

    module.exports = {
      networks: {
        polygon: {
          provider: () =>
            new HDWalletProvider(
              privateKey,
              `https://polygon-mainnet.infura.io/v3/${apiKey}`
            ),
          network_id: 137, // ID du réseau Polygon Mainnet
          gas: 5000000,
          gasPrice: 20000000000, // 20 Gwei
          confirmations: 2,
          timeoutBlocks: 200,
          skipDryRun: true,
        },
      },
      compilers: {
        solc: {
          version: "0.8.0", // Utilisez la version appropriée du compilateur Solidity
        },
      },
    };
    ```

    Remplacez <code>votre_clé_privée</code> et <code>votre_api_key</code>. Ajustez les autres paramètres si nécessaire.
5.  **Installer le paquet HDWalletProvider** : Exécutez :

    ```bash
    npm install @truffle/hdwallet-provider
    ```

    Truffle est maintenant configuré pour Polygon. Vous pouvez créer, déployer et tester des contrats intelligents sur Polygon.
