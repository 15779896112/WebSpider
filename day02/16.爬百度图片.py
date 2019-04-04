#
import json
import re

import requests
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=苍井空"
req = requests.get(url=url,headers=headers)
response = req.text
# print(response)
pic_re = '"objURL":"(.*?)"'
items = re.findall(pic_re,response,re.S)
i = 0
for item in items:
    req = requests.get(url=item, headers=headers)
    content = req.content
    name = 'img/' + str(i)+"苍老师" + ".jpg"
    i = i+1
    with open(name, 'wb') as fp:

        fp.write(content)