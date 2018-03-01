
import string


def caesar_cipher(s, key):
    result = ""
    alphabet = list(string.ascii_uppercase)

    for letter in s:
        if letter.upper() in alphabet:
            new_index = alphabet.index(letter.upper()) + key

            if new_index >= 26:
                while new_index >= 26:
                    new_index -= 25
            result += alphabet[new_index]
        elif letter == " ":
            result += " "
        else:
            result += letter
    return result

