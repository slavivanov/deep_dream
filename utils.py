from matplotlib.pyplot import imshow
from io import BytesIO
from IPython import display 
import matplotlib.pyplot as plt
import PIL.Image
import numpy as np

def display_img_array(ima):
    ima = np.clip(np.asarray(ima), 0, 255).astype('uint8')
    im = PIL.Image.fromarray(ima)
    bio = BytesIO()
    im.save(bio, format='png')
    display.display(display.Image(bio.getvalue(), format='png'))

def plot(img, scale=1, dpi=80):
    plt.figure(figsize=(img.shape[0]*scale/dpi, img.shape[1]*scale/dpi), dpi=dpi)
    imshow(img)