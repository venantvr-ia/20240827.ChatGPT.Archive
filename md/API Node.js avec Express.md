## API Node.js avec Express

| Tags |
|------|
| `Node.js` `Express` `API` |

Créez un projet Node.js et installez les dépendances nécessaires :

```bash
mkdir mon-api-express
cd mon-api-express
npm init -y
npm install express
```

Créez un fichier `index.js` et ajoutez le code suivant :

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```

Exécutez l’application :

```bash
node index.js
```

Ouvrez votre navigateur et accédez à `http://localhost:3000`. Vous devriez voir « Hello World! ».

Pour créer une API avec des routes, vous pouvez utiliser la méthode suivante :

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/users', (req, res) => {
  res.json([
    { id: 1, name: '[NOM]' },
    { id: 2, name: '[NOM]' }
  ]);
});

app.get('/users/:id', (req, res) => {
  const id = req.params.id;
  res.json({ id: id, name: '[NOM]' });
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```

Vous pouvez tester l’API avec `curl` :

```bash
curl http://localhost:3000/users
curl http://localhost:3000/users/1
```

Vous pouvez utiliser `Postman` pour tester l’API.

Pour traiter les données JSON dans le corps de la requête, vous devez utiliser le middleware `express.json()` :

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

app.post('/users', (req, res) => {
  const user = req.body;
  console.log(user);
  res.status(201).json(user);
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```

Vous pouvez tester l’API avec `curl` :

```bash
curl -X POST http://localhost:3000/users -H "Content-Type: application/json" -d '{"name":"[NOM]"}'
```

Pour gérer les erreurs, vous pouvez utiliser le middleware suivant :

```javascript
const express = require('express');
const app = express();
const port = 3000;

app.get('/error', (req, res) => {
  throw new Error('Something went wrong!');
});

app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).send('Something broke!');
});

app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});
```


## Transformer le code PHP en API NodeJS

| Tags |
|------|
| `NodeJS` `API` `PHP` `REST` `Express` |

```javascript
// Installation des dépendances :
// npm install express body-parser cors

const express = require('express');
const bodyParser = require('body-parser');
const cors = require('cors');

const app = express();
const port = 3000; // Ou le port de votre choix

app.use(cors()); // Permet les requêtes cross-origin (CORS)
app.use(bodyParser.json()); // Pour parser les requêtes en JSON
app.use(bodyParser.urlencoded({ extended: true }));

// Simulation de la classe PHP
class mdm_countries {
    constructor() {}

    european_union() {
        return {
            "": "- Choose One -",
            "NOTEU": "Non-EU Resident",
            "BE": "Belgique",
            "BG": "Bulgarie",
            "CZ": "République tchèque",
            "DK": "Danemark",
            "DE": "Allemagne"
        };
    }

    countries_int() {
        return {
            'AD': 'Andorra',
            'AE': 'United Arab Emirates',
            'AF': 'Afghanistan',
            'AG': 'Antigua and Barbuda',
            'AI': 'Anguilla',
            'AL': 'Albania',
            'AM': 'Armenia',
            'AN': 'Netherlands Antilles',
            'AO': 'Angola',
            'AQ': 'Antarctica',
            'AR': 'Argentina',
            'AS': 'American Samoa',
            'AT': 'Austria',
            'AU': 'Australia',
            'AW': 'Aruba',
            'AX': 'Aland Islands',
            'AZ': 'Azerbaijan',
            'BA': 'Bosnia and Herzegovina',
            'BB': 'Barbados',
            'BD': 'Bangladesh',
            'BE': 'Belgium'
        };
    }

    countries_fr() {
        return {
            'AF': 'Afghanistan',
            'ZA': 'Afrique Du Sud',
            'AX': 'Åland, Îles',
            'AL': 'Albanie',
            'DZ': 'Algérie',
            'DE': 'Allemagne',
            'AD': 'Andorre',
            'AO': 'Angola',
            'AI': 'Anguilla',
            'AQ': 'Antarctique',
            'AG': 'Antigua-Et-Barbuda',
            'SA': 'Arabie Saoudite',
            'AR': 'Argentine',
            'AM': 'Arménie'
        };
    }
}

const countries = new mdm_countries();

// Endpoints

app.get('/european_union', (req, res) => {
    res.json(countries.european_union());
});

app.get('/countries_int', (req, res) => {
    res.json(countries.countries_int());
});

app.get('/countries_fr', (req, res) => {
    res.json(countries.countries_fr());
});

// Démarrage du serveur
app.listen(port, () => {
    console.log(`Serveur démarré sur le port ${port}`);
});
```

**Explication:**

1.  **Installation des dépendances:** Le code commence par des instructions pour installer les dépendances nécessaires.
2.  **Import des modules:**  Importe les modules `express`, `body-parser`, et `cors`.
3.  **Initialisation de l'application:** Crée une instance de l'application Express.
4.  **Middleware:** Configure les middlewares pour gérer les requêtes CORS, parser le corps des requêtes en JSON et les données URL-encoded.
5.  **Classe PHP Simulée:**  Simule la classe PHP `mdm_countries` en JavaScript. Les méthodes PHP sont traduites en méthodes JavaScript.
6.  **Instanciation de la classe:** Crée une instance de la classe simulée.
7.  **Définition des endpoints:** Définit trois endpoints correspondant aux trois méthodes de la classe PHP :
    *   `/european_union`
    *   `/countries_int`
    *   `/countries_fr`
    Chaque endpoint appelle la méthode correspondante de l'instance `countries` et renvoie le résultat en JSON.
8.  **Démarrage du serveur:**  Démarre le serveur Express sur le port spécifié (3000 par défaut).

**Pour exécuter ce code:**

1.  Enregistrez le code dans un fichier (par exemple, `app.js`).
2.  Ouvrez un terminal et naviguez jusqu'au répertoire où vous avez enregistré le fichier.
3.  Exécutez la commande `node app.js`.
4.  L'API sera accessible via les URLs suivantes:
    *   `http://localhost:3000/european_union`
    *   `http://localhost:3000/countries_int`
    *   `http://localhost:3000/countries_fr`


## Transformer du code PHP en API Node.js avec Express

| Tags |
|------|
| `Node.js` `Express` `API` `PHP` |
<p>Pour transformer le code PHP donné en une API Node.js avec Express, vous pouvez suivre les étapes suivantes. Cette API aura des endpoints pour chaque méthode définie dans la classe <code>mdm_countries</code>.</p>
<ol>
<li>Installez Node.js et Express.</li>
<li>Créez un projet Node.js.</li>
<li>Créez un fichier <code>index.js</code> et y configurez votre serveur Express.</li>
<li>Implémentez les endpoints pour chaque méthode.</li>
</ol>
<p>Voici un exemple complet :</p>


## Installation de Node.js et Express

| Tags |
|------|
| `Node.js` `Express` `npm` `API` |

Assurez-vous que Node.js est installé sur votre machine. Créez ensuite un nouveau projet Node.js et installez Express :

```sh
mkdir mdm_countries_api
cd mdm_countries_api
npm init -y
npm install express
```


## Création du fichier index.js

| Tags |
|------|
| `Node.js` `Express` `API` `JavaScript` |

```javascript
const express = require('express');
const app = express();
const port = 3000;

class mdm_countries {
    constructor() {}

    european_union() {
        return {
            "": "- Choose One -",
            "NOTEU": "Non-EU Resident",
            "BE": "Belgique",
            "BG": "Bulgarie",
            "CZ": "République tchèque",
            "DK": "Danemark",
            "DE": "Allemagne",
            "EE": "Estonie",
            "IE": "Irlande",
            "EL": "Grèce",
            "ES": "Espagne",
            "FR": "France",
            "IT": "Italie",
            "CY": "Chypre",
            "LV": "Lettonie",
            "LT": "Lituanie",
            "LU": "Luxembourg",
            "HU": "Hongrie",
            "MT": "Malte",
            "NL": "Nouvelle-Zélande",
            "AT": "Autriche",
            "PL": "Pologne",
            "PT": "Portugal",
            "RO": "Roumanie",
            "SI": "Slovénie",
            "SK": "Slovaquie",
            "FI": "Finlande",
            "SE": "Suède",
            "UK": "Royaume-Uni"
        };
    }

    countries_int() {
        return {
            'AD': 'Andorra',
            'AE': 'United Arab Emirates',
            'AF': 'Afghanistan',
            'AG': 'Antigua and Barbuda',
            'AI': 'Anguilla',
            'AL': 'Albania',
            'AM': 'Armenia',
            'AN': 'Netherlands Antilles',
            'AO': 'Angola',
            'AQ': 'Antarctica',
            'AR': 'Argentina',
            'AS': 'American Samoa',
            'AT': 'Austria',
            'AU': 'Australia',
            'AW': 'Aruba',
            'AX': 'Aland Islands',
            'AZ': 'Azerbaijan',
            'BA': 'Bosnia and Herzegovina',
            'BB': 'Barbados',
            'BD': 'Bangladesh',
            'BE': 'Belgium',
            'BF': 'Burkina Faso',
            'BG': 'Bulgaria',
            'BH': 'Bahrain',
            'BI': 'Burundi',
            'BJ': 'Benin',
            'BL': 'Saint Barthelemy',
            'BM': 'Bermuda',
            'BN': 'Brunei',
            'BO': 'Bolivia',
            'BR': 'Brazil',
            'BS': 'Bahamas',
            'BT': 'Bhutan',
            'BV': 'Bouvet Island',
            'BW': 'Botswana',
            'BY': 'Belarus',
            'BZ': 'Belize',
            'CA': 'Canada',
            'CC': 'Cocos (Keeling) Islands',
            'CD': 'Congo (Kinshasa)',
            'CF': 'Central African Republic',
            'CG': 'Congo (Brazzaville)',
            'CH': 'Switzerland',
            'CI': 'Ivory Coast',
            'CK': 'Cook Islands',
            'CL': 'Chile',
            'CM': 'Cameroon',
            'CN': 'China',
            'CO': 'Colombia',
            'CR': 'Costa Rica',
            'CU': 'Cuba',
            'CV': 'Cape Verde',
            'CX': 'Christmas Island',
            'CY': 'Cyprus',
            'CZ': 'Czech Republic',
            'DE': 'Germany',
            'DJ': 'Djibouti',
            'DK': 'Denmark',
            'DM': 'Dominica',
            'DO': 'Dominican Republic',
            'DZ': 'Algeria',
            'EC': 'Ecuador',
            'EE': 'Estonia',
            'EG': 'Egypt',
            'EH': 'Western Sahara',
            'ER': 'Eritrea',
            'ES': 'Spain',
            'ET': 'Ethiopia',
            'FI': 'Finland',
            'FJ': 'Fiji',
            'FK': 'Falkland Islands',
            'FM': 'Micronesia',
            'FO': 'Faroe Islands',
            'FR': 'France',
            'GA': 'Gabon',
            'GB': 'United Kingdom',
            'GD': 'Grenada',
            'GE': 'Georgia',
            'GF': 'French Guiana',
            'GG': 'Guernsey',
            'GH': 'Ghana',
            'GI': 'Gibraltar',
            'GL': 'Greenland',
            'GM': 'Gambia',
            'GN': 'Guinea',
            'GP': 'Guadeloupe',
            'GQ': 'Equatorial Guinea',
            'GR': 'Greece',
            'GS': 'South Georgia and the South Sandwich Islands',
            'GT': 'Guatemala',
            'GU': 'Guam',
            'GW': 'Guinea-Bissau',
            'GY': 'Guyana',
            'HK': 'Hong Kong S.A.R., China',
            'HM': 'Heard Island and McDonald Islands',
            'HN': 'Honduras',
            'HR': 'Croatia',
            'HT': 'Haiti',
            'HU': 'Hungary',
            'ID': 'Indonesia',
            'IE': 'Ireland',
            'IL': 'Israel',
            'IM': 'Isle of Man',
            'IN': 'India',
            'IO': 'British Indian Ocean Territory',
            'IQ': 'Iraq',
            'IR': 'Iran',
            'IS': 'Iceland',
            'IT': 'Italy',
            'JE': 'Jersey',
            'JM': 'Jamaica',
            'JO': 'Jordan',
            'JP': 'Japan',
            'KE': 'Kenya',
            'KG': 'Kyrgyzstan',
            'KH': 'Cambodia',
            'KI': 'Kiribati',
            'KM': 'Comoros',
            'KN': 'Saint Kitts and Nevis',
            'KP': 'North Korea',
            'KR': 'South Korea',
            'KW': 'Kuwait',
            'KY': 'Cayman Islands',
            'KZ': 'Kazakhstan',
            'LA': 'Laos',
            'LB': 'Lebanon',
            'LC': 'Saint Lucia',
            'LI': 'Liechtenstein',
            'LK': 'Sri Lanka',
            'LR': 'Liberia',
            'LS': 'Lesotho',
            'LT': 'Lithuania',
            'LU': 'Luxembourg',
            'MO': 'Macao S.A.R., China',
            'MK': 'Macedonia',
            'MG': 'Madagascar',
            'MW': 'Malawi',
            'MY': 'Malaysia',
            'MV': 'Maldives',
            'ML': 'Mali',
            'MT': 'Malta',
            'MH': 'Marshall Islands',
            'MQ': 'Martinique',
            'MR': 'Mauritania',
            'MS': 'Montserrat',
            'MT': 'Malta',
            'MU': 'Mauritius',
            'MV': 'Maldives',
            'MW': 'Malawi',
            'MX': 'Mexico',
            'FM': 'Micronesia',
            'MD': 'Moldova',
            'MC': 'Monaco',
            'MN': 'Mongolia',
            'ME': 'Montenegro',
            'MS': 'Montserrat',
            'MZ': 'Mozambique',
            'MM': 'Myanmar',
            'NA': 'Namibia',
            'NR': 'Nauru',
            'NP': 'Nepal',
            'NI': 'Nicaragua',
            'NL': 'Netherlands',
            'NO': 'Norway',
            'NP': 'Nepal',
            'NR': 'Nauru',
            'NU': 'Niue',
            'NZ': 'New Zealand',
            'OM': 'Oman',
            'PA': 'Panama',
            'PE': 'Peru',
            'PF': 'French Polynesia',
            'PG': 'Papua New Guinea',
            'PH': 'Philippines',
            'PK': 'Pakistan',
            'PL': 'Poland',
            'PM': 'Saint Pierre and Miquelon',
            'PN': 'Pitcairn',
            'PR': 'Puerto Rico',
            'PS': 'Palestinian Territory',
            'PT': 'Portugal',
            'PW': 'Palau',
            'PY': 'Paraguay',
            'QA': 'Qatar',
            'RE': 'Reunion',
            'RO': 'Romania',
            'RS': 'Serbia',
            'RU': 'Russia',
            'RW': 'Rwanda',
            'SA': 'Saudi Arabia',
            'SB': 'Solomon Islands',
            'SC': 'Seychelles',
            'SD': 'Sudan',
            'SE': 'Sweden',
            'SG': 'Singapore',
            'SH': 'Saint Helena',
            'SI': 'Slovenia',
            'SJ': 'Svalbard and Jan Mayen',
            'SK': 'Slovakia',
            'SL': 'Sierra Leone',
            'SM': 'San Marino',
            'SN': 'Senegal',
            'SO': 'Somalia',
            'SR': 'Suriname',
            'ST': 'Sao Tome and Principe',
            'SV': 'El Salvador',
            'SY': 'Syria',
            'SZ': 'Swaziland',
            'TC': 'Turks and Caicos Islands',
            'TD': 'Chad',
            'TF': 'French Southern Territories',
            'TG': 'Togo',
            'TH': 'Thailand',
            'TJ': 'Tajikistan',
            'TK': 'Tokelau',
            'TL': 'Timor-Leste',
            'TM': 'Turkmenistan',
            'TN': 'Tunisia',
            'TO': 'Tonga',
            'TR': 'Turkey',
            'TT': 'Trinidad and Tobago',
            'TV': 'Tuvalu',
            'TW': 'Taiwan',
            'TZ': 'Tanzania',
            'UA': 'Ukraine',
            'UG': 'Uganda',
            'UM': 'United States Minor Outlying Islands',
            'US': 'United States',
            'UY': 'Uruguay',
            'UZ': 'Uzbekistan',
            'VA': 'Vatican',
            'VC': 'Saint Vincent and the Grenadines',
            'VE': 'Venezuela',
            'VG': 'British Virgin Islands',
            'VI': 'U.S. Virgin Islands',
            'VN': 'Vietnam',
            'VU': 'Vanuatu',
            'WF': 'Wallis and Futuna',
            'WS': 'Samoa',
            'YE': 'Yemen',
            'YT': 'Mayotte',
            'ZA': 'South Africa',
            'ZM': 'Zambia',
            'ZW': 'Zimbabwe',
            'USAF': 'US Armed Forces'
        };
    }

    countries_fr() {
        return {
            'AF': 'Afghanistan',
            'ZA': 'Afrique Du Sud',
            'AX': 'Åland, Îles',
            'AL': 'Albanie',
            'DZ': 'Algérie',
            'DE': 'Allemagne',
            'AD': 'Andorre',
            'AO': 'Angola',
            'AI': 'Anguilla',
            'AQ': 'Antarctique',
            'AG': 'Antigua-Et-Barbuda',
            'SA': 'Arabie Saoudite',
            'AR': 'Argentine',
            'AM': 'Arménie',
            'AW': 'Aruba',
            'AU': 'Australie',
            'AT': 'Autriche',
            'AZ': 'Azerbaïdjan',
            'BS': 'Bahamas',
            'BH': 'Bahreïn',
            'BD': 'Bangladesh',
            'BB': 'Barbade',
            'BY': 'Bélarus',
            'BE': 'Belgique',
            'BZ': 'Belize',
            'BJ': 'Bénin',
            'BM': 'Bermudes',
            'BT': 'Bhoutan',
            'BO': 'Bolivie, L\'état Plurinational De',
            'BQ': 'Bonaire, Saint-Eustache Et Saba',
            'BA': 'Bosnie-Herzégovine',
            'BW': 'Botswana',
            'BV': 'Bouvet, Île',
            'BR': 'Brésil',
            'BN': 'Brunei Darussalam',
            'BG': 'Bulgarie',
            'BF': 'Burkina Faso',
            'BI': 'Burundi',
            'KY': 'Caïmans, Îles',
            'KH': 'Cambodge',
            'CM': 'Cameroun',
            'CA': 'Canada',
            'CV': 'Cap-Vert',
            'CF': 'Centrafricaine, République',
            'CL': 'Chili',
            'CN': 'Chine',
            'CX': 'Christmas, Île',
            'CY': 'Chypre',
            'CC': 'Cocos (Keeling), Îles',
            'CO': 'Colombie',
            'KM': 'Comores',
            'CG': 'Congo',
            'CD': 'Congo, La République Démocratique Du',
            'CK': 'Cook, Îles',
            'KR': 'Corée, République De',
            'KP': 'Corée, République Populaire Démocratique De',
            'CR': 'Costa Rica',
            'CI': 'Côte D\'ivoire',
            'HR': 'Croatie',
            'CU': 'Cuba',
            'CW': 'Curaçao',
            'DK': 'Danemark',
            'DJ': 'Djibouti',
            'DO': 'Dominicaine, République',
            'DM': 'Dominique',
            'EG': 'Égypte',
            'SV': 'El Salvador',
            'AE': 'Émirats Arabes Unis',
            'EC': 'Équateur',
            'ER': 'Érythrée',
            'ES': 'Espagne',
            'EE': 'Estonie',
            'US': 'États-Unis',
            'ET': 'Éthiopie',
            'FK': 'Falkland, Îles (Malvinas)',
            'FO': 'Féroé, Îles',
            'FJ': 'Fidji',
            'FI': 'Finlande',
            'FR': 'France',
            'GA': 'Gabon',
            'GM': 'Gambie',
            'GE': 'Géorgie',
            'GS': 'Géorgie Du Sud-Et-Les Îles Sandwich Du Sud',
            'GH': 'Ghana',
            'GI': 'Gibraltar',
            'GR': 'Grèce',
            'GD': 'Grenade',
            'GL': 'Groenland',
            'GP': 'Guadeloupe',
            'GU': 'Guam',
            'GT': 'Guatemala',
            'GG': 'Guernesey',
            'GN': 'Guinée',
            'GW': 'Guinée-Bissau',
            'GQ': 'Guinée Équatoriale',
            'GY': 'Guyana',
            'GF': 'Guyane Française',
            'HT': 'Haïti',
            'HM': 'Heard-Et-Îles Macdonald, Île',
            'HN': 'Honduras',
            'HK': 'Hong Kong',
            'HU': 'Hongrie',
            'IM': 'Île De Man',
            'UM': 'Îles Mineures Éloignées Des États-Unis',
            'VG': 'Îles Vierges Britanniques',
            'VI': 'Îles Vierges Des États-Unis',
            'IN': 'Inde',
            'ID': 'Indonésie',
            'IR': 'Iran, République Islamique D\'',
            'IQ': 'Iraq',
            'IE': 'Irlande',
            'IS': 'Islande',
            'IL': 'Israël',
            'IT': 'Italie',
            'JM': 'Jamaïque',
            'JP': 'Japon',
            'JE': 'Jersey',
            'JO': 'Jordanie',
            'KZ': 'Kazakhstan',
            'KE': 'Kenya',
            'KG': 'Kirghizistan',
            'KI': 'Kiribati',
            'KW': 'Koweït',
            'LA': 'Lao, République Démocratique Populaire',
            'LS': 'Lesotho',
            'LV': 'Lettonie',
            'LB': 'Liban',
            'LR': 'Libéria',
            'LY': 'Libye',
            'LI': 'Liechtenstein',
            'LT': 'Lituanie',
            'LU': 'Luxembourg',
            'MO': 'Macao',
            'MK': 'Macédoine, L\'ex-République Yougoslave De',
            'MG': 'Madagascar',
            'MY': 'Malaisie',
            'MW': 'Malawi',
            'MV': 'Maldives',
            'ML': 'Mali',
            'MT': 'Malte',
            'MP': 'Mariannes Du Nord, Îles',
            'MA': 'Maroc',
            'MH': 'Marshall, Îles',
            'MQ': 'Martinique',
            'MU': 'Maurice',
            'MR': 'Mauritanie',
            'YT': 'Mayotte',
            'MX': 'Mexique',
            'FM': 'Micronésie, États Fédérés De',
            'MD': 'Moldova, République De',
            'MC': 'Monaco',
            'MN': 'Mongolie',
            'ME': 'Monténégro',
            'MS': 'Montserrat',
            'MZ': 'Mozambique',
            'MM': 'Myanmar',
            'NA': 'Namibie',
            'NR': 'Nauru',
            'NP': 'Népal',
            'NI': 'Nicaragua',
            'NE': 'Niger',
            'NG': 'Nigéria',
            'NU': 'Niué',
            'NF': 'Norfolk, Île',
            'NO': 'Norvège',
            'NC': 'Nouvelle-Calédonie',
            'NZ': 'Nouvelle-Zélande',
            'IO': 'Océan Indien, Territoire Britannique De L\'',
            'OM': 'Oman',
            'UG': 'Ouganda',
            'UZ': 'Ouzbékistan',
            'PK': 'Pakistan',
            'PW': 'Palaos',
            'PS': 'Palestinien Occupé, Territoire',
            'PA': 'Panama',
            'PG': 'Papouasie-Nouvelle-Guinée',
            'PY': 'Paraguay',
            'NL': 'Pays-Bas',
            'PE': 'Pérou',
            'PH': 'Philippines',
            'PN': 'Pitcairn',
            'PL': 'Pologne',
            'PF': 'Polynésie Française',
            'PR': 'Porto Rico',
            'PT': 'Portugal',
            'QA': 'Qatar',
            'RE': 'Réunion',
            'RO': 'Roumanie',
            'GB': 'Royaume-Uni',
            'RU': 'Russie, Fédération De',
            'RW': 'Rwanda',
            'EH': 'Sahara Occidental',
            'BL': 'Saint-Barthélemy',
            'SH': 'Sainte-Hélène, Ascension Et Tristan Da Cunha',
            'LC': 'Sainte-Lucie',
            'KN': 'Saint-Kitts-Et-Nevis',
            'SM': 'Saint-Marin',
            'MF': 'Saint-Martin(Partie Française)',
            'SX': 'Saint-Martin (Partie Néerlandaise)',
            'PM': 'Saint-Pierre-Et-Miquelon',
            'VA': 'Saint-Siège (État De La Cité Du Vatican)',
            'VC': 'Saint-Vincent-Et-Les Grenadines',
            'SB': 'Salomon, Îles',
            'WS': 'Samoa',
            'AS': 'Samoa Américaines',
            'ST': 'Sao Tomé-Et-Principe',
            'SN': 'Sénégal',
            'RS': 'Serbie',
            'SC': 'Seychelles',
            'SL': 'Sierra Leone',
            'SG': 'Singapour',
            'SK': 'Slovaquie',
            'SI': 'Slovénie',
            'SO': 'Somalie',
            'SD': 'Soudan',
            'SS': 'Soudan Du Sud',
            'LK': 'Sri Lanka',
            'SE': 'Suède',
            'CH': 'Suisse',
            'SR': 'Suriname',
            'SJ': 'Svalbard Et Île Jan Mayen',
            'SZ': 'Swaziland',
            'SY': 'Syrienne, République Arabe',
            'TJ': 'Tadjikistan',
            'TW': 'Taïwan, Province De Chine',
            'TZ': 'Tanzanie, République-Unie De',
            'TD': 'Tchad',
            'CZ': 'Tchèque, République',
            'TF': 'Terres Australes Françaises',
            'TH': 'Thaïlande',
            'TL': 'Timor-Leste',
            'TG': 'Togo',
            'TK': 'Tokelau',
            'TO': 'Tonga',
            'TT': 'Trinité-Et-Tobago',
            'TN': 'Tunisie',
            'TM': 'Turkménistan',
            'TC': 'Turks-Et-Caïcos, Îles',
            'TR': 'Turquie',
            'TV': 'Tuvalu',
            'UA': 'Ukraine',
            'UY': 'Uruguay',
            'VU': 'Vanuatu',
            'VE': 'Venezuela, République Bolivarienne Du',
            'VN': 'Viet Nam',
            'WF': 'Wallis Et Futuna',
            'YE': 'Yémen',
            'ZM': 'Zambie',
            'ZW': 'Zimbabwe'
        };
    }
}

const countries = new mdm_countries();

app.get('/european_union', (req, res) => {
    res.json(countries.european_union());
});

app.get('/countries_int', (req, res) => {
    res.json(countries.countries_int());
});

app.get('/countries_fr', (req, res) => {
    res.json(countries.countries_fr());
});

app.listen(port, () => {
    console.log(`API listening at http://localhost:${port}`);
});
```


## Lancement du serveur

| Tags |
|------|
| `Node.js` `API` `Serveur` |

Pour lancer le serveur, exécutez la commande suivante :

```sh
node index.js
```

L'API Node.js est désormais active et propose des endpoints pour l'obtention des listes de pays. Accédez aux endpoints via un navigateur ou un outil comme Postman afin de vérifier les résultats.
