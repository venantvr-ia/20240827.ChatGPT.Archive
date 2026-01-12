## Téléchargement de données historiques Gate.io

| Tags |
|------|
| `Gate.io` `API` `Données historiques` `Trading` |

Pour télécharger des données historiques de Gate.io, vous pouvez utiliser l'API officielle. Voici un exemple de comment récupérer les données de prix d'une paire de trading spécifique.

**Requête GET pour les données de prix (candles/ohlc)**

```
GET /api/v4/ spot/candlesticks HTTP/1.1
Host: api.gateio.ws
Content-Type: application/json
```

**Paramètres de la requête :**

*   `currency_pair` : La paire de trading (par exemple, BTC_USDT).
*   `limit` : Le nombre de bougies à retourner (max 1000, par défaut 100).
*   `interval` : La période de temps pour chaque bougie (par exemple, 1m, 5m, 1h, 1d).
*   `from` : Timestamp Unix (secondes) pour le début de la période.
*   `to` : Timestamp Unix (secondes) pour la fin de la période.

**Exemple de réponse (JSON):**

```json
[
  [
    1678886400, // Timestamp
    "26388.1",  // Open
    "26391.2",  // High
    "26385.5",  // Low
    "26388.9",  // Close
    "1.5888"   // Volume
  ],
  // ...autres données
]
```

**Informations de contact :**

Pour toute question ou assistance, veuillez contacter [NOM] à [EMAIL] ou consulter la documentation de l'API Gate.io. Pour les requêtes de support technique, contactez [NOM] à [EMAIL] ou [NOM] à [EMAIL].


## Téléchargement de Chandeliers CCXT sur Gate.io

| Tags |
|------|
| `Python` `ccxt` `Gate.io` `candlesticks` |

Vous pouvez utiliser le code suivant pour télécharger les données de chandeliers (candles) pour trois intervalles de temps différents (4h, 2h, 1h) sur Gate.io, pour une période définie par deux dates (début et fin), et sauvegarder les fichiers dans des répertoires nommés selon chaque intervalle de temps.

```python
import ccxt
import os
import time
from datetime import datetime, timedelta

# Configuration
exchange_id = 'gateio'
symbol = 'BTC/USDT'
timeframes = ['4h', '2h', '1h']
start_date = '2023-01-01'
end_date = '2023-01-03'
output_dir = 'candlesticks_data'

# Initialisation de l'échange
exchange = ccxt.gateio()

# Fonction pour convertir une date en timestamp
def date_to_timestamp(date_str):
    return exchange.parse8601(date_str + 'T00:00:00Z')

# Création des répertoires de sortie
for timeframe in timeframes:
    os.makedirs(os.path.join(output_dir, timeframe), exist_ok=True)

# Boucle sur les intervalles de temps
for timeframe in timeframes:
    start_timestamp = date_to_timestamp(start_date)
    end_timestamp = date_to_timestamp(end_date)
    all_ohlcv = []

    while start_timestamp < end_timestamp:
        try:
            ohlcv = exchange.fetch_ohlcv(symbol, timeframe, start_timestamp, limit=1000)
            if not ohlcv:
                break
            all_ohlcv.extend(ohlcv)
            start_timestamp = ohlcv[-1][0] + exchange.parse_timeframe(timeframe) * 1000
            time.sleep(exchange.rateLimit / 1000) # Respect des limites de taux
        except ccxt.ExchangeError as e:
            print(f"Erreur lors de la récupération des données : {e}")
            break
        except Exception as e:
            print(f"Une erreur inattendue s'est produite : {e}")
            break

    # Sauvegarde des données dans un fichier CSV
    if all_ohlcv:
        filename = f"{symbol.replace('/', '_')}_{timeframe}_{start_date}_{end_date}.csv"
        filepath = os.path.join(output_dir, timeframe, filename)
        with open(filepath, 'w') as f:
            for candle in all_ohlcv:
                timestamp = datetime.fromtimestamp(candle[0] / 1000).strftime('%Y-%m-%d %H:%M:%S')
                line = f"{timestamp},{candle[1]},{candle[2]},{candle[3]},{candle[4]},{candle[5]}\n"
                f.write(line)
        print(f"Données sauvegardées dans {filepath}")
    else:
        print(f"Aucune donnée n'a été récupérée pour {timeframe}")
```

