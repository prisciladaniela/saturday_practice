# La función principal para manejar archivos es open()
# Esta función recibe dos párametros, el nombre del archivo y el modo
# Los modos son:

# r: para leer y da error si el archivo no existe
# a: para realizar append(agregar al final). Si el archivo no existe, lo crea
# w: para escribir. Elimina el contenido anterior si existe.

file = open("file_handling/example.txt", "r")

# A la funciín read podemos pasar un numero y va a imprimir esa cantidad de caracteres
print(file.read(54))

# También existe la función readline() que lee línea por línea
print("Ejemplo de readline()")
print("file.readline()")
print("file.readline()")

# Debemos cerrar el archivo luego de usarlo
file.close()