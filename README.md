# CauCrawler(중앙대컴퓨터공학부 공지사항 크롤러)
## 1. Outline, Requirement
##### English
* `CauCrawler` is automated python3 module for crawling notice under 3 sites.
  * [CAUCSE](http://cse.cau.ac.kr), [ICT](http://ict.cau.ac.kr), [CAU_NOTICE](http://cau.ac.kr)
* You SHOULD modify setting(crawl.py) to use this module.
  * This Module is using `selenium`, so you need to modify path of PhantomJS or ChromeDirver in source code.
    * required to download proper driver file fit your architecture. (binary or exe ...) 
  * for more information about `selenium`, please check [here](http://www.seleniumhq.org/).

##### 한글
* `CauCrawler`은 아래의 세 사이트의 공지사항을 자동으로 긁어오기 위한 파이썬3 모듈 입니다.
   * [CAUCSE](http://cse.cau.ac.kr), [ICT](http://ict.cau.ac.kr), [CAU_NOTICE](http://cau.ac.kr)
* 모듈을 사용하기 위해서는 소스코드 내부(crawl.py)를 조금 수정해야 합니다.
  * 이 모듈은 `셀레니움`을 사용하고 있기 때문에, PhathomJS나 Chromdriver을 사용하는 경우, 소스코드 내부에서 지정된 경로를 수정해주어야 합니다.
    * 사용할 드라이버 파일(binary 또는 exe)이 존재해야 합니다. 시스템 아키텍쳐에 맞는 버젼으로 사용해주세요.
  * `selenium`에 대해서는 [여기](http://www.seleniumhq.org/)를 참조해주세요.
    
  
## 2. Usage
##### Requirement
 * You need to install several Python packages
   * If you use Python3, `sudo pip3 install telegram telepot beautifulsoup selenium bs4 python-telegram-bot`
   * If you use Python, `sudo pip install telegram telepot beautifulsoup selenium bs4 python-telegram-bot`

`$git clone https://github.com/shieldnet/CauCrawler`
```python
import CauCrawler

```

## 3. API
* I`m tired..`