**Explication du code :**

1.  **Configuration :** Définit les paramètres tels que l'ID de l'échange, le symbole, les intervalles de temps, les dates de début et de fin, et le répertoire de sortie.
2.  **Initialisation :** Initialise l'objet d'échange `ccxt.gateio()`.
3.  **Fonction `date_to_timestamp` :** Convertit une chaîne de date en timestamp.
4.  **Création des répertoires :** Crée les répertoires pour chaque intervalle de temps si ils n'existent pas.
5.  **Boucle sur les intervalles de temps :**
    *   Récupère les données de chandeliers en utilisant `exchange.fetch_ohlcv()`.
    *   Gère la pagination pour récupérer toutes les données sur la période spécifiée.
    *   Respecte les limites de taux de l'API.
    *   Gère les erreurs potentielles.
6.  **Sauvegarde des données :** Enregistre les données de chandeliers dans un fichier CSV, avec un formatage approprié.

**Pour utiliser le code :**

1.  **Installation :** Assurez-vous d'avoir installé la librairie `ccxt` : `pip install ccxt`.
2.  **Exécution :** Exécutez le script Python. Les fichiers CSV seront créés dans le répertoire `candlesticks_data`.


## Téléchargement de données historiques Gate.io avec CCXT

| Tags |
|------|
| `Python` `CCXT` `Gate.io` `API` `Trading` |

Pour télécharger des données historiques de bougies (candles) sur Gate.io en utilisant la bibliothèque CCXT en Python, suivez les étapes suivantes.

Tout d'abord, assurez-vous que CCXT est installé. Si ce n'est pas le cas, installez-le via pip :

```bash
pip install ccxt
```

Utilisez ensuite le script suivant comme base pour télécharger les données de bougies pour les intervalles de 4 heures, 2 heures et 1 heure. Ce script crée des répertoires basés sur les intervalles de temps spécifiés, télécharge les données pour chaque intervalle entre les dates de début et de fin spécifiées, puis sauvegarde ces données dans des fichiers CSV dans les répertoires correspondants.

```python
import ccxt
import pandas as pd
import os
from datetime import datetime

# Configuration
exchange_id = 'gateio'
symbol = 'BTC/USDT'  # Exemple de symbole, à ajuster selon le besoin
start_date = '2022-01-01T00:00:00Z'  # Date de début
end_date = '2022-01-10T00:00:00Z'  # Date de fin
timeframes = {
    '4h': '4h',
    '2h': '2h',
    '1h': '1h',
}

# Initialisation de l'échange
exchange = getattr(ccxt, exchange_id)({
    'rateLimit': 2000,
    'enableRateLimit': True,
})

# Fonction pour télécharger et sauvegarder les données
def fetch_save_candles(timeframe):
    directory = f"./{timeframe}"
    os.makedirs(directory, exist_ok=True)
    since = exchange.parse8601(start_date)
    end_timestamp = exchange.parse8601(end_date)
    all_candles = []

    while since < end_timestamp:
        candles = exchange.fetch_ohlcv(symbol, timeframe, since)
        if not candles:
            break
        last = candles[-1][0]
        all_candles += candles
        since = last + exchange.parse_timeframe(timeframe) * 1000  # Déplacer le curseur
        
        # Petite pause pour respecter le rate limit
        exchange.rateLimit

    df = pd.DataFrame(all_candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    filepath = f"{directory}/{symbol.replace('/', '-')}-{start_date[:10]}_{end_date[:10]}.csv"
    df.to_csv(filepath, index=False)
    print(f"Les données pour {timeframe} ont été sauvegardées dans {filepath}")

# Téléchargement et sauvegarde pour chaque intervalle
for timeframe in timeframes.values():
    fetch_save_candles(timeframe)
```

