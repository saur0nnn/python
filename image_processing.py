from PIL import Image
import numpy as np
from time import sleep
from progress.bar import IncrementalBar

image = np.array(Image.open('image.jpg'))

print("[height, width, color]")
print(image)
print("\nsawyisi fotos tipi: ", image.dtype)
print("sawyisi fotos rezolucia da color: ", image.shape)

with IncrementalBar('bad_quality_image.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(image).save('bad_quality_image.jpg', quality = 1)
    for i in range(100):
        bar.next() 

#fotodan witeli feris garda yvelas washla
image_R = image.copy()
image_R[:, :, (1, 2)] = 0

#fotodan mwvane feris garda yvelas washla
image_G = image.copy()
image_G[:, :, (0, 2)] = 0

#fotodan lurji feris garda yvelas washla
image_B = image.copy()
image_B[:, :, (0, 1)] = 0

#ferebis masivebis sheerteba (samive fotos ert fotoshi shenaxva)
image_RGB = np.concatenate((image_R, image_G, image_B), axis=1)
with IncrementalBar('colors_image.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(image_RGB).save('colors_image.jpg', quality = 100)
    for i in range(100):
        bar.next() 


#ferebis calcalke shenaxva
with IncrementalBar('RGB images >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(image_R).save('image_R.jpg')
    Image.fromarray(image_G).save('image_G.jpg')
    Image.fromarray(image_B).save('image_B.jpg')
    for i in range(100):
        bar.next() 

#inverted colors
inverted = 255 - image
with IncrementalBar('inverted_image.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(inverted).save('inverted_image.jpg')
    for i in range(100):
        bar.next() 

#resize
resize = np.array(Image.open('image.jpg').resize((256,256)))
with IncrementalBar('resized_image.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(resize).save("resized_image.jpg")
    for i in range(100):
        bar.next() 
      
#ragaca efeqti
image_32 = image // 32*32
image_64 = image // 64*64
image_128 = image // 128*128


with IncrementalBar('32, 64, 128 images >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(image_32).save('image_32.jpg')
    Image.fromarray(image_64).save('image_64.jpg')
    Image.fromarray(image_128).save('image_128.jpg')
    for i in range(100):
        bar.next() 

racxa_efeqti = np.concatenate((image_32, image_64, image_128), axis = 1)
with IncrementalBar('32, 64, 128 image >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(racxa_efeqti).save('efeqtebiani_image.jpg')
    for i in range(100):
        bar.next() 

#gamma
less = 255.0 * (image / 255.0)**(1 / 2.2)
more = 255.0 * (image / 255.0)**2.2

with IncrementalBar('gamma_image.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    image_gamma = np.concatenate((less, image, more), axis = 1)
    Image.fromarray(np.uint8(image_gamma)).save("gamma_image.jpg") 
    for i in range(100):
        bar.next() 

with IncrementalBar('more_gamma_image.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(np.uint8(more)).save("more_gamma_image.jpg")
    for i in range(100):
        bar.next() 


#trim
trimmed_image = image[900:2000, 1900:2200]
with IncrementalBar('trimmed_image.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(trimmed_image).save("trimmed_image.jpg")
    for i in range(100):
        bar.next() 

#paste trimmed image
image[1770:3100, 2700:3000] = trimmed_image[:, :]
with IncrementalBar('pasted.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(image).save("pasted_image.jpg")
    for i in range(100):
        bar.next() 

#flip
flipped_image = np.flip(np.array(Image.open('image.jpg')))
with IncrementalBar('flipped_image.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(flipped_image).save("flipped_image.jpg")
    for i in range(100):
        bar.next()
        
#rotate90
rotated90_image = np.rot90(np.array(Image.open('image.jpg')))
with IncrementalBar('rotated90_image.jpg >', suffix='%(percent).1f%% | %(elapsed_td)s') as bar:
    Image.fromarray(rotated90_image).save("rotated90_image.jpg")
    for i in range(100):
        bar.next()



print("\n--- END OF THE PROGRAM ---\n")
