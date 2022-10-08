magic_word = "microsystem"
user_input = input("Ingresa la palabra magica\n")

while user_input !=magic_word:
    print("Esa no es la palabra mágica")
    user_input = input ("Ingrese la palabra mágica\n")

print("¡Excelente! descubriste la palabra mágica")