import qrcode
import os
from pyzbar.pyzbar import decode
from PIL import Image

def cls():
    os.system("cls" if os.name == "nt" else "clear")

cls()
print("NOTICE:\nWhen this program creates a QR Code\nIt will be stored in a new PNG file\nThat will be created after this script finishes\n\nIf you would not like for this program to create a new file\nPlease press CTRL + C on your keyboard two times to end this program\nOtherwise: ")
os.system("pause")
cls()
answer = input("Would you like to create a new QR Code or decode a QR code? (e/d)\n> ")
if answer == "1":
    cls()
    data = input("What would you like to turn into a QR code?\n> ")
    name = input("What would you like the name of the file be?\n> ")
    if not (".png" in name):
        name = name + ".png"
    img = qrcode.make(data)
    img.save(name)
    print("Please check the directory this file is in to find the new file with a QR code.")

elif answer == "2":
    showerror = False
    cls()
    file_name = input("What is the name of the file you would like to decode?\n> ")
    if not (".png" in file_name):
        file_name = file_name + ".png"
    try:
        decodeQR = decode(Image.open(file_name))
    except:
        showerror = True
    if showerror:
        cls()
        print("Looks like I couldn't find that file.\nDouble check to make sure that the you spelled the name of the file correctly\nOr if the file exists at all.")
        quit()
    print('The QR code decoded is "' + decodeQR[0].data.decode('ascii') + '"')
else:
    print("Invalid input. Please try again.")
