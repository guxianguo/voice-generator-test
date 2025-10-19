"播放音频"
from arcade import load_sound,play_sound,stop_sound

class voice():

    def __init__(self,path):
        self.o =load_sound(path=path)

    def play(self):
        self.player = play_sound(self.o)

    def stop(self):
        try:
            stop_sound(self.player)
        except:
            pass
    
    
    


if __name__ == "__main__":
    testpath = r"C:\Users\steve\AppData\Local\Temp\gradio\0f884bc88fc666ad7999a2a3028aa004fc363ccdaaa3e6014f9cf9223c6c3ad7\audio.wav"
    import time
    voi = voice(testpath)
    voi.stop()
    voi.play()
    time.sleep(3)
    voi.stop()
    voi.play()
    time.sleep(3)
