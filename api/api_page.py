import requests
import json
from typing import Dict, Any, Tuple


# Чтение конфигурационного файла с API-данными и базовым URL
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Извлечение API-данных и базового URL
api_data = config.get("api", {})
base_url_api = config.get("base_url_api", "")


class ApiPage:
    """
    Класс для взаимодействия с API платформы.
    Содержит методы для работы с корзиной: добавление, удаление и изменение товаров.
    """

    def __init__(self, url: str):
        """
        Конструктор для инициализации базового URL API.

        Args:
            url (str): Базовый URL API.
        """
        self.url = url

    def add_product_to_cart_from_preview(self, quantity: str) -> Tuple[Dict[str, Any], int]:
        """
        Добавляет товар в корзину через превью.

        Args:
            quantity (str): Количество добавляемого товара.

        Returns:
            Tuple[Dict[str, Any], int]: JSON-ответ от API и HTTP-статус код.
        """
        # Создаем копию базовых данных и обновляем количество товара
        request_data = api_data.copy()
        request_data["quantity"] = quantity

        response = requests.post(
            f"{self.url}add_products_to_cart_from_preview.php",
            data=request_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )

        return response.json(), response.status_code

    def delete_product_from_cart(self) -> Tuple[Dict[str, Any], int]:
        """
        Удаляет все товары из корзины.

        Returns:
            Tuple[Dict[str, Any], int]: JSON-ответ от API и HTTP-статус код.
        """
        response = requests.post(
            f"{self.url}delete_products_from_cart_preview.php",
            data=api_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )

        return response.json(), response.status_code

    def change_amount_product_from_preview(self) -> Tuple[Dict[str, Any], int]:
        """
        Изменяет количество товара в корзине через превью.

        Returns:
            Tuple[Dict[str, Any], int]: JSON-ответ от API и HTTP-статус код.
        """
        response = requests.post(
            f"{self.url}delete_products_from_cart_preview_by_productID.php",
            data=api_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )

        return response.json(), response.status_code
