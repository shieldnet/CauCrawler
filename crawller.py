#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import telegram
import time

import sys
import unicodedata

# For Compare
cmp_data = {}
cmp_to = {}

# file name
data_cse = 'cse.txt'
data_ict = 'ict.txt'

#Telegram Information
my_token = '406303272:AAF4zhQXYz0pR-mD6kMZgQX-mKmOLp9vFQA'
bot =telegram.Bot(token = my_token)
updates = bot.getUpdates()
chat_id = bot.getUpdates()[-1].message.chat.id


# Caucse Notice
def caucseNotice(max_pages, fname):
    
    page = 1
    while page < max_pages:
        url = 'http://cse.cau.ac.kr/20141201/sub05/sub0501.php?offset=' \
              + str(page) + '&dir=bbs&nmode=list&code=oktomato_bbs05&search=&keyword=&temp1='
        
        get_information(url, 'cse', fname)
        page += 1

#ICT Notice
def ictNotice(max_pages, fname):
    
    page = 1
    while page < max_pages:
        url = 'http://ict.cau.ac.kr/20150610/sub05/sub05_01_list.php?cmd=list&cpage='+ str(page) \
              + '&idx=&search_gbn=1&search_keyword='
        
        get_information(url, 'ict', fname)
        page += 1



#get information from specified url
def get_information(url, site, file_name):
    source_code = requests.get(url)
    plain_text = source_code.content
    
    soup = BeautifulSoup(plain_text, 'html.parser')
    my_titles = soup.select(
        'td > a'
    )
    
    data = {}

    for title in my_titles:
        data[title.text] = title.get('href')
    
    for i in data:
        print(site + " > " + i.strip())
        
    save_information(file_name, site, data)


# save information to 'data.txt' in program excuted path
def save_information(file_name, site, data):
    fp = open(file_name, "w", encoding='UTF8')
    
    for s in data:
        fp.write(site + ' > ' + s.strip() + '\n')
     
    fp.close()
    print('save done')



# load information from 'data.txt' in program excuted path
def load_information(file_name, list_name):
    fp = open(file_name, "r", encoding='UTF8')
    
    while True:
        line = fp.readline()
        if not line: break
        
        list_name.append(str(line))
    
    fp.close()

def clear_information(file_name):
    fp = open(file_name, "w", encoding='UTF8')
    fp.close()

# compare crawl data from 'data.txt'
# If new thing is exist, send telegram alert
def compare_data(new, old):
    for st in new:
        if old.count(st) == 0:
            bot.sendMessage(chat_id=chat_id, text="안녕 마스터!! 새 공지가 올라왔어, 공지는 "
                                                  + st + " 인 모양이야!!" )
            print('diff')
        else:
            pass
        


###### main #####
cmp_old = []
cmp_new = []

#old
caucseNotice(2, data_cse)
ictNotice(2, data_ict)
load_information(data_cse, cmp_old)
load_information(data_ict, cmp_old)

while True:
    
    time.sleep(60)
    del cmp_old[1]
    #new
    caucseNotice(2, data_cse)
    ictNotice(2, data_ict)
    load_information(data_cse, cmp_new)
    load_information(data_ict, cmp_new)
    
    compare_data(cmp_new, cmp_old)
    
    cmp_old = list(cmp_new)
    del cmp_new[0:]
    
