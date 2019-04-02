import urllib
import random
import urllib.request
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
proxy_list = [
    {"http" : "112.87.70.41:9999"},
    {"http": "112.87.70.41:9999"},
    {"http": "112.87.70.41:9999"},
    {"http": "112.87.70.41:9999"},
    {"http": "112.87.70.41:9999"}
]

# 随机选择一个代理
proxy = random.choice(proxy_list)
# 使用选择的代理构建代理处理器对象
httpproxy_handler = urllib.request.ProxyHandler(proxy)


opener = urllib.request.build_opener(httpproxy_handler)
url = "http://www.qfedu.com/"
request = urllib.request.Request(url,headers=headers)
response = opener.open(request)
print(response.read())