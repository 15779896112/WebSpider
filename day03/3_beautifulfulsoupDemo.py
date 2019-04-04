from bs4 import BeautifulSoup

fp = open('index.html',encoding='utf-8')

soup = BeautifulSoup(fp.read(),'lxml')
# print(soup.prettify())
# print(soup.head.name)
# print(soup.title.attrs)

# 获取属性
# print(soup.a.attrs['href']) # 获取特定属性
# print(soup.a.attrs.get('href'))
# print(soup.a.get('href'))

# 获取文本
# string 只能获取一行字符
# print(soup.p.string) # None
# print(soup.p.span.string) # 文本二

# 获取节点内的内容
# print(soup.p.text) # 纯文本，不包括标签
# print(soup.p.get_text)

# 获取下一个兄弟节点，包括文本节点（换行，空白）
# print(soup.span.next_sibling)
# print(soup.span.next_sibling.next_sibling)

print(soup.b.previous_sibling)




