import json
import operator
import urllib
import urllib.request
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
list1 = []
for i in range(1,20):
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(i*20) + "&limit=20"
    req = urllib.request.Request(url=url,headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode()
    datas = json.loads(data)

    # datas = sorted(datas, key=lambda x: x['rate'], reverse=True)
    with open("电影排行榜.txt",'a+',encoding="utf-8") as fp:
        for data in datas:
            title = data['title']
            rate = data['score']
            fp.write(title+':'+rate+'\n')
        fp.write("*"*50+'\n')
