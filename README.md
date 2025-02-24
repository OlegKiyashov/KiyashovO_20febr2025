## Шаг 4,
### Струткура автоматизированные тесты (API и UI):
- **./api** - папка содержит хелперы для работы с API.
- - **./api_page.py** - файл содержит методы API (добавление, изменение, удаление товаров).
- **./pages** - папка содержит хелперы для работы с UI.
- - **./main_page.py** - файл содержит методы поиска и добавления в корзину.
- - **./cart_page.py** - файл содержит методы работы с корзиной.
- **./test** - папка содержит тесты API и UI.
- - **./test_api.py** - файл содержит тесты api. Тесты запускаются командой 'pytest test/test_api.py'
- - **./test_ui.py** - файл содержит тесты ui. Тесты запускаются командой 'pytest test/test_ui.py'
- **./config.json** - файл содержит данные url адреса для ui и api тестов.
- **./conftest.py** - файл содержит фикстуры, используемые в проекте.
- **./run.sh** - файл содержит Bash-скрипт для автоматизации процесса запуска тестов, сбора результатов, генерации Allure-отчета и его открытия в браузере.

---

### Полезные ссылки
- [Ссылка на сервис Полезных продуктов](https://altaivita.ru/)
- [Подсказка по markdown](https://www.markdownguide.org/basic-syntax/)
- [Генератор файла .gitignore](https://www.toptal.com/developers/gitignore)

---

### Стек:
- **pytest**
- **selenium**
- **requests**
- **allure**
- **config**
 
---

### Библиотеки (!)
- pip install **pytest**
- pip install **selenium**
- pip install **webdriver-manager** 
- pip install **allure-pytest**
- pip install **requests**

---

### Установка зависимостей и запуск тестов
- Установите зависимости: **`pip install -r requirements.txt`**.
- Запустите все тесты: **`pytest test`**.
- Запустите только UI-тесты: **`pytest tests/test_ui.py`**.
- Запустите только API-тесты: **`pytest tests/test_api.py`**.
- Сгенерируйте Allure-отчёт: **`./run.sh`**.
