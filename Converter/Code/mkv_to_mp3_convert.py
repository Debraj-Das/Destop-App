from moviepy.editor import *
import os
import glob

os.chdir("Assets")

for i in glob.glob("*.mkv"):
    video = VideoFileClip(i)
    audio_file = i.split(".")[0] + ".mp3"
    audio = video.audio
    audio.write_audiofile(audio_file )
    audio.close()
    video.close()
    os.remove(i)
    os.system(f"move \"{audio_file}\" ../Results")
    print(f"{i} to {audio_file} converted and move Done!***\n")
    
