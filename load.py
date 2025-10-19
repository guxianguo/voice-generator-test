"读取json.json"

from os import listdir
from os import path
import json

pathed = path.abspath(r".\data")
#print(pathed,"?")

class data:
    def __init__(self):
        print("load begin")
        self.p = dict()
        self.p_upload()
        self.data = self.end_upload()
        print("load down")

    def p_upload(self):
        """
            {'amiya': 'C:\\Users\\steve\\Desktop\\py\\gal\\voice\\data\\amiya'}
        """
        for name in listdir(pathed):
               #print(name)
                self.p.update({name:path.join(pathed,name)})
        #print(self.p)
        


    def update(self):
        """
        {'阿米娅': 'amiya'}
        """
        with open("json.json",encoding="utf8") as fp:
                p = fp.read()
                #print(p)
                return json.loads(p)

    def end_upload(self)->dict:
        """{'阿米娅': 'C:\\Users\\steve\\Desktop\\py\\gal\\voice\\data\\amiya'}"""
        l = dict()
        name = self.update()
        print(name)
        for a,b in name.items():
            try:
                l[a] = self.p[b]
            except:
                continue
        return l


da = data()

if __name__ == "__main__":
    print(da.data)
