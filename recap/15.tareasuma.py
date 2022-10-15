# Crear una función que sume todos los números hasta el número n

def sum_up_to(n):
    acc = 0

    for number in range(1, n + 1):
        acc += number
    print(acc)

sum_up_to(10)

  