from traductor.functions import encrypt_letter_to_morse,encrypt_to_morse

def test_encrypt_letter_to_morse():

    assert encrypt_letter_to_morse("A") == '.-'
    assert encrypt_letter_to_morse("x") == '-..-'
    assert encrypt_letter_to_morse(" ") == ' '

def test_encrypt_to_morse():
    assert encrypt_to_morse("almuerzo") == ".- .-.. -- ..- . .-. --.. ---"
    assert encrypt_to_morse("casero") == "-.-. .- ... . .-. ---"
                                    
    assert encrypt_to_morse("almuerzo casero") ==  ".- .-.. -- ..- . .-. --.. --- -.-. .- ... . .-. ---"

def test_encrypt_ñ():
    assert encrypt_to_morse("ñoñerias") == "--·-- ---  --·-- . .-. .. .- ..."
                                

    