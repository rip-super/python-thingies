import time
import os
from pynput.keyboard import Key, Controller
keyboard = Controller()

def cls():
  return os.system("cls" if os.name == "nt" else "clear")
  
cls()
link_num = input("Please select how many tabs you would like for this program to open. (1-5)\n> ")

if link_num ==  "1":
  link1 = input("Please enter the link you would like to open\n> ")
  cls()
  print("Please now focus your Web Browser Tab. The program will begin in 10 seconds.")
  time.sleep(10)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link1)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  
elif link_num == "2":
  link1 = input("Please enter the first link you would like to open\n> ")
  link2 = input("Please enter the second link you would like to open\n> ")
  cls()
  print("Please now focus your Web Browser Tab. The program will begin in 10 seconds.")
  time.sleep(10)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link1)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link2)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  
elif link_num ==  "3":
  link1 = input("Please enter the first link you would like to open\n> ")
  link2 = input("Please enter the second link you would like to open\n> ")
  link3 = input("Please enter the third link you would like to open\n> ")
  cls()
  print("Please now focus your Web Browser Tab. The program will begin in 10 seconds.")
  time.sleep(10)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link1)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link2)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link3)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  
elif link_num == "4":
  link1 = input("Please enter the first link you would like to open\n> ")
  link2 = input("Please enter the second link you would like to open\n> ")
  link3 = input("Please enter the third link you would like to open\n> ")
  link4 = input("Please enter the fourth link you would like to open\n> ")
  cls()
  print("Please now focus your Web Browser Tab. The program will begin in 10 seconds.")
  time.sleep(10)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link1)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link2)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link3)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link4)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)  

elif link_num ==  "5":
  link1 = input("Please enter the first link you would like to open\n> ")
  link2 = input("Please enter the second link you would like to open\n> ")
  link3 = input("Please enter the third link you would like to open\n> ")
  link4 = input("Please enter the fourth link you would like to open\n> ")
  link5 = input("Please enter the fifth link you would like to open\n> ")
  cls()
  print("Please now focus your Web Browser Tab. The program will begin in 10 seconds.")
  time.sleep(10)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link1)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link2)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link3)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link4)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  keyboard.press(Key.ctrl_l)
  keyboard.press("t")
  keyboard.release(Key.ctrl_l)
  keyboard.release("t")
  time.sleep(0.2)
  keyboard.type(link5)
  keyboard.press(Key.enter)
  keyboard.release(Key.enter)
  
else:
  print("Invalid Input. Please try again.")