## Conditions d'entrée en Python
| Tags |
|------|
| `Python` `conditions` `if` `elif` `else` |

En Python, les conditions d'entrée permettent d'exécuter des blocs de code spécifiques selon la valeur de certaines expressions booléennes. Le mot-clé `if` est le point de départ pour une condition. On peut utiliser les mots-clés `elif` (else if) et `else` pour gérer plusieurs cas.

Voici un exemple simple :

```python
x = 10
if x > 5:
    print("x est supérieur à 5")
elif x < 5:
    print("x est inférieur à 5")
else:
    print("x est égal à 5")
```

Dans cet exemple, le code vérifie d'abord si `x` est supérieur à 5. Si c'est le cas, le message "x est supérieur à 5" est affiché. Sinon, il vérifie si `x` est inférieur à 5. Si c'est le cas, le message "x est inférieur à 5" est affiché. Si aucune de ces conditions n'est vraie, le message "x est égal à 5" est affiché.

Les conditions peuvent également être imbriquées :

```python
y = 20
if y > 0:
    if y < 10:
        print("y est positif et inférieur à 10")
    else:
        print("y est positif et supérieur ou égal à 10")
else:
    print("y est négatif ou nul")
```

Dans ce cas, on vérifie d'abord si `y` est supérieur à 0. Si c'est le cas, on vérifie ensuite si `y` est inférieur à 10. Le code peut devenir complexe avec des imbrications profondes, il est donc important de bien organiser le code pour une meilleure lisibilité et maintenabilité.


## Conditions d'entrée en Python

| Tags |
|------|
| `Python` `Conditions` `if-elif-else` |

Pour gérer les conditions d'entrée en Python, on utilise des structures conditionnelles telles que <code>if</code>, <code>elif</code> et <code>else</code>. L'exemple suivant illustre leur utilisation :

```python
# Demander à l'utilisateur d'entrer un nombre
nombre = input("Entrez un nombre: ")

# Essayer de convertir l'entrée en un nombre entier
try:
    nombre = int(nombre)
    # Vérifier si le nombre est positif, négatif ou zéro
    if nombre > 0:
        print(f"Le nombre {nombre} est positif.")
    elif nombre < 0:
        print(f"Le nombre {nombre} est négatif.")
    else:
        print("Le nombre est zéro.")
except ValueError:
    # Si la
```
