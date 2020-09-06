# Mission: get the data of first sogou webpage
# 爬取搜狗首页的页面数据

import requests

if __name__ == "__main__":
    # step 1: assign url
    url = 'https://www.sogou.com/'

    # step 2: launch request, we can get the responding object based on "get()" method
    response = requests.get(url=url)
    print(response.url)
    print(response.content)

    # step 3: get the responding data in the webpage with string format
    page_text = response.text
    print(page_text)

    # step 4: save the data we get
    with open('./sogou.html', 'w', encoding='utf-8') as fp:
        fp.write(page_text)

    print('We are done!')