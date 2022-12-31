from play_video import Play

while True:
    print("Option of Songs***")
    print("0) Deva Shree Ganesha")
    print("1) pal tu pal")
    print("2) Phenix")
    print("3) Suna Hai")
    print("4) Symphony")
    print("5) Ghost")
    print("6) kaise hua")
    print("7) CONTROL")
    print("8) Stronger")
    print("9) Aigiri Nandini")
    print("For positive) Shiv Tandav")
    print("For exit enter native")
    n = int(input("Enter you song number : "))
    if n<0:
        break
    print("Python Video player Start :: ")  
    Play(n)
print("finish")