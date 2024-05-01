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

test_data = readDataFromExcel("calendar_eq")
@pytest.mark.parametrize("startDate,endDate,isValid", test_data)
def test_eq1(startDate, endDate, isValid):
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