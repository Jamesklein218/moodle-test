from selenium import webdriver
from selenium.webdriver.common.by import By
from utils.auth import login
import pytest

max = 0
def genTest():
    driver = webdriver.Chrome()
    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/mod/assign/view.php?id=652&action=grader&userid=48")
    driver.implicitly_wait(5)

    setup = driver.find_element(By.XPATH, '//label[@for="id_grade"]').text
    global max
    max = int(setup.split("of")[1].strip())
    driver.quit()
    return [-1, 0 , max // 2, max, max + 1]


test_data = genTest()
@pytest.mark.parametrize("grade", test_data)
def test_bv(grade):
    driver = webdriver.Chrome()
    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/mod/assign/view.php?id=652&action=grader&userid=48")
    driver.implicitly_wait(5)

    grade_input = driver.find_element(By.ID, "id_grade")
    grade_input.click()
    grade_input.clear()
    grade_input.send_keys(str(grade))

    global max
    
    driver.find_element(By.NAME, "savechanges").click()
    driver.implicitly_wait(3)

    if grade < 0:
        assert driver.find_element(By.XPATH, '//div[@id="id_error_grade" and @style="display: block;"]').text == "Grade must be greater than or equal to zero."
    elif grade > max:
        assert driver.find_element(By.XPATH, '//div[@id="id_error_grade" and @style="display: block;"]').text == f"Grade must be less than or equal to {max}."
    else:
        try:
            driver.find_element(By.XPATH, '//div[@id="id_error_grade" and @style="display: block;"]')
            assert False
        except:
            assert True

    driver.quit()