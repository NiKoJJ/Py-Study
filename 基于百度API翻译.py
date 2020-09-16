# urllib 库的使用
# from urllib import request

# part 1
# from urllib import request
# if __name__ == '__main__':
#     '''
#     urllib使用request.urlopen()打开和读取URL信息，返回的对象Response如同一个文本对象，可以通过调用read()进行读取，
#     在通过print（）将读取的信息打印出来
#
#     查看网页的编码方式，查看网页源代码找到head标签开始位置的chareset,可以看到网页的编码方式
#     '''
#     reponse = request.urlopen("https://fanyi.baidu.com/")  # 请求过程
#     '''
#     req=request.Request("https://fanyi.baidu.com/")
#     reponse=request.urlopen(req)
#     '''
#     html = reponse.read()
#     html = html.decode('utf-8')  # decode()对网页信息进行解码
#     print(html)


# part 2
# from urllib import request
# rep=request.Request("https://fanyi.baidu.com")
# reponse=request.urlopen(rep)
# data=reponse.read
# print('status:',reponse.status,reponse.reason)
# print("************************************\n")
# for k,v in reponse.getheaders():
#     print('%s:%s' % (k,v))


# part 3
# from urllib import request
# 使用Reponse 对象的geturl()方法、info()方法、getcode()方法获取相关的URL、相应信息和响应HTTP状态码
# if __name__=="__main__":
#     req=request.Request("https://fanyi.baidu.com")
#     reponse=request.urlopen(req)
#     print('(1)URL信息：%s'%(reponse.geturl()))
#     print('**************************************')
#     print('(2)info 信息：%s'%(reponse.info()))
#     print('**************************************')
#     print('(3)getcode 信息：%s'%(reponse.getcode()))

# part 4
# from urllib import request
# 使用user Agent 隐藏身份 （两种方法）
# if __name__=="__main__":
#     url = 'https://fanyi,baidu.com'
#     req = request.Request(url)  # 创建Request对象
# 
#     req.add_header('User-Agent','Mozilla/5.0 (Linux;Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Geoko) Chrome')
# 
#     response = request.urlopen(req)
#     html = response.read().decode('utf-8')  # 读取响应信息并解码
#     print(html)


# 最终实现
from tkinter import *
from urllib import request
from urllib import parse
import json
import hashlib


def translate_Word(en_str):
    URL = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
    '''
    en_str=input('请输入要翻译的内容‘）
    创建Form Data 字典，存储向服务器发送的data
    Form Data={'from':'en','to':'zh','q':en_str,'appid':'20200916000566773','salt':'1435660288'}
    '''
    Form_Data = {}
    Form_Data['from'] = 'auto'   # 目标语言
    Form_Data['to'] = 'zh'
    Form_Data['q'] = en_str  # 要翻译的数据
    Form_Data['appid'] = '20200916000566773'
    Form_Data['salt'] = '1435660288'
    Key = '1GpjCgJXXFOOJ4VaF0Co'
    m = Form_Data['appid'] + en_str + Form_Data['salt'] + Key
    m_MD5 = hashlib.md5(m.encode('utf-8'))
    Form_Data['sign'] = m_MD5.hexdigest()
    data = parse.urlencode(Form_Data).encode('utf-8')  # 使用urlencode（）方法转换为标准格式
    reponse = request.urlopen(URL, data)  # 传递Request 对象和转换完格式的数据
    html = reponse.read().decode('utf-8')
    translate_result = json.loads(html)  # 使用json
    print(translate_result)
    translate_result = translate_result['trans_result'][0]['dst']  # 找到翻译结果
    print('翻译结果是：%s' % translate_result)
    return translate_result


def leftClick(event):
    en_str = Entry1.get()
    print(en_str)
    vText = translate_Word(en_str)
    Entry2.config(Entry2, text=vText)
    s.set(" ")
    Entry2.insert(0, vText)


def leftClick2(event):
    s.set("")
    Entry2.insert(0, " ")


if __name__ == "__main__":
    root = Tk()
    root.title('单词翻译器')
    root.geometry('500x300')
    Label(root, text='键入翻译内容：', width=19).place(x=1, y=1)  # 绝对坐标（1,1）
    Entry1 = Entry(root, width=50)
    Entry1.place(x=110, y=1)
    Label(root, text='翻译结果(中文)：', width=18).place(x=1, y=20)
    s = StringVar()
    s.set('Hello，this is a test')
    Entry2 = Entry(root, width=50, textvariable=s)
    Entry2.place(x=110, y=20)
    Button1 = Button(root, text='翻译', width=8)
    Button1.place(x=110, y=80)
    Button2 = Button(root, text='清空', width=8)
    Button2.place(x=220, y=80)
    Button1.bind("<Button-1>", leftClick)
    Button2.bind("<Button-1>", leftClick2)
    root.mainloop()
