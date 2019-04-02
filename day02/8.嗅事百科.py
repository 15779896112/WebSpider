
# https://www.qiushibaike.com/text/page/3/

import re
import urllib.request
import requests

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

for page in range(10):

    url = "https://www.qiushibaike.com/text/page/"+str(page)+"/"
    req = requests.get(url,headers=headers)
    html = req.text
    jobnum_re = '<div class="content">\n<span>(.*?)</span>'
    items = re.findall(jobnum_re,html,re.S)
    with open('笑话大全.txt','a+',encoding="utf-8") as fp:
        for i in items:
            fp.write(i)

