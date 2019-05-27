import os
import time
import sendTelegram
while(1):
    try:
        os.system('python3.7 ./main.py')
    except :
        print('error')
        sendTelegram.error()
    time.sleep(300)
