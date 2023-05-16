import os

if not os.path.exists("Results"):
    os.mkdir("Results")

print("Some Important Note: \n Please put your Working file in **Assets** folder\n")

print("-------***Options***-------")
print("1. mvk to mp4 Convert (Video)")
print("2. mvk to mp3 Convert (Audio)")

try:
    option = int(input("Enter your option: "))
except:
    print("Please enter a valid option")
    option = int(input("Enter Vaild option: "))

if option == 1:
    print("***MKV to MP4 Convert***")
    os.system("python -u \"Code\mkv_to_mp4_convert.py\"")
elif option == 2:
    print("***MKV to MP3 Convert***")
    os.system("python -u .\Code\mkv_to_mp3_convert.py")
else:
    print("Please enter a valid option")
    exit()
