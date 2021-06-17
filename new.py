from bs4 import BeautifulSoup
import datetime
import getpass
from gmail import Gmail
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep

....

self.chrome_session = webdriver.Chrome()

....

links = self.chrome_session.find_elements_by_class_name('link-record')
links = [(link.text, link.get_attribute('href').decode('utf-8'))
         for link in links]
if len(links) == 0:
    print("No work orders available at {0}".format(
        datetime.datetime.now()))
else:
    for link_text, link_url in links:
        print("Clicking work order {0}".format(link_text))
        self.chrome_session.get(link_url)
        potential_input = self.chrome_session.find_element_by_class_name('v-actions').find_element_by_tag_name('input');
        if potential_input.get_attribute('value') == 'Accept':
            potential_input.click()
            print("Accepted work order {0} at {1}.".format(link_text,datetime.datetime.now()))
        else:
            print("Accept input not found.")
