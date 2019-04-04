import json

import requests
import urllib.parse


headers = {
    'Accept': '*/*',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Content-Length':'135',
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie':'BIDUPSID=841C51151DF3E4DB90F81C209BBDF034; PSTM=1509099787; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=841C51151DF3E4DB90F81C209BBDF034:SL=0:NR=10:FG=1; BDUSS=JUSDNlb2RDM2h6WTRkMHo0QXBZbmVpcWhKcGtrVHFZYXp6b0RiYWxsWWNXcWhiQVFBQUFBJCQAAAAAAAAAAAEAAADxVECTSG9sbGXN8s~IyfoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABzNgFsczYBbSU; MCITY=-340%3A; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; H_PS_PSSID=; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1553928939,1554123218,1554196112,1554198196; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1554199279; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22vie%22%2C%22text%22%3A%22%u8D8A%u5357%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; delPer=0; PSINO=7; locale=zh',
    'Host': 'fanyi.baidu.com',
    'Origin':'https://fanyi.baidu.com',
    'Referer':'https://fanyi.baidu.com/translate?aldtype=16047&query=&keyfrom=baidu&smartresult=dict&lang=auto2zh',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
}

data = {
    'from':'zh',
    'to':'en',
    'query':'自由',
    'transtype':'translang',
    'simple_means_flag':3,
    'sign': '384913.81056',
    'token':'86634bb16e20a09e4fa29f68ae490d53'
}


url = 'https://fanyi.baidu.com/transapi'
response = requests.post(url,data=data,headers=headers)
response.encoding = 'utf-8'
res = response.text
res = json.loads(res)
print(res['data'][0]['src']+':'+res['data'][0]['dst'])

