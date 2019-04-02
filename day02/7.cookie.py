import requests


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url = "http://www.baidu.com/"
response = requests.get(url=url,headers=headers)
# print(response.cookies)
# 将cookie对象转化成字典
cookies = requests.utils.dict_from_cookiejar(response.cookies)
print(cookies)