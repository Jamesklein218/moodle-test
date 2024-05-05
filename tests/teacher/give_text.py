from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.auth import login
from utils.core import enable_edit_mode

from parameterized import parameterized
import utils.readData as readData
import time
import unittest

@parameterized.expand(readData.readDataFromExcel("GiveText"))
def test_bv(title, text):
    driver = webdriver.Chrome()
    login(driver,"teacher", "moodle")
    driver.get("https://school.moodledemo.net/mod/page/view.php?id=45")
    give_text_btn = driver.find_element(By.XPATH,"//section[@id='region-main']/div[2]/div/div/ul/li[4]/a")
    give_text_btn.click()

    title_input = driver.find_element(By.ID,"id_name")
    text_input = driver.find_element(By.ID,"id_introeditor")
    # text_input = driver.find_element(By.XPATH, "//body[@id='tinymce']")
    submt_btn = driver.find_element(By.ID, "id_submitbutton2")

    title_input.clear()
    time.sleep(5)
    title_input.send_keys(title)
    time.sleep(5)
    current_content = text_input.get_attribute("value")
    # Modify the content to remove the <img> tag
    current_content.replace('<p><img class="img-fluid align-top" src="https://school.moodledemo.net/draftfile.php/160/user/draft/275575117/Jardin%20du%20Musee%20Rodin%20Paris%20Le%20Penseur%2020050402%20%2802%29.jpg" alt="Rodin\'s The Thinker" width="75" height="100"></p>', '')
    # print("clear the picture")
    time.sleep(5)
    # text_input.send_keys(text)
    # print("input new text")
    submt_btn.click()
    time.sleep(15)

    driver.quit()
