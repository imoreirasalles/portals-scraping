from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#open brownser and website
browser = webdriver.Chrome() 
browser.get('http://ims.com.br')

#close browser
browser.quit()