import json
import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36"
}


def getData(url):

    req = requests.get(url,headers=headers)

    content = req.text

    movie_list = json.loads(content)
    # print(movie_list)

    # # 遍历每个电影，并存储图片
    for movie in movie_list:
        cover_url = movie.get('cover_url')  # 图片url
        title = movie.get('title')  # 电影名
        print(title)


if __name__ == "__main__":

    for i in range(1, 3):
        url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=" + str(
        i * 20) + "&limit=20"

        getData(url)











