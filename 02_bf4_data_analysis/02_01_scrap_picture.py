#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
if __name__ == "__main__":
    #如何爬取图片数据
    url = "https://pic.qiushibaike.com/system/pictures/12336/123366678/medium/3N9TOTAK5VKXX9GD.jpg"
    #content返回的是二进制形式的图片数据
    #text(字符串)  content(二进制)  json() (对象)
    img_data = requests.get(url=url).content

    with open('./qiutu1.jpg','wb') as fp:
        fp.write(img_data)