## Calcul de l'Indice de Force Relative (RSI)
| Tags |
|------|
| `RSI` `trading` `analyse technique` |

Le calcul de l'Indice de Force Relative (RSI) nécessite plusieurs étapes.  Le RSI est un indicateur de momentum qui mesure l'ampleur des récents changements de prix pour évaluer les conditions de surachat ou de survente d'un actif.

**1. Calcul des variations de prix:**

Commencez par calculer les variations de prix pour chaque période.  Pour chaque période, soustrayez le prix de clôture de la période précédente du prix de clôture de la période actuelle.

**2. Calcul des gains et des pertes moyens:**

Après avoir calculé les variations de prix, vous devez calculer les gains et les pertes moyens sur une période spécifique (généralement 14 périodes).

*   **Gain moyen:** Somme des gains sur la période / Nombre de périodes
*   **Perte moyenne:** Somme des pertes sur la période / Nombre de périodes (les pertes sont exprimées en valeurs absolues)

La formule pour le calcul initial des gains et des pertes moyens est la suivante :

```
Gain moyen = Somme des gains sur les 14 dernières périodes / 14
Perte moyenne = Somme des pertes sur les 14 dernières périodes / 14
```

Après le calcul initial, les gains et les pertes moyens pour les périodes suivantes sont calculés comme suit :

```
Gain moyen = [(Gain moyen précédent \* 13) + Gain actuel] / 14
Perte moyenne = [(Perte moyenne précédente \* 13) + Perte actuelle] / 14
```

**3. Calcul de la Force Relative (RS):**

La Force Relative (RS) est calculée en divisant le gain moyen par la perte moyenne.

```
RS = Gain moyen / Perte moyenne
```

**4. Calcul du RSI:**

Enfin, le RSI est calculé à l'aide de la formule suivante :

```
RSI = 100 - (100 / (1 + RS))
```

Le RSI est généralement affiché sous la forme d'une ligne oscillant entre 0 et 100. Les valeurs supérieures à 70 indiquent généralement des conditions de surachat, tandis que les valeurs inférieures à 30 indiquent généralement des conditions de survente.


## Calcul du Relative Strength Index (RSI)

| Tags |
|------|
| `RSI` `indicateur technique` `analyse technique` `finance` |

Le RSI (Relative Strength Index) est un indicateur technique utilisé en analyse technique pour mesurer la force relative d'un actif financier. Il compare la magnitude des gains récents à celle des pertes récentes sur une période de temps spécifique. Le calcul s'effectue avec la formule suivante :

RSI = 100 - (100 / (1 + RS))

Où RS représente le rapport de la moyenne des gains sur une période donnée à la moyenne des pertes sur la même période.

La formule pour calculer RS est :

RS = (Moyenne des gains sur une période donnée) / (Moyenne des pertes sur une période donnée)

La période utilisée pour le calcul du RSI peut varier, mais une période de 14 jours est couramment utilisée.

Pour calculer le RSI, on calcule d'abord la moyenne des gains et des pertes sur la période choisie, puis on calcule RS. Enfin, la formule RSI est appliquée. Le résultat final se situe généralement entre 0 et 100.

Le RSI est un indicateur parmi d'autres et ne doit pas être utilisé seul pour prendre des décisions. Il est souvent utilisé en combinaison avec d'autres indicateurs pour une analyse plus complète.
