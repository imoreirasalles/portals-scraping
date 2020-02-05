from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

#open webdriver and site
with webdriver.Chrome() as driver:
     driver.get('http://201.73.128.131:8080/portals/#/search')
#find the search bar and writ
     WebDriverWait(driver, 10).until(lambda s: s.find_element_by_id("search").is_displayed())
     driver.find_element_by_id("search").send_keys("ferrez" + Keys.RETURN)
     input()
#close webdriver
    driver.quit()
     
    
    



#with webdriver.Chrome() as driver:
    #wait = WebDriverWait(driver, 10)
    #driver.get("https://google.com.br/")
    #driver.find_element_by_name("q").send_keys("cheese" + Keys.RETURN)
    #first_result = wait.until(presence_of_element_located((By.CSS_SELECTOR, "h3>div")))
    #print(first_result.get_attribute("textContent"))