import json
import operator
import urllib
import urllib.request
headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

for i in range(2):
    url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags=&start='+str(i)

    req = urllib.request.Request(url,headers=headers)
    response = urllib.request.urlopen(req)
    data = response.read().decode()
    data = json.loads(data)
    datas = data['data']
    datas = sorted(datas, key=lambda x: x['rate'], reverse=True)
    for data in datas:
        casts= data['casts']
        title = data['title']
        rate = data['rate']
        print(title,':',casts,rate)




