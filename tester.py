# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 15:52:07 2019

@author: USER
"""

import pandas as pd

test_student_data = pd.read_csv("test_students_data.csv")

import json

cut_off_scores = json.loads( open("cut_off_scores.json").read()  )

for course,score in zip(test_student_data['Program'],test_student_data['Jamb_Total']):
    if course in cut_off_scores and cut_off_scores[course] >= score:
#        if student
        print(course)
#        break
#    for i in cut_off_scores:
#        if