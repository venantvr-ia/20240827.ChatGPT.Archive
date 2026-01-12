## Swap avec ParaSwap sur Polygon

| Tags |
|------|
| `Polygon` `ParaSwap` `Swap` `DeFi` |

Le tutoriel suivant explique comment effectuer un swap sur Polygon en utilisant ParaSwap.

**Prérequis**

*   Un portefeuille compatible avec Polygon, par exemple MetaMask.
*   Des fonds (tokens) dans votre portefeuille Polygon.

**Étape 1 : Configuration du portefeuille**

1.  Assurez-vous que votre portefeuille est connecté au réseau Polygon. Si ce n'est pas le cas, ajoutez le réseau Polygon à votre portefeuille. Les informations nécessaires pour configurer Polygon sont :
    *   Nom du réseau : Polygon Mainnet
    *   Nouvelle RPC URL : `https://polygon-rpc.com/`
    *   ID de chaîne : 137
    *   Symbole : MATIC
    *   Explorateur de blocs : `https://polygonscan.com/`
2.  Importez votre portefeuille existant ou créez-en un nouveau.

**Étape 2 : Accéder à ParaSwap**

1.  Visitez le site web de ParaSwap : [URL]
2.  Connectez votre portefeuille en cliquant sur le bouton "Connect Wallet". Sélectionnez votre portefeuille dans la liste des options (par exemple, MetaMask).

**Étape 3 : Effectuer le swap**

1.  Sélectionnez le token que vous souhaitez swapper dans le champ "You sell".
2.  Sélectionnez le token que vous souhaitez recevoir dans le champ "You buy".
3.  Entrez le montant de tokens que vous souhaitez swapper.
4.  Cliquez sur le bouton "Swap".
5.  Votre portefeuille vous demandera de confirmer la transaction. Examinez les détails de la transaction, y compris les frais de gas, et confirmez.
6.  Attendez que la transaction soit confirmée sur la blockchain Polygon. Vous pouvez suivre la progression de la transaction sur un explorateur de blocs tel que Polygonscan.

**Exemple de code (JavaScript/Web3.js - Non exhaustif)**

```javascript
// Connexion à MetaMask (exemple simplifié)
if (window.ethereum) {
  try {
    // Demande l'accès au compte
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const account = accounts[0];
    console.log("Connecté à :", account);
  } catch (error) {
    console.error("Erreur de connexion :", error);
  }
} else {
  console.log('MetaMask non détecté');
}

// Fonction pour effectuer un swap (exemple simplifié, nécessite ParaSwap API)
async function effectuerSwap(tokenIn, tokenOut, amountIn) {
  // 1. Appeler l'API ParaSwap pour obtenir les données du swap
  // const swapData = await getParaSwapData(tokenIn, tokenOut, amountIn);

  // 2. Préparer et signer la transaction avec Web3.js
  // const tx = await préparerTransaction(swapData);

  // 3. Envoyer la transaction à la blockchain
  // await envoyerTransaction(tx);
}
```

**Dépannage**

*   **Erreurs de gas:** Assurez-vous d'avoir suffisamment de MATIC dans votre portefeuille pour couvrir les frais de gas.
*   **Transactions bloquées:** Si une transaction est bloquée, essayez d'augmenter les frais de gas dans votre portefeuille et de la resoumettre.
*   **Problèmes de réseau:** Vérifiez l'état du réseau Polygon et ParaSwap.

**Avertissements**

*   Effectuez vos propres recherches (DYOR) avant d'utiliser des protocoles DeFi.
*   Les swaps peuvent être sujets à des slippage (décalage de prix).
*   Soyez vigilant face aux arnaques et aux sites web frauduleux.
*   Ce tutoriel est fourni à titre informatif uniquement et ne constitue pas un conseil financier.

**Contact**

Pour toute question ou assistance, veuillez contacter [NOM] à [EMAIL] ou [IP].


## Effectuer un swap sur ParaSwap (Polygon)

| Tags |
|------|
| `ParaSwap` `Polygon` `Swap` `MetaMask` `DeFi` |

Pour effectuer un swap sur ParaSwap en utilisant le réseau Polygon (anciennement Matic), suivez les étapes ci-dessous. Assurez-vous de disposer d'un portefeuille compatible avec le réseau Polygon, comme MetaMask, et d'avoir suffisamment de tokens et de MATIC pour les frais de gaz.

