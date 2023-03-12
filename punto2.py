X = int(input("Ingresa el primer numero: ")) 
y = int(input("Ingresa el segundo numero: ")) 
z = int(input("Ingresa el tercer numero: ")) 
if X != y and X != z and y != z:
    if X > y:
        if X > z:
            print("El numero mayor es: ",X)
        else:
            print("El numero mayor es: ",z)
    else:
        if y > z:
            print("El numero mayor es: ",y)
        else:
            print("El numero mayor es: ",z)
else:
    print("Ingrese 3 numeros diferentes ")

