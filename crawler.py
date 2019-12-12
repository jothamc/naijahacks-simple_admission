# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:05:37 2019

@author: USER
"""

from bs4 import BeautifulSoup

page_source = open("jbc.html").read()

soup = BeautifulSoup(page_source,"html.parser")

h2soup = soup.select("h2>span")
faculties = []
for i in h2soup:
    faculties.append(i.get_text())
faculties.pop(0)

h3soup = soup.select("h3")
subjects = {}
for i in h3soup:
    try:
        subject = i.get_text()
        subjects[subject] = i.next_sibling.get_text()
    except:
        continue

subjects.pop('Sponsored:')

import re

courses = {}

for i in subjects:
   a = subjects[i]
   i = re.sub(r'(\d+\.)','',i)
   i = i.strip(":")
   a = a.replace("(See other requirements)",'')
   courses[i] = a.strip()

# print(courses)

# all_subjects = set([courses[x] for x in courses])
# print(all_subjects)