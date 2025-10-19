"函数装饰器的批处理"

trans = []

def add_trans(func):
    """将deal开头的函数加入trans，装饰器，双重保障"""
    if(func.__name__.startswith("deal")):    
        trans.append(func)
    else:
        raise NameError
    
    def transs(arg):
        func(arg)

    return transs

def deal(data):
    b = data
    for i in trans:
        b = i(b)
    return b


def searchct(text,data:dict):
    """返回文本中第一个在data中的名字"""
    ct = ("",200)
    #print(text)
    for i in data.keys():
        index = text["data"].find(i)
        if index>=0 and index < ct[1]:
            ct = (i,index)
    if ct[1] >= 0 and ct[1]<200:
        return ct[0]
    else:
        print("未识别，启用male")
        return "male"


#exmaple
@add_trans
def deal_point(unstr):
    re = unstr
    dic = {"·":"。","":""}
    for a,b in dic.items():
        re = re.replace(a,b)
    return re