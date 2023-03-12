def calcular(x,y):
    if x % y == 0:  
        print(f"{x} es nuliplo de {y}")
    elif y % x == 0:
        print(f"{y} es multiplo de {x}")
    else:
        print("Los numeros no son multiplos")


b = int(input("Ingresa un numero: "))
c = int(input("Ingresa un numero: "))
calcular(c,b)

