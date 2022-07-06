import os
import datetime
os.system('pip3 install -r requirements.txt')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import chromedriver_autoinstaller

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')  
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')  

driver.implicitly_wait(1) # 요 위에 까지는 코드를 실행하기 위한 준비

url = 'https://www.ncdc.noaa.gov/cdo-web/search'

driver.get(url)
Select(driver.find_element(By.ID, 'selectedDataset')).select_by_index(2) #데이터 종류 선택 -> 완료

driver.find_element(By.CLASS_NAME, 'noaa-daterange-input').click() #날짜 범위 선택
Select(driver.find_elements(By.CLASS_NAME, 'ui-datepicker-year')[0]).select_by_value('1987')
Select(driver.find_elements(By.CLASS_NAME, 'ui-datepicker-month')[0]).select_by_index(0)
driver.find_elements(By.CLASS_NAME, 'ui-state-default')[0].click()

Select(driver.find_elements(By.CLASS_NAME, 'ui-datepicker-year')[-1]).select_by_value('2017')
Select(driver.find_elements(By.CLASS_NAME, 'ui-datepicker-month')[-1]).select_by_index(11)
driver.find_elements(By.CLASS_NAME, 'ui-state-default')[-1].click()

