#-*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import log_func
import requests

import datetime

FUNCTION_STR = '[CRAWLER] '

# Where is chromedriver
path_chromedriver = "D:\\University\\dev\\chromedriver.exe"
path_panthomjs = "/usr/lib/phantomjs/phantomjs"

#Page URL
cse_notice_url = 'http://cse.cau.ac.kr/sub05/sub0501.php'
ict_notice_url = 'http://ict.cau.ac.kr/20150610/sub05/sub05_01_list.php'
cau_notice_url = 'https://www.cau.ac.kr/04_ulife/causquare/notice/notice_list.php?bbsId=cau_notice&category1=%C7%D0%BB%E7'
#dormitory_notice_url = 'https://dormitory.cau.ac.kr/bbs/bbs_list.php?bbsID=notice&bbsID=notice'

#HTML Selector
cse_selector = ['#listpage_form > table > tbody > tr:nth-child(1) > td.aleft > a',
'#listpage_form > table > tbody > tr:nth-child(2) > td.aleft > a',
'#listpage_form > table > tbody > tr:nth-child(3) > td.aleft > a',
'#listpage_form > table > tbody > tr:nth-child(4) > td.aleft > a',
'#listpage_form > table > tbody > tr:nth-child(5) > td.aleft > a',
'#listpage_form > table > tbody > tr:nth-child(6) > td.aleft > a',
'#listpage_form > table > tbody > tr:nth-child(7) > td.aleft > a',
'#listpage_form > table > tbody > tr:nth-child(8) > td.aleft > a',
'#listpage_form > table > tbody > tr:nth-child(9) > td.aleft > a',
'#listpage_form > table > tbody > tr:nth-child(10) > td.aleft > a',
]

#Time Selector
cse_time_selector = ['#listpage_form > table > tbody > tr:nth-child(1) > td:nth-child(5)',
'#listpage_form > table > tbody > tr:nth-child(2) > td:nth-child(5)',
'#listpage_form > table > tbody > tr:nth-child(3) > td:nth-child(5)',
'#listpage_form > table > tbody > tr:nth-child(4) > td:nth-child(5)',
'#listpage_form > table > tbody > tr:nth-child(5) > td:nth-child(5)',
'#listpage_form > table > tbody > tr:nth-child(6) > td:nth-child(5)',
'#listpage_form > table > tbody > tr:nth-child(7) > td:nth-child(5)',
'#listpage_form > table > tbody > tr:nth-child(8) > td:nth-child(5)',
'#listpage_form > table > tbody > tr:nth-child(9) > td:nth-child(5)',
'#listpage_form > table > tbody > tr:nth-child(10) > td:nth-child(5)',
]

ict_time_selector = ['body > div > div.content > div > table > tbody > tr:nth-child(1) > td:nth-child(3)',
'body > div > div.content > div > table > tbody > tr:nth-child(2) > td:nth-child(3)',
'body > div > div.content > div > table > tbody > tr:nth-child(3) > td:nth-child(3)',
'body > div > div.content > div > table > tbody > tr:nth-child(4) > td:nth-child(3)',
'body > div > div.content > div > table > tbody > tr:nth-child(5) > td:nth-child(3)',
'body > div > div.content > div > table > tbody > tr:nth-child(6) > td:nth-child(3)',
'body > div > div.content > div > table > tbody > tr:nth-child(7) > td:nth-child(3)',
'body > div > div.content > div > table > tbody > tr:nth-child(8) > td:nth-child(3)',
'body > div > div.content > div > table > tbody > tr:nth-child(9) > td:nth-child(3)',
'body > div > div.content > div > table > tbody > tr:nth-child(10) > td:nth-child(3)',
]
'''
dormitory_selector = [
'#content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(2) > span > a',
'#content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(4) > span > a',
'#content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(6) > span > a',
'#content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(8) > span > a',
'#content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(10) > span > a',
'#content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(12) > span > a',
'#content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(14) > span > a',
'#content > div:nth-child(2) > table > tbody > tr:nth-child(2) > td:nth-child(16) > span > a',
]
'''

ict_selector = ['body > div > div.content > div > table > tbody > tr > td.cont > a',]
cau_selector = '#bbs > tbody > tr > td > a'

#Site Name
cse_site_name = '컴퓨터 공학부'
ict_site_name = '창의 ICT 공과대학'
cau_site_name = '중앙대학교'
#dormitory_site_name = '중앙대학교 기숙사 블루미르홀'

#File Informaton
cse_data = 'cse.txt'
ict_data = 'ict.txt'
cau_data = 'cau.txt'
#dormitory_data = 'dormitory.txt'

#List of History
cse_history = 'cse_history.txt'
ict_history = 'ict_history.txt'
cau_history = 'cau_history.txt'
#dormitory_history = 'dormitory_history.txt'


#list of information
cse_information = {'url' : cse_notice_url, 'selector' : cse_selector, 'site_name' : cse_site_name, 'data' : cse_data, 'history' : cse_history, 'time':cse_time_selector}
ict_information = {'url' : ict_notice_url, 'selector' : ict_selector, 'site_name' : ict_site_name, 'data' : ict_data, 'history' : ict_history, 'time':ict_time_selector}
cau_information = {'url' : cau_notice_url, 'selector' : cau_selector, 'site_name' : cau_site_name, 'data' : cau_data, 'history' : cau_history, 'time':cse_time_selector}
#dormitory_information = {'url' : dormitory_notice_url, 'selector' : dormitory_selector, 'site_name' : dormitory_site_name, 'data' : dormitory_data, 'history' : dormitory_history}

#def get_driver():
#    driver_dir = path_panthomjs
#    # driver = webdriver.Chrome(driver_dir)
#    driver = webdriver.PhantomJS(driver_dir)
#    
#    # driver.implicitly_wait(3)
#    return driver
#    

def crawller(information_list):
    log_func._log('Information Load', FUNCTION_STR)
    
    url = information_list['url']
    selector = information_list['selector']
    site_name = information_list['site_name']
    data = information_list['data']
    db_file = information_list['history']
    time_selector = information_list['time']

    log_func._log('Crawlling Start :' + site_name, FUNCTION_STR)
    # driver = get_driver()
    # driver.get(url)
    # html = driver.page_source
    req = requests.get(url)
    html = req.content
    # for Debug
    # print(html)
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup)

    notices = []
    for element_of_selector in selector:
        notices += soup.select(element_of_selector)

    time_stamp = []
    for element_of_time_selector in time_selector:
        time_stamp += soup.select(element_of_time_selector)

    log_func._log('HTML parsed', FUNCTION_STR)
    
    

    fp = open(data, "w", encoding='UTF8')
    compare_db_write_fp = open(db_file, "w", encoding='UTF8')
    compare_db_read_fp = open(db_file,"r", encoding='UTF8')
    
    clear_time_stamp = []
    for time in time_stamp:
        time = time.text.strip()
        clear_time_stamp.append(datetime.datetime.strptime(time, '%Y.%m.%d'))
        
    time_cnt = 0
    today = datetime.datetime.today()
    for title in notices:
        time_delta = today-clear_time_stamp[time_cnt]
        time_cnt += 1
        if time_delta.days >= 1:
            pass
        else:
            print(site_name + ":" + title.text.strip())
            fp.write(site_name + ' : ' + title.text.strip()+'\n')


    fp.close()
    time_cnt = 0
    log_func._log('File Write Complete..', FUNCTION_STR)
  
    #driver.close()
