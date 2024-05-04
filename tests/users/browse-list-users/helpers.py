from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def reset_filter_form(driver: webdriver.Chrome):
    fields_to_clear = [
        "user:firstname_operator",
        "user:lastname_operator",
        "user:timecreated_operator",
        "user:lastaccess_operator",
        "user:timemodified_operator",
    ]

    for field_name in fields_to_clear:
        Select(driver.find_element(By.NAME, field_name)).select_by_visible_text(
            "Is any value"
        )
