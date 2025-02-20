-- 1) Выведите все уникальные названия продуктов
SELECT DISTINCT product_name FROM Products;

-- 2) Выведите id, название и стоимость продуктов с содержанием клетчатки (fiber) более 5 граммов
SELECT p.product_id, p.product_name, p.price
FROM Products p
JOIN NutritionalInformation n ON p.product_id = n.product_id
WHERE n.fiber > 5;

-- 3) Выведите название продукта с самым высоким содержанием белка (protein)
SELECT p.product_name
FROM Products p
JOIN NutritionalInformation n ON p.product_id = n.product_id
ORDER BY n.protein DESC
LIMIT 1;

-- 4) Подсчитайте общую сумму калорий для продуктов каждой категории, но не учитывайте продукты с нулевым жиром (fat = 0). Выведите id категории, сумму калорий
SELECT p.category_id, SUM(p.calories) AS total_calories
FROM Products p
JOIN NutritionalInformation n ON p.product_id = n.product_id
WHERE n.fat > 0
GROUP BY p.category_id;

-- 5) Рассчитайте среднюю цену товаров каждой категории. Выведите название категории, среднюю цену
SELECT c.category_name, ROUND(AVG(p.price), 2) AS avg_price
FROM Products p
JOIN Categories c ON p.category_id = c.category_id
GROUP BY c.category_name;
