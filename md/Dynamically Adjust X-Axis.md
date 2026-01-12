## Ajustement dynamique de l'axe des abscisses

| Tags |
|------|
| `graphique` `axe des abscisses` `JavaScript` `D3.js` |

Ce document présente comment ajuster dynamiquement l'échelle de l'axe des abscisses d'un graphique en utilisant JavaScript et la librairie D3.js. L'objectif est de s'assurer que les données soient toujours visualisées correctement, même lorsque les valeurs sur l'axe des abscisses changent.

### Pré-requis

*   Connaissance de base de HTML, CSS et JavaScript.
*   Compréhension des concepts fondamentaux de D3.js (sélections, liaisons de données, échelles).

### Configuration initiale

Supposons que nous ayons un fichier HTML de base :

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Dynamic X-Axis</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        .axis path,
        .axis line {
            fill: none;
            stroke: black;
            shape-rendering: crispEdges;
        }
    </style>
</head>
<body>
    <div id="chart"></div>
    <script src="script.js"></script>
</body>
</html>
```

Et un fichier JavaScript `script.js` :

```javascript
// Définition des données initiales
const data = [
    { date: new Date("2023-01-01"), value: 10 },
    { date: new Date("2023-01-15"), value: 20 },
    { date: new Date("2023-02-01"), value: 15 },
    { date: new Date("2023-02-15"), value: 25 }
];

// Configuration du graphique
const margin = { top: 20, right: 20, bottom: 30, left: 50 };
const width = 600 - margin.left - margin.right;
const height = 400 - margin.top - margin.bottom;

// Création du conteneur SVG
const svg = d3.select("#chart")
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

// Création des échelles
const xScale = d3.scaleTime()
    .domain(d3.extent(data, d => d.date))
    .range([0, width]);

const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.value)])
    .range([height, 0]);

// Création de l'axe des abscisses
const xAxis = d3.axisBottom(xScale);

// Ajout de l'axe des abscisses au graphique
const xAxisGroup = svg.append("g")
    .attr("class", "axis")
    .attr("transform", `translate(0,${height})`)
    .call(xAxis);

// Ajout des points de données (exemple)
svg.selectAll("circle")
    .data(data)
    .enter()
    .append("circle")
    .attr("cx", d => xScale(d.date))
    .attr("cy", d => yScale(d.value))
    .attr("r", 5);
```

### Mise à jour dynamique de l'axe des abscisses

Pour ajuster l'axe des abscisses dynamiquement, nous devons redéfinir l'échelle et redessiner l'axe à chaque changement de données.

```javascript
function updateChart(newData) {
    // Mise à jour de l'échelle des abscisses
    xScale.domain(d3.extent(newData, d => d.date));

    // Mise à jour de l'axe des abscisses
    xAxisGroup.transition() // Ajout d'une transition pour une animation fluide
        .duration(750) // Durée de la transition en millisecondes
        .call(xAxis);

    // Mise à jour des points de données
    const circles = svg.selectAll("circle")
        .data(newData);

    circles.exit().remove(); // Suppression des anciens éléments

    circles.transition()
        .duration(750)
        .attr("cx", d => xScale(d.date))
        .attr("cy", d => yScale(d.value));

    circles.enter()
        .append("circle")
        .attr("cx", d => xScale(d.date))
        .attr("cy", d => yScale(d.value))
        .attr("r", 5);
}

