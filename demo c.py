# -*- coding:UTF-8 -*-
import requests

if __name__ == '__main__':
    target = 'http://www.biquge.cm/6/6217/3638117.html'
    req = requests.get(url=target)
    html=req.content
    # 使用req.content返回的是bytes型的数据
    html_doc=str(html,'gbk')
    # 然后将bytes型数据转化为str数据
    print(html_doc)
#获取文章内容