import string

def alphabet_position(letter):
    let = letter.lower()
    pos = 0
    for alpha in string.ascii_lowercase:
        if alpha == let:
            break
        pos += 1
    return pos

def rotate_character(char, rot):
    if char not in string.ascii_letters:
        return char
    is_upper = False
    if char in string.ascii_uppercase:
        is_upper = True
    letpos = alphabet_position(char.lower())
    newpos = (letpos + rot) % 26
    finallet = string.ascii_lowercase[newpos]
    if is_upper:
        finallet = finallet.upper()
    return finallet
