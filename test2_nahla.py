from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
service= Service(executable_path=ChromeDriverManager().install())
driver= webdriver.Chrome(service=service)


driver.get("https://www.nahla.ba")
driver.maximize_window()

podnaslovi= driver.find_elements(By.TAG_NAME, "h2")
polje_ime= driver.find_element(By.ID, "mce-FNAME")
polje_ime.click()
polje_ime.send_keys("Lamija Mezit")
driver.quit()