#有道翻译
import urllib.request as r
import urllib.parse as p
import json
import time

def process(url,data):
    #使用urlencode方法转换标准格式
    data = p.urlencode(data).encode('utf-8')
    #先定义header则需要在()中加入',head',后定义不用
    req = r.Request(url,data)   
        #后定义header则需要用到add_header函数
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
                    (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    #传递Request对象和转换完格式的数据
    response = r.urlopen(req,data)
    #读取信息并解码(\uxxxx为unicode模式)
    html = response.read().decode('utf-8')
    #使用JSON
    target =json.loads(html)
    return target
    
def Jinshan(onlyone=1,content=None):
    url = 'http://fy.iciba.com/ajax.php?a=fy'
    ##head = {}
    ##head['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
    ##                    (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

    data = {}
    data['f']= 'auto'
    data['t']= 'auto'

    while onlyone==1:
        data['w'] = input('请输入要翻译的内容(输入"q!"结束)：')
        if data['w'] == 'q!':
            break
                
        target = process(url,data)
        if 'out' in target['content']:
            print("金山翻译结果：%s" % (target['content']['out']))
        else:
            print("金山翻译结果：%s" % (target['content']['word_mean']))
        time.sleep(3)   #系统休息3秒钟
Jinshan()
