
from selenium.webdriver.common.by import By

def login(driver, username, password):
    driver.get("https://school.moodledemo.net/login/index.php")

    driver.implicitly_wait(0.5)

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys(username)
    password_input.send_keys(password)

    driver.find_element(By.ID, "loginbtn").click()

    driver.implicitly_wait(0.5)
