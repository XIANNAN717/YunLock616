# -*- coding: gb18030 -*-
# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
url = "http://jira.upqing.com/secure/Dashboard.jspa"
driver.get(url)

driver.find_element_by_id("login-form-username").send_keys("596609597")
driver.find_element_by_id("login-form-password").send_keys("en=BK7K-")
driver.find_element_by_xpath("//*[@id='login']").click()

main_handle = driver.current_window_handle #当前窗口句柄
all_handles = driver.window_handles #所有窗口句柄
sleep(2)
print(main_handle)
print(all_handles)
if len(all_handles)>1:
    for main_handle in all_handles:
        if main_handle != "CDwindow":
            driver.switch_to.window(main_handle)
