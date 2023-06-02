#
#
# egi ari chatpgts namoqmedari xoda odesme sheizleba damchirdes da egdos aq
#
#

import requests
import threading
import time

# Function to perform HTTP request and print the status code
def get_url_status(url):
    response = requests.get(url)
    timestamp = time.strftime("%H:%M:%S", time.localtime())
    print(f"{timestamp} - {url}: {response.status_code}")

# Create threads for each request
thread1 = threading.Thread(target=get_url_status, args=('https://midi7.ge',))
thread2 = threading.Thread(target=get_url_status, args=('https://youtube.com',))
thread3 = threading.Thread(target=get_url_status, args=('http://shamainhoboss.c1.biz',))

# Start the threads
thread1.start()
thread2.start()
thread3.start()

# Wait for all threads to finish
thread1.join()
thread2.join()
thread3.join()
