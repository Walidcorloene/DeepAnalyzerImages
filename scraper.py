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


# specifies the path to the chromedriver.exe
driver = webdriver.Chrome("./chromedriver.exe")
# Load .env file
load_dotenv(verbose=True)

driver.maximize_window()
# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element(By.ID, 'session_key')

# send_keys() to simulate key strokes
username.send_keys(os.getenv("LINKEDIN_USERNAME"))

# sleep for 0.5 seconds
time.sleep(0.5)

# locate password form by_class_name
password = driver.find_element(By.ID, 'session_password')

# send_keys() to simulate key strokes
password.send_keys(os.getenv("LINKEDIN_PASSWORD"))

time.sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()

time.sleep(0.5)


# get source code of my networks profiles and scroll n times
def networkSource(link):
    driver.get(link)
    time.sleep(3)
    for _ in range(50):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)
        sel = Selector(text=driver.page_source)
    return sel


# get Href of each linkeidn profile in source code
def LinkedinHref(sel=networkSource('https://www.linkedin.com/mynetwork/')):
    linkedin = []
    path = 'https://www.linkedin.com'
    linkedin_href = [a.attrib['href'] for a in sel.css('a')]
    for link in linkedin_href:
        truelink = re.findall("(\/in\/[A-z0-9_%-]{5,})+\/?", link)
        linkedin.append(truelink)
        linkedin_urls = set([path+item for x in linkedin for item in x])
    return linkedin_urls


def downloadProfile():
    imagename = os.listdir(os.getenv("LOCAL_IMAGES"))
    for linkedin_url in LinkedinHref():
        # get the profile URL
        driver.get(linkedin_url)
        picture_url = driver.find_elements(
            By.CLASS_NAME, 'pv-top-card__non-self-photo-wrapper.ml0')
        for url in picture_url:
            # get the source of the images profile
            a = url.find_element(By.TAG_NAME, 'img').get_attribute('src')
            # get the source of the name profile
            text = driver.find_element_by_class_name(
                "text-heading-xlarge.inline.t-24.v-align-middle.break-words").text
            # # download the image
            try:
                 if text not in imagename:
                    urllib.request.urlretrieve(a, "images/"+text+".png")
                    # add a 5 second pause loading each URL
                    time.sleep(2)
            except AssertionError:
                print("No picture to download")


if __name__ == "__main__":
    downloadProfile()
