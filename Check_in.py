#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 12:04:48 2018

@author: dominikklepl
"""

# =============================================================================
# Hey you lazy student

# With this script you go around the incredibly boring, annoying Qwickly check in process.
# The only thing it requires is a csv file with your login and password to Blackboard named "info.csv".
# If you're not using Mac or for same reason you do but Safari is not your default browser you'll need to
# replace the word "Safari" on line 38 with name of your browser. Selenium library supports 
# at the moment follwing browsers:
#   Safari, IE, Edge, Chrome Firefox.

# Selenium is an amazing Python package for automated navigating through the web. Don't worry your machine
# shouldn't be hijacked. For those interested check out their documentation 
# (http://selenium-python.readthedocs.io/index.html). It can do a lot of cool stuff.

# From now on you can enjoy the lecture without having to think of Qwickly. You can run the script
# from your terminal by typing in Check in.py
# =============================================================================


from selenium import webdriver
import time
import pandas as pd

#open the file with login info and course name
info = pd.read_csv('Check_in.csv',sep=';')

#extract the information from the csv file
user=info.iloc[0]['Username']
password=info.iloc[0]['Password']

#ask for which course you're checking in
which_course = input("Hello, enjoying lecture? BTW what lecture would that be? \n 0: Social and cultural dynamics in cognition \n 1: Computational Modeling for Cognitive Science \n 2: Models of perception and action \n Your answer: ")
which_course = int(which_course)

#depending on which_course choose the correct row in info
course=info.iloc[which_course]['Course']

#open browser - replace Safari with your browser of choice
driver = webdriver.Safari()
driver.maximize_window()

time.sleep(2)

driver.get("https://blackboard.au.dk/webapps/bb-auth-provider-shibboleth-BBLEARN/execute/shibbolethLogin?returnUrl=https%3A%2F%2Fblackboard.au.dk%2Fwebapps%2Fportal%2Fframeset.jsp&authProviderId=_102_1")
time.sleep(2)

#find all the boxes needed to login to blackboard
username_box = driver.find_element_by_id('username')
password_box = driver.find_element_by_id('password')
login_button = driver.find_element_by_class_name('button')

#fill in the boxes and click on "login" button
username_box.send_keys(user)
password_box.send_keys(password)
login_button.click()

#wait for the page to load
time.sleep(5)

#now we're on the main page of blackboard
#choose the course - SocKult from the "My courses" table
course_link = driver.find_element_by_link_text(course)
course_link.click()

time.sleep(2)

#click on Qwickly in the side menu
qwickly_button = driver.find_element_by_link_text('Qwickly')
qwickly_button.click()

time.sleep(2)
#click on check in
checkin_button = driver.find_element_by_name("studentCheckIn")
checkin_button.click()


#That's it for now but as after next lecture it will be possible to even click on Check In button
#or in case of Mel's lecture to enter the password

#preparation for entering password
# =============================================================================
# if which_course ==2: #that means we'll need a password
#    code = input("Could you repeat the code Mel just told you? Pretty please.")
#     
#     #find the code input box
#     code_box = driver.find_element_by_id('')
#     code_box.send_keys(code)
#     
#     #and click on accept or maybe hit Enter?
# =============================================================================
    
    


