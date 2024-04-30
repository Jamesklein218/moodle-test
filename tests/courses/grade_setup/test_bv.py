
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.auth import login

def test_bv1():
    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")

    driver.get("https://school.moodledemo.net/grade/edit/tree/index.php?id=59")

    driver.quit()
