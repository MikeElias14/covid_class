from selenium import webdriver
import browser_cookie3
import time
import requests
import re
import os

def make_dir(path):
  if not os.path.exists(path):
      os.makedirs(path)

def get_video(video_url, lect_path):
  r = requests.get(video_url)

  with open(lect_path + "/lect.mp4", 'wb') as f:
    f.write(r.content)

def get_slides(elements, lect_path):
  slides_path = lect_path + '/slides'
  make_dir(slides_path)

  for slide in elements:
    slide_url = slide.get_attribute("src")
    slide_name = slide_url.split('/')[-1]
    r = requests.get(slide_url)

    with open(slides_path + '/' + slide_name, 'wb') as f:
      f.write(r.content)


def main():

  # set vars
  learn_url = "https://learn.uwaterloo.ca"
  bongo_url = input("Enter the lecture url: ") 
  file_path = input("Enter the file path where you would like to save this lecture: ")
  make_dir(file_path)

  # visit home page
  driver = webdriver.Chrome('./chromedriver')
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

  # Get name
  invalid_chars = [':', '/', '*', '?', '<', '>']
  lect_name = driver.find_elements_by_class_name("content-title-description")[0].text[7:].split("\n")[0]
  for char in invalid_chars: 
   lect_name = lect_name.replace(char, ' ')

  lect_path = file_path + '\\' + lect_name

  make_dir(lect_path)

  # Get elements
  video_url = driver.find_elements_by_id("vjs_video_3_html5_api")[0].get_attribute("src")
  slides_elements = driver.find_elements_by_class_name("c-bbb-player__thumbnail-image")

  # Get video
  print('Got video URL. Downloading video...')
  get_video(video_url, lect_path) 


  # Get Slides
  print('Video Downloaded. Downloading slides...')
  get_slides(slides_elements, lect_path)

  driver.quit()


if __name__ == "__main__":
    main()