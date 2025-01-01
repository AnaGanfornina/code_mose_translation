
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
    'N': '-.',#pon la ñ
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
    '9': '----.'
}

#user = input("Qué desea transcribir?")

def encrypt_letter_to_morse(letter:str)-> str:
    """
    Función que encripta las letras y las transforma en 
    código morse
    """
    new_letter = ""
    letter_up =  letter.upper()
    if letter_up in morse_code:
        for clave,valor in morse_code.items():
            
            if letter_up == clave:
                new_letter = valor
                break
    else:
        new_letter = letter

    return new_letter



def encrypt_to_morse(word:str)->str:
    new_word = ""
    remplaced_word = word.replace(" ","")
    for letter in remplaced_word:
        new_word += encrypt_letter_to_morse(letter) + " "
    return new_word.strip()

 


#falla porque mete un espacio entre palabra y palabra de mas, pero no en el final ni en el principio