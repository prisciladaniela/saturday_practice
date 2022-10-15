#Crear una funcion que entregue el volumen de un cilindro
import math
def cylinder_volume(r,h):
    volume = math.pi*r**2*h
    return volume 


result = cylinder_volume(10,5)
print(result)

