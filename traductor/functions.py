
morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'Ñ':' --·--',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    ' ': ' '
}

def encrypt_letter_to_morse(letter:str)-> str:
    """
    Función que encripta las letras y las transforma en 
    código morse
    """
    new_letter = ""
    letter_up =  letter.upper()
    
    for clave,valor in morse_code.items():
            
        if letter_up == clave:
            new_letter = valor
            break

    return new_letter

def encrypt_to_morse(word:str)->str:
    """
    Función que encripta las palabras y las transforma en 
    código morse
    Separa cada palabra con doble espacio
    """
    new_word = ""

    for letter in word:
        new_word += encrypt_letter_to_morse(letter) + " "
    return new_word.strip()


def encrypt_letter_to_plane(code):
    """
    Función que encripta los puntos y rallas y los transforma en 
    texto plano
    """
    new_letter = ""

    for clave,valor in morse_code.items():
        if code  == valor:
            new_letter = clave
            break
        else:
            new_letter = code
    return new_letter

def encrypt_to_plane(code):
    word_list = code.split("  ")
    
    new_word = ""
    for word in word_list:
        sign_list = word.split(" ")
        for sign in sign_list:
            new_word += encrypt_letter_to_plane(sign) 
        new_word += " "
    return new_word.lower().strip()

