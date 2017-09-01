import seleniumCrawller
import loadInformation
import sendTelegram
import log_func

cmp_old = []
cmp_new = []

FUNCTION_STR = '[  MAIN ] '

def load_set(destination):
    loadInformation.load_information(seleniumCrawller.cse_data, destination)
    loadInformation.load_information(seleniumCrawller.ict_data, destination)
    loadInformation.load_information(seleniumCrawller.cau_data, destination)
    
def crawl_set():
    seleniumCrawller.crawller(seleniumCrawller.cse_information)
    seleniumCrawller.crawller(seleniumCrawller.ict_information)
    seleniumCrawller.crawller(seleniumCrawller.cau_information)

if __name__ == "__main__":
    
    load_set(cmp_old)
    # For Test (Erase 1 Old Notice)
    # del cmp_old[1]
    while True:
        log_func._log('Crawlling', FUNCTION_STR)
        # Crawling
        bg_driver = seleniumCrawller.get_driver()
        crawl_set()
        bg_driver.close()
        
        load_set(cmp_new)
        
        sendTelegram.compare_data(cmp_new, cmp_old)
        
        cmp_old = list(cmp_new)
        del cmp_new[:]
        break
    