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


# This Script scrape profile images from the page of each profile 


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
        time.sleep(0.5)
        # locate password form by_ID
        password = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.ID, 'session_password')))
        # send_keys() to simulate key strokes
        password.send_keys(os.getenv("LINKEDIN_PASSWORD"))
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
            EC.presence_of_element_located((By.CLASS_NAME, 'msg-overlay-bubble-header__button.truncate.ml2')))
        MessagingList.click()
    # Scrolling with chrono of 5 seconds ( you can changes as you like)
        time_end = time.time() + 5
        while time.time() < time_end:
            # To execute the scroll in webpage
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)
            # Appending the source code of the page
            sel = Selector(text=driver.page_source)
    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
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
    print("Local link <------>>>>>>", linksStored())
    return linktoload

# Get the links from storelink

def linksStored():
    with open('storelink.txt', "r") as local:
        local_links = local.readlines()
        # to remove the \n
        final_link = [local.strip("\n") for local in local_links]
        local.close()
    return final_link

# Adding links  in local

def storeLinks(links):
    with open('storelink.txt', 'a') as f:
        f.write(links+" \n")
        f.close()
    return links


def downloadImages(picture_url, image_name, linkedin_url):
    i = 0
    # Fet the source of the images profile
    url_img = picture_url.find_element(By.TAG_NAME, 'img').get_attribute('src')
    if (str(url_img).startswith("https://media-exp1.licdn.com/")):
        try:
            # get the source of the name profile
            text = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, "text-heading-xlarge.inline.t-24.v-align-middle.break-words"))).text
            # Compare the name of local images and the futur downloading images to not have a double
            if text+'.png' not in image_name:
                # Download the image
                urllib.request.urlretrieve(
                    url_img, "images/"+re.sub(" ", "_", text)+".png")
                # Add the link to the local txt
                storeLinks(linkedin_url)
                print("Download successfull, the link downloaded",linkedin_url)
                # add a 5 second pause loading each URL
                time.sleep(5)
            else:
                # Download the image
                i += 1
                urllib.request.urlretrieve(
                    url_img, "images/"+str(i)+'-'+re.sub(" ", "_", text)+".png")
                # Add the link to the local txt
                storeLinks(linkedin_url)
                print("Download successfull, the link downloaded",)
                # add a 5 second pause loading each URL
                time.sleep(5)
        except urllib.error.HTTPError as e:
            print(e.code)
            print(e.read())
            pass

# DownLoad function to get profile images

def downloadImageAndLink(driver):
    try:
        # Getting our list of images
        image_name = os.listdir(os.getenv("LOCAL_IMAGES"))
        for linkedin_url in linkToDownload():
            # Get the profile URL
            driver.get(linkedin_url)
            # Get picture URL
            picture_url = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'pv-top-card__non-self-photo-wrapper.ml0')))
            downloadImages(picture_url, image_name, linkedin_url)
    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
    driver.close()


if __name__ == "__main__":
    driver = initWebdriver()
    downloadImageAndLink(driver)
