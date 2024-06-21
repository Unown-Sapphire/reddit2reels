import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui
from subreddit import random_title
import os

chrome_driver_path = "chromedriver-win64/chromedriver-win64/chromdriver.exe"

user_data_dir = "C:/Users/dmneh/Downloads/chrome-user-data"

options = webdriver.ChromeOptions()
options.add_argument(f"user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=options)

m = 1

# Open Instagram
driver.get("https://www.instagram.com/")
driver.maximize_window()
driver.implicitly_wait(20)

wait = WebDriverWait(driver, 10)

for file in os.listdir("videos/video_parts"):
    create_button = wait.until(EC.presence_of_element_located((By.XPATH , "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a"))).click()
    post_button = wait.until(EC.presence_of_element_located((By.XPATH , "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/div/div/div[1]/a[1]"))).click()
    select_from_computer = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button"))).click()
    time.sleep(5)
    pyautogui.write(f'C:\\Users\\dmneh\\Desktop\\ADHDTrap\\videos\\video_parts\\test_{m}.mp4', interval=0.05)
    pyautogui.press('enter')

    time.sleep(2)
    change_resolution = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div/button"))).click()
    time.sleep(2)
    reels_resolution = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[1]/div/div[1]/span"))).click()

    next_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div"))).click()

    time.sleep(2)
    thumbnail_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div/div"))).click()
    time.sleep(5)
    pyautogui.write(f'C:\\Users\\dmneh\\Desktop\\ADHDTrap\\images\\thumbnail_{m}.png', interval=0.05)
    pyautogui.press('enter')

    time.sleep(2)
    next2_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div"))).click()

    time.sleep(3.5)

    caption_text = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[1]/div[1]"))).send_keys(f'{random_title} Part {m}! #reddit #askreddit #aita #tifu #subreddit #subwaysurfers #redditstories #viral #story #storytime')
    share_button = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[6]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[1]/div/div/div/div[3]/div/div"))).click()

    time.sleep(180)

    m+=1

    driver.refresh()

driver.quit()
