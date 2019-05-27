import crawl
import loadInformation
import sendTelegram
import log_func

cmp_old = []
cmp_new = []

FUNCTION_STR = '[  MAIN ] '

def load_set(destination):
    loadInformation.load_information(crawl.cse_data, destination)
    loadInformation.load_information(crawl.ict_data, destination)
#    loadInformation.load_information(crawl.dormitory_data, destination)
#   loadInformation.load_information(crawl.cau_data, destination)
    
def crawl_set():
    crawl.crawller(crawl.cse_information)
    crawl.crawller(crawl.ict_information)
#    crawl.crawller(crawl.dormitory_information)
#    crawl.crawller(crawl.cau_information)

if __name__ == "__main__":
    
    load_set(cmp_old)
    # For Test (Erase 1 Old Notice)
    # del cmp_old[1]
    while True:
        log_func._log('Crawlling', FUNCTION_STR)
        # Crawling
        #bg_driver = crawl.get_driver()
        crawl_set()
        #bg_driver.close()
        
        load_set(cmp_new)
        
        sendTelegram.compare_data(cmp_new, cmp_old)
        
        cmp_old = list(cmp_new)
        del cmp_new[:]
        break
   
