from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def setSelect(driver, eleId, value):
    selEle = driver.find_element(By.ID, eleId)
    selObj = Select(selEle)
    selObj.select_by_visible_text(value)

def setValueById(driver, eleId, value):
    ele = driver.find_element(By.ID, eleId)
    ele.send_keys(value)

def parseDate(rawDate):
    return rawDate.split(',')