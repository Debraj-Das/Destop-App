from moviepy.editor import *
import os
import glob

os.chdir("Assets")

for i in glob.glob("*.mkv"):
    video = VideoFileClip(i)
    new_video = i.split(".")[0] + ".mp4"
    video.write_videofile(new_video, codec='libx264', audio_codec='aac')
    video.close()
    os.remove(i)
    os.system(f"move \"{new_video}\" ../Results")
    print(f"{i} to {new_video} converted Done!***\n")
    
