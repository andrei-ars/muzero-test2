from selenium import webdriver
import time
import re
from xpath_soup import xpath_soup

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
#options.binary_location = "/usr/bin/chromium"
driver = webdriver.Chrome(chrome_options=options)
window_before = driver.window_handles[0]
driver.get("https://demosites.testgold.dev/login")
html_code = driver.page_source

#f = open("/ram/tmp/1.html", "wt")
#f.write(html_code)
#f.close()

from bs4 import BeautifulSoup
html_soup = BeautifulSoup(html_code, 'lxml')
#allTags = html_soup.findAll(element_tag)
elems = html_soup.find_all('input') # findAll
print(elems)
print(xpath_soup(elems[0]))