// Exemple d'appel pour mettre à jour le graphique avec de nouvelles données
// Simulation de nouvelles données après un certain temps
setTimeout(() => {
    const newData = [
        { date: new Date("2023-01-01"), value: 15 },
        { date: new Date("2023-01-20"), value: 25 },
        { date: new Date("2023-02-10"), value: 20 },
        { date: new Date("2023-02-28"), value: 30 }
    ];
    updateChart(newData);
}, 3000); // Mise à jour après 3 secondes
```

Dans cet exemple, la fonction `updateChart` prend de nouvelles données en paramètre, recalcule l'échelle de l'axe des abscisses en fonction de ces nouvelles données et met à jour l'axe.  La fonction utilise également des transitions pour animer les changements, ce qui rend le graphique plus interactif.  Les points de données sont aussi mis à jour, en supprimant les anciens, et en ajoutant/mettant à jour les nouveaux.

### Conclusion

En suivant ces étapes, vous pouvez créer des graphiques D3.js avec des axes des abscisses qui s'adaptent dynamiquement aux changements de données.  L'utilisation des transitions permet d'améliorer l'expérience utilisateur.  Ce concept est applicable à d'autres types de graphiques et d'échelles.


## Récupération et ajustement des timestamps

| Tags |
|------|
| `JavaScript` `Timestamp` `Échelle de temps` |

Récupérer les timestamps minimum et maximum des séries temporelles (1h et 12h) en JavaScript et ajuster l'échelle en conséquence.


## Configuration des options de l'axe X dans ApexCharts

| Tags |
|------|
| `ApexCharts` `JavaScript` `xaxis` `candlestick` |

```javascript
const options1h = {
    chart: {
        type: 'candlestick',
        height: 350,
        width: 1300,
        animations: {
            enabled: false,
            easing: 'linear',
            dynamicAnimation: {
                speed: 1000
            }
        }
    },
    series: [{
        name: '1h Candles',
    }],
    xaxis: {
        type: 'datetime',
        range: 3600000 * 12, // Afficher les dernières 12 heures
        forceNiceScale: true,
        labels: {
            formatter: function(value) {
                return new Date(value).toLocaleTimeString();
            }
        }
    }
};

const options12h = {
    chart: {
        type: 'candlestick',
        height: 350,
        width: 1500,
        animations: {
            enabled: false,
            easing: 'linear',
            dynamicAnimation: {
                speed: 1000
            }
        }
    },
    series: [{
        name: '12h Candles',
    }],
    xaxis: {
        type: 'datetime',
        range: 3600000 * 24 * 5, // Afficher les derniers 5 jours
        forceNiceScale: true,
        labels: {
            formatter: function(value) {
                return new Date(value).toLocaleDateString();
            }
        }
    }
};

const chart1h = new ApexCharts(document.querySelector("#chart1h"), options1h);
const chart12h = new ApexCharts(document.querySelector("#chart12h"), options12h);

chart1h.render();
chart12h.render();

function fetchData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const data12h = data.data_12h.map(d => ({
                x: d.timestamp,
                y: [d.open, d.high, d.low, d.close]
            }));
            const data1h = data.data_1h.map(d => ({
                x: d.timestamp,
                y: [d.open, d.high, d.low, d.close]
            }));

            // Définir dynamiquement min et max de l'axe X pour scroller
            const lastTimestamp1h = data1h[data1h.length - 1].x;
            const lastTimestamp12h = data12h[data12h.length - 1].x;

            chart1h.updateOptions({
                xaxis: {
                    min: lastTimestamp1h - 3600000 * 12,
                    max: lastTimestamp1h
                }
            });
            chart12h.updateOptions({
                xaxis: {
                    min: lastTimestamp12h - 3600000 * 24 * 5,
                    max: lastTimestamp12h
                }
            });

            chart1h.updateSeries([{ name: '1h Candles', data: data1h }]);
            chart12h.updateSeries([{ name: '12h Candles', data: data12h }]);
        })
        .catch(error => console.error('Error fetching data:', error));

    setTimeout(fetchData, 1000);  // Récupérer les nouvelles données chaque seconde
}

fetchData();  // Initialisation de la récupération
```


## Ajustement d'échelle temporelle en JavaScript
| Tags |
|------|
| `JavaScript` `Time Series` `Timestamp` `Interval` |

Il semble que vous travailliez avec JavaScript pour manipuler des séries temporelles, en utilisant des intervalles d'une heure et de douze heures. Pour ajuster une échelle de temps basée sur les valeurs minimales et maximales des timestamps de ces séries, vous pouvez suivre l'approche suivante :

1.  **Récupération des timestamps minimaux et maximaux** : Commencez par extraire les valeurs minimales et maximales des timestamps des deux séries.
2.  **Ajustement de**


## Visualisation ApexCharts : Bougies 1h & 12h

| Tags |
|------|
| `JavaScript` `ApexCharts` `Graphique` `Finance` |


## Ajustement des échelles temporelles avec ApexCharts

| Tags |
|------|
| `JavaScript` `ApexCharts` `Graphique` `Timestamp` |

```javascript
const options1h = {
    chart: {
        type: 'candlestick',
        height: 350,
        width: 1300,
        animations: {
            enabled: false,
            easing: 'linear',
            dynamicAnimation: {
                speed: 1000
            }
        }
    },
    series: [{
        name: '1h Candles',
    }],
    xaxis: {
        type: 'datetime',
        range: 3600000 * 120, // Afficher les dernières 12 heures
        forceNiceScale: true,
        labels: {
            formatter: function(value) {
                return new Date(value).toLocaleTimeString();
            }
        }
    }
};

