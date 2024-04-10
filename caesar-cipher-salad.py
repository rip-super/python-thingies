import os
def cls():
    os.system("cls" if os.name == "nt" else "clear")

cls()
FIRST_CHAR_CODE = ord("A")
LAST_CHAR_CODE = ord("Z")
CHAR_RANGE = LAST_CHAR_CODE - FIRST_CHAR_CODE + 1

def caesar_shift(message, shift):
    result = ""
    for char in message.upper():
        if char.isalpha():
          char_code = ord(char)
          new_char_code = char_code + shift
          if new_char_code > LAST_CHAR_CODE:
              new_char_code -= CHAR_RANGE
          if new_char_code < FIRST_CHAR_CODE:
              new_char_code += CHAR_RANGE
          new_char = chr(new_char_code)
          result += new_char
        else:
            result += char
        
    print(result)

answer = input("Would you like to encrypt or decrypt?(e/d)\n> ") 

if answer == "e":
    cls()
    user_message = input("Message to encrypt:\n> ")
    caesar_shift(user_message, 22)
    
elif answer == "d":
    cls()
    user_message = input("Message to decrypt:\n> ")
    caesar_shift(user_message, -22)
    
else:
    print("Invalid Input")