import os
import base64
from cryptography.fernet import Fernet

def cls():
    os.system("cls" if os.name == "nt" else "clear")

cls()
print("-- Welcome --\n")
print("Please type an option and press enter:\n")
print("e - Encrypt with passphrase")
print("d - Decrypt with passphrase")
print("x - Exit\n")
choice = input("Choice: ")

if choice == "e":
  cls()
  print("-- Encrypt with passphrase --\n")
  print("You have chosen to encrypt a string with a passphrase.\n")
  string = input("Please enter the string to encrypt: ")
  print("\nYou will now create a passphrase. The passphrase is used for\nencryption and is set during encryption of the string.\nThe passphrase cannot be more than 32 characters long.\n")
  passphrase = input("Please enter a passphrase to use during encryption: ")
  if len(passphrase) > 32:
    print("\nThe passphrase cannot be more than 32 characters long.")
  else:
    key = passphrase
    for i in range(32 - len(passphrase)):
      key = key + "_"
    key = base64.b64encode(key.encode())
    f = Fernet(key)
    stringenc = f.encrypt(string.encode())
    print("\nEncrypted string: " + stringenc.decode())
elif choice == "d":
  cls()
  print("-- Decrypt with passphrase --\n")
  print("You have chosen to decrypt a string with a passphrase.\n")
  string = input("Please enter the string to decrypt: ")
  print("\nYou will now enter the passphase. The passphase is used for decryption\nand is set during encryption of the string. You must enter the same\npassphrase as used during encryption or decryption will fail.\n")
  passphrase = input("Please enter the passphrase used to encrypt the string: ")
  if len(passphrase) > 32:
    print("\nThe passphrase cannot be more than 32 characters long.")
  else:
    key = passphrase
    for i in range(32 - len(passphrase)):
      key = key + "_"
    key = base64.b64encode(key.encode())
    try:
      f = Fernet(key)
      stringenc = f.decrypt(string.encode())
      print("\nDecrypted string: " + stringenc.decode())
    except:
      print("\nThe passphrase is invalid.")
elif choice != "x":
  print("\nInvalid input.")