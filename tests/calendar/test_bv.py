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

def test_bv1():
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    login(driver, "teacher", "moodle")

    driver.get("https://school.moodledemo.net/my/index.php")

    driver.implicitly_wait(2)
    newEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='new-event-button']")))

    newEventBtn.click()

    saveEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='save']")))

    saveEventBtn.click()

    eventNameErrorMsg = driver.find_element(By.ID, "id_error_name")
    assert eventNameErrorMsg.is_displayed() 

    driver.quit()

def test_bv2():
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
    setSelect(driver, "id_timestart_day", "1")
    setSelect(driver, "id_timestart_month", "January")
    setSelect(driver, "id_timestart_year", "2020")
    setSelect(driver, "id_timestart_hour", "00")
    setSelect(driver, "id_timestart_minute", "00")
    driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
    driver.find_element(By.ID, "id_duration_2").click()
    setValueById(driver, "id_timedurationminutes", "0")

    saveEventBtn.click()
    time.sleep(5)

    durationErrorMsg = driver.find_element(By.ID, "fgroup_id_error_durationgroup")
    assert durationErrorMsg.is_displayed() 

    driver.quit()

def test_bv3():
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
    setSelect(driver, "id_timestart_day", "1")
    setSelect(driver, "id_timestart_month", "January")
    setSelect(driver, "id_timestart_year", "2020")
    setSelect(driver, "id_timestart_hour", "00")
    setSelect(driver, "id_timestart_minute", "00")

    driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
    driver.find_element(By.ID, "id_duration_1").click()
    setSelect(driver, "id_timedurationuntil_day", "1")
    setSelect(driver, "id_timedurationuntil_month", "January")
    setSelect(driver, "id_timedurationuntil_year", "2020")
    setSelect(driver, "id_timedurationuntil_hour", "00")
    setSelect(driver, "id_timedurationuntil_minute", "00")

    saveEventBtn.click()
    time.sleep(5)

    durationErrorMsg = driver.find_element(By.ID, "fgroup_id_error_durationgroup")
    assert durationErrorMsg.is_displayed() 

    driver.quit()

# def test_bv3():
#     driver = webdriver.Chrome()

#     wait = WebDriverWait(driver, 10)

#     login(driver, "teacher", "moodle")

#     driver.get("https://school.moodledemo.net/my/index.php")

#     driver.implicitly_wait(2)
#     newEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='new-event-button']")))

#     newEventBtn.click()

#     eventNameInput = driver.find_element(By.ID, "id_name")
#     saveEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='save']")))

#     setValueById(driver, "id_name", "Test Event")
#     setSelect(driver, "id_timestart_day", "1")
#     setSelect(driver, "id_timestart_month", "January")
#     setSelect(driver, "id_timestart_year", "2020")
#     setSelect(driver, "id_timestart_hour", "00")
#     setSelect(driver, "id_timestart_minute", "00")

#     driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
#     driver.find_element(By.ID, "id_duration_1").click()
#     setSelect(driver, "id_timedurationuntil_day", "1")
#     setSelect(driver, "id_timedurationuntil_month", "January")
#     setSelect(driver, "id_timedurationuntil_year", "2020")
#     setSelect(driver, "id_timedurationuntil_hour", "00")
#     setSelect(driver, "id_timedurationuntil_minute", "00")

#     saveEventBtn.click()
#     time.sleep(1)

#     eventNameErrorMsg = driver.find_element(By.ID, "fgroup_id_error_durationgroup")
#     assert eventNameErrorMsg.is_displayed() 

#     driver.quit()

def test_bv4():
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
    setSelect(driver, "id_timestart_day", "1")
    setSelect(driver, "id_timestart_month", "January")
    setSelect(driver, "id_timestart_year", "2020")
    setSelect(driver, "id_timestart_hour", "00")
    setSelect(driver, "id_timestart_minute", "00")

    driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
    driver.find_element(By.ID, "id_duration_1").click()
    setSelect(driver, "id_timedurationuntil_day", "31")
    setSelect(driver, "id_timedurationuntil_month", "December")
    setSelect(driver, "id_timedurationuntil_year", "2019")
    setSelect(driver, "id_timedurationuntil_hour", "23")
    setSelect(driver, "id_timedurationuntil_minute", "59")

    saveEventBtn.click()
    wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button[data-action='save'] > span[data-region='loading-icon-container']")))
    time.sleep(3) # Has to wait for a while due to the lack of UI synchronization of the website

    durationErrorMsg = driver.find_element(By.ID, "fgroup_id_error_durationgroup")
    assert durationErrorMsg.is_displayed() 

    driver.quit()
    
def test_bv5():
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

test_data = readDataFromExcel("calendar_bva")
@pytest.mark.parametrize("startDate,endDate,isValid", test_data)
def test_bv6(startDate, endDate, isValid):
    start_time = parseDate(startDate)
    end_time = parseDate(endDate)
    
    driver = webdriver.Chrome()

    wait = WebDriverWait(driver, 10)

    login(driver, "teacher", "moodle")

    driver.get("https://school.moodledemo.net/my/index.php")

    driver.implicitly_wait(2)
    newEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='new-event-button']")))

    newEventBtn.click()

    saveEventBtn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-action='save']")))
    setValueById(driver, "id_name", "Test Event")
    driver.find_element(By.CLASS_NAME, "moreless-toggler").click()
    driver.implicitly_wait(2)
    driver.find_element(By.ID, "id_duration_1").click()

    setSelect(driver, "id_timestart_day", start_time[0])
    setSelect(driver, "id_timestart_month", start_time[1])
    setSelect(driver, "id_timestart_year", start_time[2])
    setSelect(driver, "id_timestart_hour", start_time[3])
    setSelect(driver, "id_timestart_minute", start_time[4])

    setSelect(driver, "id_timedurationuntil_day", end_time[0])
    setSelect(driver, "id_timedurationuntil_month", end_time[1])
    setSelect(driver, "id_timedurationuntil_year", end_time[2])
    setSelect(driver, "id_timedurationuntil_hour", end_time[3])
    setSelect(driver, "id_timedurationuntil_minute", end_time[4])


    if (isValid == 'N'):
        saveEventBtn.click()
        wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR, "button[data-action='save'] > span[data-region='loading-icon-container']")))
        time.sleep(5) # Has to wait for a while due to the lack of UI synchronization of the website

        durationErrorMsg = driver.find_element(By.ID, "fgroup_id_error_durationgroup")
        assert durationErrorMsg.is_displayed() 
    else:
        saveEventBtn.click()
        time.sleep(5)

        modalEle = driver.find_element(By.CLASS_NAME, "modal")
        assert not modalEle.is_displayed()

    driver.quit()