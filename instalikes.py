from asyncio import wait
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


#print("Hello World. This is from Selenium python script.")
url = 'https://www.instagram.com'

#load the Chrome webdriver with the location

driver = webdriver.Chrome('Location of the Chrome Webdriver',chrome_options=chrome_options)
driver.get(url)
time.sleep(2)

#Replace your username and password here to login to the instagram.

username = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input").send_keys("username")
password = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input").send_keys("password")
Enter = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]").click()
time.sleep(5)
#notnow = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button").click()
print("Reached here")

search = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/div/a/div/div[1]").click()

#Replace here the hashtag from which you want to like the pictures.

hashtag_search = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div/input").send_keys("#your_hashtag")
time.sleep(5)
#print("Reached Here")
profile = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div[2]/div/div[1]").click()
time.sleep(10)
post1 = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[1]/div/div/div[1]/div[1]/a/div/div[2]").click()
time.sleep(2)
like1 = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
time.sleep(4)
next1 = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div").click()
time.sleep(2)

#adjust the range based on your assumptions.

for i in range(1,100):
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button").click()
    time.sleep(3)
    print("Liked Picture:", i)

driver.close()
