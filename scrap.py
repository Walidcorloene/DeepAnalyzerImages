# import web driver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from parsel import Selector
import requests
import os
import csv
import time

# defining new variable passing two parameters

# writer = csv.writer(open(linkedin, 'wb'))

# writerow() method to the write to the file object
# writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(
    '/Users/WalidCorleone/selenium/webdriver/chromedriver/chromedriver')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_id('session_key')


# send_keys() to simulate key strokes
username.send_keys('khirdine.walid@gmail.com')

# sleep for 0.5 seconds
time.sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_id('session_password')

# send_keys() to simulate key strokes
password.send_keys('LINKDIN2lkref6w@')

time.sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()

time.sleep(0.5)

# # locate search form by_name
# search_query = driver.find_element(By.CLASS_NAME,'search-global-typeahead__input.always-show-placeholder')

# print(search_query)
# # send_keys() to simulate the search text key strokes
# search_query.send_keys('"dev"')

# # .send_keys() to simulate the return key
# search_query.send_keys(Keys.RETURN)


driver.get('https:www.google.com')
time.sleep(3)

accept = driver.find_element(By.ID, 'L2AGLb')
accept.click()

time.sleep(1)

search_query = driver.find_element(By.NAME, 'q')
search_query.send_keys('site:linkedin.com/in/ OR site:linkedin.com/pub/ -intitle:profiles -inurl:"/dir"')
time.sleep(0.5)

search_query.send_keys(Keys.RETURN)
time.sleep(3)


# linkedin_urls = driver.find_elements(By.CLASS_NAME, 'iUh30.qLRx3b.tjvcx')
# linkedin_urls = [url.text for url in linkedin_urls]
# time.sleep(1)

# nextt = driver.find_element(By.ID, 'pnnext')
# nextt.click()
# time.sleep(1)

# linkedin_urls2 = driver.find_elements(By.CLASS_NAME, 'iUh30.qLRx3b.tjvcx')
# linkedin_urls2 = [url.text for url in linkedin_urls2]
# linkedin_urls.extend(linkedin_urls2)

# for i in linkedin_urls:
#     print(i)

# time.sleep(1)

linkedin = []
for _ in range(10):
    linkedin_urls = driver.find_elements(By.CLASS_NAME, 'yuRUbf')
    for url in linkedin_urls:
        a = url.find_element(By.TAG_NAME, 'a').get_attribute('href')
        linkedin.append(a)
    time.sleep(0.5)
    nextt = driver.find_element(By.ID, 'pnnext')
    nextt.click()

print(linkedin)
print(len(linkedin))
print(linkedin[0])
time.sleep(0.5)
# For loop to iterate over each URL in the list

for linkedin_url in linkedin:
    if len(linkedin_url) != 0:
       # get the profile URL
        driver.get(linkedin_url)

   # add a 5 second pause loading each URL
        time.sleep(5)

   # assigning the source code for the webpage to variable sel
        sel = Selector(text=driver.page_source)
time.sleep(0.5)
all_iamges = sel.xpath('//div[@class="pv-top-card--photo"]//img[@src]').extract_first()

for img in all_iamges:
    url = img.get_attribute('src')
    filename = url.split("/")[-1]
    print('url:', url)
    print('filename:', filename)
    print('-----')

    full_path = os.path.join('/Users/WalidCorleone/selenium/', filename)

    response = requests.get(url)
    with open(full_path, "wb") as fh:
        fh.write(response.content)
# terminates the application
driver.quit()
# driver.quit()
