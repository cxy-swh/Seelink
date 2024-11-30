# 数据加密
# Url = https://wx.qmpsee.com/articleDetail?id=feef62bfdac45a94b9cd89aed5c235be


import requests
import execjs
from pathlib import Path
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://wx.qmpsee.com',
    'Platform': 'web',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Source': 'see',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="130", "Google Chrome";v="130", "Not?A_Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = {
    'page': '1',
    'num': '20',
    'ca_uuid': 'feef62bfdac45a94b9cd89aed5c235be',
}

response = requests.post('https://wyiosapi.qmpsee.com/Web/getCaDetail', headers=headers, data=data).json()
encrypt_data = response['encrypt_data']

datas = execjs.compile(Path('1.js').read_text()).call('pp', encrypt_data)

for i in datas:
    news_title = i['news_title']
    news_source = i['news_source']
    content = i['content']
    create_time = i['create_time']
    print("---------------------------------------------------------------------------------------")
    print('%s\n%s\n%s\n%s\n' % (news_title,news_source,content,create_time))