from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    """
    Класс для взаимодействия с главной страницей интернет-магазина.
    """

    def __init__(self, driver: WebDriver):
        """
        Конструктор класса MainPage.

        Args:
            driver (WebDriver): WebDriver экземпляр для управления браузером.
        """
        self._driver = driver

    def find_element_and_click(self, css_selector: str):
        """
        Находит элемент на странице по CSS селектору и нажимает на него.

        Args:
            css_selector (str): CSS селектор элемента.
        """
        # Ожидаем, пока элемент станет кликабельным, и нажимаем на него
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()

    @allure.step(
        "Выполняем поиск товара в поисковой строке по переданному "
        "наименованию - '{product_name}'."
    )
    def search_product_by_search_field(self, product_name: str):
        """
        Выполняет поиск товара через поисковую строку на главной странице.

        Args:
            product_name (str): Наименование товара для поиска.
        """
        # Находим поле поиска по его XPath и вводим название товара
        search_field = self._driver.find_element(
            By.XPATH, "//input[@placeholder='Поиск товаров']"
        )
        search_field.clear()  # Очищаем поле перед вводом
        search_field.send_keys(product_name)
        # Нажимаем на кнопку поиска
        self.find_element_and_click("div.searchpro__field-button-container")

    @allure.step(
        "Находим на странице результатов поиска необходимый "
        "товар - '{product_name_to_add}' и добавляем его в корзину."
    )
    def add_product_to_cart(self, product_name_to_add: str) -> str:
        """
        Находит товар на странице поиска и добавляет его в корзину.

        Args:
            product_name_to_add (str): Наименование товара,
             который нужно добавить в корзину.

        Returns:
            str: Наименование добавленного товара.
        """
        # Ждем, пока загрузятся элементы с информацией о товарах
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "div.rating_search_product")
            )
        )
        # Получаем список всех контейнеров с информацией о товарах
        product_info_containers = self._driver.find_elements(
            By.CSS_SELECTOR, "div.product__item"
        )
        for container in product_info_containers:
            # Извлекаем название товара из атрибута "alt" изображения
            product_img = container.find_element(By.CSS_SELECTOR, "img")
            product_name = product_img.get_attribute("alt")
            if product_name == product_name_to_add:
                # Если название совпадает, нажимаем кнопку "Добавить в корзину"
                add_button = container.find_element(
                    By.CSS_SELECTOR, "div.product__buy button"
                )
                add_button.click()
                return product_name
        # Если товар не найден, выбрасываем исключение
        raise ValueError(
            f"Товар с названием '{
                         product_name_to_add}' не найден."
        )

    @allure.step("Переходим на страницу корзины.")
    def go_to_cart(self):
        """
        Переходит на страницу корзины через соответствующий
         элемент на главной странице.
        """
        # Кликаем на ссылку корзины
        self.find_element_and_click("a[href='/cart/']")
        # Подтверждаем переход, если появляется дополнительное окно
        self.find_element_and_click("a.dropdown-go-over")
