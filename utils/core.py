
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

def enable_edit_mode(driver):
    try:
        editmode_button = WebDriverWait(driver, 5).until(lambda driver: driver.find_element(By.NAME, "setmode"))
    except Exception:
        editmode_button = None

    assert editmode_button != None

    is_editmode = editmode_button.get_attribute("checked")

    if not is_editmode:
        editmode_button.click()
        driver.implicitly_wait(5)
