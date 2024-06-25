from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

chrome_path = r'C:\\Users\\HP\\Desktop\\gitstuff\\chromedriver.exe' 

driver = webdriver.Chrome(service=Service(chrome_path),options=chrome_options)

driver.get("https://practicetestautomation.com/practice-test-login/")