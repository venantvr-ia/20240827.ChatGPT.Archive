## Swap avec Paraswap sur Polygon

| Tags |
|------|
| `Polygon` `Paraswap` `Swap` `DeFi` |

Le guide suivant décrit comment échanger des tokens sur Polygon en utilisant Paraswap.

### Prérequis

*   Un portefeuille compatible avec Polygon (par exemple, Metamask).
*   Des fonds dans votre portefeuille pour couvrir les frais de transaction et l'échange.

### Étape 1 : Configuration du réseau Polygon dans Metamask

Si vous n'avez pas déjà configuré le réseau Polygon dans Metamask, vous devez le faire.

1.  Ouvrez Metamask.
2.  Cliquez sur le menu déroulant du réseau en haut.
3.  Sélectionnez "Ajouter un réseau".
4.  Remplissez les informations du réseau Polygon :

    *   Nom du réseau : Polygon Mainnet
    *   Nouvelle RPC URL : <https://polygon-rpc.com/>
    *   ID de chaîne : 137
    *   Symbole de la devise : MATIC
    *   URL de l'explorateur de blocs : <https://polygonscan.com/>
5.  Cliquez sur "Enregistrer".

### Étape 2 : Accéder à Paraswap

Rendez-vous sur le site web de Paraswap : <https://paraswap.io/>.

### Étape 3 : Connexion du portefeuille

Cliquez sur le bouton "Connect Wallet" et sélectionnez Metamask (ou votre portefeuille préféré). Suivez les instructions pour connecter votre portefeuille.

### Étape 4 : Sélection des tokens

1.  Dans l'interface de Paraswap, sélectionnez le token que vous souhaitez échanger dans le champ "You sell".
2.  Sélectionnez le token que vous souhaitez recevoir dans le champ "You buy".

### Étape 5 : Saisie du montant

Entrez le montant du token que vous souhaitez échanger. Paraswap affichera le montant estimé que vous recevrez.

### Étape 6 : Swap

1.  Cliquez sur le bouton "Swap".
2.  Metamask s'ouvrira et vous demandera de confirmer la transaction. Examinez les détails de la transaction, y compris les frais de gaz.
3.  Cliquez sur "Confirmer" pour effectuer l'échange.

### Étape 7 : Attente de la confirmation

Attendez que la transaction soit confirmée sur la blockchain Polygon. Vous pouvez suivre l'état de la transaction sur un explorateur de blocs Polygon tel que Polygonscan.

### Dépannage

*   **Erreurs de gaz** : Si la transaction échoue en raison d'une erreur de gaz, essayez d'augmenter le montant de gaz dans Metamask.
*   **Transactions lentes** : Les transactions peuvent prendre un certain temps. Soyez patient et attendez la confirmation.
*   **Problèmes de connexion** : Assurez-vous d'avoir une connexion internet stable et que votre portefeuille est correctement connecté.

### Contact

Pour toute question ou problème, veuillez contacter [NOM] à [EMAIL].

Si vous constatez un comportement suspect, merci de le signaler à [EMAIL] ou [IP].


## Effectuer un Swap avec Web3 et Paraswap

| Tags |
|------|
| `Web3.js` `Polygon` `Paraswap` `Smart Contract` `Swap` |

Pour effectuer un swap avec Web3 et le smart contract Paraswap sur Polygon, suivez ces étapes :

1.  Importez la bibliothèque Web3.js et configurez la connexion à la chaîne Polygon :

    ```javascript
    const Web3 = require('web3');
    const web3 = new Web3('https://rpc-mainnet.maticvigil.com/');
    ```

2.  Importez le smart contract Paraswap :

    ```javascript
    const paraswapABI = require('./paraswapABI.json');
    const paraswapAddress = '0x86969d29f5fd327e1009bA66072BE22Db6017cC6';
    const paraswapContract = new web3.eth.Contract(paraswapABI, paraswapAddress);
    ```

3.  Vérifiez le solde de votre compte pour vous assurer que vous avez suffisamment de fonds pour le swap :

    ```javascript
    const myAddress = '[NOM]';
    const myBalance = await web3.eth.getBalance(myAddress);
    ```

4.  Définissez les paramètres de votre swap :

    ```javascript
    const fromTokenAddress = '0x...'; // l'adresse du jeton que vous échangez
    const toTokenAddress = '0x...'; // l'adresse du jeton que vous recevez
    const amountToExchange = web3.utils.toWei('1', 'ether'); // le montant que vous souhaitez échanger (en wei)
    const minAmountToReceive = web3.utils.toWei('0.9', 'ether'); // le montant minimum que vous souhaitez recevoir (en wei)
    const deadline = Math.floor(Date.now() / 1000) + 60 * 10; // la date limite pour le swap (10 minutes à partir de maintenant)
    ```

5.  Approvisionnez le contrat avec le jeton que vous échangez :

    ```javascript
    const fromTokenContract = new web3.eth.Contract(tokenABI, fromTokenAddress);
    const allowance = await fromTokenContract.methods.allowance(myAddress, paraswapAddress).call();
    if (allowance < amountToExchange) {
      await fromTokenContract.methods.approve(paraswapAddress, amountToExchange).send({from: myAddress});
    }
    ```

6.  Effectuez le swap :

    ```javascript
    const swapResult = await paraswapContract.methods.swap(
      fromTokenAddress,
      toTokenAddress,
      amountToExchange,
      minAmountToReceive,
      myAddress,
      deadline
    ).send({from: myAddress});
    ```

7.  Vérifiez le résultat du swap :

    ```javascript
    console.log('Amount received:', swapResult.events.Swap.returnValues.amountReceived);
    ```

Les adresses des jetons doivent être valides sur Polygon. Vous devez également disposer de fonds suffisants pour les frais de gaz.
