from moviepy.editor import *
import os
import glob

def convert():
    for i in glob.glob("*.m4v"):
        d = "Now_This_files_converts.m4v"
        os.rename(i, d)
        video = VideoFileClip(d)
        new_video = d[:-4] + ".mp4"
        video.write_videofile(new_video, codec='libx264', audio_codec='aac' , threads = 4)
        video.close()
        os.remove(d)
        d = i[:-4]+".mp4"
        os.rename(new_video, d)
        print(f"{i} to {d} converted Done!***\n")


def Director():
    list = os.listdir()
    list_dir = []
    for i in list:
        if os.path.isdir(i):
            list_dir.append(i)
    return list_dir


if __name__ == "__main__":
    Dir = Director()
    for i in Dir:
        print(f"{i} Convert Started")
        os.chdir(i)
        convert()
        os.chdir("..")
        print(f"{i} folder Convert Completed")
