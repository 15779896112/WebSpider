from http import  cookiejar
import  urllib.request

# 第一步 创建cookiejar对象
cookies = cookiejar.CookieJar()
#
cookie_handler = urllib.request.HTTPCookieProcessor(cookies)

# http = urllib.request.HTTPHandler()
opener = urllib.request.build_opener(cookie_handler)
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url = "http://www.baidu.com/"
req = urllib.request.Request(url,headers=headers)
response = opener.open(req)
# print(response.read().decode())
for cookie in cookies:
    print(cookie.name,cookie.value)

