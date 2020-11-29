from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Mac
chrome_path = '/Users/hayato/Desktop/ScrapingBeginner/chromedriver'
# Windows
# chrome_path = r'C:\Users\hayato\Desktop\ScrapingBeginner\chromedriver'

options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
url = 'https://search.yahoo.co.jp/image'
driver.get(url)

sleep(3)

query = 'プログラミング'
search_box = driver.find_element_by_class_name('SearchBox__searchInput')
search_box.send_keys(query)
search_box.submit()

sleep(3)


driver.quit()
