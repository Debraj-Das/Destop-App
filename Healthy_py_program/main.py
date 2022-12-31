from play_video import Play
import time

def routine():
    total_hour = 0
    while total_hour<4:
        time.sleep(30)
        print("Please take your Eye exercise ")
        print("For Stop the video enter backspace")
        Play(1)
        time.sleep(30)
        print("Plese take you 400 ml water")
        Play(2)
        time.sleep(30)
        print("Please take 2 min exercise")
        Play(1)
        time.sleep(30)
        total_hour+=1
        print("Learning is sourse of prograss")
        print("Again start you Learning and untill you completed",total_hour,"hours")

    print("You completed 4 hour long learning take a 30 min break")
    return

if __name__=='__main__':
    print("Started the process :: ")
    while True:
        routine()
        time.sleep(60)