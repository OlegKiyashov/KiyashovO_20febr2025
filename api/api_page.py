import requests
import json
from typing import Dict, Any, Tuple

with open("config.json", "r") as config_file:
    config = json.load(config_file)

api_data = config.get("api", {})
base_url_api = config.get("base_url_api", "")


class ApiPage:
    def __init__(self, url: str):
        self.url = url

    def add_product_to_cart_from_preview(
        self, quantity: str
    ) -> Tuple[Dict[str, Any], int]:
        request_data = api_data.copy()
        request_data["quantity"] = quantity

        response = requests.post(
            f"{self.url}add_products_to_cart_from_preview.php",
            data=request_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        return response.json(), response.status_code

    def delete_product_from_cart(self) -> Tuple[Dict[str, Any], int]:
        response = requests.post(
            f"{self.url}delete_products_from_cart_preview.php",
            data=api_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        return response.json(), response.status_code

    def change_amount_product_from_preview(self) -> Tuple[Dict[str, Any], int]:
        response = requests.post(
            f"{self.url}delete_products_from_cart_preview_by_productID.php",
            data=api_data,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
        )

        return response.json(), response.status_code
