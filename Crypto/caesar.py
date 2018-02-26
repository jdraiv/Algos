
import string


def caesar_cipher(key, s):
    result = ""
    alphabet = list(string.ascii_uppercase)

    for letter in s:
        if letter != " ":
            new_index = alphabet.index(letter.upper()) + key

            if new_index >= 26:
                while new_index >= 26:
                    new_index -= 25
            result += alphabet[new_index]
        else:
            result += " "
    return result
