import os
import time
os.system('pip3 install -r requirements.txt')
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import chromedriver_autoinstaller
import pyautogui

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]

try:
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe')  
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe') 

states_list = ['ALABAMA', 'ARIZONA', 'ARKANSAS', 'CALIFORNIA', 'COLORADO', 'FLORIDA', 'GEORGIA', 
'HAWAII', 'IDAHO', 'ILLINOIS', 'INDIANA', 'IOWA', 'KANSAS', 'KENTUCKY', 'LOUISIANA',
'MAINE', 'MICHIGAN', 'MINNESOTA', 'MISSISSIPPI', 'MISSOURI', 'MONTANA', 'NEBRASKA', 
'NEW JERSEY', 'NEW YORK', 'NORTH CAROLINA', 'NORTH DAKOTA', 'OHIO', 'OREGON', 'PENNSYLVANIA',
'SOUTH DAKOTA', 'TENNESSEE', 'TEXAS', 'UTAH', 'VERMONT', 'VIRGINIA', 'WASHINGTON', 
'WEST VIRGINIA', 'WISCONSIN', 'WYOMING'] 

driver.implicitly_wait(1) # 요 위에 까지는 코드를 실행하기 위한 준비

url = 'https://www.ncdc.noaa.gov/cdo-web/search'

def get_data(year, state):
    driver.get(url)
    Select(driver.find_element(By.ID, 'selectedDataset')).select_by_visible_text('Global Summary of the Month') #데이터 종류 선택 -> 완료

    driver.find_element(By.CLASS_NAME, 'noaa-daterange-input').click() #날짜 범위 선택 -> 완료
    time.sleep(1)
    Select(driver.find_elements(By.CLASS_NAME, 'ui-datepicker-year')[0]).select_by_value(str(year))
    Select(driver.find_elements(By.CLASS_NAME, 'ui-datepicker-month')[0]).select_by_index(0)
    driver.find_elements(By.CLASS_NAME, 'ui-state-default')[0].click()

    time.sleep(1)
    Select(driver.find_elements(By.CLASS_NAME, 'ui-datepicker-year')[-1]).select_by_value(str(year))  
    Select(driver.find_elements(By.CLASS_NAME, 'ui-datepicker-month')[-1]).select_by_index(11)
    driver.find_elements(By.CLASS_NAME, 'ui-state-default')[-1].click()

    driver.find_element(By.XPATH, '//*[@id="noaa-daterange-form"]/button[1]').click() #날짜 설정 -> 완료

    Select(driver.find_element(By.ID, 'selectedResultType')).select_by_visible_text('States') #검색 방식 선택 -> 완료

    driver.find_element(By.ID, 'selectedSearchString').send_keys(state) #검색어 입력 -> 완료

    driver.find_element(By.ID, 'searchSubmit').click() #검색 버튼 클릭 -> 완료
    time.sleep(1)

    while True:
        if driver.find_elements(By.XPATH, '/html/body/div[1]/div[2]/div/form/div[2]/div[2]/div[2]/div/div[1]/a'):
            break

    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/div[2]/div[2]/div[2]/div/div[1]/a').click() #장바구니에 담기
    time.sleep(1)

    pyautogui.moveTo(614, 396) #마우스 커서 위치 잠시 다른 곳으로 이동
    pyautogui.moveTo(1214, 396) #마우스 커서를 장바구니를 볼 수 있는 위치로 이동 -> 완료
    driver.find_element(By.ID, 'cartPreviewButton').click() #장바구니로 이동 -> 완료

    driver.find_elements(By.CLASS_NAME, 'productSelect')[-1].click() # csv 상품 선택 -> 완료

    driver.find_elements(By.XPATH, '//*[@id="cartContinue"]/button')[0].click() # 다음 단계 클릭 -> 완료
    time.sleep(1)

    while True:
        if driver.find_elements(By.XPATH, '//*[@id="dataTypesContainer"]/ul/li[2]/label'):
            break
    driver.find_element(By.XPATH, '//*[@id="dataTypesContainer"]/ul/li[2]/label').click() # 증발량 상세 항목 선택 -> 완료
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/div/div[4]/ul/li[2]/div/ul/li[3]/input').click() #증발량 선택 -> 완료
    driver.find_element(By.XPATH, '//*[@id="dataTypesContainer"]/ul/li[4]/label').click() # 강수량 상세 항목 선택 -> 완료
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/div/div[4]/ul/li[4]/div/ul/li[6]/input').click() #강수량 선택 -> 완료
    driver.find_element(By.XPATH, '//*[@id="dataTypesContainer"]/ul/li[6]/label').click() #기온 상세 항목 선택 -> 완료
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/div/div[4]/ul/li[6]/div/ul/li[6]/input').click() #최고기온 선택 -> 완료
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/div/div[4]/ul/li[6]/div/ul/li[7]/input').click() #최저기온 선택 -> 완료
    driver.find_element(By.XPATH, '//*[@id="dataTypesContainer"]/ul/li[7]/label').click() # 풍목 상세 항목 선택 -> 완료
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/form/div/div[4]/ul/li[7]/div/ul/li[1]/input').click() #평균 풍속 선택 -> 완료
    

    driver.find_element(By.ID, 'buttonContinue').click()#다음 단계 클릭 -> 완료
    time.sleep(1)

    while True:
        if driver.find_elements(By.ID, 'email'):
            break
    driver.find_element(By.ID, 'email').send_keys('pythonlover1457@gmail.com') #이메일 입력 -> 완료
    driver.find_element(By.ID, 'emailConfirmation').send_keys('pythonlover1457@gmail.com') #이메일 확인 입력 -> 완료

    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/form/div/div[4]/input').click() #주문 완료

for year in range(1987, 2018):
    for state in states_list:
        get_data(year, state)
        time.sleep(1)