const options12h = {
    chart: {
        type: 'candlestick',
        height: 350,
        width: 1500,
        animations: {
            enabled: false,
            easing: 'linear',
            dynamicAnimation: {
                speed: 1000
            }
        }
    },
    series: [{
        name: '12h Candles',
    }],
    xaxis: {
        type: 'datetime',
        range: 3600000 * 24 * 5, // Afficher les dernières 5 jours
        forceNiceScale: true,
        labels: {
            formatter: function(value) {
                return new Date(value).toLocaleDateString();
            }
        }
    }
};

const chart1h = new ApexCharts(document.querySelector("#chart1h"), options1h);
const chart12h = new ApexCharts(document.querySelector("#chart12h"), options12h);

chart1h.render();
chart12h.render();

function fetchData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const data12h = data.data_12h.map(d => ({
                x: d.timestamp,
                y: [d.open, d.high, d.low, d.close]
            }));
            const data1h = data.data_1h.map(d => ({
                x: d.timestamp,
                y: [d.open, d.high, d.low, d.close]
            }));

            // Définir dynamiquement min et max de l'axe X pour scroller
            const lastTimestamp1h = data1h[data1h.length - 1].x;
            const lastTimestamp12h = data12h[data12h.length - 1].x;

            chart1h.updateOptions({
                xaxis: {
                    min: lastTimestamp1h - 3600000 * 12,
                    max: lastTimestamp1h
                }
            });
            chart12h.updateOptions({
                xaxis: {
                    min: lastTimestamp12h - 3600000 * 24 * 5,
                    max: lastTimestamp12h
                }
            });

            chart1h.updateSeries([{ name: '1h Candles', data: data1h }]);
            chart12h.updateSeries([{ name: '12h Candles', data: data12h }]);
        })
        .catch(error => console.error('Error fetching data:', error));

    setTimeout(fetchData, 1000);  // Récupérer les nouvelles données chaque seconde
}

fetchData();  // Initialisation de la récupération
```


## Ajustement dynamique de l'échelle des axes X avec ApexCharts

| Tags |
|------|
| `ApexCharts` `JavaScript` `Candlestick` `Graphique` `Timestamp` `Axe X` |

Pour ajuster dynamiquement l'échelle de l'axe des x en fonction des timestamps minimaux et maximaux des données dans vos graphiques de bougies (candlestick charts) sur ApexCharts, vous pouvez modifier votre fonction `fetchData()` pour calculer ces valeurs et les appliquer aux options des graphiques. Voici comment :

1.  Calculez le `min` et le `max` pour les timestamps des données 1h et 12h.
2.  Mettez à jour les options de l'axe des x pour les graphiques `chart1h` et `chart12h` en fonction de ces valeurs.

Voici le code JavaScript modifié pour incorporer ces changements :

```javascript
function fetchData() {
    fetch('/data')
        .then(response => response.json())
        .then(data => {
            const data12h = data.data_12h.map(d => ({
                x: d.timestamp,
                y: [d.open, d.high, d.low, d.close]
            }));
            const data1h = data.data_1h.map(d => ({
                x: d.timestamp,
                y: [d.open, d.high, d.low, d.close]
            }));

            // Calculer les timestamps minimaux et maximaux pour les données 1h et 12h
            const minTimestamp1h = Math.min(...data1h.map(d => d.x));
            const maxTimestamp1h = Math.max(...data1h.map(d => d.x));
            const minTimestamp12h = Math.min(...data12h.map(d => d.x));
            const maxTimestamp12h = Math.max(...data12h.map(d => d.x));

            // Mettre à jour les options des axes des x pour les graphiques
            chart1h.updateOptions({
                xaxis: {
                    min: minTimestamp1h,
                    max: maxTimestamp1h
                }
            });
            chart12h.updateOptions({
                xaxis: {
                    min: minTimestamp12h,
                    max: maxTimestamp12h
                }
            });

            chart1h.updateSeries([{ name: '1h Candles', data: data1h }]);
            chart12h.updateSeries([{ name: '12h Candles', data: data12h }]);
        })
        .catch(error => console.error('Error fetching data:', error));

    setTimeout(fetchData, 1000);  // Récupérer les nouvelles données chaque seconde
}

