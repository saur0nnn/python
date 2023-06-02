import requests
import threading
from bs4 import BeautifulSoup

def wamoxeba(url):
    r = requests.get(url)
    
    if r.status_code == 200:
        html = BeautifulSoup(r.content, 'html.parser')
        scrap = html.prettify()
        
        saxeli = url.split("//")[-1].replace("/", "_") + ".html"
        
        with open(saxeli, "w", encoding="utf-8") as file:
            file.write(scrap)
    else:
        print(f"racxa errori warmoishva roca amas vparsavdi: {url}")

count = int(input('websitebis raodenoba: '))
websites = []

for z in range(count):
    website = input("sheiyvane linki: ")
    websites.append(website)

threads = []

for website in websites:
    thread = threading.Thread(target=wamoxeba, args=(website,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

print("egaa zmao mshvidobashi")
