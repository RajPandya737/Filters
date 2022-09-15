import numpy as np
from matplotlib import pyplot as plt
from imageio.v2 import imread
def main():
    a = imread('eiffel.jpg')
    b = []
    for row in a:
        to_add = []
        for col in row:
            to_add.append(0.21*col[0]+0.72*col[1]+0.07*col[2])
        b.append(to_add)
    color = input("""What color would you like to shift the image 
    (options are black, red, blue, green, orange, purple, yellow)\n""")

    if color.lower()[:3] == 'red':
        color = 'hot'
    elif color.lower()[:5] == 'black':
        color = 'gray'
    elif color[:4] == 'blue':
        color = 'Blues'
    elif color[:5] == 'green':
        color = 'Greens'
    elif color[:6] == 'orange':
        color = 'Oranges'
    elif color[:6] == 'purple':
        color = 'Purples'
    elif color[:6] == 'yellow':
        color = 'afmhot'


    im = plt.imshow(b, cmap=color)
    plt.show()

if __name__ == '__main__':
    main()
