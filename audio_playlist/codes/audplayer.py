from moviepy.editor import VideoFileClip
import numpy as np

def play_mp4_audio(filename):
    video = VideoFileClip(filename)
    audio = video.audio
    audio.preview()

played = np.zeros(20)
list_of_songs = np.arange(1, 21, 1)
c = 0
r = 0
x = int(input("Enter the number of times to play the playlist: "))
while r < x:
    i = np.random.choice(list_of_songs)
    if played[i-1] == 0:
        ch = str(input("The next song on queue is aud" + str(i) + ". Press 'c' to continue, 's' to skip: "))
        if ch == 's':
            played[i-1] = 1
        else:
            print("Now playing aud" + str(i) + ".mp4...")
            play_mp4_audio("/home/aditya_varun_v/Documents/prv/audio_playlist/vid_files/aud" + str(i) + ".mp4")
        c = c + 1
        played[i-1] = 1
        if c == 20:
            played = np.zeros(20)
            c = 0
            r = r + 1
            continue
    else:
        continue

