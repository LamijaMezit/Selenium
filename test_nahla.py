from selenium import webdriver 
from selenium.webdriver.firefox.service import Service
options=webdriver.FirefoxOptions()
service = Service('geckodriver.exe')
driver = webdriver.Firefox(service=service, options=options) 

driver.get("http://www.nahla.ba") 

driver.quit()

