import requests

headers = {
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
'Accept-Encoding': 'gzip, deflate, br',
'Accept-Language': 'zh-CN,zh;q=0.9',
'Connection':'keep-alive',
'Cookie': '_ga=GA1.2.1589746288.1534253638; pgv_pvi=103292928; pt2gguin=o1642899961; pgv_pvid=7131224145; _gcl_au=1.1.1498555995.1550462008; PHPSESSID=b6fo1g44cvhhvmuag0rcns9h35; pgv_si=s4369615872',
'Host':'hr.tencent.com',
'Referer':'https://hr.tencent.com/position.php?keywords=&tid=87&lid=2218',
'Upgrade-Insecure-Requests': '1',
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

url = "https://hr.tencent.com/position.php"
params = {
    'keywords':'',
    'tid':87,
    'lid':2218,
}
response = requests.get(url=url,params=params,headers=headers)
content = response.text
# job_re = ""
print(content)
