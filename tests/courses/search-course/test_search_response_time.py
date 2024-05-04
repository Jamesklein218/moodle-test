from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.auth import login
import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.readData import readDataFromExcel


test_data = readDataFromExcel("Response-Search")
@pytest.mark.parametrize("query, have_result", test_data)
def test_response_time(query, have_result):
    driver = webdriver.Chrome()
    login(driver, "student", "moodle")
    driver.get("https://school.moodledemo.net/my/courses.php")
    driver.implicitly_wait(10)

    # wait course fully loaded
    driver.find_element(By.XPATH, '//div[@data-region="card-deck"]')
    time.sleep(4)

    input_search = driver.find_element(By.XPATH, '//input[@name="search"]')
    input_search.send_keys(query + Keys.ENTER)

    # wait for loading circle to disappear
    loading_circle = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/section/div/aside/section/div/div/div[1]/div[2]/div/div/div[1]/span')
    WebDriverWait(driver, 2).until(EC.invisibility_of_element(loading_circle))

    driver.implicitly_wait(0)
    if have_result == "no":
        try:
            res = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/section/div/aside/section/div/div/div[1]/div[2]/div/div/div[1]/div/div/p')
            assert res.text == "No courses"
        except:
            assert False
    else:
        try:
            driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div/section/div/aside/section/div/div/div[1]/div[2]/div/div/div[1]/div/div[@data-region="card-deck"]')
            assert True
        except:
            assert False
    driver.quit()