import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import shutil
import os


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