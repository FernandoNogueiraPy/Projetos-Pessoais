from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import os


options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=C:\\Users\\Moltt\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument('--profile-directory=Profile 4')



driver = webdriver.Chrome(service_args=["--user-data-dir=C:\\Users\\Moltt\\AppData\\Local\\Google\\Chrome\\User Data",'--profile-directory=Profile 4'])
driver.get("https://www.google.co.in")