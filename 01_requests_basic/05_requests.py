#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 任务：爬取某城市KFC门店信息

# Method 0: 爬取某城市KFC门店信息(仅展示网站第一页门店信息)
# Reference: https://zhuanlan.zhihu.com/p/140768687

import requests
import json
city = input("please input the city: ")
url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}

data = {
    "cname": "",
    "pid": "",
    "keyword": city,
    "pageIndex": "1",
    "pageSize": "10",
}

# 因为这里是提交表单，所以采用post的方法，data是用来实现参数动态化，等同于get方法中的params参数的作用
response = requests.post(url=url, headers=headers, data=data)
get_text = response.json()
print(get_text,'\n')

for item in get_text['Table1']:
    store = item['storeName']
    address = item['addressDetail']
    print(store + ': ' + address)



# Method 1: 爬取某城市所有KFC门店信息
# Reference: https://zhuanlan.zhihu.com/p/140768687

import requests
import json

city = input("please input the city: ")
url='http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}

data = {
    "cname": "",
    "pid": "",
    "keyword": city,
    "pageIndex": '1',
    "pageSize": "10",
}

for page_num in range(1, 3):
    data["pageIndex"] = page_num

    #因为这里是提交表单，所以采用post的方法，data是用来实现参数动态化，等同于get方法中的params参数的作用
    response = requests.post(url=url, headers=headers, data=data)
    get_text = response.json()
    print(get_text, '\n')

    for item in get_text['Table1']:
        store = item['storeName']
        address = item['addressDetail']
        others = item['pro']
        print(store + ': ' + address + ', ' + others)



# Method 2: 爬取某城市所有KFC门店信息
# Reference: https://www.pythonf.cn/read/48386
import requests
import json

city = input("please input the city: ")

url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx"

params = {
    "op": "keyword"
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36"
}

data = {
    "cname": "",
    "pid": "",
    "keyword": city,
    "pageIndex": '1',
    "pageSize": "10",
}

store_datas = []
for i in range(1, 3):
    data["pageIndex"] = i
    response = requests.post(url, params=params, data=data, headers=headers)
    print(response.content)

    res = response.json()
    print(res)
    print("正在处理第%s页..." % i)

    for store in res["Table1"]:
        storeName = store["storeName"]
        address = store["addressDetail"]
        store_data = {"门店名称": storeName, "地址": address}
        print(store_data)
        store_datas.append(store_data)

fileName = city + 'kfc' + '.json'
f = open(fileName, "w", encoding="utf-8")
f.write(json.dumps(store_datas, ensure_ascii=False, indent=4) + "\n")
f.close()