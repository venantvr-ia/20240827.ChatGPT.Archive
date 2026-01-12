## ParaSwap: Contrat de meilleure route

| Tags |
|------|
| `DeFi` `Swap` `Ethereum` `Smart Contract` |

Le contrat Best Route de ParaSwap est responsable de la recherche du meilleur itinéraire de swap pour un jeton à un autre. Il intègre plusieurs agrégateurs de swap et DEX pour trouver l'itinéraire le plus efficace en termes de prix et de frais.

### Aperçu du contrat

Le contrat est écrit en Solidity et est déployé sur le réseau Ethereum. Il utilise l'interface `IParaSwapPool`.

```solidity
pragma solidity ^0.7.0;

interface IParaSwapPool {
    function getRate(
        address _srcToken,
        address _destToken,
        uint256 _srcQty
    ) external view returns (uint256, uint256);

    function swap(
        address _srcToken,
        address _destToken,
        uint256 _srcQty,
        uint256 _minDestQty,
        uint256 _deadline,
        address _receiver,
        bytes calldata _params
    ) external payable returns (uint256);
}
```

### Méthodes principales

*   `getRate()`: Retourne le taux de conversion et les frais pour un swap spécifique.
*   `swap()`: Exécute le swap en utilisant l'itinéraire spécifié.

### Flux de travail

1.  L'utilisateur appelle la fonction `getRate()` en spécifiant les jetons source et de destination, ainsi que la quantité de jetons source.
2.  Le contrat interroge différents agrégateurs et DEX pour trouver le meilleur itinéraire.
3.  Le contrat retourne le taux de conversion et les frais.
4.  L'utilisateur appelle la fonction `swap()` pour exécuter le swap.
5.  Le contrat exécute le swap en utilisant l'itinéraire sélectionné.

### Sécurité

Le contrat a été audité par [NOM] et [NOM]. Le code source est disponible sur [URL].

### Contact

Pour toute question, veuillez contacter [EMAIL].


## Obtenir la meilleure route avec ParaSwap

| Tags |
|------|
| `ParaSwap` `Smart Contract` `DeFi` `DEX` |

Pour obtenir la meilleure route en utilisant le contrat intelligent ParaSwap, suivez ces étapes :

1.  **Accéder à ParaSwap :** Visitez le site web officiel ([URL]), ou utilisez l'application mobile disponible sur iOS et Android.
2.  **Connecter votre portefeuille :** Connectez votre portefeuille Ethereum (MetaMask, Ledger, Trust Wallet, etc.) et autorisez l'accès.
3.  **Sélectionner les jetons :** Choisissez les jetons à échanger. Sélectionnez le jeton "De" et le jeton "Vers" dans les listes déroulantes.
4.  **Saisir le montant :** Indiquez le montant du jeton à échanger.
5.  **Obtenir la meilleure route :** ParaSwap agrège les données de plusieurs DEX pour trouver la route la plus avantageuse. Le contrat intelligent analyse les plateformes (Uniswap, SushiSwap, Bancor, etc.) et propose la meilleure route en termes de coût et de liquidité.
6.  **Autoriser l'échange de jetons :** Si c'est la première fois que vous échangez un jeton spécifique, vous devrez autoriser ParaSwap à échanger ce jeton. Cliquez sur "Autoriser" et confirmez la transaction dans votre portefeuille.
7.  **Confirmer la transaction :** Si les détails vous conviennent, cliquez sur "Échanger" et confirmez la transaction dans votre portefeuille. Ajustez les paramètres de gaz si nécessaire.
8.  **Suivre la transaction :** Suivez l'état de la transaction sur des explorateurs de blockchain (Etherscan, etc.).

En suivant ces étapes, vous utiliserez le contrat intelligent ParaSwap pour obtenir la meilleure route d'échange possible, optimisant ainsi les taux et réduisant les frais.


## Interaction avec ParaSwap via Web3.js

