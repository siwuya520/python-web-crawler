# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     target = 'http://www.biquge.cm/6/6217/3638117.html'
     req = requests.get(url = target)
     html = req.content
     html_doc = str(html, 'gbk')
     bf = BeautifulSoup(html_doc)
     texts = bf.find_all('div', id="content")
     print(texts)