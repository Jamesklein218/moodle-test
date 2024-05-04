from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


def reset_upload_form(driver: webdriver.Chrome):
    Select(driver.find_element(By.ID, "id_userfield")).select_by_visible_text(
        "username"
    )

    Select(driver.find_element(By.ID, "id_overwritepicture")).select_by_visible_text(
        "No"
    )


def upload_user_pictures(driver: webdriver.Chrome, file_name: str):
    WebDriverWait(driver, 30).until(
        lambda driver: check_finished_loading_file_chooser(driver)
    )

    driver.find_element(By.NAME, "userpicturesfilechoose").click()

    WebDriverWait(driver, 30).until(
        lambda driver: driver.find_element(By.NAME, "repo_upload_file")
    )

    driver.find_element(By.NAME, "repo_upload_file").send_keys(file_name)

    driver.find_element(By.XPATH, '//button[text()="Upload this file"]').click()


def check_finished_loading_file_chooser(driver: webdriver.Chrome):
    filechooser = driver.find_element(By.CLASS_NAME, "filemanager-loading")

    return filechooser.value_of_css_property("display") == "none"


def check_changed_page(driver: webdriver.Chrome):
    return driver.find_element(By.XPATH, '//div[contains(text(), "Users updated:")]')


def count_users_updated(driver: webdriver.Chrome):
    alert = driver.find_element(By.XPATH, '//div[contains(text(), "Users updated:")]')
    link_text = alert.find_element(By.TAG_NAME, "button").text
    alert_text = alert.text[: -len(link_text)]
    return int(alert_text.strip()[15:])


def count_errors(driver: webdriver.Chrome):
    alert = driver.find_element(By.XPATH, '//div[contains(text(), "Errors:")]')
    link_text = alert.find_element(By.TAG_NAME, "button").text
    alert_text = alert.text[: -len(link_text)]
    return int(alert_text.strip()[8:])
