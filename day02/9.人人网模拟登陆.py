import http.cookiejar
import urllib.request

# 创建 cookiejar对象
cookie = http.cookiejar.CookieJar()

handle =urllib.request.HTTPCookieProcessor(cookie)

opener =urllib.request.build_opener(handle)

post_url = "https://passport.weibo.cn/signin/login"