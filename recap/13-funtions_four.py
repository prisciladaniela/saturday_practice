#Completar la siguiente funcion que imprima cualquier tabla de multiplicacion hasta el 12



def multiplication_tables(number = 1):
    print('########################')
    for i in range(1,13):
        print(number, "x",i,"=", number * i)
    
    
multiplication_tables(2)
multiplication_tables(7)




    