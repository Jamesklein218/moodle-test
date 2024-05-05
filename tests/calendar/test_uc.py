from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time
import pytest
from utils.auth import login
from utils.readData import readDataFromExcel
from utils.calendar import setSelect, setValueById, parseDate

def test_uc1():
  driver = webdriver.Chrome()

  wait = WebDriverWait(driver, 10)

  login(driver, "teacher", "moodle")

  driver.get("https://school.moodledemo.net/my/index.php")

  driver.implicitly_wait(2)
  newEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='new-event-button']")))

  newEventBtn.click()

  eventNameInput = driver.find_element(By.ID, "id_name")
  saveEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='save']")))

  setValueById(driver, "id_name", "Test Event")
  setSelect(driver, "id_timestart_day", "12")
  setSelect(driver, "id_timestart_month", "January")
  setSelect(driver, "id_timestart_year", "2020")
  setSelect(driver, "id_timestart_hour", "00")
  setSelect(driver, "id_timestart_minute", "00")

  saveEventBtn.click()
  time.sleep(1.5)

  modalEle = driver.find_element(By.CLASS_NAME, "modal")
  assert not modalEle.is_displayed()

  driver.quit()

def test_uc2():
  driver = webdriver.Chrome()

  wait = WebDriverWait(driver, 10)

  login(driver, "student", "moodle")

  driver.get("https://school.moodledemo.net/my/index.php")

  driver.implicitly_wait(2)
  try:
    newEventBtn = driver.find_element(By.CSS_SELECTOR, "button[data-action='new-event-button']")
    assert False
  except NoSuchElementException:
    assert True

  driver.quit()

def test_uc3():
  driver = webdriver.Chrome()

  wait = WebDriverWait(driver, 10)

  login(driver, "teacher", "moodle")

  driver.get("https://school.moodledemo.net/my/index.php")

  driver.implicitly_wait(2)
  newEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='new-event-button']")))

  newEventBtn.click()

  eventNameInput = driver.find_element(By.ID, "id_name")
  saveEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='save']")))

  setValueById(driver, "id_name", "Test Event")
  setSelect(driver, "id_timestart_day", "12")
  setSelect(driver, "id_timestart_month", "January")
  setSelect(driver, "id_timestart_year", "2025")
  setSelect(driver, "id_timestart_hour", "00")
  setSelect(driver, "id_timestart_minute", "00")

  setSelect(driver, "id_eventtype", "Course")
  
  driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/form/fieldset/div[2]/div[4]/div[2]/div[3]/span").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/form/fieldset/div[2]/div[4]/div[2]/ul/li[1]").click()
  time.sleep(2)
  

  saveEventBtn.click()
  time.sleep(2)

  modalEle = driver.find_element(By.CLASS_NAME, "modal")
  assert not modalEle.is_displayed()

  driver.quit()

def test_uc4():
  driver = webdriver.Chrome()

  wait = WebDriverWait(driver, 10)

  login(driver, "teacher", "moodle")

  driver.get("https://school.moodledemo.net/my/index.php")

  driver.implicitly_wait(2)
  newEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='new-event-button']")))

  newEventBtn.click()

  eventNameInput = driver.find_element(By.ID, "id_name")
  saveEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='save']")))

  setValueById(driver, "id_name", "Test Event")
  setSelect(driver, "id_timestart_day", "12")
  setSelect(driver, "id_timestart_month", "January")
  setSelect(driver, "id_timestart_year", "2025")
  setSelect(driver, "id_timestart_hour", "00")
  setSelect(driver, "id_timestart_minute", "00")

  setSelect(driver, "id_eventtype", "Group")
  
  driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/form/fieldset/div[2]/div[5]/div[2]/div[3]/span").click()
  time.sleep(2)
  driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/form/fieldset/div[2]/div[5]/div[2]/ul/li[1]").click()
  time.sleep(2)

  saveEventBtn.click()
  time.sleep(2)

  modalEle = driver.find_element(By.CLASS_NAME, "modal")
  assert not modalEle.is_displayed()

  driver.quit()