import urllib
from urllib import request
import  urllib.parse

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
kw = input('请输入内容：')
params ={
    'wd':kw
}
params = urllib.parse.urlencode(params)

url = "http://www.baidu.com/"+params
req = urllib.request.Request(url,data=None,headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))