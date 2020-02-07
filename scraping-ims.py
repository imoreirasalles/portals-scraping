import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

"""Este script serve para pesquisar em uma página web determinada
    e coletar algum dado, exportando o contéudo de pesquisa com o dado
    extraído para um arquivo CSV"""

#abre o xlsx de referência para pesquisa
df= pd.read_excel('cumulus_teste.xlsx', 'Teste', index_col=None, na_values=['NA'])

#cria um dataframe para ser usado na pesquisa
ds_view= pd.DataFrame(df, columns=['Record_Name_1'])
ds_out=[]
#pesquisa por célula do dataframe 
def websearch (ds_view):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    for cell in df["Record_Name_1"]:
        record_name=(str(cell))
        with webdriver.Chrome(chrome_options=chrome_options) as driver:
            driver.get('http://201.73.128.131:8080/portals/#/search/')
            WebDriverWait(driver,10).until(lambda s: s.find_element_by_id("search").is_displayed())
            driver.find_element_by_id("search").send_keys(str(record_name) + Keys.RETURN)
            driver.find_element("h-ref")
            ds_view['URL']= ds_view.apply(lambda row: row.Record_Name_1, axis=1)
    print (ds_view)
websearch(ds_view)
