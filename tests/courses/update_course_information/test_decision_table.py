from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from utils.auth import login


def test_011_001():
    """Name empty, short name empty, category empty"""

    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/course/edit.php?id=51")

    # Find input element for full name
    full_name_input = driver.find_element(By.ID, "id_fullname")
    full_name_input.clear()

    # Find input element for short name
    short_name_input = driver.find_element(By.ID, "id_shortname")
    short_name_input.clear()

    # Find category select element
    course_category_row = driver.find_element(By.ID, "fitem_id_category")
    # Find all spans within the row with role='option'
    chosen_categories = course_category_row.find_elements(
        By.XPATH, ".//span[@role='option']"
    )
    for category in chosen_categories:
        category.click()

    category_select = course_category_row.find_element(By.ID, "id_category")

    # Find input element with type 'submit'
    submit_btn = driver.find_element(By.NAME, "saveanddisplay")
    submit_btn.click()

    assert "is-invalid" in full_name_input.get_attribute("class")
    assert "is-invalid" in short_name_input.get_attribute("class")
    assert "is-invalid" in category_select.get_attribute("class")


def test_011_002():
    """Name empty, short name empty, category non-empty"""

    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/course/edit.php?id=51")

    # Find input element for full name
    full_name_input = driver.find_element(By.ID, "id_fullname")
    full_name_input.clear()

    # Find input element for short name
    short_name_input = driver.find_element(By.ID, "id_shortname")
    short_name_input.clear()

    # Find an 'ul' with class 'form-autocomplete-suggestions' and click on any 'li' that has non-empty text
    category_row = driver.find_element(By.ID, "fitem_id_category")
    category_row.find_element(
        By.CSS_SELECTOR, "span.form-autocomplete-downarrow"
    ).click()
    category_dropdown = category_row.find_element(
        By.CSS_SELECTOR, "ul.form-autocomplete-suggestions"
    )
    category_options = category_dropdown.find_elements(By.TAG_NAME, "li")

    for category in category_options:
        if category.text.strip():
            category.click()
            break

    category_select = driver.find_element(By.ID, "id_category")

    # Click on save & display button
    submit_btn = driver.find_element(By.NAME, "saveanddisplay")
    submit_btn.click()

    assert "is-invalid" in full_name_input.get_attribute("class")
    assert "is-invalid" in short_name_input.get_attribute("class")
    assert "is-invalid" not in category_select.get_attribute("class")


def test_011_003():
    """Name empty, short name non-empty, category empty"""

    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/course/edit.php?id=51")

    # Find input element for full name
    full_name_input = driver.find_element(By.ID, "id_fullname")
    full_name_input.clear()

    # Find input element for short name
    short_name_input = driver.find_element(By.ID, "id_shortname")
    short_name_input.clear()
    short_name_input.send_keys("A short name for this course")

    # Find category select element
    course_category_row = driver.find_element(By.ID, "fitem_id_category")
    # Find all spans within the row with role='option'
    chosen_categories = course_category_row.find_elements(
        By.XPATH, ".//span[@role='option']"
    )
    for category in chosen_categories:
        category.click()

    category_select = course_category_row.find_element(By.ID, "id_category")

    # Find input element with type 'submit'
    submit_btn = driver.find_element(By.NAME, "saveanddisplay")
    submit_btn.click()

    assert "is-invalid" in full_name_input.get_attribute("class")
    assert "is-invalid" not in short_name_input.get_attribute("class")
    assert "is-invalid" in category_select.get_attribute("class")


def test_011_004():
    """Name empty, short name non-empty, category non-empty"""

    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/course/edit.php?id=51")

    # Find input element for full name
    full_name_input = driver.find_element(By.ID, "id_fullname")
    full_name_input.clear()

    # Find input element for short name
    short_name_input = driver.find_element(By.ID, "id_shortname")
    short_name_input.clear()
    short_name_input.send_keys("A short name for this course")

    # Find an 'ul' with class 'form-autocomplete-suggestions' and click on any 'li' that has non-empty text
    category_row = driver.find_element(By.ID, "fitem_id_category")
    category_row.find_element(
        By.CSS_SELECTOR, "span.form-autocomplete-downarrow"
    ).click()
    category_dropdown = category_row.find_element(
        By.CSS_SELECTOR, "ul.form-autocomplete-suggestions"
    )
    category_options = category_dropdown.find_elements(By.TAG_NAME, "li")

    for category in category_options:
        if category.text.strip():
            category.click()
            break

    category_select = driver.find_element(By.ID, "id_category")

    # Find input element with type 'submit'
    submit_btn = driver.find_element(By.NAME, "saveanddisplay")
    submit_btn.click()

    assert "is-invalid" in full_name_input.get_attribute("class")
    assert "is-invalid" not in short_name_input.get_attribute("class")
    assert "is-invalid" not in category_select.get_attribute("class")


