# # import required modules
# from os import path
# from pydub import AudioSegment

# # assign files
# input_file = "audio.mp3"
# output_file = "result.wav"
# AudioSegment.converter = "C:\\Users\\debra\\AppData\\Roaming\\Python\\Python311\\site-packages\\ffmpeg\\audio.py"
# # convert mp3 file to wav file
# sound = AudioSegment.from_mp3(input_file)
# sound.export(output_file, format="wav")


# # import required modules
import subprocess

# convert mp3 to wav file
subprocess.call(['ffmpeg', '-y' '-i', 'audio.mp3',
				'converted_toav_file.wav'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.STDOUT,
                shell=True
                )
print("done")


# import os
# import subprocess

# if os.path.exists("audio.mp3"):
#     audio = "audio.mp3"
#     print("yes", audio)
#     subprocess.call(['ffmpeg', '-i', audio, 'converted_to_wav_file.mp3'])
