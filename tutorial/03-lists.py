import math
squares = [1,4,9,16,25]

#Desafio: A partir del arreglo anterior crear uno que tenga sus raices

roots = []

for number in squares:
    roots.append(int(math.sqrt(number)))

print(roots)

# roots = [1,2,3,4,5]

# roots = [1,2,3,4,5]

## sqrt : sqrt o raiz cuadrada
## square : sq
## root : rt

## append: agrega al final

##Remplazar algun elemento del arreglo segun el indice
roots[4] = 6

print(roots)