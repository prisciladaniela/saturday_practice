# Crear una función que imprima los números divisibles por 3 hasta el número n

def divisibles_by_three(n):
  print ("#########")
  for number in range(1,n + 1):
    if number % 3 == 0:
      print(number)

divisibles_by_three(50)
