## Superposition de graphiques de bougies

| Tags |
|------|
| `Trading` `Finance` `Python` `Graphiques` |

L'objectif est de superposer des graphiques en chandeliers de différentes périodes dans un seul et même graphique, en utilisant Python.

L'exemple de code suivant montre comment réaliser cette superposition. Il se base sur la librairie `mplfinance`.

```python
import yfinance as yf
import mplfinance as mpf

# Récupération des données
ticker = "AAPL"
data_1h = yf.download(ticker, period="7d", interval="1h")
data_1d = yf.download(ticker, period="7d", interval="1d")

# Création des graphiques
mpf.plot(data_1h, type="candle", style="yahoo", title=f"{ticker} - 1H et 1D")
mpf.plot(data_1d, type="candle", style="yahoo", addplot=mpf.make_addplot(data_1h["Close"], panel=0, color="blue", title="1H Close"))
```

Ce script télécharge les données de [NOM] pour les périodes de 1 heure et 1 jour, puis les affiche en utilisant `mplfinance`. La fonction `make_addplot` est employée pour superposer le graphique 1 heure sur le graphique 1 jour.


## Superposition de graphiques TradingView JS

| Tags |
|------|
| `TradingView` `JavaScript` `Graphiques` `Widget API` |

Pour superposer des graphiques à bougies de différentes périodes (par exemple, bougies de 12 heures sur bougies d'1 heure) en utilisant la bibliothèque JavaScript TradingView, suivez les étapes ci-dessous.  Cela implique principalement l'utilisation de la Widget API de TradingView pour intégrer plusieurs séries de données sur un seul graphique.


## Intégration de la bibliothèque TradingView

| Tags |
|------|
| `TradingView` `JavaScript` `HTML` `Bibliothèque` |

Assurez-vous d'avoir inclus la bibliothèque TradingView dans votre projet. Vous pouvez l'ajouter via un script tag dans votre fichier HTML :

```html
<script type="text/javascript" src="https://s3.tradingview.com/tv.js"></script>
```


## Configuration du Widget de Graphique

| Tags |
|------|
| `TradingView` `JavaScript` `Widget` `Graphique` |

Initialisez le widget de graphique dans votre script JavaScript. Configurez les options requises telles que l'identifiant du conteneur, les symboles et l'intervalle.

```javascript
new TradingView.widget({
  "container_id": "tv_chart_container",
  "autosize": true,
  "symbol": "AAPL",
  "interval": "60",
  "timezone": "exchange",
  "theme": "light",
  "style": "1",
  "toolbar_bg": "#f1f3f6",
  "enable_publishing": false,
  "hide_side_toolbar": false,
  "allow_symbol_change": true,
  "details": true
});
```


## Ajout d'une série supplémentaire

| Tags |
|------|
| `TradingView` `JavaScript` `Graphique` `createStudy` `addSeries` |

Pour ajouter une série de bougies de 12 heures sur le même graphique, utilisez la fonction <code>createStudy</code> ou <code>addSeries</code>. Cela peut varier en fonction de la version de la bibliothèque que vous utilisez. Voici un exemple général de la façon dont vous pourriez ajouter cette série :

```javascript
chartWidget.onChartReady(function() {
  var chart = chartWidget.chart();
  chart.createStudy('Moving Average', false, false, [14], null, {'Plot.color': 'blue'});

  // Ajouter une série de bougies de 12 heures
  chart.createStudy('Heikin Ashi', true, true, [720], function(series) {
    series.setSymbol("AAPL", {
      timeframe: '720'
    });
  });
});
```


## Test et ajustement du graphique

| Tags |
|------|
| `TradingView` `Pine Script` `Graphique` |

Une fois le code intégré, validez l'affichage correct des bougies de 12 heures superposées aux bougies d'une heure. Ajustez les paramètres selon les besoins pour un rendu et un comportement optimaux.


## Informations complémentaires sur l'implémentation

| Tags |
|------|
| `TradingView` `API` `Débogage` |

La documentation officielle de TradingView constitue la ressource de référence pour les options et les méthodes actuelles de l'API, qui peut évoluer.

Le débogage des implémentations peut être réalisé grâce aux outils de développement intégrés à votre navigateur.

Pour les implémentations spécifiques ou avancées, une exploration approfondie de la documentation de l'API ou une consultation des forums et communautés spécialisées de TradingView peut s'avérer nécessaire.


## Bibliothèques alternatives de visualisation financière

| Tags |
|------|
| `JavaScript` `Visualisation de données` `TradingView` `Finance` |

Si vous souhaitez superposer des bougies de différentes périodicités (par exemple, des bougies de 12 heures sur des bougies d'1 heure) et que vous cherchez une alternative à TradingView, plusieurs bibliothèques JavaScript populaires sont disponibles pour la visualisation de données financières. Voici quelques options potentielles :


## Lightweight Charts de TradingView

| Tags |
|------|
| `Lightweight Charts` `TradingView` `JavaScript` `Graphiques financiers` |

Lightweight Charts, également de TradingView, est une bibliothèque plus légère et plus rapide, spécialement conçue pour les graphiques financiers. Elle prend en charge la superposition de données provenant de diverses sources, avec moins de surcharge que le widget TradingView complet.

```javascript
const chart = LightweightCharts.createChart(document.body, { width: 600, height: 300 });
const lineSeries = chart.addLineSeries();
const candleSeries = chart.addCandlestickSeries();

// Exemple d'ajout de données pour chaque série
candleSeries.setData([
  { time: '2020-01-01', open: 100, high: 110, low: 90, close: 105 },
  // plus de données...
]);
lineSeries.setData([
  { time: '2020-01-01', value: 105 },
  // plus de données...
]);
```


## ApexCharts : Bibliothèque de graphiques moderne

| Tags |
|------|
| `ApexCharts` `Graphiques` `JavaScript` `Candlestick` |

ApexCharts est une bibliothèque de graphiques moderne qui prend en charge de nombreux types de graphiques, y compris les graphiques à bougies. Elle est facile à utiliser et hautement personnalisable, bien que moins spécialisée dans les données financières que Lightweight Charts.

```javascript
var options = {
  series: [{
    name: 'Candle',
    type: 'candlestick',
    data: [
      {x: new Date(1538778600000), y: [6629.81, 6650.5, 6623.04, 6633.33]},
      // plus de données...
    ]
  }, {
    name: 'Line',
    type: 'line',
    data: [
      {x: new Date(1538778600000), y: 6633.33},
      // plus de données...
    ]
  }],
  chart: {
    height: 350,
    type: 'line',
  },
  stroke: {
    width: [0, 4]
  },
  title: {
    text: 'CandleStick Chart'
  },
  yaxis: {
    labels: {
      formatter: function (value) {
        return value.toFixed(0);
      }
    }
  }
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
```


## Chart.js pour graphiques financiers

| Tags |
|------|
| `Chart.js` `JavaScript` `graphique à bougies` `chartjs-chart-financial` |

Chart.js est une bibliothèque JavaScript polyvalente pour la création de graphiques. Pour les graphiques en chandeliers, un plugin tel que <code>chartjs-chart-financial</code> est requis.

```javascript
var ctx = document.getElementById('myChart').getContext('2d');
var chart = new Chart(ctx, {
    type: 'candlestick',
    data: {
        datasets: [{
            label: 'CHRT - Stock',
            data: [{
                t: new Date('2019-03-01'),
                o: 145.3,
                h: 148.2,
                l: 143.1,
                c: 145.8
            },
            // plus de données...
            ]
        }]
    },
    options: {
        scales: {
            xAxes: [{
                type: 'time',
                time: {
                    unit: 'month'
                }
            }]
        }
    }
});
```

Chaque option présente des avantages et des inconvénients en termes de fonctionnalités, d'utilisation et de performances. Le choix doit être basé sur les exigences spécifiques, en particulier pour la manipulation et la visualisation des données financières.
