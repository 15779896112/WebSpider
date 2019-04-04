import re

import pymysql as pymysql
import requests
from bs4 import BeautifulSoup

# 1.链接数据库                                   )
conn = pymysql.Connect(host='localhost',
                       user='root',
                       password='123456',
                       database='python1812',
                       port=3306,
                       charset='utf8')

# 2.创建游标
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)



headers = {
    "User-Agent": "User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}

def get_NextUrl(url):

    req = requests.get(url,headers=headers)
    soup = BeautifulSoup(req.text,'lxml')
    next_url = soup.findAll("a",id='next')
    return next_url[0].get('href',0)


def qq_hr(url):

    req = requests.get(url,headers=headers)
    data = req.text
    soup = BeautifulSoup(data,'lxml')

    data = soup.find_all('table',class_="tablelist")
    print("*"*50)
    for line in  data[0].find_all('tr',class_=["even","odd"]):
        line = line.prettify()
        # print(line)
        item_re = '<td.*?>(.*?)</td>'
        data = re.findall(item_re,line,re.S)
        name_re = '<a.*?>(.*?)</a>'
        name = re.findall(name_re,data[0],re.S)
        name = name[0].strip()
        typer = data[1].strip()
        num =data[2].strip()
        addr = data[3].strip()
        sql = "insert into jobs values('{}','{}','{}','{}')".format(name, typer, num,addr)
        try:
            # pymysql自动开启事务，关闭了自动提交功能
            rows = cursor.execute(sql)
            if rows > 0:  # 插入成功
                conn.commit()  # 提交
            else:
                conn.rollback()  # 回滚

        except Exception as e:
            pass




if __name__ == "__main__":
    url = "https://hr.tencent.com/position.php?keywords=python"
    for i in range(10):
        url = get_NextUrl(url)
        url = "https://hr.tencent.com/"+url
        qq_hr(url)