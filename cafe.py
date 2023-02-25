import re

def drink(beverage_name):
    beverage_name = beverage_name.replace(" ", "")
    pattern = re.compile("^[a-zA-Z]{2,15}$")
    if pattern.match(beverage_name):
        print("Valido nombre de bebida")
    else:
        print("Invalido nombre de bebida")

def size_list(size_string):
    size_list = []
    try:
        # Remove spaces and split the string into a list
        size_string = size_string.replace(" ", "")
        size_list = [int(num) for num in size_string.split(",")]
        
        # Validate the size list
        if len(size_list) < 1 or len(size_list) > 5:
            print("El numero de los tamanos de bebidas debe ser entre 1 y 5")
            return None
        for num in size_list:
            if num < 1 or num > 48:
                print("Los tamanos deben estar en un rango de 1 - 48")
                return None
        if size_list != sorted(size_list):
            print("Los números deben estar en orden ascendente")
            return None
    except ValueError:
        print("Invalid size list.")
        return None
    
    print("El orden de los tamanos es la siguiente", sorted(size_list))
    return sorted(size_list)

# Get input from the user
input_string = input(" ingresa el nombre de la bebida y despues el tamano")

# Split the input string into the beverage name and size list
input_list = input_string.split(",")

# Call the functions to validate the input
if len(input_list) < 2:
    print("No ingresaste bien los valores recuerda que debe ser primero el nombre y depsues con una coma ',' sigue los tamanos de la bebida .")
else:
    beverage_name = input_list[0]
    size_string = ",".join(input_list[1:])
    drink(beverage_name)
    size_list(size_string)
