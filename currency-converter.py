import requests
import os
import itertools
import threading
import time
import sys

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done == True:
            break
        sys.stdout.write("\rConverting currency..." + c)
        sys.stdout.flush()
        time.sleep(0.65)
    sys.stdout.write('\rDone!             ')

def cls():
  os.system("cls" if os.name == "nt" else "clear")


cls()
fromCurr = input("What currency would you like to convert from?\n> ").upper()
toCurr = input("What currency would you like to convert to?\n> ").upper()

while True:
    try:
        amount = float(input("What is the amount of money you would like to convert?\n> "))
    except:
        cls()
        print('The amount needs to be numeric')
        continue
            
    if not amount > 0:
        cls()
        print('Amount needs to be greater than 0')
        continue
    else:
        break
    
url = f"https://api.apilayer.com/fixer/convert?to={toCurr}&from={fromCurr}&amount={amount}"

payload = {}
headers= {"apikey": "UXQCcN69jaT3ee5DYgQ2Y3YbTZ8cznNR"}

done = False
t = threading.Thread(target=animate)
t.start()

try:
    response = requests.request("GET", url, headers=headers, data = payload)
    done = True
    result = response.json()
    print(f"\n{amount} {fromCurr} is {str(round(float(result["result"]), 2))} {toCurr}")

except:
    done = True
    cls()
    sys.exit('Failed to create link.\nThe following might be the causes\n-> No internet connection\n-> Invalid currency name(s)')
