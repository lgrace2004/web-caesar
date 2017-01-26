def alphabet_position(letter):
    letter = letter.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    position = alphabet.find(letter)
    return position


def rotate_character(char, rot):

    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char in lower_case:
        new_char_num = (alphabet_position(char) + rot) % 26
        new_char = lower_case[new_char_num]
    elif char in upper_case:
        new_char_num = (alphabet_position(char) + rot) % 26
        new_char = upper_case[new_char_num]
    else:
        new_char = char

    return new_char

def encrypt(text,rot):

    encrypted_message = ""
    for char in text:
        new_char = rotate_character(char,rot)
        encrypted_message = encrypted_message + new_char
    return encrypted_message
