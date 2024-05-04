from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.auth import login
from utils.core import enable_edit_mode

from parameterized import parameterized
import utils.readData as readData
import time
import unittest

# @parameterized.expand(readData.readDataFromExcel("AddNewUser"))
@parameterized.expand(readData.readDataFromExcel("AddNewUser"))
def test_uc(username, password, fname, lname, email, res):  
    driver = webdriver.Chrome()
    login(driver, "manager", "moodle")

    driver.get("https://school.moodledemo.net/mod/page/view.php?id=47")
    add_user_link = driver.find_element(By.XPATH, '//a[text()="Add a new user"]')
    add_user_link.click()
    username_input = driver.find_element(By.XPATH, '//*[@id="id_username"]')
    #input password
    password_btn = driver.find_element(By.XPATH, "//div[@id='fitem_id_newpassword']/div[2]/div/div/a/span/span/em")

    # password_btn.click()
    password_input = driver.find_element(By.XPATH, '//*[@id="id_newpassword"]')
    fname_input = driver.find_element(By.ID, "id_firstname")
    lname_input = driver.find_element(By.ID, "id_lastname")
    email_input = driver.find_element(By.ID,"id_email") 

    submit_btn = driver.find_element(By.ID,"id_submitbutton")


    username_input.send_keys(username)
    time.sleep(5)
    password_btn.click()
    password_input.send_keys(password)
    time.sleep(5)
    fname_input.send_keys(fname)
    time.sleep(5)
    lname_input.send_keys(lname)
    time.sleep(5)
    email_input.send_keys(email)
    time.sleep(5)

    submit_btn.click()
    time.sleep(5)

    if res == "Changes saved":
        result = res    
    elif username == "":
        result = driver.find_element(By.ID, "id_error_username")
        print (result.text)
    elif password == "":
        result = driver.find_element(By.ID, "id_error_newpassword")
        print (result.text)
    elif fname == "":
        result = driver.find_element(By.ID, "id_error_firstname")
        print (result.text)
    elif lname == "":
        result = driver.find_element(By.ID, "id_error_lastname")
        print (result.text)
    elif res == "Invalid email address":
        result = driver.find_element(By.ID, "id_error_email")

    
    time.sleep(5)
    if res != "Changes saved":
        assert result.text == res
        
    time.sleep(15)
    driver.quit()
# class AddNewUser(unittest.TestCase):
#     def setUp(self):
#         self.driver = webdriver.Chrome()
#         self.driver.implicitly_wait(30)
#         self.driver.maximize_window()
#         login(self.driver, "teacher", "moodle")
#         self.driver.get("https://school.moodledemo.net/mod/page/view.php?id=47")
#         self.addNewUser()

#         self.driver.quit
#     def addNewUser(self):
#         add_user_link = self.driver.find_element(By.XPATH, '//a[text()="Add a new user"]')
#         add_user_link.click()


# if __name__=='__main__':
#     unittest.main()


