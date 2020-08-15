from urllib import request
if __name__=='__main__':
    reponse=request.urlopen("https://fanyi.baidu.com/")
    html=reponse.read()
    html=html.decode('utf-8')
    print(html)