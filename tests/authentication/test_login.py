
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.auth import login

def test_auth_student():
    driver = webdriver.Chrome()

    login(driver, "student", "moodle")

    driver.get("https://school.moodledemo.net/user/edit.php")

    id_input = driver.find_element(By.ID, "id_email")

    assert id_input.get_attribute("value") == "barbaragardner249@example.com" # Student Role

    driver.quit()

def test_auth_teacher():
    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")

    driver.get("https://school.moodledemo.net/user/edit.php")

    id_input = driver.find_element(By.ID, "id_email")

    assert id_input.get_attribute("value") == "jeffreysanders199@example.com"

    driver.quit()

def test_auth_manager():
    driver = webdriver.Chrome()

    login(driver, "manager", "moodle")

    driver.get("https://school.moodledemo.net/user/editadvanced.php")

    id_input = driver.find_element(By.ID, "id_email")

    assert id_input.get_attribute("value") == "annaalexand246@example.com"

    driver.quit()

def test_auth_parent():
    driver = webdriver.Chrome()

    login(driver, "parent", "moodle")

    driver.get("https://school.moodledemo.net/user/edit.php")

    id_input = driver.find_element(By.ID, "id_email")

    assert id_input.get_attribute("value") == "joycegardner144@example.com"

    driver.quit()

def test_auth_privacyofficer():
    driver = webdriver.Chrome()

    login(driver, "privacyofficer", "moodle")

    driver.get("https://school.moodledemo.net/user/profile.php")

    try:
        element = driver.find_element(By.XPATH, "//*[text()[contains(., 'privacyofficer@example.com')]]")
    except Exception:
        element = None

    assert element != None

    driver.quit()

