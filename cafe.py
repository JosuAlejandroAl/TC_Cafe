import re

def drink(item_name):
    item_name = item_name.replace(" ", "")
    pattern = re.compile("^[a-zA-Z]{2,15}$") #validate only alphabetic characters and minimum of 2 and a maximum of 15 characters
    if pattern.match(item_name):
        print("Valido nombre de bebida")
    else:
        print("Invalido nombre de bebida")

def size_list(size_value):
    size_list = []
    try:
        # remove blank spaces
        size_value = size_value.replace(" ", "")
        size_list = [int(num) for num in size_value.split(",")]
        
        # validate the size conditionals
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
        print("invalido los valores de la lista")
        return None
    
    print("El orden de los tamanos es la siguiente", sorted(size_list))
    return sorted(size_list)

# open the file and read the test cases
with open('test.txt', 'r') as f:
    input_lines = f.readlines()

for line in input_lines:
    input_list = line.strip().split(",")
    
    # call the functions 
    if len(input_list) < 2:
        print("No ingresaste bien los valores recuerda que debe ser primero el nombre de la bebida y despues con una coma ',' sigue los tamanos de la bebida")
    else:
        item_name = input_list[0]
        size_value = ",".join(input_list[1:]) #input list is split using the comma as a separator
        drink(item_name)
        size_list(size_value)