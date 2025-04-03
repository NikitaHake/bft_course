import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from allure_commons.types import AttachmentType
import shutil, os
import time

@pytest.fixture(scope="session", autouse=True)
def clean_allure_results():
    if os.path.exists("../allure-results"):
        shutil.rmtree("../allure-results")
    os.makedirs("../allure-results", exist_ok=True)

@pytest.fixture(scope="function")
def wd():
    chrome_options = Options()
    chrome_options.add_argument("--remote-allow-origins=*")

    wd = webdriver.Chrome(options=chrome_options)
    wd.maximize_window()
    yield wd
    wd.quit()

@allure.feature("Тесты DemoQA")
@allure.story("Работа с элементами формы")

def test_dakhnenko(wd):
    with allure.step("Открываем страницу ДемоТеста"):
        wd.get("https://demoqa.com/")
        allure.attach(wd.get_screenshot_as_png(), name="DemoTest", attachment_type=AttachmentType.PNG)

    with allure.step("Кликаем по элементу меню - Elements (для открытия)"):
        elements_open_button = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div[1]"))
        )
        elements_open_button.click()
        allure.attach(wd.get_screenshot_as_png(), name="Elements Open", attachment_type=AttachmentType.PNG)

    with allure.step("Кликаем по элементу меню - Text Box"):
        text_box_button = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/div/ul/li[1]"))
        )
        text_box_button.click()
        allure.attach(wd.get_screenshot_as_png(), name="Text Box", attachment_type=AttachmentType.PNG)

    with allure.step("Заполняем поле Full Name"):
        name_field = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[1]/div[2]/input"))
        )
        name_field.click()
        name_field.clear()
        name_field.send_keys("Дахненко Н.В.")
        allure.attach(wd.get_screenshot_as_png(), name="Name_entered", attachment_type=AttachmentType.PNG)

    with allure.step("Заполняем поле Email"):
        email_field = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[2]/div[2]/input"))
        )
        email_field.click()
        email_field.clear()
        email_field.send_keys("n.dakhnenko@gmail.com")
        allure.attach(wd.get_screenshot_as_png(), name="Email_entered", attachment_type=AttachmentType.PNG)

    with allure.step("Заполняем поле Address1"):
        address1_field = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[3]/div[2]/textarea"))
        )
        address1_field.click()
        address1_field.clear()
        address1_field.send_keys("city Kaliningrad, st. Sovietskiy pr 3 ")
        allure.attach(wd.get_screenshot_as_png(), name="Address1_entered", attachment_type=AttachmentType.PNG)

    with allure.step("Заполняем поле Address2"):
        address2_field = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[4]/div[2]/textarea"))
        )
        address2_field.click()
        address2_field.clear()
        address2_field.send_keys("city Kaliningrad, st. Sovietskiy pr 5 ")
        allure.attach(wd.get_screenshot_as_png(), name="Address2_entered", attachment_type=AttachmentType.PNG)

    with allure.step("Кликаем по элементу  - Submit"):
        submit_button = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/form/div[5]/div/button"))
        )
        submit_button.click()

    with allure.step("Кликаем по элементу меню - Elements (для закрытия)"):
        elements_close_button = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[1]/span/div"))
        )
        elements_close_button.click()

    with allure.step("Кликаем по элементу меню - Widgets (для открытьия)"):
        widgets_open_button = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[4]/span/div"))
        )
        widgets_open_button.click()
        allure.attach(wd.get_screenshot_as_png(), name="Widgets Open", attachment_type=AttachmentType.PNG)

    with allure.step("Кликаем по элементу - Progress Bar"):
        progress_bar_button = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div/div/div[4]/div/ul/li[5]"))
        )
        progress_bar_button.click()

    with allure.step("Кликаем по элементу - Start"):
        start_button = WebDriverWait(wd, 2).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/button"))
        )
        start_button.click()
        allure.attach(wd.get_screenshot_as_png(), name="Start button", attachment_type=AttachmentType.PNG)

    with allure.step("Ожидание загрузки до 100%"):
        hundred_field = WebDriverWait(wd, 15).until(
            EC.text_to_be_present_in_element((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[2]/div[2]/div"), "100%")
        )
        allure.attach(wd.get_screenshot_as_png(), name="Full Bar, 100%", attachment_type=AttachmentType.PNG)

    with allure.step("Открываем новую страницу в другой вкладке"):
        og_window = wd.current_window_handle
        wd.switch_to.new_window('tab')
        wd.get("https://media1.tenor.com/m/W0YAWB2MQ_sAAAAC/testing-testing-can-continue.gif")
        time.sleep(3)
        allure.attach(wd.get_screenshot_as_png(), name="Gifka :)", attachment_type=AttachmentType.PNG)

# allure serve allure-results