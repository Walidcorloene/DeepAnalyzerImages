# import web driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from dotenv import load_dotenv
from parsel import Selector
import urllib.request
import time
import re
import os

# Load .env file
load_dotenv(verbose=True)

# specifies the path to the chromedriver.exe
def initWebdriver():
    driver = webdriver.Chrome(os.getenv("WEBDRIVER_PATH"))

    # Maximaze page size
    driver.maximize_window()
    # driver.get method() will navigate to a page given by the URL address
    driver.get('https://www.linkedin.com')

    try:
        # locate email form by_ID
        username = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, 'session_key')))
        # send_keys() to simulate key strokes
        username.send_keys(os.getenv("LINKEDIN_USERNAME"))
    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
    time.sleep(0.5)
    try:
        # locate password form by_ID
        password = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, 'session_password')))
        # send_keys() to simulate key strokes
        password.send_keys(os.getenv("LINKEDIN_PASSWORD"))

    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
    time.sleep(0.5)
    try:
        # Locate submit button by_xpath
        sign_in_button = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.XPATH, '//*[@type="submit"]')))
        # Signin button click
        sign_in_button.click()
    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
    return driver

# Get source code of my networks profiles and scroll n times
def networkSource(link, driver):
    driver.get(link)
    try:
        # To close messaging list
        MessagingList = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, 'ember60')))
        MessagingList.click()
    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
    # Scrolling with chrono of 5 seconds ( you can changes as you like)
    time_end = time.time() + 5
    while time.time() < time_end:
        # To execute the scroll in webpage
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1.5)
        # Appending the source code of the page
        sel = Selector(text=driver.page_source)
    return sel


# Get Href of each linkedin profile in source code
def linkedinHref(driver):
    sel = networkSource('https://www.linkedin.com/mynetwork/', driver)
    linkedin = []
    path = 'https://www.linkedin.com'
    # to get all the link in the script a
    linkedin_href = [a.attrib['href'] for a in sel.css('a')]
    for link in linkedin_href:
        # getting the true linkeidn profile
        truelink = re.findall("(\/in\/[A-z0-9_%-]{5,})+\/?", link)
        linkedin.append(truelink)
        linkedin_urls = set([path+item for x in linkedin for item in x])
    print('nombre de profile recuperer <<<<<<<<<.......................>>>>>>>', len(
        linkedin_urls))
    return linkedin_urls

# Get the urls from local and check if they already exists in href got
def linkToDownload():
    links = linkedinHref(driver)
    linktoload = [row for row in links if row not in linksStored()]
    print("Les profile a télécharger <<<<<<<<<.......................>>>>>>>", linktoload)
    return linktoload

# Get the links from storelink
def linksStored():
    with open('storelink.txt',"r") as local:
        locallinks=local.readlines()
        local.close()
    return locallinks

# Adding links  in local
def storeLinks(links):
    with open('storelink.txt', 'a') as f:
        f.write(links+" \n")
        f.close()
    return links

# DownLoad function to get profile images
def downloadProfile(driver):
    # Getting our list of images
    i=0
    imagename = os.listdir(os.getenv("LOCAL_IMAGES"))
    for linkedin_url in linkToDownload():
        # Get the profile URL
        driver.get('https://www.linkedin.com/in/nora-agbakhamen')
        # Get picture URL
        picture_url = driver.find_elements(
            By.CLASS_NAME, 'pv-top-card__non-self-photo-wrapper.ml0')
        for url in picture_url:
            # Fet the source of the images profile
            url_img = url.find_element(By.TAG_NAME, 'img').get_attribute('src')
            if (str(url_img).startswith("https://media-exp1.licdn.com/")):
                # get the source of the name profile
                text = driver.find_element(
                    By.CLASS_NAME, "text-heading-xlarge.inline.t-24.v-align-middle.break-words").text
                try:
                    # Compare the name of local images and the futur downloading images to not have a double
                    if text+'.png' not in imagename:
                        # Download the image
                        urllib.request.urlretrieve(
                            url_img, "images/"+text+".png")
                        # Add the link to the local txt
                        storeLinks(linkedin_url)
                        print("Download successfull")
                        # add a 5 second pause loading each URL
                        time.sleep(5)                        
                except urllib.error.HTTPError as e:
                    print(e.code)
                    print(e.read())
                    continue  # continue to next row
    driver.close()


if __name__ == "__main__":
    driver = initWebdriver()

    downloadProfile(driver)
