import requests
import json
import os
import itertools
import threading
import time
import sys

def animate():
    for i in itertools.cycle(['|', '/', '-', '\\']):
        if done == True:
            break
        sys.stdout.write("\rCreating your link, please wait..." + i)
        sys.stdout.flush()
        time.sleep(0.65)
    sys.stdout.write('\rDone!             ')

def cls():
  os.system("cls" if os.name == "nt" else "clear")

cls()
longLink = input("Please enter the link to shorten: ")
if not ("https://" in longLink or "http://" in longLink):
  longLink = "https://" + longLink

done = False
t = threading.Thread(target=animate)
t.start()


try:
  response = requests.post("https://api-ssl.bitly.com/v4/shorten", json = {"domain": "bit.ly", "long_url": longLink}, headers = {"Authorization": "Bearer 21c7782eac5bd3857c46edb348ee23233259a755"})
  done = True
  print("\nShortened link: " + json.loads(response.text)["link"])
    
   
except:
  done = True
  cls()
  sys.exit('Failed to create link.\nThe following might be the causes\n-> No internet connection\n-> Invalid link')

