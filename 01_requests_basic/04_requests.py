#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 任务：爬取豆瓣电影喜剧排行榜

import requests
import json
if __name__ == "__main__":
    url = 'https://movie.douban.com/j/chart/top_list'

    param = {
        'type': '24',
        'interval_id': '100:90',
        'action':'',
        'start': '0',  # 从库中的第几部电影去取
        'limit': '20', # 一次取出的个数
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

    response = requests.get(url=url, params=param, headers=headers)

    list_data = response.json()
    print(list_data)

    fp = open('./douban.json', 'w', encoding='utf-8')
    json.dump(list_data, fp=fp, ensure_ascii=False)
    print('Done!!!')