#!/usr/bin/env python
# -*- coding:utf-8 -*-

import  requests
import json
if __name__ == "__main__":

    id_list = []  # 存储企业的id
    all_data_list = []  # 存储所有的企业详情数据

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'

    }

    #批量获取不同企业的id值
    url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    for page in range(1,6):
        page = str(page)
        data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':'',
        }
        json_ids = requests.post(url=url, headers=headers, data=data).json()
        for dic in json_ids['list']:
            id_list.append(dic['ID'])

    #获取企业详情数据
    post_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_list:
        data = {
            'id':id
        }
        detail_json = requests.post(url=post_url, headers=headers, data=data).json()
        all_data_list.append(detail_json)

    #持久化存储all_data_list
    fp = open('./allData.json', 'w', encoding='utf-8')
    json.dump(all_data_list, fp=fp, ensure_ascii=False)
    print('Done!!!')