# Podemos leer las líneas de un archivo utilizando for. Ejemplo
file = open('file_handling/example.txt')

line_number = 1
for line in file:
    print(line_number, line)
    # line_number = line_number + 1
    line_number += 1