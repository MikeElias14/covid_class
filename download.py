from selenium import webdriver
import browser_cookie3
import time
import requests
import re

driver = webdriver.Chrome('./chromedriver')

learn_url = "https://learn.uwaterloo.ca"
bongo_url = "https://bongo-ca.youseeu.com/spa/student/class/190649/meeting-preview/479604?lti-scope=d2l-resource-syncmeeting-open"

# visit home page
driver.get(learn_url)

# set cookies
bongo_cookies = browser_cookie3.chrome(domain_name='bongo-ca.youseeu.com')
learn_cookies = browser_cookie3.chrome(domain_name='learn.uwaterloo.ca')

for c in bongo_cookies:
    cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'secure': c.secure and True or False}
    driver.add_cookie(cookie)
for c in learn_cookies:
    cookie = {'domain': c.domain, 'name': c.name, 'value': c.value, 'secure': c.secure and True or False}
    driver.add_cookie(cookie)

# then visit the home page again, should sign in. Then we go to the lesson
driver.get(learn_url)
driver.get(bongo_url)
time.sleep(10)

# now we get the video from the lesson page and download it 
video_element = driver.find_elements_by_id("vjs_video_3_html5_api")[0]
video_url = video_element.get_attribute("src")

driver.quit()

print('Got video URL. Beginning download...')
r = requests.get(video_url)

with open('C:\\Users\\Mike\\Documents\\4aSchool\\test.mp4', 'wb') as f:
    f.write(r.content)

print('done')