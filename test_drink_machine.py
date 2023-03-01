import drink_machine

# Test Cases
def test_drink_valid():
    assert drink_machine.drink("cocacola") == True
    
def test_drink_invalid_length():
    assert drink_machine.drink("a") == False
    assert drink_machine.drink("a" * 16) == False

def test_drink_invalid_chars():
    assert drink_machine.drink("123") == False
    assert drink_machine.drink("coca cola") == False

def test_size_list_valid():
    assert drink_machine.size_list("1,2,3,4,5") == [1,2,3,4,5]
    
def test_size_list_invalid_length():
    assert drink_machine.size_list("") == False
    assert drink_machine.size_list("1,2,3,4,5,6") == False

def test_size_list_invalid_values():
    assert drink_machine.size_list("0,1,2,3,4") == False
    assert drink_machine.size_list("1,2,3,50") == False

def test_size_list_not_sorted():
    assert drink_machine.size_list("5,4,3,2,1") == False
    assert drink_machine.size_list("1,3,2,4,5") == False

def test_valid_input():
    assert drink_machine.drink("cocacola") == True
    assert drink_machine.size_list("1,2,3,4,5") == [1,2,3,4,5]

def test_invalid_input():
    assert drink_machine.drink("coca cola") == False
    assert drink_machine.size_list("1,2,3,4,49") == False
    assert drink_machine.size_list("1,2,3,4,0") == False
    assert drink_machine.size_list("1,3,2,4,5") == False
