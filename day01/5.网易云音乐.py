import datetime
import json
import re
import time
import urllib
import urllib.request
import urllib.parse


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url = "https://music.163.com/weapi/v1/resource/comments/R_SO_4_1353443885?csrf_token="
data = {
'params': 'ddBVgnPDbKpVBZJJR6LC2Ncqb8e2NdNTMQmEgvg0AgiNKsxQ0+47UVmkUx9xWrXPzwOO8WSm9WYygqxKnz09RVkrs2GcDWzCBcieX/WHjIFGSvl2CeAeUUjA0ybyYnBKda1roaExnxcRIcvnFbht3XfDkyZLdsTtx+Os+RdGxgcU7KBILPRSiV/YrXdGSI5YIqkL6381kYTA+krqM1XSx9dmLINyMXVjs4yys+j2X48=',
'encSecKey': '8cc2fdfb94efa909e9c264850d2f51f61c9921a14125a43e190731e4b18424bce79982fba719a0449df77eb1223ede70b9fd7a35d4823e9d8b044d5e5ac8649ea73dff9db4d301afd858a67dd4030efb658f60cf4ad8f45d62dbe51f807fde2b343b5b3c0d005f738a1bfc233c73ce0e95a2d25bf1c730f66feb1a6fdaf8513a'
}
data = urllib.parse.urlencode(data).encode()
req = urllib.request.Request(url,data=data,headers=headers)
response = urllib.request.urlopen(req)
content = response.read().decode()

content = json.loads(content)

hotComments = content['hotComments']
# print(hotComments)
for hotComment in hotComments:
    username = hotComment['user']['nickname']
    timer = hotComment['time']
    content = hotComment['content']

    print(username,content)



