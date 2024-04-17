import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
def getCode(log, pas):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://mmofarmers.space/webmail")
    time.sleep(3)
    name = driver.find_element(by=By.ID,value="rcmloginuser")
    passw = driver.find_element(by=By.ID,value="rcmloginpwd")
    loginbutton = driver.find_element(by=By.ID,value="rcmloginsubmit")
    name.send_keys(log)
    passw.send_keys(pas)
    loginbutton.click()
    time.sleep(3)
    preletter = driver.find_element(by=By.ID,value="messagelist")
    letter = preletter.find_element(by=By.PARTIAL_LINK_TEXT,value="Ваш код подтверждения HoYoverse")
    code = re.sub("\D", "", letter.text)
    return code
