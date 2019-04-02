import requests

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
params = {
    'wd':"岛国"
}
response = requests.get('http://www.baidu.com/s',params=params,headers=headers)
# print(response.text)
print(response.content.decode())