fetchData();  // Initialisation de la récupération
```

Ce code met à jour les plages `min` et `max` de l'axe des x pour chacun des graphiques basé sur les timestamps minimaux et maximaux présents dans les données chargées. Cela garantit que les échelles des graphiques sont calibrées pour afficher toutes les données pertinentes dès leur chargement.


## Formatage de date et heure avec toLocaleString

| Tags |
|------|
| `JavaScript` `toLocaleString` `Date` |

Pour formater les étiquettes de l'axe des x afin d'inclure la date et l'heure, les fonctions `formatter` des options de l'axe des x de vos graphiques peuvent être modifiées. L'utilisation de `toLocaleString()` avec des options de formatage appropriées permet d'afficher les deux informations.

Ajustement des fonctions de formateur pour les deux graphiques :

```javascript
const options1h = {
    chart: {
        type: 'candlestick',
        height: 350,
        width: 1300,
        animations: {
            enabled: false,
            easing: 'linear',
            dynamicAnimation: {
                speed: 1000
            }
        }
    },
    series: [{
        name: '1h Candles',
    }],
    xaxis: {
        type: 'datetime',
        range: 3600000 * 120, // Afficher les dernières 12 heures
        forceNiceScale: true,
        labels: {
            formatter: function(value) {
                return new Date(value).toLocaleString('fr-FR', {
                    hour: '2-digit',
                    minute: '2-digit',
                    second: '2-digit'
                });
            }
        }
    }
};

const options12h = {
    chart: {
        type: 'candlestick',
        height: 350,
        width: 1500,
        animations: {
            enabled: false,
            easing: 'linear',
            dynamicAnimation: {
                speed: 1000
            }
        }
    },
    series: [{
        name: '12h Candles',
    }],
    xaxis: {
        type: 'datetime',
        range: 3600000 * 24 * 5, // Afficher les dernières 5 jours
        forceNiceScale: true,
        labels: {
            formatter: function(value) {
                return new Date(value).toLocaleString('fr-FR', {
                    year: 'numeric',
                    month: '2-digit',
                    day: '2-digit',
                    hour: '2-digit',
                    minute: '2-digit'
                });
            }
        }
    }
};
```

*   Pour `options1h`, `toLocaleString()` est utilisé pour afficher l'heure, les minutes et les secondes, ce qui est pertinent pour une résolution horaire.
*   Pour `options12h`, les options incluent la date complète (année, mois, jour) ainsi que l'heure et les minutes, approprié pour des données sur plusieurs jours.

Ces options utilisent le code de localisation `'fr-FR'` pour formatter la date selon les normes françaises. Le code de localisation ou les options de formatage peuvent être ajustés selon les besoins spécifiques.


## Conversion de 12 heures en millisecondes

| Tags |
|------|
| `Conversion` `Temps` `JavaScript` |

Pour convertir 12 heures en millisecondes, il faut connaître les équivalences suivantes :

*   1 heure = 60 minutes
*   1 minute = 60 secondes
*   1 seconde = 1000 millisecondes

Par conséquent, la conversion se calcule comme suit :

[ 12 \text{ heures} \times 60 \text{ minutes par heure} \times 60 \text{ secondes par minute} \times 1000 \text{ millisecondes par seconde} ]

[ 12 \times 60 \times 60 \times 1000 = 43,200,000 \text{ millisecondes} ]

Par conséquent, 12 heures équivalent à 43 200 000 millisecondes. Cette valeur est utilisable dans du code JavaScript pour définir des intervalles ou des plages temporelles en millisecondes.
