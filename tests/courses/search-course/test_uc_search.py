from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from utils.auth import login
import time
        
def test_uc1():
    driver = webdriver.Chrome() 
    login(driver, "student", "moodle")
    driver.get("https://school.moodledemo.net/my/courses.php")
    driver.implicitly_wait(5)

    input_search = driver.find_element(By.XPATH, '//input[@name="search"]')
    input_search.click()
   
    assert input_search.value_of_css_property("box-shadow") != "none"

    input_search.send_keys(Keys.RETURN)
    time.sleep(1)

    check = driver.find_element(By.XPATH, '//button[@data-action="clearsearch"]')
    assert check.get_attribute("class") == "btn btn-clear d-none"

    driver.quit()

def test_uc2():
    driver = webdriver.Chrome()
    login(driver, "student", "moodle")
    driver.get("https://school.moodledemo.net/my/courses.php")
    driver.implicitly_wait(5)

    input_search = driver.find_element(By.XPATH, '//input[@name="search"]')
    input_search.click()
   
    assert input_search.value_of_css_property("box-shadow") != "none"

    input_search.send_keys("Moodle" + Keys.ENTER)
    time.sleep(1)

    check = driver.find_element(By.XPATH, '//button[@data-action="clearsearch"]')
    assert check.get_attribute("class") != "btn btn-clear d-none"

    try:
        driver.find_element(By.XPATH, '//div[@data-region="card-deck"]')
        assert True
    except:
        assert False
    
    driver.quit()

def test_uc3():
    driver = webdriver.Chrome()
    login(driver, "student", "moodle")
    driver.get("https://school.moodledemo.net/my/courses.php")
    driver.implicitly_wait(5)

    input_search = driver.find_element(By.XPATH, '//input[@name="search"]')
    input_search.click()
   
    assert input_search.value_of_css_property("box-shadow") != "none"

    input_search.send_keys(" " + Keys.ENTER)
    time.sleep(1)

    check = driver.find_element(By.XPATH, '//button[@data-action="clearsearch"]')
    assert check.get_attribute("class") != "btn btn-clear d-none"

    try:
        res = driver.find_element(By.XPATH, '//div[@data-region="empty-message"]/p')
        assert res.text == "No courses"
    except:
        assert False
    
    driver.quit()