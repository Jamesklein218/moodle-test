
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.auth import login
from utils.core import enable_edit_mode

import time

def test_uc1():
    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")

    driver.get("https://school.moodledemo.net/course/view.php?id=59")

    enable_edit_mode(driver)

    driver.find_element(By.CLASS_NAME, 'bulkEnable').click()

    first_checkbox = WebDriverWait(driver, 5).until(lambda driver:driver.find_element(By.CSS_SELECTOR, "input[id^='cmCheckbox'][type='checkbox']"))
    first_checkbox.click()

    # https://stackoverflow.com/questions/11908249/debugging-element-is-not-clickable-at-point-error
    driver.execute_script("document.querySelector(\"#selectall\").click()")
    # WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, 'selectall')))
    # driver.find_element(By.ID, 'selectall').click()

    bulk_select_inputs_after = driver.find_elements(By.CSS_SELECTOR, ".bulkselect input[id^='cmCheckbox'][type='checkbox']")

    for bulk_select_input in bulk_select_inputs_after:
        assert bulk_select_input.get_attribute("checked") == "true"

    driver.quit()

