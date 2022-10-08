import random
import time

#El mmódulo random tiene varias funciones para trabajar con numeros aleatorios.
#La función choice es una de las mas usadas eligiendo un elemento al azar desde un lista

fruits = ['manzana','pera','frutillas','piña']

#Imprimir una fruta al azar 
print('Redoble de tambores.....')

for i in range(1,3):
    print(".")
    time.sleep(0.5)

print('Tu fruta es:')
print(random.choice(fruits))    

