#-*- coding: utf-8 -*-
import log_func

FUNCTION_STR = '[LOADINF] '

def load_information(file_name, list_name):
    log_func.log('Load FILE' + file_name, FUNCTION_STR)
    #IOException
    try:
        fp = open(file_name, "r", encoding='UTF8')
    except FileNotFoundError:
        log_func.log('IOxception:notFound' + file_name, FUNCTION_STR)
        fp = open(file_name, "w", encoding='UTF8')
        fp.close()
        fp = open(file_name, "r", encoding='UTF8')
    
    while True:
        line = fp.readline()
        if not line: break
        
        list_name.append(str(line))
    
    fp.close()