import re
from selenium import webdriver
import browser_cookie3

def expand_element(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root

driver = webdriver.Chrome('./chromedriver')

# visit home page
learn_url = "https://learn.uwaterloo.ca"
bongo_url = "https://bongo-ca.youseeu.com/spa/student/class/190649/meeting-preview/479604?lti-scope=d2l-resource-syncmeeting-open"
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

# now we get the video from the lesson page and download it

element_root = driver.find_elements_by_id("root")
# element_root_shadow = expand_element(element_root)
# settingsBasicPage = settingsShadowRoot.find_element_by_tag_name("settings-basic-page")
# settingsBasicPageShadowroot = expand_root_element(settingsBasicPage)
# settingsPrivacyPage = settingsBasicPageShadowroot.find_element_by_tag_name("settings-privacy-page")
# settingsPrivacyShadowRoot = expand_root_element(settingsPrivacyPage)
# settingsClearBrowsingDataDialog = settingsPrivacyShadowRoot.find_element_by_tag_name(
#     "settings-clear-browsing-data-dialog")
# settingsClearBrowsingDataDialogShadowRoot = expand_root_element(settingsClearBrowsingDataDialog)
# settingsClearBrowsingDataDialogShadowRoot.find_element_by_id("clearBrowsingDataConfirm").click()

ids = driver.find_elements_by_xpath('//*[@id]')
for ii in ids:
    # print(ii.tag_name)
    print(ii.get_attribute('id'))    # id name as string

driver.quit()
# print(video_url)