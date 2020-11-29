from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Mac
chrome_path = '/Users/hayato/Desktop/ScrapingBeginner/chromedriver'
# Windows
# chrome_path = r'C:\Users\hayato\Desktop\ScrapingBeginner\chromedriver'

# --> 自動アクセスを実装してみる
options = Options()
options.add_argument('--incognito')

driver = webdriver.Chrome(executable_path=chrome_path, options=options)
url = 'https://tech-diary.net'
driver.get(url)

sleep(5)

driver.quit()
