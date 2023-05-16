import os , glob

l = glob.glob('*.jpg')
for i in l:
    os.remove(i)
    print(f"Deleted {i}")