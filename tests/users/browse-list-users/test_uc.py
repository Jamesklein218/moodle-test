from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from utils.auth import login
from helpers import reset_filter_form


def test_009_001():
    """Use case testing: Browse list of users using the "contains" filter"""
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


def test_009_002():
    """Use case testing: Browse list of users using the "doesn't contain" filter"""
    driver = webdriver.Chrome()

    login(driver, "manager", "moodle")
    driver.get("https://school.moodledemo.net/admin/user.php")

    driver.find_element(By.ID, "dropdownFiltersButton").click()
    reset_filter_form(driver)

    first_name_select = Select(driver.find_element(By.NAME, "user:firstname_operator"))
    first_name_select.select_by_visible_text("Does not contain")

    not_contain_input = driver.find_element(By.NAME, "user:firstname_value")
    not_contain_input.clear()
    not_contain_input.send_keys("Alice")
    not_contain_input.send_keys(Keys.ENTER)

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
        assert "alice" not in user_name_link.text.lower()


def test_009_003():
    """Use case testing: Browse list of users using the "is equal to" filter"""
    driver = webdriver.Chrome()

    login(driver, "manager", "moodle")
    driver.get("https://school.moodledemo.net/admin/user.php")

    driver.find_element(By.ID, "dropdownFiltersButton").click()
    reset_filter_form(driver)

    first_name_select = Select(driver.find_element(By.NAME, "user:firstname_operator"))
    first_name_select.select_by_visible_text("Is equal to")

    is_eq_input = driver.find_element(By.NAME, "user:firstname_value")
    is_eq_input.clear()
    is_eq_input.send_keys("Brian Franklin")
    is_eq_input.send_keys(Keys.ENTER)

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
        assert "Brian Franklin" == user_name_link.text


def test_009_004():
    """Use case testing: Browse list of users using the "starts with" filter"""
    driver = webdriver.Chrome()

    login(driver, "manager", "moodle")
    driver.get("https://school.moodledemo.net/admin/user.php")

    driver.find_element(By.ID, "dropdownFiltersButton").click()
    reset_filter_form(driver)

    first_name_select = Select(driver.find_element(By.NAME, "user:firstname_operator"))
    first_name_select.select_by_visible_text("Starts with")

    starts_with_input = driver.find_element(By.NAME, "user:firstname_value")
    starts_with_input.clear()
    starts_with_input.send_keys("amy")
    starts_with_input.send_keys(Keys.ENTER)

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
        assert user_name_link.text.lower().startswith("amy")


def test_009_005():
    """Use case testing: Browse list of users using the "ends with" filter"""
    driver = webdriver.Chrome()

    login(driver, "manager", "moodle")
    driver.get("https://school.moodledemo.net/admin/user.php")

    driver.find_element(By.ID, "dropdownFiltersButton").click()
    reset_filter_form(driver)

    first_name_select = Select(driver.find_element(By.NAME, "user:lastname_operator"))
    first_name_select.select_by_visible_text("Starts with")

    ends_with_input = driver.find_element(By.NAME, "user:lastname_value")
    ends_with_input.clear()
    ends_with_input.send_keys("griffin")
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
        assert user_name_link.text.lower().endswith("griffin")


def test_009_006():
    """Use case testing: Browse list of users using the "is empty" filter"""
    driver = webdriver.Chrome()

    login(driver, "manager", "moodle")
    driver.get("https://school.moodledemo.net/admin/user.php")

    driver.find_element(By.ID, "dropdownFiltersButton").click()
    reset_filter_form(driver)

    first_name_select = Select(driver.find_element(By.NAME, "user:firstname_operator"))
    first_name_select.select_by_visible_text("Is empty")

    driver.find_element(By.NAME, "submitbutton").click()

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
        assert " " not in user_name_link.text.strip()
