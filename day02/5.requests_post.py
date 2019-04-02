# i: 哈喽
# from: AUTO
# to: AUTO
# smartresult: dict
# client: fanyideskweb
# salt: 15541932285349
# sign: 3fce6fb4d99212fa9a86700dabacea2f
# ts: 1554193228534
# bv: 470df6afd582fe67e18c2221dab59fb3
# doctype: json
# version: 2.1
# keyfrom: fanyi.web
# action: FY_BY_CLICKBUTTION
# typoResult: false

# http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule

import requests
import  urllib.parse
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
data = {
    'i': '艹尼玛',
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': 15541932285349,
    'sign': '3fce6fb4d99212fa9a86700dabacea2f',
    'ts':1554193228534,
    'bv': '470df6afd582fe67e18c2221dab59fb3',
    'doctype':'json',
    'version':2.1,
    'keyfrom':'fanyi.web',
    'action':'FY_BY_CLICKBUTTION',
    'typoResult':'false',
}
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
response = requests.post(url,data=data,headers=headers)
response=response.content.decode()
# response=response.json()
print(response)