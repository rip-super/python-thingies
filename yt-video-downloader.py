import itertools
import threading
import time
import sys
import os
from pytube import YouTube
from pytube.exceptions import RegexMatchError, VideoUnavailable

def cls():
    os.system("cls" if os.name == "nt" else "clear")

def video_downloader(video_url):
    my_video = YouTube(video_url)
    if my_video.streams:
        my_video = my_video.streams.get_highest_resolution()
        my_video.download("C:\\Users\\nmdas\\Downloads\\Downloaded Videos")
        return my_video.title
    else:
        raise VideoUnavailable("Video is not available")

def animate(done_event):
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done_event.is_set():
            break
        sys.stdout.write('\rDownloading your video, please wait...' + c)
        sys.stdout.flush()
        time.sleep(0.65)
    sys.stdout.write('\rDone!     ')

def main():
    cls()
    done_event = threading.Event()
    youtube_link = input('Please enter the YouTube video link:\n> ')
    if not ("https://" in youtube_link or "http://" in youtube_link):
        youtube_link = "https://" + youtube_link
    t = threading.Thread(target=animate, args=(done_event,))
    t.start()

    try:
        video = video_downloader(youtube_link)
        done_event.set()
        cls()
        print(f'\n"{video}" downloaded successfully!!')
    
    except (RegexMatchError, VideoUnavailable) as e:
        done_event.set()
        cls()
        sys.exit(f'Failed to download video\nError: {e}')
    
    except Exception as e:
        done_event.set()
        cls()
        sys.exit(f'Failed to download video\nError: {e}')

if __name__ == "__main__":
    main()
