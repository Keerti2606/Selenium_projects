from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time



chrome_options = Options()
chrome_options.add_argument("--start-maximized")

chrome_path = r'C:\\Users\\HP\\Desktop\\gitstuff\\chromedriver.exe' 

driver = webdriver.Chrome(service=Service(chrome_path),options=chrome_options)

driver.get("https://practicetestautomation.com/practice-test-login/")

time.sleep(10)

user = driver.find_element(By.ID,'username')
user.send_keys('student')

time.sleep(10)

passw = driver.find_element(By.ID,'password')

with open('test.txt','r') as myfile:
    password = myfile.read().replace('\n',' ')
passw.send_keys(password)

submit = driver.find_element(By.ID,'submit')
submit.click()


