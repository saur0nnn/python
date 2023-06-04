import threading
import requests
import shutil

images = []
threads = []
names = []

count = int(input('fotoebis raodenoba: '))

for a in range(count):
    img = input("\nfotos linki: ")
    name = input('failis saxeli (gafartoebit [.png / .jpg]): ')
    names.append(name)
    images.append(img)

def download(url, name):
    try:
        r = requests.get(url, stream=True)
        
        with open(name, 'wb') as f:
            shutil.copyfileobj(r.raw, f)
        
    except requests.exceptions.RequestException:
        print("ver gadmovwer mititebul fotos")

for i in range(count):
    thread = threading.Thread(target=download, args=(images[i], names[i]))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("\nThe End")
