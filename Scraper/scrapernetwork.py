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


# This Script scrape profile images from the page My Network  


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

def networkSource(link):
    driver.get(link)
    try:
        time.sleep(3)
        # Get the list messaging and remove it
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((
            By.XPATH, "//button/li-icon[@type='chevron-down-icon']"))).click()
        # Scrolling with chrono of 3 minutes ( you can changes as you like)
        time_end = time.time() + 60 * 3
        while time.time() < time_end:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)
            sel = Selector(text=driver.page_source)
    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
    return sel


# Get src of each linkedin image profile

def linkedinImgSrc():
    sel = networkSource('https://www.linkedin.com/mynetwork/')
    # to get all the link in the script a
    image_profile = set([a.attrib['src']
                        for a in sel.css('img')
                         if ("profile-displayphoto-shrink" or
                        "profile-framedphoto-shrink" in a.attrib['src'])])
    return image_profile


# Get the urls from local and check if they already exists in href got

def linkToDownload():
    links = linkedinImgSrc()
    linktoload = [row for row in links if row not in linksStored()]
    print("Les profile a télécharger <<<<<<<<<.......................>>>>>>>", linktoload)
    print("Local link <------>>>>>>", linksStored())
    return linktoload


# Get the links from storelink

def linksStored():
    with open('imagename.txt', "r") as local:
        local_links = local.readlines()
        # to remove the \n
        final_link = [local.strip("\n") for local in local_links]
        local.close()
    return final_link


# Adding links in local

def StoreImgName(links):
    with open('imagename.txt', 'a') as f:
        f.write(links+" \n")
        f.close()
    return links


# Get the identifier of the images

def GetImageName(src):
    name = re.findall("(a&.=..[A-z0-9_-]*)", src)
    return name


def downloadImages(image_url, image_name):
    try:
        # Getting our list of images
        local_image_names = linksStored()
        # Compare the name of local images and the futur downloading images to not have a double
        for name in image_name:
            if name+'.png' not in local_image_names:
                # Download the image
                urllib.request.urlretrieve(
                    image_url, "images/"+re.sub("\/", "_", name)+".png")
                # Add the link to the local txt
                StoreImgName(image_url)
                print("Download successfull, the link downloaded", image_url, '\n')
                # add a 5 second pause loading each URL
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        pass


# DownLoad function to get profile images

def downloadImageAndLink(driver):
    try:
        for image_url in linkToDownload():
            # get the url of each images and find the idientifier
            image_name = GetImageName(image_url)
            downloadImages(image_url, image_name)
    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
    driver.close()


if __name__ == "__main__":
    driver = initWebdriver()
    downloadImageAndLink(driver)
