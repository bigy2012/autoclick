import pyautogui as pg
import webbrowser
import time
import json
import sys
import datetime


url = open('url.json')
data = json.load(url)


def autoClick(keyword, qty):
        chat = pg.locateCenterOnScreen('3.png')
        start, end = keyword.split("-")

        if chat is not None:
            pg.click(chat)
            for i in range(int(start), int(end) + 1):
                pg.typewrite(str(i))
                pg.press('enter')
        else:
            print('ขออภัยผมหาห้องแชทไม่พบ!!')
            time.sleep(5)
            return False
        main()

def convertTime(time, seconds):
    hours, minutes = time.split(':')
    second = seconds
    down_second = int(seconds) - 0.2
    down_minutes = int(minutes) - 1

    return



def process(keyword, qty, date_object, date_input) :
    time_input_object = datetime.datetime.strptime(date_input, "%H:%M")
    current_time = datetime.datetime.now().strftime("%H:%M")
    start = convertTime(current_time, datetime.datetime.now().strftime("%S"))

    while current_time != date_input:
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(1)
        current_time = datetime.datetime.now()
        if time_input_object != date_input:
            process(keyword, qty, date_object, date_input)
        else:
            autoClick(keyword, qty)
            break
    
    autoClick(keyword, qty)
    sys.exit()


def main():
    exTime = datetime.datetime.now().strftime("%H:%M")
    date_input = input("เวลาที่คุณต้องการให้เปิดใช้งาน (เช่น "+ str(exTime) +") : ")
    format_string = "%H:%M"
    try:
        date_object = datetime.datetime.strptime(date_input, format_string)
    except ValueError:
        print('เวลาของคุณไม่ถูกต้อง')
        time.sleep(10)
        return False
    else:
        keyword = input('ข้อความของคุณ ? ')
        qty = int(data['qty'])

    process(keyword, qty, date_object, date_input)
    

if __name__ == "__main__":
    # webbrowser.open(data['url_01'])
    main()




