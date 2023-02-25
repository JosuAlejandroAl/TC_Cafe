import re

def drink(cadena):
    cadena = cadena.replace(" ", "")
    patron = re.compile("^[a-zA-Z]{2,15}$")
    if patron.match(cadena):
        print("valido")
    else:
        print("No tenemos esa bedida")
    
cadena_valida = input("Ingresa el nombre de la bebida: ")
print(drink(cadena_valida))  

# funcion de la lista

def listNum(listSize):
    lista_numeros = []
    try:
        listSize = [int(numero.strip()) for numero in sizeDrink.replace(" ", "").split(",")]
        if len(listSize) < 1 or len(listSize) > 5:
            print("La lista debe tener entre 1 y 5 números")
            return None
        for numero in listSize:
            if numero < 1 or numero > 48:
                print("Los números deben estar en el rango del 1 al 48")
                return None
        lista_numeros = sorted(listSize)
        if lista_numeros != listSize:
            print("Los números deben estar en orden ascendente")
            return None
    except ValueError:
        print("Algo ocurrio mal")
        return None
    return lista_numeros

sizeDrink = input("Ingresa el tamano de la bebida: ")
lista_numeros = listNum(sizeDrink)
if lista_numeros:
    print("La lista ordenada es:", lista_numeros)
else:
    print("Su prueba no fue valida") 