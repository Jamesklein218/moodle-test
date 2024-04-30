
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

def test_uc2_and_uc3():
    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")

    driver.get("https://school.moodledemo.net/course/view.php?id=59")

    is_properly_setup = WebDriverWait(driver, 5).until(
        lambda driver: 
            len(list(filter(lambda x: x.get_attribute('innerText') and "Hidden from students" in str(x.get_attribute('innerText')), driver.find_elements(By.CSS_SELECTOR, "button[id^='dropwdownbutton']")))) == 0)

    assert is_properly_setup

    # Use case 2
    enable_edit_mode(driver)

    WebDriverWait(driver, 5).until(lambda driver: driver.find_element(By.CLASS_NAME, 'bulkEnable')).click()

    checkboxes = WebDriverWait(driver, 5).until(lambda driver:driver.find_elements(By.CSS_SELECTOR, "input[id^='cmCheckbox'][type='checkbox']"))

    assert len(checkboxes) > 5

    for box in checkboxes[:5]:
        driver.execute_script(f"document.getElementById(\"{box.get_attribute('id')}\").click()")

    driver.execute_script(f"document.querySelector(\"button[title='Activity availability']\").click()")

    modal = WebDriverWait(driver, 5).until(lambda driver:driver.find_element(By.CLASS_NAME, 'modal'))

    assert modal != None

    hide_radio = WebDriverWait(modal, 1).until(lambda modal: modal.find_element(By.ID, 'hideRadio'))

    modal_footer = driver.find_element(By.CLASS_NAME, 'modal-footer')

    WebDriverWait(modal_footer, 5).until(lambda modal_footer:modal_footer.find_elements(By.TAG_NAME, 'button')[1].get_attribute('disabled'))

    hide_radio.click()

    driver.find_element(By.CLASS_NAME, 'modal-footer').find_elements(By.TAG_NAME, 'button')[1].click()

    res = WebDriverWait(driver, 5).until(
        lambda driver: 
            len(list(filter(lambda x: x.get_attribute('innerText') and "Hidden from students" in str(x.get_attribute('innerText')), driver.find_elements(By.CSS_SELECTOR, "button[id^='dropwdownbutton']")))) == 5)

    assert res

    # Use case 3
    checkboxes_1 = WebDriverWait(driver, 5).until(lambda driver:driver.find_elements(By.CSS_SELECTOR, "input[id^='cmCheckbox'][type='checkbox']"))

    assert len(checkboxes_1) > 5

    for box in checkboxes_1[:5]:
        driver.execute_script(f"document.getElementById(\"{box.get_attribute('id')}\").click()")

    driver.execute_script(f"document.querySelector(\"button[title='Activity availability']\").click()")

    modal = WebDriverWait(driver, 10).until(lambda driver:driver.find_element(By.CLASS_NAME, 'modal'))

    assert modal != None

    show_radio = WebDriverWait(modal, 2).until(lambda modal: modal.find_element(By.ID, 'showRadio'))

    modal_footer = driver.find_element(By.CLASS_NAME, 'modal-footer')

    WebDriverWait(modal_footer, 10).until(lambda modal_footer:modal_footer.find_elements(By.TAG_NAME, 'button')[1].get_attribute('disabled'))

    show_radio.click()

    driver.find_element(By.CLASS_NAME, 'modal-footer').find_elements(By.TAG_NAME, 'button')[1].click()

    res = WebDriverWait(driver, 10).until(
        lambda driver: 
            len(list(filter(lambda x: x.get_attribute('innerText') and "Hidden from students" in str(x.get_attribute('innerText')), driver.find_elements(By.CSS_SELECTOR, "button[id^='dropwdownbutton']")))) == 0)

    assert res

    driver.quit()

