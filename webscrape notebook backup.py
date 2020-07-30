#!/usr/bin/env python
# coding: utf-8

# In[196]:


from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import pandas as pd

PATH_TO_CHROMEDRIVER = "C:/Users/12244/yoonp/independentCS/kpop/chromedriver.exe"
driver = webdriver.Chrome(PATH_TO_CHROMEDRIVER)

stage_name = []
full_name = []
korean_name = []
korean_stage_name = []
date_of_birth = []
group = []
country = []
second_country = []
height = []
weight = []
birthplace = []
other_group = []
former_group = []
gender = []
position = []
instagram = []
twitter = []

driver.get("https://dbkpop.com/db/all-k-pop-idols")
driver.maximize_window()

XPATH_SELECTOR = "//div[@id='table_1_length']//label//div[contains(@class, 'btn-group bootstrap-select length_menu')]"
driver.implicitly_wait(30)
div_to_select = driver.find_element_by_xpath(XPATH_SELECTOR)
selector = div_to_select.find_element_by_xpath("//select[@name='table_1_length']")

select = Select(selector)
select.select_by_value('-1')

XPATH_COLUMN = "//div[@id='table_1_wrapper']//div[contains(@class, 'dt-buttons')]//a[contains(@class, 'dt-button buttons-collection buttons-colvis DTTT_button DTTT_button_colvis')]"
div_to_columns = driver.find_element_by_xpath(XPATH_COLUMN)
div_to_columns.click()

for i in range(1,19):
    XPATH_SCROLL_DOWN_COLUMN = "//div[contains(@class, 'dt-button-collection')]//a[" + str(i) + "]"
    div_to_sdc = driver.find_element_by_xpath(XPATH_SCROLL_DOWN_COLUMN)
    attribute_name  = div_to_sdc.get_attribute("class")

    #clicks if check is not checked!
    if attribute_name == "dt-button buttons-columnVisibility":
        driver.execute_script("arguments[0].click();", div_to_sdc)
        #clicks apparently lol
        
XPATH_TO_TABLE = "//div[@id='table_1_wrapper']//div[contains(@class, 'wdtscroll')]//table[@id='table_1']//tbody"
table_element = driver.find_element_by_xpath(XPATH_TO_TABLE)
all_rows = table_element.find_elements_by_xpath("//tr")
all_values = all_rows[0].find_elements_by_xpath("//td")

n = 18
kpop_artists = [all_values[i * n:(i + 1) * n] for i in range((len(all_values) + n - 1) // n )] #split all_values into every 18
if not len(kpop_artists[-1]) == 18:
    del kpop_artists[-1]

for artist in kpop_artists:
    stage_name.append(artist[1].text)
    full_name.append(artist[2].text)
    korean_name.append(artist[3].text)
    korean_stage_name.append(artist[4].text)
    date_of_birth.append(artist[5].text)
    group.append(artist[6].text)
    country.append(artist[7].text)
    second_country.append(artist[8].text)
    height.append(artist[9].text)
    weight.append(artist[10].text)
    birthplace.append(artist[11].text)
    other_group.append(artist[12].text)
    former_group.append(artist[13].text)
    gender.append(artist[14].text)
    position.append(artist[15].text)
    instagram.append(artist[16].text)
    twitter.append(artist[17].text) 
    print(artist[1].text, artist[2].text, artist[3].text, artist[4].text, artist[5].text, artist[6].text, artist[7].text, artist[8].text, artist[9].text, artist[10].text, artist[11].text, artist[12].text, artist[13].text, artist[14].text, artist[15].text, artist[16].text, artist[17].text)


# In[ ]:


#As of 4/4/2020, there are 1291 artists


# In[218]:


#remove the extras
attributes = [stage_name, full_name, korean_name, korean_stage_name, date_of_birth, group, country, second_country, height, 
                weight, birthplace, other_group, former_group, gender, position, instagram, twitter]

total_num = len(kpop_artists)
            
for att in attributes:
    if total_num == len(att):
        del att[-1]


# In[231]:


df = pd.DataFrame({'Stage Name':stage_name,'Full Name':full_name,'Korean Name':korean_name,
                'Korean Stage Name':korean_stage_name,'Date of Birth':date_of_birth,'Group':group,
                'Country':country,'Second Country':second_country,'Height':height,'Weight':weight,
                'Birthplace':birthplace,'Other Group':other_group,'Former Group':former_group,
                'Gender':gender,'Position':position,'Instagram':instagram,'Twitter':twitter}) 
df.to_csv('kpop.csv', index=False, encoding='utf-8-sig')

