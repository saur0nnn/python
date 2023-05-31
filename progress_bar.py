from time import sleep
from progress.bar import IncrementalBar

with IncrementalBar('gamma_image.jpg >', suffix='%(percent).1f%% | %(eta)ds') as bar:
    for i in range(100):
        sleep(0.1)
        bar.next()        
        
        