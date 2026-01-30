# ***********************************************************************************************************************

# He visto en shorts de Youtube esta manera de ordenar una lista y quitar duplicados

old = ['a','b','a','c','b','a']

new = []

for item in old:
    if item not in new:
        new.append(item)

print(new)

# Dice que otra forma de hacerlo es asi:

old = ['a','b','a','c','b','a']
new = list(dict.fromkeys(old).keys())
print(new)

# Básicamente acorta en una linea el trabajo de antes.