#-*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import telegram
import time
import telepot

import copy
import sys
import unicodedata

# For Compare
cmp_data = {}
cmp_to = {}

ict_num_of_title = []
cse_num_of_title = []


# file name
data_cse = 'cse.txt'
data_ict = 'ict.txt'
data_chat_id = 'chat_id.txt'

#Telegram Information
my_token = '406303272:AAF4zhQXYz0pR-mD6kMZgQX-mKmOLp9vFQA'


#Webhook Delete
bot = telepot.Bot(my_token)
bot.deleteWebhook()


bot =telegram.Bot(token = my_token)
updates = bot.getUpdates()
chat_id = []

def cse_url_ret(idx):
   retstr = '[컴퓨터공학부링크]('
   retstr += 'http://cse.cau.ac.kr/20141201/sub05/sub0501.php)'
   print("CSE")
   return retstr


def ict_url_ret(idx):
    retstr = '[창의ICT링크]('
    retstr += 'http://ict.cau.ac.kr/20150610/sub05/sub05_01_list.php)'
    
    return retstr

# load information from 'data.txt' in program excuted path
def load_chat_id():
    fp = open(data_chat_id, "r", encoding='UTF8')
    
    while True:
        line = fp.readline()
    
        if not line: break
        if '#' in line:
            pass
        else:
            if('\n' in line):
                chat_id.append(str(line[:-1]))
            else:
                chat_id.append(str(line))
    
    fp.close()

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


def ict_geturl(max_pages):
    page = 1
    tmp_title_nums = []
    while page < max_pages:
        page +=1
        
        url = 'http://ict.cau.ac.kr/20150610/sub05/sub05_01_list.php?cmd=list&cpage='+ str(page) \
              + '&idx=&search_gbn=1&search_keyword='
        source_code = requests.get(url)
        plain_text = source_code.content
    
        soup = BeautifulSoup(plain_text, 'html.parser')
        
        my_titles = soup.select(
            'td > a'
        )
    
        data = {}
    
        for title in my_titles:
            tmp_title_nums.append(str(title)[28:31])
            
            data[title.text] = title.get('href')
            
        #중복원소 삭제
        

        global ict_num_of_title
        ict_num_of_title = copy.deepcopy(tmp_title_nums)


def cse_geturl(max_pages):
    page = 1
    while page < max_pages:
        page += 1

        url = 'http://cse.cau.ac.kr/20141201/sub05/sub0501.php?offset=' \
              + str(page) + '&dir=bbs&nmode=list&code=oktomato_bbs05&search=&keyword=&temp1='
        source_code = requests.get(url)
        plain_text = source_code.content
    
        soup = BeautifulSoup(plain_text, 'html.parser')
        
        my_titles = soup.select(
            'td > a'
        )
        

        data = {}
        tmp_title_nums = []
        
            
        print('debug')
    
        for title in my_titles:
            tmp_title_nums.append(str(title)[65:68])
            data[title.text] = title.get('href')
       
        global cse_num_of_title
        cse_num_of_title = list(tmp_title_nums)
        


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
    print(site + ' save done...')


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
    idx = 0
    for st in new:
        if old.count(st) == 0:
            str = "안녕 마스터!! 새 공지가 올라왔어, 공지는 " \
                  + st + " 인 모양이야!!\n"
            if st.find('ict') != -1:
                str += ict_url_ret(idx)
            else:
                str += cse_url_ret(idx)
                
                
            for ids in chat_id:
                bot.sendMessage(chat_id=ids, text=str, parse_mode='Markdown')
                print('diff')
            
            idx+=1
        else:
            idx+=1
            pass
        
    
        


###### main #####




load_chat_id()

cmp_old = []
cmp_new = []

#old
print(chat_id)
load_information(data_cse, cmp_old)
load_information(data_ict, cmp_old)

while True:
    print('Sleep 60 seconds...')
    time.sleep(1)
    
    #ict get writing num
    ict_geturl(2)
    #cse get writing num
    cse_geturl(2)
    # new
    caucseNotice(2, data_cse)
    print (cse_num_of_title)
    ictNotice(2, data_ict)
    print (ict_num_of_title)
    load_information(data_cse, cmp_new)
    load_information(data_ict, cmp_new)
    
    #ict는 idx에 x2해서 url 출력할 것
    compare_data(cmp_new, cmp_old)
    
    cmp_old = list(cmp_new)
    del cmp_new[0:]
