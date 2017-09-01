#-*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import log_func


FUNCTION_STR = '[CRAWLER] '

# Where is chromedriver
path_chromedriver = "D:\\University\\dev\\chromedriver.exe"
path_panthomjs = "D:\\University\\dev\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe"

#Page URL
cse_notice_url = 'http://cse.cau.ac.kr/20141201/sub05/sub0501.php'
ict_notice_url = 'http://ict.cau.ac.kr/20150610/sub05/sub05_01_list.php'
cau_notice_url = 'https://www.cau.ac.kr/04_ulife/causquare/notice/notice_list.php?bbsId=cau_notice&category1=%C7%D0%BB%E7'

#HTML Selector
cse_selector = '#listpage_form > table.nlist > tbody > tr > td > a'
ict_selector = 'body > div > div.content > div > table > tbody > tr > td.cont > a'
cau_selector = '#bbs > tbody > tr > td > a'

#Site Name
cse_site_name = '컴퓨터 공학부'
ict_site_name = '창의 ICT 공과대학'
cau_site_name = '중앙대학교'

#File Informaton
cse_data = 'cse.txt'
ict_data = 'ict.txt'
cau_data = 'cau.txt'

#list of information
cse_information = {'url' : cse_notice_url, 'selector' : cse_selector, 'site_name' : cse_site_name, 'data' : cse_data}
ict_information = {'url' : ict_notice_url, 'selector' : ict_selector, 'site_name' : ict_site_name, 'data' : ict_data}
cau_information = {'url' : cau_notice_url, 'selector' : cau_selector, 'site_name' : cau_site_name, 'data' : cau_data}

def get_driver():
    driver_dir = path_panthomjs
    # driver = webdriver.Chrome(driver_dir)
    driver = webdriver.PhantomJS(driver_dir)
    
    # driver.implicitly_wait(3)
    return driver
    

def crawller(information_list):
    log_func._log('Information Load', FUNCTION_STR)
    
    url = information_list['url']
    selector = information_list['selector']
    site_name = information_list['site_name']
    data = information_list['data']

    log_func._log('Crawlling Start :' + site_name, FUNCTION_STR)
    driver = get_driver()
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select(selector)
    log_func._log('HTML parsed', FUNCTION_STR)
    
    fp = open(data, "w", encoding='UTF8')
        
    for title in notices:
        fp.write(site_name + ' : ' + title.text.strip()+'\n')
        
    fp.close()
    log_func._log('File Write Complete..', FUNCTION_STR)
    
    driver.close()