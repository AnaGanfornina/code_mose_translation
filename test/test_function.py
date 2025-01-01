from traductor.functions import encrypt_letter_to_morse,encrypt_to_morse,encrypt_letter_to_plane

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

def test_encrypt_letter_to_plane():
    assert encrypt_letter_to_plane('.-') == "A"
    assert encrypt_letter_to_plane('-..-') == "X"
    assert encrypt_letter_to_plane(' ') == " "

def _test_encrypt_to_plain():
    #assert encrypt_to_plane
    pass