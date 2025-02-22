import allure
import json

# Загружаем конфигурацию из файла
with open("config.json", "r") as config_file:
    config = json.load(config_file)

base_url_ui = config.get("base_url_ui")
PRODUCT_NAME = config.get("product_name")


@allure.feature("UI тесты для функционала корзины")
@allure.title("Тест поиска и добавления товара в корзину")
@allure.description(
    "Выполняем поиск товара по названию, проверяем успешное добавление в корзину."
)
@allure.id(1)
@allure.severity("Blocker")
def test_search_product(main_page, cart_page):
    """Тест проверяет поиск товара и его добавление в корзину."""

    # Ищем товар через строку поиска
    main_page.search_product_by_search_field(PRODUCT_NAME)

    # Добавляем товар в корзину и проверяем название
    product_added = main_page.add_product_to_cart(PRODUCT_NAME)
    with allure.step("Проверяем соответствие названия добавленного товара"):
        assert product_added == PRODUCT_NAME, "Название товара не совпадает."

    # Переходим в корзину
    main_page.go_to_cart()

    # Проверяем наличие товара в корзине
    is_product_in_cart = cart_page.find_product_in_cart(PRODUCT_NAME)
    with allure.step("Проверяем, что товар находится в корзине"):
        assert is_product_in_cart, "Товар не найден в корзине."


@allure.feature("UI тесты для функционала корзины")
@allure.title("Тест удаления товара из корзины")
@allure.description(
    "Добавляем товар в корзину, затем удаляем его и проверяем отсутствие в корзине."
)
@allure.id(2)
@allure.severity("Blocker")
def test_delete_product_from_cart(main_page, cart_page):
    """Тест проверяет удаление товара из корзины."""

    # Добавляем товар в корзину
    main_page.search_product_by_search_field(PRODUCT_NAME)
    product_added = main_page.add_product_to_cart(PRODUCT_NAME)

    with allure.step("Проверяем соответствие названия добавленного товара"):
        assert product_added == PRODUCT_NAME, "Название товара не совпадает."

    # Переходим в корзину и удаляем товар
    main_page.go_to_cart()
    is_deleted = cart_page.delete_product_in_cart(PRODUCT_NAME)

    with allure.step("Проверяем, что товар удален из корзины"):
        assert is_deleted, "Товар не был удалён из корзины."


@allure.feature("UI тесты для функционала корзины")
@allure.title("Тест изменения количества товара в корзине")
@allure.description(
    "Добавляем товар в корзину, меняем количество и проверяем корректность изменения."
)
@allure.id(3)
@allure.severity("Blocker")
def test_change_amount(main_page, cart_page):
    """Тест проверяет изменение количества товара в корзине."""

    # Добавляем товар в корзину
    main_page.search_product_by_search_field(PRODUCT_NAME)
    product_added = main_page.add_product_to_cart(PRODUCT_NAME)

    with allure.step("Проверяем соответствие названия добавленного товара"):
        assert product_added == PRODUCT_NAME, "Название товара не совпадает."

    # Переходим в корзину
    main_page.go_to_cart()

    # Получаем текущее количество товара
    amount_before = int(cart_page.get_product_quantity(PRODUCT_NAME))

    # Изменяем количество товара
    amount_to_add = 2
    cart_page.change_amount_product_in_cart(PRODUCT_NAME, "more", amount_to_add)

    # Проверяем обновленное количество
    amount_after = int(cart_page.get_product_quantity(PRODUCT_NAME))
    expected_amount = amount_before + amount_to_add

    with allure.step("Проверяем, что количество товара изменилось корректно"):
        assert amount_after == expected_amount, (
            f"Ожидалось {expected_amount}, получено {amount_after}."
        )
