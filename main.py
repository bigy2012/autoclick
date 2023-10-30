import pyautogui as pg
import webbrowser
import time
import json
import sys
import datetime
import random

url = open('url.json')
data = json.load(url)

def autoClick(keyword, qty, clas):
        chat = pg.locateCenterOnScreen('3.png')
        start, end = keyword.split("-")
        pg.click(chat)

        if chat is not None:
            for i in range(int(start), int(end) + 1):
                for c in range(1, int(clas)):
                    random_integer = random.randint(int(start), int(end))
                    print(random_integer)
                    pg.typewrite(str(random_integer))
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
    total_date_input = str(hours) + ':' + str(down_minutes) + ':' + '55'

    return total_date_input



def process(keyword, qty, date_object, date_input, clas) :
    # time_input_object = datetime.datetime.strptime(date_input, "%H:%M")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    start = convertTime(date_input, datetime.datetime.now().strftime("%S"))

    while current_time != start:
        print(datetime.datetime.now().strftime("%H:%M:%S"))
        time.sleep(1.2)
        current_time = datetime.datetime.now()
        if current_time != start:
            process(keyword, qty, date_object, date_input, clas)
        else:
            autoClick(keyword, qty, clas)
            break
    
    autoClick(keyword, qty, clas)
    sys.exit()


def main():
    exTime = datetime.datetime.now().strftime("%H:%M")
    clas = input("จำนวนรอบการรันเลข : ")
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

    process(keyword, qty, date_object, date_input, clas)
    

if __name__ == "__main__":
    # webbrowser.open(data['url_01'])
    main()




