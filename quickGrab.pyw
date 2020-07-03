
from PIL import ImageGrab
import os
import time


# Globals
# ------------------
x_pad = 1723
y_pad = 415
 
def screenGrab():
    box = (x_pad, y_pad, x_pad + 167, y_pad+ 411 )
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +
'.png', 'PNG')


def main():
    screenGrab()

   
 
if __name__ == '__main__':
    main()
