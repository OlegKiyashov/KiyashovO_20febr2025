from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CartPage:
    """
    Класс для взаимодействия с корзиной на веб-странице.
    """

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def find_element_and_click(self, css_selector: str):
        element = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()

    @allure.step("Проверяем наличие товара в корзине.")
    def find_product_in_cart(self, product_name: str) -> bool:
        try:
            WebDriverWait(self._driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "a.basket__name"))
            )
            products = self._driver.find_elements(By.CSS_SELECTOR, "a.basket__name")
            return any(product.text.strip() == product_name for product in products)
        except Exception:
            return False

    @allure.step("Удаляем товар из корзины.")
    def delete_product_in_cart(self, product_name: str) -> bool:
        try:
            WebDriverWait(self._driver, 20).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div.basket__delete i"))
            )
            delete_buttons = self._driver.find_elements(By.CSS_SELECTOR, "div.basket__delete i")
            products = self._driver.find_elements(By.CSS_SELECTOR, "a.basket__name")

            for i, product in enumerate(products):
                if product.text.strip() == product_name:
                    delete_buttons[i].click()
                    return True
        except Exception:
            return False
        return False

    @allure.step("Изменяем количество товара в корзине.")
    def change_amount_product_in_cart(self, product_name: str, action: str, amount: int):
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a.basket__name"))
        )
        products = self._driver.find_elements(By.CSS_SELECTOR, "a.basket__name")
        less_buttons = self._driver.find_elements(By.CSS_SELECTOR, "button.less")
        more_buttons = self._driver.find_elements(By.CSS_SELECTOR, "button.more")

        for i, product in enumerate(products):
            if product.text.strip() == product_name:
                for _ in range(amount):
                    current_amount = int(self.get_product_quantity(product_name))
                    button = less_buttons[i] if action == "less" else more_buttons[i]
                    button.click()

                    WebDriverWait(self._driver, 10).until(
                        lambda driver: int(self.get_product_quantity(product_name)) != current_amount
                    )

    @allure.step("Получаем количество указанного товара в корзине.")
    def get_product_quantity(self, product_name: str) -> str:
        WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.basket__name"))
        )
        products = self._driver.find_elements(By.CSS_SELECTOR, "a.basket__name")
        quantities = self._driver.find_elements(By.CSS_SELECTOR, "span.num")

        for i, product in enumerate(products):
            if product.text.strip() == product_name:
                WebDriverWait(self._driver, 5).until(EC.visibility_of(quantities[i]))
                return quantities[i].text
        return "0"
