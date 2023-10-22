import pyautogui as pg
import webbrowser
import time



def autoClick(keyword):
    pg.click(750, 509)
    time.sleep(0.2)
    pg.typewrite(keyword, interval=0.2)
    pg.press('enter')
    return True
        

keyword = input('Keyword : ')
googleOpen = webbrowser.open('http://google.co.th', new=1)

time.sleep(1.5)
if googleOpen == True :
    autoClick(keyword)

# print(pg.position())



