# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = 'http://www.biquge.cm/6/6217/3638117.html'
    req = requests.get(url=target)
    print(req.text)
#获取文章内容但有乱码