"按键监听,app启动"
import pynput
from sys import exit

import crime


class p():
    
    def __init__(self):
        self.main = crime.mai()

    def start(self):
        self.main.run(crime.type_audio)

    def stopvoice(self):
        self.main.stopvoice()

    def es(self):
        exit()

if __name__ == "__main__":
    start = p()
    with pynput.keyboard.GlobalHotKeys({"<ctrl>+<alt>" : start.start,"<ctrl>+<cmd>":start.stopvoice,"<ctrl>+<shift>+e":start.es}) as listener:
        print("按键监听开始")
        listener.join()