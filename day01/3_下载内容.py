import urllib
from urllib import request
import  urllib.parse

# url中只能出现数字字母下划线，中文需要转义
request.urlretrieve("http://www.baidu.com/",r'baidu.html')
strings='中文'
s = urllib.parse.quote(strings)
print(s)
