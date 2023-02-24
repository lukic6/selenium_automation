from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path, chrome_options=chrome_options)
driver.get("https://orteil.dashnet.org/cookieclicker/")

driver.implicitly_wait(3)

consent = driver.find_element(By.CLASS_NAME, "fc-button-label")
consent.click()

lang = driver.find_element(By.ID, "langSelect-EN")
lang.click()

driver.implicitly_wait(5)

cookie = driver.find_element(By.ID, "bigCookie")
cookie_count = driver.find_element(By.ID, "cookies") 
items = [driver.find_element(By.ID, "productPrice" + str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
#actions.move_to_element(cookie)
actions.click(cookie)
for i in range(5000):
    actions.perform()
    actions.click(cookie)
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()