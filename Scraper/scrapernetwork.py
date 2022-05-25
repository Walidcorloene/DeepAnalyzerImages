from unicodedata import name
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from dotenv import load_dotenv
from parsel import Selector
import urllib.request
import uuid
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
        time_end = time.time() + 1
        while time.time() < time_end:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1.5)
            sel = Selector(text=driver.page_source)
    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
    return sel


# Get true src of a person profile

# def GetTrueSrc(src):
#     profile = ['profile-displayphoto-shrink_200_200',
#                'profile-framedphoto-shrink_200_200']
#     true_src = [true for true in src if any(prof in true for prof in profile)]
#     return true_src


# Get src of each linkedin image profile

def linkedinImgSrc():
    sel = networkSource('https://www.linkedin.com/mynetwork/')
    image_profile=[]
    alt=[]
    # to get all the link in the script a
    for a in sel.css('a.ember-view.discover-entity-type-card__link img.lazy-image.ember-view.discover-entity-type-card__image-circle.Elevation-0dp.EntityPhoto-circle-7'):
       image_profile.append(a.attrib['src'])
       alt.append(re.sub(" ","_",a.attrib['alt']))
    return image_profile, alt



# Get the urls from local and check if they already exists in href got


def linkToDownload():
    links,name = linkedinImgSrc()
    linktoload = [row for row in links if row not in linksStored()]
    image_alt= [ alt for alt in name if alt not in LocalImageName()]
    print("Les profile a télécharger <<<<<<<<<.......................>>>>>>>", linktoload)
    print("Number of images to download >>>>>>>>>>>>>", len(linktoload))
    print("Les profile a télécharger <<<<<<<<<.......................>>>>>>>", image_alt)
    print("Number of images to download >>>>>>>>>>>>>", len(image_alt))
    return dict(zip(linktoload, image_alt))


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

#def GetImageName(src):
 #   name = re.findall("image\/([a-zA-Z0-9_-]*)", src)
  #  return name


# Get the name of local images

def LocalImageName():
    local_image_name = os.listdir(os.getenv("LOCAL_IMAGES"))
    return local_image_name

# This return an image with the name of image


def DownloaderUrl(img_url, img_name):
    return urllib.request.urlretrieve(img_url, "images/"+img_name+".png")


def downloadImages(image_url, name_alt):
    try:
        # Check if the list of image is not empty
        # Download the image
        DownloaderUrl(image_url, name_alt)
        # Add the link to the local txt
        StoreImgName(image_url)
        print("Download successfull, the link downloaded", image_url,"and image name is ", name_alt, '\n')
    except urllib.error.HTTPError as e:
        print(e.code)
        print(e.read())
        pass


# DownLoad function to get profile images

def downloadImageAndLink(driver):
    try:
        url_alt=linkToDownload()
       
        for image_url,name_alt  in url_alt.items():
            # Get the url of each images and find the idientifier to set it for image name
                 print(image_url,name_alt)
                 downloadImages(image_url, name_alt)
    except NoSuchElementException:
        print("\tError finding MessagingList")
        pass
    driver.close()


if __name__ == "__main__":
    driver = initWebdriver()
    downloadImageAndLink(driver)
