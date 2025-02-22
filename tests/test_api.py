import allure


@allure.feature("API тесты для функционала корзины")
@allure.title("Тест на добавление товара в корзину")
@allure.description(
    "Добавляем товар в корзину и проверяем корректность ответа API."
)
@allure.id(1)
@allure.severity("Blocker")
def test_add_product_to_cart_from_preview(api):
    """
    Тест на добавление товара в корзину через превью.

    Args:
        api (AltaivitaApi): Экземпляр API клиента.
    """
    amount = "1"  # Количество товаров для добавления

    # Отправляем запрос на добавление товара в корзину
    result_add_product, status_code = api.add_product_to_cart_from_preview(
        amount
    )

    with allure.step("Проверяем корректность статус-кода и ответа API"):
        assert (
            status_code == 200
        ), f"Ожидался статус-код 200, но получен {
            status_code}"
        assert (
            result_add_product["status"] == "ok"
        ), f"Ожидался статус 'ok', но получен {result_add_product['status']}"
        assert (
            result_add_product["btn_text"] == "Добавлено"
        ), f"Ожидался текст кнопки 'Добавлено', но получен {
                result_add_product['btn_text']}"
        assert (
            result_add_product["sum_quantity"] == amount
        ), f"Ожидалось количество {amount}, но получено {
                result_add_product['sum_quantity']}"

    # Удаляем товар из корзины для очистки состояния
    api.delete_product_from_cart()


@allure.feature("API тесты для функционала корзины")
@allure.title("Тест на удаление товара из корзины")
@allure.description(
    "Добавляем товар в корзину, затем удаляем его и проверяем,"
    " что корзина пуста."
)
@allure.id(2)
@allure.severity("Blocker")
def test_delete_product_from_cart(api):
    """
    Тест на удаление товара из корзины.

    Args:
        api (AltaivitaApi): Экземпляр API клиента.
    """
    amount = "1"  # Количество товаров для добавления

    # Добавляем товар в корзину
    result_add_product, status_code = api.add_product_to_cart_from_preview(
        amount
    )

    with allure.step("Проверяем корректность добавления товара"):
        assert (
            status_code == 200
        ), f"Ожидался статус-код 200, но получен {
            status_code}"
        assert (
            result_add_product["status"] == "ok"
        ), f"Ожидался статус 'ok', но получен {result_add_product['status']}"
        assert (
            result_add_product["btn_text"] == "Добавлено"
        ), f"Ожидался текст кнопки 'Добавлено', но получен {
                result_add_product['btn_text']}"

    amount_before_delete = int(result_add_product["sum_quantity"])

    # Удаляем товар из корзины
    result_delete_product, status_code_delete = api.delete_product_from_cart()
    amount_after_delete = int(result_delete_product["sum_quantity"])

    with allure.step("Проверяем, что корзина пуста после удаления товара"):
        assert (
            status_code_delete == 200
        ), f"Ожидался статус-код 200, но получен {
            status_code_delete}"
        assert (
            result_delete_product["status"] == "ok"
        ), f"Ожидался статус 'ok', но получен {
                result_delete_product['status']}"
        assert (
            amount_after_delete == 0
        ), f"Ожидалось, что корзина пуста, но количество товаров: {
                amount_after_delete}"
        assert (
            amount_before_delete > amount_after_delete
        ), "Количество товаров в корзине не уменьшилось после удаления"


@allure.feature("API тесты для функционала корзины")
@allure.title("Тест на изменение количества товара в корзине")
@allure.description(
    "Добавляем товар в корзину, затем изменяем его количество "
    "и проверяем корректность изменения."
)
@allure.id(3)
@allure.severity("Blocker")
def test_change_amount_product(api):
    """
    Тест на изменение количества товара в корзине.

    Args:
        api (AltaivitaApi): Экземпляр API клиента.
    """
    amount = "2"  # Изначальное количество товара

    # Добавляем товар в корзину
    result_add_product, status_code = api.add_product_to_cart_from_preview(
        amount
    )

    with allure.step("Проверяем корректность добавления товара"):
        assert (
            status_code == 200
        ), f"Ожидался статус-код 200, но получен {
            status_code}"
        assert (
            result_add_product["status"] == "ok"
        ), f"Ожидался статус 'ok', но получен {result_add_product['status']}"
        assert (
            result_add_product["btn_text"] == "Добавлено"
        ), f"Ожидался текст кнопки 'Добавлено', но получен {
                result_add_product['btn_text']}"

    amount_before_change = int(result_add_product["sum_quantity"])

    # Изменяем количество товара в корзине
    result_change, status_code_change = (
        api.change_amount_product_from_preview()
    )
    amount_after_change = int(result_change["sum_quantity"])

    with allure.step("Проверяем корректность изменения количества товара"):
        assert (
            status_code_change == 200
        ), f"Ожидался статус-код 200, но получен {
            status_code_change}"
        assert (
            result_change["status"] == "ok"
        ), f"Ожидался статус 'ok', но получен {result_change['status']}"
        expected_amount = amount_before_change - 1
        assert (
            amount_after_change == expected_amount
        ), f"Ожидалось {expected_amount}, но получено {amount_after_change}"

    # Удаляем товар из корзины для очистки состояния
    api.delete_product_from_cart()
