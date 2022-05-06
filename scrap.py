# import web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from parsel import Selector
import requests
import re
import urllib.request
from selenium import webdriver
import time
import os
from dotenv import load_dotenv

# defining new variable passing two parameters

# writer = csv.writer(open(linkedin, 'wb'))

# writerow() method to the write to the file object
# writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('./chromedriver.exe')
# Load .env file
load_dotenv(verbose=True)

driver.maximize_window()
# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_id('session_key')


# send_keys() to simulate key strokes
username.send_keys(os.getenv("LINKEDIN_USERNAME"))

# sleep for 0.5 seconds
time.sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_id('session_password')

# send_keys() to simulate key strokes
password.send_keys(os.getenv("LINKEDIN_PASSWORD"))

time.sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()

time.sleep(0.5)

# get source code of my networks profiles and scroll 30 times
driver.get('https://www.linkedin.com/mynetwork/')
time.sleep(3)
for _ in range(1):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1.5)
    sel = Selector(text=driver.page_source)
# get Href of each linkeidn profile in source code
linkedd = [a.attrib['href'] for a in sel.css('a')]
time.sleep(1)

linkedin = []
linke = 'https://www.linkedin.com'
for url in linkedd:
    x = re.findall("\/in\/[A-z0-9_-]+\/?", url)
    linkedin.append(x)
    linkedin_urls = [linke+item for x in linkedin for item in x]

i=0
for linkedin_url in linkedin_urls:
    if len(linkedin_url) > 35:
        # get the profile URL
        driver.get(linkedin_url)
        picture_url = driver.find_elements(
            By.CLASS_NAME, 'pv-top-card__non-self-photo-wrapper.ml0')
        for url in picture_url:
            a = url.find_element(By.TAG_NAME, 'img').get_attribute('src')
            # # download the image
            try:
                i += 1
                urllib.request.urlretrieve(a, "images/AdNonAd"+str(i)+".png")
                # add a 5 second pause loading each URL
                time.sleep(2)
            except AssertionError:
                print("No picture to download")
