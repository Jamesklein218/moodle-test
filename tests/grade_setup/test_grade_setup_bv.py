
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_grade_setup_bv1():
    driver = webdriver.Chrome()

    driver.get("https://school.moodledemo.net/login/index.php")

    title = driver.title
    assert title == "Log in to the site | Mount Orange School"

    driver.implicitly_wait(0.5)

    # text_box = driver.find_element(by=By.NAME, value="my-text")
    # submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
    #
    # text_box.send_keys("Selenium")
    # submit_button.click()
    #
    # message = driver.find_element(by=By.ID, value="message")
    # value = message.text
    # assert value == "Received!"

    driver.quit()
