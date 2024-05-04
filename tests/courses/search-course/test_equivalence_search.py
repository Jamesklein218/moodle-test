from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.auth import login
import time
import pytest
from utils.readData import readDataFromExcel

test_data = readDataFromExcel("Search")
@pytest.mark.parametrize("query, have_result", test_data)
def test_equivalence_1(query , have_result):
    driver = webdriver.Chrome() 
    login(driver, "student", "moodle")
    driver.get("https://school.moodledemo.net/my/courses.php")
    driver.implicitly_wait(5)

    input_search = driver.find_element(By.XPATH, '//input[@name="search"]')
    input_search.click()
    input_search.send_keys(query + Keys.ENTER)
    time.sleep(1)

    if have_result == "yes":
        try:
            driver.find_element(By.XPATH, '//div[@data-region="card-deck"]')
            assert True
        except:
            assert False
    else:
        try:
            res = driver.find_element(By.XPATH, '//div[@data-region="empty-message"]/p')
            assert res.text == "No courses"
        except:
            assert False        
    driver.quit()
        

