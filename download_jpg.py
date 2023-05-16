import multiprocessing
import requests
import time

def downloadFile(url, name):
  print(f"Started Downloading {name}")
  response = requests.get(url)
  open(f"file{name}.jpg", "wb").write(response.content)
  print(f"Finished Downloading {name}")
 

if __name__ == "__main__":
    url = "https://picsum.photos/2000/3000"
    pros = []
    n = int(input("enter the no of img :"))
    time1 = time.perf_counter()
    for i in range(n):
        p = multiprocessing.Process(target=downloadFile, args=[url, i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
    # calculate the total time taken
    time2 = time.perf_counter()
    print("time : ",time2 - time1)
