import json
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import MainPage
from pages.cart_page import CartPage
from api.api_page import ApiPage

# Загружаем конфигурацию из файла
with open("config.json", "r") as config_file:
    config = json.load(config_file)

BASE_URL_UI = config.get("base_url_ui")
BASE_URL_API = config.get("base_url_api")


@pytest.fixture
def browser():
    """Фикстура для инициализации браузера."""
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.get(BASE_URL_UI)  # Переход на главную страницу
    driver.implicitly_wait(4)  # Устанавливаем неявное ожидание
    driver.maximize_window()  # Разворачиваем окно браузера

    yield driver  # Передаем WebDriver в тест

    driver.quit()  # Закрываем браузер после выполнения теста


@pytest.fixture
def main_page(browser):
    """Фикстура для работы с главной страницей."""
    return MainPage(browser)


@pytest.fixture
def cart_page(browser):
    """Фикстура для работы со страницей корзины."""
    return CartPage(browser)


@pytest.fixture
def api():
    """Фикстура для взаимодействия с API."""
    return ApiPage(BASE_URL_API)
