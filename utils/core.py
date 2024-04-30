
from selenium.webdriver.common.by import By

def enable_edit_mode(driver):
    try:
        editmode_button = driver.find_element(By.NAME, "setmode")
    except Exception:
        editmode_button = None

    assert editmode_button != None

    is_editmode = editmode_button.get_attribute("checked")

    if not is_editmode:
        editmode_button.click()
        driver.implicitly_wait(5)
