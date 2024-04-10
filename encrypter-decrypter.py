import random
import string
import os

def cls():
  os.system("cls" if os.name == "nt" else "clear")

cls()
characters = " " + string.punctuation + string.digits + string.ascii_letters
characters = list(characters)
key = characters.copy()

random.shuffle(key)

#ENCRYPT
text = input("Please enter a message to encrypt: ")
cipher_text = ""

for letter in text:
    index = characters.index(letter)
    cipher_text += key[index]

print(f"Encrypted message: {cipher_text}")

answer = input("Would you like to decrypt the message? (y/n):  ")
if answer == "y":

#DECRYPT
  text = ""

  for letter in cipher_text:
      index = key.index(letter)
      text += characters[index]
  
  print(f"Decrypted message: {text}")
  
if answer == "n":
  print("Have a nice day!")