from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
# OPTION 1: use the following options for headless operation
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')
# OPTION 2: use interactive mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get("<URL>")
sleep(2)
try:
    driver.find_element(By.ID, "cookie-accept-all-button").click()
except:
    print("No cookie banner found, continue...")

# send username
username = driver.find_element(By.ID, "Username")
username.send_keys("<LOGIN_NAME>")
password = driver.find_element(By.ID, "Password")
password.send_keys("<PASSWORD>")
password.submit()
sleep(10)
driver.close()