def test_011_005():
    """Name non-empty, short name empty, category empty"""

    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/course/edit.php?id=51")

    # Find input element for full name
    full_name_input = driver.find_element(By.ID, "id_fullname")
    full_name_input.clear()
    full_name_input.send_keys("A full name for this course")

    # Find input element for short name
    short_name_input = driver.find_element(By.ID, "id_shortname")
    short_name_input.clear()

    # Find category select element
    course_category_row = driver.find_element(By.ID, "fitem_id_category")
    # Find all spans within the row with role='option'
    chosen_categories = course_category_row.find_elements(
        By.XPATH, ".//span[@role='option']"
    )
    for category in chosen_categories:
        category.click()

    category_select = course_category_row.find_element(By.ID, "id_category")

    # Find input element with type 'submit'
    submit_btn = driver.find_element(By.NAME, "saveanddisplay")
    submit_btn.click()

    assert "is-invalid" not in full_name_input.get_attribute("class")
    assert "is-invalid" in short_name_input.get_attribute("class")
    assert "is-invalid" in category_select.get_attribute("class")


def test_011_006():
    """Name non-empty, short name empty, category non-empty"""

    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/course/edit.php?id=51")

    # Find input element for full name
    full_name_input = driver.find_element(By.ID, "id_fullname")
    full_name_input.clear()
    full_name_input.send_keys("A full name for this course")

    # Find input element for short name
    short_name_input = driver.find_element(By.ID, "id_shortname")
    short_name_input.clear()

    # Find an 'ul' with class 'form-autocomplete-suggestions' and click on any 'li' that has non-empty text
    category_row = driver.find_element(By.ID, "fitem_id_category")
    category_row.find_element(
        By.CSS_SELECTOR, "span.form-autocomplete-downarrow"
    ).click()
    category_dropdown = category_row.find_element(
        By.CSS_SELECTOR, "ul.form-autocomplete-suggestions"
    )
    category_options = category_dropdown.find_elements(By.TAG_NAME, "li")

    for category in category_options:
        if category.text.strip():
            category.click()
            break

    category_select = driver.find_element(By.ID, "id_category")

    # Find input element with type 'submit'
    submit_btn = driver.find_element(By.NAME, "saveanddisplay")
    submit_btn.click()

    assert "is-invalid" not in full_name_input.get_attribute("class")
    assert "is-invalid" in short_name_input.get_attribute("class")
    assert "is-invalid" not in category_select.get_attribute("class")


def test_011_007():
    """Name non-empty, short name non-empty, category empty"""

    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/course/edit.php?id=51")

    # Find input element for full name
    full_name_input = driver.find_element(By.ID, "id_fullname")
    full_name_input.clear()
    full_name_input.send_keys("A full name for this course")

    # Find input element for short name
    short_name_input = driver.find_element(By.ID, "id_shortname")
    short_name_input.clear()
    short_name_input.send_keys("A short name for this course")

    # Find category select element
    course_category_row = driver.find_element(By.ID, "fitem_id_category")
    # Find all spans within the row with role='option'
    chosen_categories = course_category_row.find_elements(
        By.XPATH, ".//span[@role='option']"
    )
    for category in chosen_categories:
        category.click()

    category_select = course_category_row.find_element(By.ID, "id_category")

    # Find input element with type 'submit'
    submit_btn = driver.find_element(By.NAME, "saveanddisplay")
    submit_btn.click()

    assert "is-invalid" not in full_name_input.get_attribute("class")
    assert "is-invalid" not in short_name_input.get_attribute("class")
    assert "is-invalid" in category_select.get_attribute("class")


def test_011_008():
    """Name non-empty, short name non-empty, category non-empty"""

    driver = webdriver.Chrome()

    login(driver, "teacher", "moodle")
    driver.get("https://school.moodledemo.net/course/edit.php?id=51")

    # Find input element for full name
    full_name_input = driver.find_element(By.ID, "id_fullname")
    full_name_input.clear()
    full_name_input.send_keys("A full name for this course")

    # Find input element for short name
    short_name_input = driver.find_element(By.ID, "id_shortname")
    short_name_input.clear()
    short_name_input.send_keys("A short name for this course")

    short_name_input.send_keys(Keys.TAB)

    # Find an 'ul' with class 'form-autocomplete-suggestions' and click on any 'li' that has non-empty text
    category_row = driver.find_element(By.ID, "fitem_id_category")
    category_row.find_element(
        By.CSS_SELECTOR, "span.form-autocomplete-downarrow"
    ).click()
    category_dropdown = category_row.find_element(
        By.CSS_SELECTOR, "ul.form-autocomplete-suggestions"
    )
    category_options = category_dropdown.find_elements(By.TAG_NAME, "li")

    for category in category_options:
        if category.text.strip():
            category.click()
            break

    category_select = driver.find_element(By.ID, "id_category")

    # Check that there are no errors shown
    assert "is-invalid" not in full_name_input.get_attribute("class")
    assert "is-invalid" not in short_name_input.get_attribute("class")
    assert "is-invalid" not in category_select.get_attribute("class")

    # Check that course is saved successfully
    submit_btn = driver.find_element(By.NAME, "saveanddisplay")
    submit_btn.click()

    new_url = "https://school.moodledemo.net/course/view.php?id=51"
    WebDriverWait(driver, 10).until(EC.url_to_be(new_url))
