import random
from playsound import playsound

playlist = ['1.mp3', '2.mp3', '3.mp3', '4.mp3', '5.mp3', '6.mp3', '7.mp3', '8.mp3', '9.mp3', '10.mp3', '11.mp3', '12.mp3', '13.mp3', '14.mp3', '15.mp3', '16.mp3', '17.mp3', '18.mp3', '19.mp3', '20.mp3']

while True:
    # Generate a random number within the range of the song list
    random_number = random.randint(0, len(playlist) - 1)

    # Play a random song in playlist
    song_to_play = playlist[random_number]
    playsound(song_to_play)
