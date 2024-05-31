import os
import urllib.request
import re
import threading
import sys
import requests
import base64
import json
from bs4 import BeautifulSoup
from pytube import YouTube
from moviepy.editor import VideoFileClip

waiting = False

def cls():
    os.system("cls" if os.name == "nt" else "clear")

target_dir = os.path.join(os.path.expanduser('~'), 'Downloads', 'Downloaded Songs')
totalTasks = 0
tasksDone = 0

def updatePercent(total, done):
    barLength = 30
    percent = round(done / total * 100, 0)
    numEquals = int(percent / (100 / barLength))
    numSpaces = barLength - numEquals
    sys.stdout.write("\rDownloading Songs: [{}{}] {}%".format('=' * numEquals, ' ' * numSpaces, percent))
    sys.stdout.flush()

def create_mp3(keyword):
    try:
        global waiting
        global tasksDone
        global totalTasks
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)
    
        search_keyword = keyword.replace(" ", "+")
        html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
        video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
        video_url = "https://www.youtube.com/watch?v=" + video_ids[0]
        yt = YouTube(video_url)
        yt.streams.first().download(target_dir)
        song_title = yt.title
        waiting = False
    
        downloaded_filename = yt.streams.first().default_filename
        downloaded_file_path = os.path.join(target_dir, downloaded_filename)
    
        if os.path.exists(downloaded_file_path):
            mp3_file_path = os.path.splitext(downloaded_file_path)[0] + ".mp3"
            video = VideoFileClip(downloaded_file_path)
            audio = video.audio
            audio.write_audiofile(mp3_file_path, logger=None, verbose=False)
            video.close()
            audio.close()
            os.remove(downloaded_file_path)
        else:
            cls()
            print("Error. Could not create MP3 file")
    except:
        pass
    tasksDone += 1
    updatePercent(totalTasks, tasksDone)

def download_mp3s(song_list):
    global totalTasks
    threads = []
    totalTasks = len(song_list)
    for song in song_list:
        thread = threading.Thread(target=create_mp3, args=(song,))
        threads.append(thread)
        thread.start()
        

    for thread in threads:
        thread.join()

def main():
    cls()
    playlistUrl = input("Please paste a Spotify playlist URL: ")
    cls()
    sys.stdout.write("Working... ")
    sys.stdout.flush()
    playlistHtml = requests.get(playlistUrl).text
    soup = BeautifulSoup(playlistHtml, "html.parser")
    main = json.loads(base64.b64decode(soup.find(id="initial-state").contents[0]))
    song_list = []
    for j in main["entities"]["items"]:
        for i in main["entities"]["items"][j]["content"]["items"]:
            song = i["itemV2"]["data"]
            song_list.append(song["name"] + " by " + song["artists"]["items"][0]["profile"]["name"])
    download_mp3s(song_list)
    print("\nMP3s downloaded to " + target_dir)

if __name__ == "__main__":
    main()