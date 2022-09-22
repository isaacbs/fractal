import numpy as np
import matplotlib.pyplot as plt



def mandel(width, height):
    image = [[0]*width]*height
    for i in range(width):
        for j in range(height):
            x0 = i/width*2.47-2.00
            y0 = j/height*2.24-1.12
            x, y = 0, 0
            x2, y2 = 0, 0
            i = 0
            while((x2 + y2 <= 4) and (i < 1000)):
                y = 2*x*y + y0
                x = x2-y2 + x0
                x2 = x*x
                y2 = y*y
                i += 1
            image[i,j] =  i
    return image

plot = plt.figure()
