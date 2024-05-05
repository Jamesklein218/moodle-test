from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from utils.auth import login
from utils.network import download_file, get_user_picture_url
from helpers import (
    reset_upload_form,
    upload_user_pictures,
    check_changed_page,
    count_users_updated,
    count_errors,
)
import os


VALID_PICTURE_FILENAME = os.path.join(os.getcwd(), "valid_picture.zip")
INVALID_PICTURE_FILENAME = os.path.join(os.getcwd(), "invalid_picture.zip")

NON_ZIP_URL = (
    "https://drive.google.com/uc?export=download&id=1QNg1Dx827-KVoVoxyT7IZsI1OrFeJpBl"
)
NON_ZIP_FILENAME = os.path.join(os.getcwd(), "non_zip_file.png")

EMPTY_ZIP_URL = (
    "https://drive.google.com/uc?export=download&id=1qhxKYKbztQKtNsO7n_N40l1ymUaFethG"
)
EMPTY_ZIP_FILENAME = os.path.join(os.getcwd(), "empty_zip.zip")


def test_010_001():
    """Equivalence class: Valid zip files that contains files matching user info, valid match criteria, valid overwrite option"""

    driver = webdriver.Chrome()
    login(driver, "manager", "moodle")

    driver.get("https://school.moodledemo.net/admin/tool/uploaduser/picture.php")
    reset_upload_form(driver)
    download_file(get_user_picture_url(valid=True), VALID_PICTURE_FILENAME)

    upload_user_pictures(driver, VALID_PICTURE_FILENAME)

    Select(driver.find_element(By.ID, "id_userfield")).select_by_visible_text(
        "username"
    )

    Select(driver.find_element(By.ID, "id_overwritepicture")).select_by_visible_text(
        "No"
    )

    WebDriverWait(driver, 30).until(
        lambda driver: driver.find_element(
            By.XPATH, "//div[@class='filepicker-filename']//a"
        )
    )

    driver.find_element(By.ID, "id_submitbutton").click()

    WebDriverWait(driver, 30).until(lambda driver: check_changed_page(driver))

    assert count_errors(driver) == 0


def test_010_002():
    """
    Equivalence class: Valid zip files but contains
    files not matching any user info, valid match criteria,
    valid overwite option
    """

    driver = webdriver.Chrome()
    login(driver, "manager", "moodle")

    driver.get("https://school.moodledemo.net/admin/tool/uploaduser/picture.php")
    reset_upload_form(driver)
    download_file(get_user_picture_url(valid=False), INVALID_PICTURE_FILENAME)

    upload_user_pictures(driver, INVALID_PICTURE_FILENAME)

    Select(driver.find_element(By.ID, "id_userfield")).select_by_visible_text(
        "username"
    )

    Select(driver.find_element(By.ID, "id_overwritepicture")).select_by_visible_text(
        "No"
    )

    WebDriverWait(driver, 30).until(
        lambda driver: driver.find_element(
            By.XPATH, "//div[@class='filepicker-filename']//a"
        )
    )

    driver.find_element(By.ID, "id_submitbutton").click()

    WebDriverWait(driver, 30).until(lambda driver: check_changed_page(driver))

    assert count_errors(driver) > 0


def test_010_004():
    """
    Equivalence class: Non-zip file format,
    valid match criteria, valid overwite option
    """

    driver = webdriver.Chrome()
    login(driver, "manager", "moodle")

    driver.get("https://school.moodledemo.net/admin/tool/uploaduser/picture.php")
    reset_upload_form(driver)
    download_file(NON_ZIP_URL, NON_ZIP_FILENAME)

    upload_user_pictures(driver, NON_ZIP_FILENAME)

    Select(driver.find_element(By.ID, "id_userfield")).select_by_visible_text(
        "username"
    )

    WebDriverWait(driver, 30).until(
        lambda driver: driver.find_element(
            By.XPATH, "//div[contains(text(), 'filetype cannot be accepted')]"
        )
    )


def test_010_005():
    """
    Equivalence class: Empty zip file,
    valid match criteria, valid overwrite option
    """

    driver = webdriver.Chrome()
    login(driver, "manager", "moodle")

    driver.get("https://school.moodledemo.net/admin/tool/uploaduser/picture.php")
    reset_upload_form(driver)
    download_file(EMPTY_ZIP_URL, EMPTY_ZIP_FILENAME)

    upload_user_pictures(driver, EMPTY_ZIP_FILENAME)

    Select(driver.find_element(By.ID, "id_userfield")).select_by_visible_text(
        "username"
    )

    Select(driver.find_element(By.ID, "id_overwritepicture")).select_by_visible_text(
        "No"
    )

    driver.find_element(By.ID, "id_submitbutton").click()

    WebDriverWait(driver, 30).until(
        lambda driver: driver.find_element(
            By.XPATH, "//div[contains(text(), 'Cannot unzip pictures file.')]"
        )
    )
