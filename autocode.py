import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

#program to write code that checks if a number is prime without using modulus(%)

time.sleep(5)

keyboard.type('number = int(input("> "))\n')
#2**4 is the 4 bit integer limit, 2**8 is 8 bit integer limt and so on.
#to handle every single number that a computer can use you would have to do 2**32 which equates to about 4.2 billion
#(2**32 is the 32 bit integer bit limit which the the largest number that (most) computers can process)
for i in range(2**4 + 1):
    odd_even = "even" if i % 2 == 0 else "odd"
    if i == 0:
        keyboard.type('if number == 0:\n')
        keyboard.type('    print("even")\n')
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)
    else:
        keyboard.type(f'elif number == {i}:\n')
        keyboard.type(f'    print("{odd_even}")\n')
        keyboard.press(Key.backspace)
        keyboard.release(Key.backspace)