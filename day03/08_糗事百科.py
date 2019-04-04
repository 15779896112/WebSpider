import re
import urllib.request
import requests
from bs4 import BeautifulSoup

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

def getData(url):
    req = requests.get(url,headers=headers)
    html = req.text
    soup = BeautifulSoup(html,'lxml')

    items = soup.select('#content-left > div .content')
    with open('笑话大全.txt','a+',encoding="utf-8") as fp:
        for i in items:
            con = i.span
            text_re = '\n(.*?)\n'
            cont = re.findall(text_re,con.text,re.S)
            fp.write(cont[1]+'\n'+'\n')

if __name__ == "__main__":

    for page in range(1, 3):
        url = "https://www.qiushibaike.com/text/page/" + str(page) + "/"
        getData(url)

