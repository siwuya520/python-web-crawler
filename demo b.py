# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = 'http://www.biquge.cm/6/6217/3638117.html'
    req = requests.get(url=target)
    req.encoding='gbk'
    # 我们可以在调用response.text()之前使用response.encoding=‘编码格式’
    print(req.text)