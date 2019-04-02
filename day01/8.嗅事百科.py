
# https://www.qiushibaike.com/text/page/3/

import re
import urllib.request

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

#获取前程无忧的接口

url = "https://www.qiushibaike.com/text/page/1/"


req = urllib.request.Request(url,headers=headers)

response = urllib.request.urlopen(req)

html = response.read().decode()
# print(html)


jobnum_re = '<div class="content">\n<span>(.*?)</span>'

items = re.findall(jobnum_re,html,re.S)
for i in items:
    print(i,"\n")