Ce script utilise la bibliothèque pandas pour faciliter la manipulation des données et leur sauvegarde en format CSV. Assurez-vous d'avoir pandas installé (`pip install pandas`) pour éviter tout problème lors de l'exécution.

Notez que les API et les limites de taux peuvent varier, et ce script peut nécessiter des ajustements en fonction de ces limites et de la quantité de données demandées. De plus, vous devrez ajuster le `symbol` et les `start_date`/`end_date` selon vos besoins spécifiques.

Ce script est un point de départ. Vous pourriez avoir besoin de l'adapter en fonction de vos besoins spécifiques, des limites de l'API Gate.io, ou de gérer les éventuelles erreurs/exceptions qui peuvent survenir lors des requêtes API.


## Synchroniser les données Gate.io avec des timeframes

| Tags |
|------|
| `Python` `CCXT` `Gate.io` `Timeframes` `API` |

Pour synchroniser les points de départ et de fin des données sur Gate.io lors du téléchargement de données sur différents timeframes, convertissez les dates de début et de fin en timestamps uniques. Utilisez ces timestamps pour toutes les requêtes, garantissant ainsi une synchronisation des données.

Le script suivant illustre cette approche :

```python
import ccxt
import pandas as pd
import os
from datetime import datetime

# Configuration
exchange_id = 'gateio'
symbol = 'BTC/USDT'  # Ajuster selon le besoin
start_date_str = '2022-01-01T00:00:00Z'  # Date de début en string
end_date_str = '2022-01-10T00:00:00Z'  # Date de fin en string
timeframes = ['4h', '2h', '1h']

# Initialisation de l'échange
exchange = getattr(ccxt, exchange_id)({
    'rateLimit': 2000,
    'enableRateLimit': True,
})

# Conversion des dates de début et de fin en timestamp
start_timestamp = exchange.parse8601(start_date_str)
end_timestamp = exchange.parse8601(end_date_str)

# Fonction pour télécharger et sauvegarder les données
def fetch_save_candles(timeframe):
    directory = f"./{timeframe}_data"
    os.makedirs(directory, exist_ok=True)
    all_candles = []

    since = start_timestamp
    while since < end_timestamp:
        candles = exchange.fetch_ohlcv(symbol, timeframe, since, limit=1000)  # Assure-toi que le 'limit' est adéquat
        if not candles:
            break
        last = candles[-1][0]
        all_candles.extend(candles)
        since = last + 1  # Pour éviter de récupérer la dernière bougie déjà téléchargée
        
        # Petite pause pour respecter le rate limit
        exchange.rateLimit

    # Création du DataFrame et sauvegarde en CSV
    df = pd.DataFrame(all_candles, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    filepath = f"{directory}/{symbol.replace('/', '-')}-{start_date_str[:10]}_to_{end_date_str[:10]}.csv"
    df.to_csv(filepath, index=False)
    print(f"Les données pour {timeframe} ont été sauvegardées dans {filepath}")

# Téléchargement et sauvegarde pour chaque intervalle
for timeframe in timeframes:
    fetch_save_candles(timeframe)
```

Ce script utilise <code>start_timestamp</code> comme point de départ commun et <code>end_timestamp</code> pour contrôler la fin du téléchargement. La gestion de la limite (<code>limit=1000</code>) dans <code>fetch_ohlcv</code> est essentielle pour respecter les limites de l'API et récupérer toutes les données dans l'intervalle spécifié.

Ajustez les paramètres tels que les dates, le symbole et assurez-vous que les bibliothèques CCXT et pandas sont installées avant l'exécution.
