from helpers import alphabet_position, rotate_character
from sys import argv, exit

def user_input_is_valid():
    if(len(argv) != 2):
        return False
    if(argv[1].isdigit()):
        return True
    return False


def encrypt(text, rot):
    buffer = ""
    if(len(argv) == 2):
        rot = argv[1]
    for let in text:
        buffer += rotate_character(let,rot)
    return buffer


def main():
    if not user_input_is_valid():
        print("usage: python3 caesar.py n")
        exit()
    print(encrypt(input("Type a message:")))
    
if __name__ == '__main__':
    main()

