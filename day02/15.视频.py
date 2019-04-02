# https://vodkgeyttp8.vod.126.net/cloudmusic/36f8/core/8554/1b416b42d113142c0b2b9461a18b1871.mp4?wsSecret=b5c942c2d0bcdc3276337dcf2724e877&wsTime=1554212161
import requests
url = "https://vodkgeyttp8.vod.126.net/cloudmusic/36f8/core/8554/1b416b42d113142c0b2b9461a18b1871.mp4?wsSecret=b5c942c2d0bcdc3276337dcf2724e877&wsTime=1554212161"
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
response = requests.get(url,headers=headers)
con = response.content
with open('my.mp4','wb') as fp:
    fp.write(con)