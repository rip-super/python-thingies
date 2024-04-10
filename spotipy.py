import os
import urllib.request
import re
import threading
import time
import sys
import requests
import base64
import json
from bs4 import BeautifulSoup
from pytube import YouTube
from moviepy.editor import VideoFileClip

waiting = False
def anim():
    spinnerChars = ["|", "/", "—", "\\"]
    while waiting:
        for i in range(4):
            if not waiting:
                break
            sys.stdout.write("\b" + spinnerChars[i])
            sys.stdout.flush()
            time.sleep(0.65)

def animate(text):
    global waiting
    waiting = True
    sys.stdout.write(text)
    threading.Thread(target=anim).start()

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def create_mp3(keyword):
    global waiting
    target_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'Downloaded Songs')
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    search_keyword = keyword.replace(" ", "+")
    cls()
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    video_url = "https://www.youtube.com/watch?v=" + video_ids[0]

    animate("Fetching Video... ")
    yt = YouTube(video_url)
    yt.streams.first().download(target_dir)
    song_title = yt.title
    waiting = False
    print("\nVideo Found!")

    downloaded_filename = yt.streams.first().default_filename
    downloaded_file_path = os.path.join(target_dir, downloaded_filename)

    if os.path.exists(downloaded_file_path):
        print("Converting Video... ")
        mp3_file_path = os.path.splitext(downloaded_file_path)[0] + ".mp3"
        video = VideoFileClip(downloaded_file_path)
        audio = video.audio
        audio.write_audiofile(mp3_file_path)
        cls()
        video.close()
        audio.close()
        os.remove(downloaded_file_path)

        print("Successfully created MP3 file!\n> " + song_title + ".mp3" + " created in " + target_dir)
    else:
        print("Error. Could not create MP3 file")

def main():
  cls()
  playlistUrl = input("Please paste a Spotify playlist URL: ")
  playlistHtml = requests.get(playlistUrl).text
  soup = BeautifulSoup(playlistHtml, "html.parser")
  main = json.loads(base64.b64decode(soup.find(id="initial-state").contents[0]))
  for j in main["entities"]["items"]:
    for i in main["entities"]["items"][j]["content"]["items"]:
      song = i["itemV2"]["data"]
      create_mp3(song["name"] + " by " + song["artists"]["items"][0]["profile"]["name"])
  cls()
  print("All MP3s have been downloaded successfully!")


if __name__ == "__main__":
    main()