<ol>
<li>
Connectez votre portefeuille :
Rendez-vous sur le site de ParaSwap (https://paraswap.io/) et cliquez sur "Connect Wallet" pour connecter votre portefeuille compatible, comme MetaMask.
</li>
<li>
Configurez votre portefeuille pour Polygon :
Si vous n'avez pas encore configuré votre portefeuille MetaMask pour le réseau Polygon, suivez ces étapes :
<ol type="a">
<li>Ouvrez MetaMask et cliquez sur le menu déroulant en haut, puis sur "Custom RPC".</li>
<li>Saisissez les informations suivantes :</li>
<ul>
<li>Network Name: Polygon</li>
<li>New RPC URL: https://rpc-mainnet.maticvigil.com/</li>
<li>Chain ID: 137</li>
<li>Currency Symbol: MATIC</li>
<li>Block Explorer URL: https://polygonscan.com/</li>
</ul>
<li>Cliquez sur "Save" pour enregistrer les paramètres.</li>
</ol>
</li>
<li>
Approvisionnez votre portefeuille avec des tokens et des MATIC :
Assurez-vous que votre portefeuille contient les tokens que vous souhaitez échanger, ainsi que des MATIC pour couvrir les frais de gaz. Si vous avez besoin de transférer des tokens vers Polygon, vous pouvez utiliser un pont tel que le Polygon Bridge (https://wallet.polygon.technology/bridge/).
</li>
<li>
Sélectionnez les tokens à échanger :
Sur la page principale de ParaSwap, choisissez le token que vous souhaitez échanger (de) et le token que vous voulez recevoir (à). Saisissez le montant que vous souhaitez échanger.
</li>
<li>
Autorisez ParaSwap à utiliser vos tokens :
Si c'est la première fois que vous utilisez ParaSwap avec ce token, vous devrez peut-être autoriser ParaSwap à interagir avec vos tokens en cliquant sur "Unlock" ou "Approve". Confirmez la transaction dans votre portefeuille.
</li>
<li>
Confirmez l'échange :
Une fois que vous avez sélectionné les tokens et saisi le montant, ParaSwap vous montrera le taux de change et le montant que vous recevrez. Si vous êtes satisfait des détails, cliquez sur "Swap" et confirmez la transaction dans votre portefeuille.
</li>
<li>
Attendez la confirmation de la transaction :
Le temps de confirmation peut varier en fonction de la congestion du réseau. Une fois que la transaction est confirmée, vous verrez les tokens échangés dans votre portefeuille.
</li>
</ol>
Notez que les étapes spécifiques peuvent varier légèrement en fonction de l'interface utilisateur de ParaSwap et des mises à jour du réseau Polygon.


## Effectuer un swap avec Python, Web3 et ParaSwap

| Tags |
|------|
| `Python` `Web3` `ParaSwap` `Polygon` `Smart Contract` |

Pour effectuer un swap en utilisant Python, web3 et le smart contract ParaSwap sur le réseau Polygon, suivez ces étapes :

1.  **Installation des dépendances**

    Installez les bibliothèques Python `web3` et `eth-account` en utilisant pip :

    ```bash
    pip install web3 eth-account
    ```

2.  **Obtention des informations du contrat**

    Récupérez les informations du contrat ParaSwap (adresse du contrat, ABI) pour Polygon. Vous pouvez les trouver sur [URL].

3.  **Préparation du code Python**

    ```python
    import json
    from web3 import Web3
    from eth_account import Account

    # Configuration des informations du réseau Polygon
    polygon_rpc_url = "[URL_RPC]"
    w3 = Web3(Web3.HTTPProvider(polygon_rpc_url))

    # Clés privées et publiques
    private_key = "[PRIVATE_KEY]"
    account = Account.from_key(private_key)
    public_key = account.address

    # Adresse et ABI du contrat ParaSwap
    paraswap_contract_address = "[PARASWAP_CONTRACT_ADDRESS]"
    paraswap_abi = json.loads("[PARASWAP_CONTRACT_ABI_JSON]")

    # Configuration des tokens à échanger
    src_token = "[SRC_TOKEN_ADDRESS]"
    dest_token = "[DEST_TOKEN_ADDRESS]"
    src_amount = 100  # Montant du token source à échanger
    min_destination_amount = 90  # Montant minimum du token de destination à recevoir

    # Création d'une instance du contrat ParaSwap
    contract = w3.eth.contract(address=Web3.toChecksumAddress(paraswap_contract_address), abi=paraswap_abi)

    # Construction de la transaction
    transaction = contract.functions.swap(
        src_token,
        dest_token,
        src_amount,
        min_destination_amount,
        public_key,  # Beneficiary
        0,  # Referral
        '0x',  # Data
    ).buildTransaction({
        'chainId': 137,
        'gas': 250000,
        'gasPrice': w3.toWei('10', 'gwei'),
        'nonce': w3.eth.getTransactionCount(public_key),
    })

    # Signature et envoi de la transaction
    signed_transaction = w3.eth.account.signTransaction(transaction, private_key)
    transaction_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

    # Affichage de l'identifiant de la transaction
    print(f"Transaction hash: {transaction_hash.hex()}")
    ```

    Remplacez `[PRIVATE_KEY]`, `[PARASWAP_CONTRACT_ADDRESS]`, `[PARASWAP_CONTRACT_ABI_JSON]`, `[SRC_TOKEN_ADDRESS]`, `[DEST_TOKEN_ADDRESS]` et `[URL_RPC]` par les valeurs appropriées.

4.  **Exécution du code Python**

    Exécutez le script Python préparé. L'identifiant de la transaction sera affiché. Vérifiez la transaction sur [URL_EXPLORER].

    Ajustez les paramètres de gaz et le prix du gaz en fonction des conditions du réseau.
