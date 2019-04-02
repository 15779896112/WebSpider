import json

import requests
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
list1 = []
for i in range(1,5):
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(i*20) + "&limit=20"
    req = requests.get(url=url,headers=headers)
    response = req.text

    datas = json.loads(response)
    for data in datas:
        pic = data['cover_url']
        req = requests.get(url=pic,headers=headers)
        content = req.content
        name = 'img/' + data['title'] + ".jpg"
        with open(name, 'wb') as fp:
            fp.write(content)

