# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
     server = 'http://www.biquge.cm/'
     target =  'http://www.biquge.cm/6/6217/'
     req = requests.get(url = target)
     html = req.content
     html_doc=str(html,'gbk')
     div_bf = BeautifulSoup(html_doc)
     div = div_bf.find_all('div', id='list'  )
     a_bf = BeautifulSoup(str(div[0]))
     a = a_bf.find_all('a')
     for each in a:
          print(each.string, server + each.get('href'))