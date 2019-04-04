import requests
from bs4 import BeautifulSoup
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url = "https://music.163.com/#/playlist?id=2735889770"

req = requests.get(url,headers=headers)
print(req.text)

