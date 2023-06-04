import requests
import threading

websites = []
threads = []

def check(url):
    try:
        req = requests.get(url)
        
        if req.status_code == 200:
            print(f"{url} -> chartulia")
        else:
            print(f"{url} -> miuwvdomelia")
    except requests.exceptions.RequestException:
        print(f"{url} -> gamortulia")

count = int(input('websitebis raodenoba: '))

for a in range(count):
    w = input("website link: ")
    websites.append(w)

for w in websites:
    thread = threading.Thread(target=check, args=(w,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("\nThe end")
