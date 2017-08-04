#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import sys
import unicodedata

def spider(max_pages):
    
    page = 1
    while page < max_pages:
        print(' Now ' + str(page) + '<<<<' )
        
        url = 'http://cse.cau.ac.kr/20141201/sub05/sub0501.php?offset=' + str(page) + '&dir=bbs&nmode=list&code=oktomato_bbs05&search=&keyword=&temp1='
        source_code = requests.get(url)
        plain_text = source_code.content
        
        soup = BeautifulSoup(plain_text, 'html.parser')
        my_titles = soup.select(
            'td > a'
        )
        
        my_nums = soup.select(
            'tr > td'
        )
        
        for nums in my_nums:
            print(nums)
        
        page += 1
        
        data = {}

        for title in my_titles:
            data[title.text] = title.get('href')
            
        for i in data:
            print (i)

spider(2)
