from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.auth import login
from utils.core import enable_edit_mode

import time
import unittest

options = Options()
options.add_experimental_option("detach", True)
def test_bd1():  
    driver = webdriver.Chrome()
    login(driver, "manager", "moodle")

    driver.get("https://school.moodledemo.net/mod/page/view.php?id=47")
    add_user_link = driver.find_element(By.XPATH, '//a[text()="Add a new user"]')
    # add_user_link = driver.find_element(By.XPATH, '//a[@href="http://school.moodledemo.net/user/editadvanced.php?id=-1"]')
    add_user_link.click()

    time.sleep(100)
class AddNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        login(self.driver, "teacher", "moodle")
        self.driver.get("https://school.moodledemo.net/mod/page/view.php?id=47")
        self.addNewUser()

        self.driver.quit
    def addNewUser(self):
        add_user_link = self.driver.find_element(By.XPATH, '//a[text()="Add a new user"]')
        add_user_link.click()


if __name__=='__main__':
    unittest.main()


