#!/usr/bin/env python
# -*- coding:utf-8 -*-


from bs4 import BeautifulSoup


if __name__ == "__main__":
    #将本地的html文档中的数据加载到该对象中
    fp = open('./test.html', 'r', encoding='utf-8')
    soup = BeautifulSoup(fp, features='html5lib')
    # print(soup)
    # print(soup.a)                                  # soup.tagName返回： html中第一次出现的tagName标签
    # print(soup.div)                                # soup.tagName返回： html中第一次出现的tagName标签

    # print(soup.find('div'))                        # find('tagName'): 等同于soup.div
    # print(soup.find('div', class_='song'))         # class_用于属性定位，注意class后面的下划线
    # print(soup.find('div', class_='song').text)    # .text用于返回：div下，song级别下的所有文本
    # print(soup.find('div', class_='song').string)  # .text用于返回：div下，song级别下的所有文本
    # print(soup.find_all('a'))                      # 返回：html中所有出现的tagName标签，以列表形式返回


    # print(soup.select('.tang'))                       # select('选择对象')
    # print(soup.select('.tang > ul > li > a'))         # >: 表示一个层级
    # print(soup.select('.tang > ul > li > a')[0])      # >: 表示一个层级
    # print(soup.select('.tang > ul a')[0]['href'])     # 空格: 表示多个层级, 获得href
    # print(soup.select('.tang > ul a')[0]['title'])    # 空格: 表示多个层级, 获得title
    # print(soup.select('.tang > ul a')[0].text)        # 空格: 表示多个层级, 获得标签下所有的文本内容
    # print(soup.select('.tang > ul a')[0].get_text())  # 空格: 表示多个层级, 获得标签下所有的文本内容
    # print(soup.select('.tang > ul a')[0].string)      # 空格: 表示多个层级, 获得标签下直系的文本内容


    # count = len(soup.select('.tang > ul a'))
    # print(count)
    # for i in range(count):
    #     print(soup.select('.tang > ul a')[i]['href'], soup.select('.tang > ul a')[i].text)  # 空格: 表示多个层级