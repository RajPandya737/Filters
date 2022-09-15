#IMPORTS
import numpy as np
from matplotlib import pyplot as plt
from imageio.v2 import imread
#


def main():
    #gets the images pixels in RGB values
    a = imread('eiffel.jpg')
    #store brightness values
    bright = []
    #goes through RGB values and calculates an artificial brightness using a formula based on the percieved human brightness
    for row in a:
        to_add = []
        for col in row:
            to_add.append(0.21*col[0]+0.72*col[1]+0.07*col[2])
        bright.append(to_add)
    #greyscales the image
    im = plt.imshow(bright, cmap='gray')
    plt.show()
#excecutes method
if __name__ == '__main__':
    main()
