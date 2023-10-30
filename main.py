import pyautogui as pg
import webbrowser
import time
import json
import datetime

url = open('url.json')
data = json.load(url)

def autoClick(keyword, qty):
    chat = pg.locateCenterOnScreen('3.png')

    if chat is not None:
        pg.click(chat)
        for i in range(1, qty + 1):
            pg.typewrite(keyword)
            pg.press('enter')
    else:
        print('ขออภัยผมหาห้องแชทไม่พบ!!')
        time.sleep(5)
        return False

# Open the web page
webbrowser.open(data['url_01'])
# Wait for the web page to load
time.sleep(5)

date_input = input("เวลาที่คุณต้องการให้เปิดใช้งาน (เช่น 13:30) : ")
keyword = input('ข้อความของคุณ ? ')
qty = int(data['qty'])

while True:
    current_time = datetime.datetime.now().strftime("%H:%M")

    if current_time == date_input:
        autoClick(keyword, qty)
        break
    else:
        # Calculate the time to the next minute and sleep until then
        time_to_next_minute = 60 - int(datetime.datetime.now().strftime("%S"))
        time.sleep(time_to_next_minute)
        print('โปรดรอให้ถึง ' + date_input)