import telegram
import time
import telepot
import log_func

import loadInformation
import returnPageUrl


cmp_data = {}
cmp_to = {}

#Telegram Information
my_token = '406303272:AAF4zhQXYz0pR-mD6kMZgQX-mKmOLp9vFQA'
bot =telegram.Bot(token = my_token)

# compare crawl data from 'data.txt'
# If new thing is exist, send telegram alert

FUNCTION_STR = '[SENDDER] '

def logging(input_str):
    t = time.localtime()
    BASE_LOG = str(time.asctime(t)) + " :: " + FUNCTION_STR + input_str
    print(BASE_LOG)


# File Informaton
data_chat_id = 'chat_id.txt'
chat_id = []


def load_chat_id():
    log_func.log('Load Chat ID', FUNCTION_STR)
    # IOException
    try:
        fp = open(data_chat_id, "r", encoding='UTF8')
    except FileNotFoundError:
        fp = open(data_chat_id, "w", encoding='UTF8')
        fp.close()
        fp = open(data_chat_id, "r", encoding='UTF8')
    
    while True:
        line = fp.readline()
        
        if not line: break
        if '#' in str(line):
            pass
        if str(line).find('#') != -1:
            pass
        
        if '\n' in line:
            chat_id.append(str(line[:-1]))
        else:
            chat_id.append(str(line))
    
    print (chat_id)
    fp.close()

def compare_data(new, old):
    logging('Load Telegram chat id')
    load_chat_id()
    logging('Load Complete')
    
    idx = 0
    for st in new:
        if old.count(st) == 0:
            str = "안녕 마스터!! 새 공지가 올라왔어, 공지는 " \
                  + st + "인 모양이야!!\n"
            if st.find('창의') != -1:
                str += returnPageUrl.ict_url_ret()
            else:
                if st.find('컴퓨터') != -1:
                    str += returnPageUrl.cse_url_ret()
                else:
                    str += returnPageUrl.cau_url_ret()
            
            for ids in chat_id:
                log_func.log('Send Message.. '+ids, FUNCTION_STR)
                bot.sendMessage(chat_id=ids, text=str, parse_mode='Markdown')
            
            idx += 1
        else:
            idx += 1
            pass