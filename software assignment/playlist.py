import os
import random
from playsound import playsound

folder_path = '/home/lahari/playlists'  

# List all files in the folder
files = os.listdir(folder_path)

# Randomize the file list
random.shuffle(files)

# Iterate over the randomized files
for file_name in files:
    file_path = os.path.join(folder_path, file_name)
    absolute_path = os.path.abspath(file_path)
    print(absolute_path)
    # Play the sound file
    playsound(absolute_path)

