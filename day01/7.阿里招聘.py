# pageSize: 10
# t: 0.38474336775699025
# keyWord:
# location: 深圳
# second:
# first:
# pageIndex: 1

import json
import re
import urllib
import urllib.request
import urllib.parse


headers = {
"User-Agent":"User-Agent, Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"
}
url = "https://job.alibaba.com/zhaopin/socialPositionList/doList.json"

for i in range(5):
    data = {
        'pageSize': 10,
        't': 0.38474336775699025,
        # 'keyWord':'',
        'location': '深圳',
        # 'second':'',
        'first':'综合类',
        'pageIndex': i

    }
    data = urllib.parse.urlencode(data).encode()
    req = urllib.request.Request(url,data=data,headers=headers)
    response = urllib.request.urlopen(req)
    content = response.read().decode()


    comments_list = json.loads(content)
    jobs = comments_list['returnValue']['datas']
    for job in jobs:
        # 名字、学历、部门、岗位要求、工作经验
        name = job['name']
        requirement = job['requirement']
        departmentName = job['departmentName']
        degree = job['degree']
        workExperience = job['workExperience']
        print(name,degree,departmentName,requirement,workExperience)
        with open('alibaba.txt','a+',encoding='utf-8') as fp:
            fp.write("岗位名称：{}\n".format(name))
            fp.write("学历要求：{}\n".format(degree))
            fp.write("部门：{}\n".format(departmentName))
            fp.write("岗位要求：{}\n".format(requirement))
            fp.write("工作经历：{}\n".format(workExperience))
            fp.write("*"*50+'\n')



