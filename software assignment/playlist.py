import os
import random
from playsound import playsound

folder_path = input("Enter the path to the folder: ")
files = os.listdir(folder_path)
random.shuffle(files)

play_next_song = True
for file_name in files:
    if not play_next_song:
        break

    file_path = os.path.join(folder_path, file_name)
    print("Playing:", file_path)
    playsound(file_path)
    
    print("Press Enter to play the next song or 'q' to quit.")
    user_input = input()
    
    if user_input.lower() == 'q':
        play_next_song = False
