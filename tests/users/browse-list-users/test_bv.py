from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from utils.auth import login
from helpers import reset_filter_form


def test_009_007():
    """Boundary value testing: Search with no filter"""
    driver = webdriver.Chrome()

    login(driver, "manager", "moodle")
    driver.get("https://school.moodledemo.net/admin/user.php")

    driver.find_element(By.ID, "dropdownFiltersButton").click()
    reset_filter_form(driver)

    driver.find_element(By.NAME, "submitbutton").click()

    WebDriverWait(driver, 5).until(
        lambda driver: driver.find_element(By.CLASS_NAME, "toast-body")
    )

    # Find a tbody element in page
    all_rows = driver.find_elements(By.XPATH, "//tbody//tr")

    non_empty_rows = [
        row for row in all_rows if "emptyrow" not in row.get_attribute("class")
    ]

    assert len(non_empty_rows) > 0


def test_009_008():
    """Boundary value testing: Last name filter - nominal value"""
    driver = webdriver.Chrome()

    login(driver, "manager", "moodle")
    driver.get("https://school.moodledemo.net/admin/user.php")

    driver.find_element(By.ID, "dropdownFiltersButton").click()
    reset_filter_form(driver)

    Select(
        driver.find_element(By.NAME, "user:lastname_operator")
    ).select_by_visible_text("Contains")

    ends_with_input = driver.find_element(By.NAME, "user:lastname_value")
    ends_with_input.clear()
    ends_with_input.send_keys("Hill")
    ends_with_input.send_keys(Keys.ENTER)

    WebDriverWait(driver, 5).until(
        lambda driver: driver.find_element(By.CLASS_NAME, "toast-body")
    )

    # Find a tbody element in page
    all_rows = driver.find_elements(By.XPATH, "//tbody//tr")

    non_empty_rows = [
        row for row in all_rows if "emptyrow" not in row.get_attribute("class")
    ]

    for row in non_empty_rows:
        cell_c1 = row.find_element(By.CLASS_NAME, "c1")
        user_name_link = cell_c1.find_element(By.XPATH, ".//a")
        assert user_name_link.text.lower().endswith("hill")


def test_009_009():
    """Boundary value testing: First name filter - nominal value"""
    driver = webdriver.Chrome()

    login(driver, "manager", "moodle")
    driver.get("https://school.moodledemo.net/admin/user.php")

    driver.find_element(By.ID, "dropdownFiltersButton").click()
    reset_filter_form(driver)

    first_name_select = Select(driver.find_element(By.NAME, "user:firstname_operator"))
    first_name_select.select_by_visible_text("Contains")

    contains_input = driver.find_element(By.NAME, "user:firstname_value")
    contains_input.clear()
    contains_input.send_keys("Alice")
    contains_input.send_keys(Keys.ENTER)

    WebDriverWait(driver, 5).until(
        lambda driver: driver.find_element(By.CLASS_NAME, "toast-body")
    )

    # Find a tbody element in page
    all_rows = driver.find_elements(By.XPATH, "//tbody//tr")

    non_empty_rows = [
        row for row in all_rows if "emptyrow" not in row.get_attribute("class")
    ]

    for row in non_empty_rows:
        cell_c1 = row.find_element(By.CLASS_NAME, "c1")
        user_name_link = cell_c1.find_element(By.XPATH, ".//a")
        assert "alice" in user_name_link.text.lower()
