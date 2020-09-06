# -*- coding:utf-8 -*-
# 任务：简易网页采集器


# UA: User-Agent (请求载体的身份标识)
# UA检测：门户网站的服务器会检测对应请求载体的身份标识，
#   - 若身份标识为某一款浏览器，则说明该请求是一个正常的请求。
#   - 若身份标识不是某一款浏览器，则说明该请求不是一个正常的请求（爬虫），可能请求会失败。
# 故而，我们的爬虫程序为了请求成功，要进行UA伪装，伪装成某一款浏览器的请求。


import requests

if __name__ == "__main__":
    # step 0: UA camouflage, set UA is a fake request by some browsers
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
    }

    # step 1: assign url
    # url = 'https://www.sogou.com/search?q=kobe'
    url = 'https://www.google.com/search'

    # 处理url携带的参数：因为参数是动态的，故封装到字典中
    kw = input('please enter a word:')
    param = {
        'q' : kw
    }

    # step 2: launch request, we can get the responding object based on "get()" method
    response = requests.get(url=url, params=param, headers=headers)

    # step 3: get the responding data in the webpage with string format
    page_text = response.text

    # step 4: save the data we get
    fileName = kw + '.html'
    with open(fileName, 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print(fileName, 'was saved successfully!')