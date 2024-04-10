import itertools
import threading
import time
import sys
from pytube import YouTube
import os

def cls():
    os.system("cls" if os.name =="nt" else "clear")

def video_downloader(video_url):
    my_video = YouTube(video_url)
    my_video = my_video.streams.get_highest_resolution()
    my_video.download("C:\\Users\\nmdas\\Downloads\\Downloaded Videos")
    return my_video.title

def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done == True:
            break
        sys.stdout.write('\rDownloading your video, please wait...' + c)
        sys.stdout.flush()
        time.sleep(0.65)
    sys.stdout.write('\rDone!     ')

cls()
done = False
youtube_link = input('Please enter the YouTube video link:\n> ')
if not ("https://" in youtube_link or "http://" in youtube_link):
  youtube_link = "https://" + youtube_link
t = threading.Thread(target=animate)
t.start()

try:
    video = video_downloader(youtube_link)
    done = True
    cls()
    print(f'\n"{video}" downloaded successfully!!')
 
except:
    done = True
    cls()
    sys.exit('Failed to download video\nThe following might be the causes\n-> No internet connection\n-> Invalid video link')