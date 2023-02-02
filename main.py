from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException

tinder_url = 'https://tinder.com'
s = Service("C:\development\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get(tinder_url)
time.sleep(2)
Enter_account_button = driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
# '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a'
driver.maximize_window()
Enter_account_button.click()
time.sleep(2)

# part2 Enter popup menu
#/div[2]/main/div/div[1]/div/div/div[3]/span/div[2]/button')
#//*[@id="q-1390893042"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button
#fb3.click()
time.sleep(2)
fb = driver.find_element(By.XPATH, '//*[@id="q-1390893042"]/main/div/div/div[1]/div/div/div[3]/span/div[2]/button')
fb.click()
window_after = driver.window_handles[1]
time.sleep(15)
driver.switch_to.window(window_after)
#driver.maximize_window()
time.sleep(2)
email_addr=driver.find_element(By.ID,'email')
email_addr.send_keys('shlomo.2fb@gmail.com')
idpass=driver.find_element(By.ID,'pass')
idpass.send_keys("OpenW2022")
time.sleep(2)
loginbutton=driver.find_element(By.ID,'loginbutton')
loginbutton.click()
time.sleep(6)

