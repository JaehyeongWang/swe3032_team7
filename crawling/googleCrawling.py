#-*- coding:utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
# 드라이버 초기화
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pandas as pd

# 맥북만
s = Service('/Users/jewel/Downloads/chromedriver_mac64/chromedriver')

options = Options()
# options.add_argument('--headless')        # Head-less 설정
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

def googleCrawling(text_name, start, finish, DOWNLOAD_PATH):
    f = open(f'./{text_name}.txt', 'r')
    file_names = f.readlines()
    f.close()

    for ind, file_name in enumerate(file_names[start:finish]):
        file_name = file_name.split('.')[0]
        print(ind+start, file_name)
        URL = 'https://trends.google.co.kr/trends/explore'
        driver = webdriver.Chrome('chromedriver', options=options)
        driver.get(URL)
        URL2 = f'https://trends.google.co.kr/trends/explore?date=today%205-y&q={file_name}'
        driver.get(URL2)
        try: 
            driver.find_element(By.ID, 'af-error-container')
            driver.quit()
            driver = webdriver.Chrome('chromedriver', options=options)
            driver.get(URL)
            search = driver.find_element(By.ID, 'input-1')
            search.send_keys(file_name)
            search.send_keys(Keys.RETURN)
            driver.implicitly_wait(90)
            driver.find_element(By.ID, 'select_value_label_34').click()
            driver.find_element(By.ID, 'select_option_44').click()
            driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]').click()
            print('downloaded')
        except:
            driver.implicitly_wait(90)
            driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]').click()
            print('downloaded')
        finally:
            time.sleep(5)
            driver.quit()
            df = pd.read_csv(f'{DOWNLOAD_PATH}/multiTimeline.csv')
            df.columns = [file_name]
            df.drop('주', axis=0, inplace=True)
            df.to_csv(f'./{text_name}_search/{file_name}.csv')
            os.remove(f'{DOWNLOAD_PATH}/multiTimeline.csv')

option = Options()
option.add_argument('--headless')        # Head-less 설정
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')

def googleCrawling_mac(text_name, start, finish, DOWNLOAD_PATH):
    f = open(f'./{text_name}.txt', 'r')
    file_names = f.readlines()
    f.close()

    for ind, file_name in enumerate(file_names[start:finish]):
        file_name = file_name.split('.')[0]
        print(ind+start, file_name)
        URL = 'https://trends.google.co.kr/trends/explore'
        driver = webdriver.Chrome(service=s, options=option)
        driver.get(URL)
        URL2 = f'https://trends.google.co.kr/trends/explore?date=today%205-y&q={file_name}'
        driver.get(URL2)
        try: 
            driver.find_element(By.ID, 'af-error-container')
            driver.quit()
            driver = webdriver.Chrome(service=s, options=option)
            driver.get(URL)
            search = driver.find_element(By.ID, 'input-1')
            search.send_keys(file_name)
            search.send_keys(Keys.RETURN)
            driver.implicitly_wait(90)
            driver.find_element(By.ID, 'select_value_label_34').click()
            driver.find_element(By.ID, 'select_option_44').click()
            driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]').click()
            print('downloaded')
        except:
            driver.implicitly_wait(90)
            driver.find_element(By.XPATH, '/html/body/div[3]/div[2]/div/md-content/div/div/div[1]/trends-widget/ng-include/widget/div/div/div/widget-actions/div/button[1]').click()
            print('downloaded')
        finally:
            driver.quit()
            df = pd.read_csv(f'{DOWNLOAD_PATH}/multiTimeline.csv')
            df.columns = [file_name]
            df.drop('주', axis=0, inplace=True)
            df.to_csv(f'./{text_name}_search/{file_name}.csv')
            os.remove(f'{DOWNLOAD_PATH}/multiTimeline.csv')