import time
import fbchat
from fbchat import Client
from fbchat.models import *

# คลาสสืบทอดจาก Client ของ fbchat
class ScheduledMessenger(Client):
    def __init__(self, email, password):
        super().__init__(email, password)

    # ฟังก์ชันส่งข้อความในกลุ่ม
    def send_scheduled_group_message(self, group_id, message, timestamp):
        self.send(Message(text=message), thread_id=group_id, thread_type=ThreadType.GROUP, schedule=timestamp)

if __name__ == "__main__":
    # เข้าสู่ระบบด้วยบัญชี Facebook
    client = ScheduledMessenger("wasaniy121@gmail.com", "wasaniy2527_@AaA")

    # ID ของกลุ่ม Facebook Chat ที่คุณต้องการส่งข้อความ
    group_id = "6183062878460507"

    # ข้อความที่คุณต้องการส่ง
    message = "Hello, this is a scheduled group message!"

    # เวลาที่คุณต้องการส่งข้อความ (เป็น timestamp)
    # ในตัวอย่างนี้คือการตั้งเวลาส่งข้อความในอีก 1 นาที
    timestamp = int(time.time()) + 60

    # ส่งข้อความในกลุ่มตามเวลาที่กำหนด
    client.send_scheduled_group_message(group_id, message, timestamp)

    # ออกจากระบบ
    client.logout()
