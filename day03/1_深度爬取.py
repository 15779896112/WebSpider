import requests
import re

headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

def get_content(url):
    try:
        res = requests.get(url,headers=headers)

        # print(res.text)
        return res.text
    except:
        return ""

# 获取子url列表
i = 0
def get_son_url(url):
    global i
    content = get_content(url)
    href_re = '<a.*?href="(.*?)".*?>'
    href_list = re.findall(href_re,content,re.S)
    # pic_img ='<img src="(.*?)".*?>'
    # imgs = re.findall(pic_img,content,re.S)
    pic_re = '"objURL":"(.*?)"'
    imgs = re.findall(pic_re, content, re.S)

    for item in imgs:
        try:
            if item.startswith('http'):
                req = requests.get(url=item, headers=headers)
                content = req.content
                name = 'img/' + str(i)  + ".jpg"
                i = i + 1
                with open(name, 'wb') as fp:
                    fp.write(content)
        except:
            break
    return href_list

def deep_crawer(url):

    if deep_dict[url]>2:
        return
    print("当前层级：",deep_dict[url])
    son_list = get_son_url(url)
    for sonurl in son_list:
        if sonurl.startswith('http'):
            if sonurl not in deep_dict:
                deep_dict[sonurl] =deep_dict[url] +1
                # print(sonurl)
                deep_crawer(sonurl)

if __name__ == "__main__":
    url ='https://www.baidu.com/s?ie=utf-8&wd=%E8%8B%8D%E4%BA%95%E7%A9%BA'
    deep_dict = {}
    deep_dict[url] = 1

    deep_crawer(url)


