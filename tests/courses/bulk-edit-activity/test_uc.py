
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.auth import login
from utils.core import enable_edit_mode

import time

def test_uc1():
    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")

    driver.get("https://school.moodledemo.net/course/view.php?id=59")

    enable_edit_mode(driver)

    driver.find_element(By.CLASS_NAME, 'bulkEnable').click()

    driver.implicitly_wait(5)

    bulk_select_inputs = driver.find_elements(By.CSS_SELECTOR, "input[id^='cmCheckbox'][type='checkbox']")

    assert len(bulk_select_inputs) > 0

    bulk_select_inputs[0].click()

    selectall_btn = driver.find_element(By.ID, "selectall")

    assert selectall_btn.get_attribute("disabled") == None

    time.sleep(1)

    selectall_btn.click()

    # bulk_select_inputs_after = driver.find_elements(By.CSS_SELECTOR, ".bulkselect input[id^='cmCheckbox'][type='checkbox']")
    #
    # for bulk_select_input in bulk_select_inputs_after:
    #     assert bulk_select_input.get_attribute("checked") == "true"

    driver.quit()

