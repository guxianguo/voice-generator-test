"向cosyvoice和umiocr发送请求"

import imgtobase
from requests import get,post
from gradio_client import Client, file

URL = r"http://127.0.0.1"
PORT = "1224"
API = r"/api/ocr"
OPT = r"/api/ocr/get_options"

way = URL+":"+PORT +API



orcoption_cn = {
    "ocr.language" : "models/config_chinese.txt",
    "tbpu.parser": "multi_para",
    "ocr.cls" : "false",
    "ocr.limit_side_len" : "9999",
    "data.format" : "text"
}

orcoption_jp = {
    "ocr.language" : "models/config_japan.txt",
    "tbpu.parser": "multi_para",
    "ocr.cls" : "false",
    "ocr.limit_side_len" : "9999",
    "data.format" : "text"
}

orcoption_cn_te = {
    "ocr.language":"简体中文",
    "ocr.language.chi_sim":True,
    "tbpu.parser": "none",
    "ocr.cls" : "false",
    "ocr.limit_side_len" : "9999",
    "data.format" : "text"
}

orcoption_jp_te = {
    "ocr.language":"日本語",
    "ocr.language.jpn":True,
    "tbpu.parser": "none",
    "ocr.cls" : "false",
    "ocr.limit_side_len" : "9999",
    "data.format" : "text",
    "ocr.vert" : True
}

def send(data,option = orcoption_cn):
    edi = {
        "base64":data,
        "options":option
    }
    result = post(way,json=edi)
    return result.json()

def option():
    op = URL+":"+PORT+OPT
    res =get(op)
    return res.json()


class send2():

    def __init__(self):
        self.client = Client("http://127.0.0.1:50004/")
        self.ty1 = "跨语种复刻"
        self.ty2 = "3s急速复刻"

    def __call__(self,text,prompt,fileway):
        print("开始生成音频")
        result = self.client.predict(
		    tts_text=str(text),
		    mode_checkbox_group=self.ty2,
		    prompt_text=str(prompt),
		    prompt_wav_upload=file(str(fileway)),
		    prompt_wav_record=file(str(fileway)),
		    instruct_text="有一些严肃",
		    seed=0,
		    stream="false",
		    speed=1,
		    api_name="/generate_audio"
        )
        print("生成音频结束")
        return result




if __name__ == "__main__":
    import pprint
    print("option")
    pprint.pprint(option())
    print("---------------^---------------")
    pprint.pprint(send(imgtobase.imgtobasefromfp("test4.png"),option=orcoption_jp_te))
    print("---------------^---------------")
    # l = send2()
    # p = l(
    #     "你好，我是顾咸国",
    #     "博士，如果过去的那些记忆，您还能回想起一些的话......我真的很高兴。嗯，我的小提琴还不够熟练，但是......既然这里只有您能听到，我想试着演奏一下。一首有些怀旧的曲子。",
    #     r"C:\Users\steve\Desktop\Π神\gal\data\amiya\1.wav")

    # print(p)
    # print("diffrentlaug")

    # l = send2()
    # p = l(
    #     "你好，我是顾咸国",
    #     "君は日常的に多くのオペレーターと接すると思うが、君の意志を左右する意図を孕む言葉には警戒してくれ。自我を保ち、必要とあらば私に相談するといい。もちろん、君には……私など必要ないと思うが。そうだろう？",
    #     r"C:\Users\steve\Desktop\Π神\gal\data\kaierxi\1.wav"
    # )   
    # print(p)