

def validar(x):
    vocales = "AEIOUaeiou"
    if x in vocales:
        print(f"La letra {x} es una vocal")
    else:
        print(f"La letra {x} es una consonante")


letra = input("ingresa la letra: ")
validar(letra)