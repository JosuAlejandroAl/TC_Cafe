import re

def drink(item_name):
    item_name = item_name.replace(" ", "")
    pattern = re.compile("^[a-zA-Z]{2,15}$")
    if pattern.match(item_name):
        return True
    else:
        return False


def size_list(size_value):
    size_list = []
    try:
        # Remove spaces and split the string into a list
        size_value = size_value.replace(" ", "")
        size_list = [int(num) for num in size_value.split(",")]
        
        # Validate the size list
        if len(size_list) < 1 or len(size_list) > 5:
            return False
        for num in size_list:
            if num < 1 or num > 48:
                return False
        if size_list != sorted(size_list):
            return False
    except ValueError:
        return False
    
    return sorted(size_list)