| Tags |
|------|
| `Web3.js` `ParaSwap` `Smart Contract` `Ethereum` `JavaScript` |

Oui, il est possible d'interagir avec le contrat intelligent ParaSwap en utilisant la bibliothèque Web3.js. Voici un exemple simplifié de la manière dont vous pouvez le faire :

1.  Installez Web3.js : Vous pouvez installer Web3.js en utilisant npm (Node Package Manager) avec la commande suivante :

```bash
npm install web3
```

2.  Importez Web3.js et connectez-vous à un fournisseur :

```javascript
const Web3 = require('web3');
const web3 = new Web3('<INFURA_RINKEBY_URL>'); // Remplacez <INFURA_RINKEBY_URL> par l'URL de votre fournisseur Infura ou d'un autre fournisseur Ethereum.
```

3.  Ajoutez les adresses des contrats et ABI :

```javascript
const paraswapContractAddress = '<PARASWAP_CONTRACT_ADDRESS>'; // Remplacez <PARASWAP_CONTRACT_ADDRESS> par l'adresse du contrat intelligent ParaSwap.
const paraswapABI = <PARASWAP_ABI>; // Remplacez <PARASWAP_ABI> par l'ABI du contrat intelligent ParaSwap.
```

4.  Créez une instance du contrat intelligent ParaSwap :

```javascript
const paraswapContract = new web3.eth.Contract(paraswapABI, paraswapContractAddress);
```

5.  Préparez les informations de la transaction :

```javascript
const fromToken = '<FROM_TOKEN_ADDRESS>'; // Remplacez <FROM_TOKEN_ADDRESS> par l'adresse du jeton que vous souhaitez échanger.
const toToken = '<TO_TOKEN_ADDRESS>'; // Remplacez <TO_TOKEN_ADDRESS> par l'adresse du jeton que vous souhaitez acquérir.
const amount = web3.utils.toWei('<AMOUNT>'); // Remplacez <AMOUNT> par le montant du jeton que vous souhaitez échanger.
const userAddress = '<USER_ADDRESS>'; // Remplacez <USER_ADDRESS> par l'adresse de votre portefeuille Ethereum.
```

6.  Obtenez les détails de la meilleure route :

```javascript
async function getBestRoute() {
  try {
    const bestRoute = await paraswapContract.methods.getBestRoute(fromToken, toToken, amount, userAddress).call();
    console.log("Meilleure route : ", bestRoute);
  } catch (error) {
    console.error("Erreur lors de la récupération de la meilleure route : ", error);
  }
}
getBestRoute();
```

Ce code simplifié vous montre comment utiliser Web3.js pour interagir avec le contrat intelligent ParaSwap et obtenir la meilleure route pour votre échange de jetons. Vous devrez remplacer les valeurs fictives par les vraies adresses de contrat, ABI et autres informations pertinentes.

N'oubliez pas que pour effectuer des transactions (échanges), vous devrez également signer et envoyer des transactions à l'aide de Web3.js et de votre portefeuille Ethereum (comme MetaMask).


## Adresse du contrat ParaSwap sur Polygon

| Tags |
|------|
| `ParaSwap` `Polygon` `Smart Contract` `Blockchain` |

Pour trouver l'adresse du contrat intelligent ParaSwap sur le réseau Polygon (anciennement Matic), référez-vous à la documentation officielle de ParaSwap ou utilisez un explorateur de blockchain Polygon, tel que Polygonscan.

Il est important de noter qu'au dernier point de connaissance en septembre 2021, ParaSwap n'était pas disponible sur le réseau Polygon. Les informations peuvent être obsolètes. Consultez toujours la documentation officielle de ParaSwap ou les annonces officielles pour les dernières mises à jour concernant la disponibilité de ParaSwap sur Polygon.

Si ParaSwap est désormais disponible sur Polygon, l'adresse du contrat intelligent sera différente de celle utilisée sur Ethereum. Assurez-vous d'utiliser l'adresse correcte pour éviter toute perte de fonds.
