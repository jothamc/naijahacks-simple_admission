# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:38:32 2019

@author: USER
"""

from selenium import webdriver
from bs4 import BeautifulSoup



wd = webdriver.Firefox()
wd.get("https://nigerianscholars.com/school-news/jamb-subject-combinations-for-all-courses")
page_source = wd.page_source

home_page = BeautifulSoup(page_source,"html.parser")
pretty_home_page = home_page.prettify()

file = open("jamb_combos.html","w")
file.write( pretty_home_page )
file.close()
