import win32api, win32con
from PIL import ImageGrab
import os
import time
import datetime
from PIL import ImageOps
from numpy import *

"""
Cookie Clicking Point:
(290,480)
"""
# Globals
# ------------------
x_pad = 1723
y_pad = 415

xCookie = 229
yCookie = 379
 
def screenGrab():
    box = (x_pad, y_pad, x_pad + 167, y_pad+ 411 )
    im = ImageGrab.grab(box)
    #im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) +'.png', 'PNG')
    return im

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    
def mousePos(cord):
    time.sleep(0.01)
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))
    
def mousePosCookie(cord):
    time.sleep(0.01)
    win32api.SetCursorPos((cord[0],cord[1]))
    
def get_cordsCookie():
    x,y = win32api.GetCursorPos()
    print x,y
   
def get_cords():
    x,y = win32api.GetCursorPos()
    x = x - x_pad
    y = y - y_pad
    print x,y

def clickAlltheCookies(iterations, xkoord, ykoord):
    i = 1
    while i < iterations:                     
            mousePosCookie((xkoord, ykoord))
            leftClick()
            i += 1

            
#mousePos
class Cord:
    Cursor = (-234, -72)
    Grandma =(-234, -30)
    Farm = (-236, -6)
    Mine = (-235, 29)
    Factory = (-233, 58)
    Bank = (-232, 95)
    Temple = (-228, 127)
    Wizardtower =(-237, 159)
    Rocket =(-224, 195)
    Zerg = (-224, 228)

class imBuilds:
    imCursor = (137,23)
    imGrandma =(137,65)
    imFarm = (137,107)
    imMine = (137,146)
    imFactory = (137,186)
    imBank = (137,223)
    imTemple = (137,264)
    imWizardtower =(137,304)
    imRocket =(137,346)
    imZerg = (137,386)

class RGBavailable():
    imCursoravailable = (140, 133, 117)
    imGrandmaavailable = (148, 143, 124)
    imFarmavailable = (144, 142, 127)
    imMineavailable = (160, 157, 137)
    imFactoryavailable = (146, 141, 122)
    imBankavailable = (155, 150, 131)
    imTempleavailable = (139, 137, 124)
    imWizardtoweravailable = (155, 152, 135)

def investCookies():

    #click on rocket and zerg

    while 1==1:
        time.sleep(.1)
        im = screenGrab()
        if im.getpixel(imBuilds.imWizardtower) == RGBavailable.imWizardtoweravailable:
            mousePos(Cord.Wizardtower)
            time.sleep(.05)
            leftClick()
        else:
            break
        
    while 1==1:
        time.sleep(.1)
        im = screenGrab()
        if im.getpixel(imBuilds.imTemple) == RGBavailable.imTempleavailable:
            mousePos(Cord.Temple)
            time.sleep(.05)
            leftClick()
        else:
            break

    while 1==1:
        time.sleep(.1)
        im = screenGrab()
        if im.getpixel(imBuilds.imBank) == RGBavailable.imBankavailable:
            mousePos(Cord.Bank)
            time.sleep(.05)
            leftClick()
        else:
            break

    while 1==1:
        time.sleep(.1)
        im = screenGrab()
        if im.getpixel(imBuilds.imFactory) == RGBavailable.imFactoryavailable:
            mousePos(Cord.Factory)
            time.sleep(.05)
            leftClick()
        else:
            break

    while 1==1:
        time.sleep(.1)
        im = screenGrab()
        if im.getpixel(imBuilds.imMine) == RGBavailable.imMineavailable:
            mousePos(Cord.Mine)
            time.sleep(.05)
            leftClick()
        else:
            break

    while 1==1:
        time.sleep(.1)
        im = screenGrab()
        if im.getpixel(imBuilds.imFarm) == RGBavailable.imFarmavailable:
            mousePos(Cord.Farm)
            time.sleep(.05)
            leftClick()
        else:
            break

    while 1==1:
        time.sleep(.1)
        im = screenGrab()
        if im.getpixel(imBuilds.imGrandma) == RGBavailable.imGrandmaavailable:
            mousePos(Cord.Grandma)
            time.sleep(.05)
            leftClick()
        else:
            break

    while 1==1:
        time.sleep(.1)
        im = screenGrab()
        if im.getpixel(imBuilds.imCursor) == RGBavailable.imCursoravailable:
            mousePos(Cord.Cursor)
            time.sleep(.05)
            leftClick()
        else:
            break

def investCookiesSimple():
            mousePos(Cord.Wizardtower)
            time.sleep(.05)
            leftClick()

            mousePos(Cord.Temple)
            time.sleep(.05)
            leftClick()

            mousePos(Cord.Bank)
            time.sleep(.05)
            leftClick()
            
            mousePos(Cord.Factory)
            time.sleep(.05)
            leftClick()

            mousePos(Cord.Mine)
            time.sleep(.05)
            leftClick()

            mousePos(Cord.Farm)
            time.sleep(.05)
            leftClick()
            
            mousePos(Cord.Grandma)
            time.sleep(.05)
            leftClick()

            mousePos(Cord.Cursor)
            time.sleep(.05)
            leftClick()

        
def main():
    time.sleep(5)
    f = open("Log.txt", "a")      
    i = 1
    while 1 == 1 :
        clickAlltheCookies(100, xCookie, yCookie)
        investCookies()
        f.write(str(datetime.datetime.now()) + " Loop Number " + str(i) + "\n")
        i += 1
    f.close()
  
    
if __name__ == '__main__':
    main()
