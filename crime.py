"主框架"
from PIL import ImageGrab
import imgtobase
import screen
import send
import deal
import load
import playsound

import time


LAUNG = send.orcoption_jp


type_audio = "type_audio"
type_trans = "type_trans"

class mai:

    def __init__(self):
        #time.sleep(3)
        self.busy = False
        self.lau = LAUNG
        self.data = load.da.data            #{'阿米娅': 'C:\\Users\\steve\\Desktop\\Π神\\gal\\data\\amiya'}
        screen.main()
        self.box = screen.box1
        print("box:",self.box)
        try:
            self.voiceclient = send.send2()
        except:
            print("cosyvoice连接失败")

    def poss(self,show = False):
        """截图"""
        self.busy = True
        pic = ImageGrab.grab(self.box)
        print(show)
        if(show):pic.show()
        tex = imgtobase.image_to_base64(pic)
        print("截图完成")
        return tex

    def send(self,possed)->dict:
        """图像->文本"""
        print("开始识别文本")
        p = send.send(possed,option=self.lau)
        print("识别文本完成")
        return p
    
    def ct(self,text)->str:
        """图像识别->角色识别"""
        p = text
        #print("文本-》"+text["data"])
        p = deal.searchct(text,self.data)
        print("识别角色",p)
        return p

    def poss_send_ct(self)->str:
        """截图->识别->返回角色名"""
        return self.ct(self.send(self.poss()))
    
    def poss_send_ct_audio(self):
        """返回音频地址"""
        data = self.send(self.poss())
        print("data" , data)
        name = self.ct(data)
        data  = self.trans(data,name)
        path =self.getaudio(data=data,name=name)
        print("生成的音频地址",path)
        return path

        
    def trans(self,data:dict,name)->str:
        """识别角色->处理"""
        result = deal.deal(data["data"].replace(name,""))
        print("trans")
        return result

    def getaudio(self,data,name):
        """获取音频地址"""
        o = self.getway(name=name)
        return self.voiceclient(text=data,prompt=o["promp"],fileway=o["way"])
        
    def playvoice(self,path):
        self.sound = playsound.voice(path=path)
        self.sound.play()

    def stopvoice(self):
        try:
            self.sound.stop()
        except:
            pass

    def getway(self,name):
        """通过名字查询prompt和wav地址"""
        way = self.data[name]
        with open(way+"\\script.txt","r",encoding="utf8") as fp:
            promp = fp.read()
        return {"way":way + "\\1.wav","promp":promp}
    

    def type_audio(self):
        "语音模式"
        try:
            path = self.poss_send_ct_audio()
            self.busy = False
            self.playvoice(path=path)
        except:
            self.busy = False

    def type_trans(self):
        "翻译模式"
        try:
            text = self.send(self.poss())
            print(text)
        except:
            pass



    def run(self,ty,*arg,**args):
        try:
            l = getattr(self,ty)
            #print(arg,args)
            l(*arg,**args)
        except AttributeError:
            print("unknow type")
        

if __name__ == "__main__":
    print("start")
    time.sleep(2)
    print("wake")
    p = mai()
    p.run("type_trans")
    
