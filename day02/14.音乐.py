# http://m10.music.126.net/20190402214701/c22e807825934438b800cf537d63cbc0/ymusic/050f/520e/5508/2e4f56c916ed06c205b5bbf67c2b395f.mp3

import requests
url = "http://m10.music.126.net/20190402214701/c22e807825934438b800cf537d63cbc0/ymusic/050f/520e/5508/2e4f56c916ed06c205b5bbf67c2b395f.mp3"
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
response = requests.get(url,headers=headers)
con = response.content
with open('my.mp3','wb') as fp:
    fp.write(con)