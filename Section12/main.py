from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Mac
chrome_path = '/Users/hayato/Desktop/ScrapingBeginner/chromedriver'
# Windows
# chrome_path = r'C:\Users\hayato\Desktop\ScrapingBeginner\chromedriver'

# --> STEP1 : Yahoo画像検索に自動でアクセスする
options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
url = 'https://search.yahoo.co.jp/image'
driver.get(url)

sleep(3)

# --> STEP2 : プログラミングで検索する
query = 'プログラミング'
search_box = driver.find_element_by_class_name('SearchBox__searchInput')
search_box.send_keys(query)
search_box.submit()

sleep(3)

# --> STEP3 : スクロールして表示件数を増やす
height = 500
while height < 3000:

    driver.execute_script("window.scrollTo(0, {});".format(height))
    height += 100
    print(height)

    sleep(1)

driver.quit()
