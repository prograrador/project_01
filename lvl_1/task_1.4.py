#
# РАНХиГС. Python. Поток 2
# Коновченко Александр Михайлович
#

# Задача 1.4.

# Есть словарь кодов товаров titles

titles = {
    'Кроссовки тип 3 (Adidas)': '100000110',
    'Мячик тип 2 (Adidas)': '100000146',
    'Кепка тип 1 (Adidas)': '100000149',
    'Ремень тип 2 (Nike)': '100000194',
    'Футболка тип 1 (Adidas)': '100000224',
    'Шапка тип 5 (Puma)': '100000280',
}

# Товары находятся на складе и сохранены в виде словаря списков словарей,
# которые отражают количество товаров в магазине по каждому коду.

store = {
    '100000110': [{'quantity': 31, 'price': 1637}],
    '100000146': [{'quantity': 4, 'price': 45}, {'quantity': 10, 'price': 48}],
    '100000149': [{'quantity': 28, 'price': 279}, {'quantity': 32, 'price': 291}],
    '100000194': [{'quantity': 8, 'price': 220}, {'quantity': 1, 'price': 170}],
    '100000224': [{'quantity': 61, 'price': 438}, {'quantity': 23, 'price': 302},  {'quantity': 50, 'price': 412}],
    '100000280': [{'quantity': 26, 'price': 175}, ]
}

# Рассчитайте на какую сумму лежит каждого товара на складе.
#
# Вывести суммарную стоимость каждого товара в магазине в формате:
# "<товар> - <кол-во> шт, стоимость <общая стоимость> руб"

# Пример: "Кроссовки тип 3 (Adidas) - 31 шт, стоимость 50747 руб"
curr_good_code = ''
reversed_titles = dict((v, k) for k, v in titles.items())  # получаем обратный словарь: {код: наименование}
for curr_good_code in store:       # цикл по ключам в словаре store, где ключ - curr_good_code - это код товара
    curr_good_items = store[curr_good_code]     # из словаря store по коду товара получаем список элементов с ценой и количеством
    curr_good_quantity_sum = 0                  # обнуляем счетчик количества
    curr_good_prices_sum = 0                    # обнуляем счетчик общей стоимости товаров
    for item in curr_good_items:    # цикл по элементам с ценой и количеством
        curr_good_quantity_sum += item['quantity']    # суммируем все значения элементов с ключом 'quantity'
        # собираем общую стоимость товаров (элемент 'quantity' * элемент 'price'
        curr_good_prices_sum += item['quantity'] * item['price']
    # в цикле по ключам в словаре store (т.е. для каждого кода товара) выводим наименование, код, общее кол-во и общую
    #    стоимость товара
    print(f'{reversed_titles[curr_good_code]} ({curr_good_code}) - '
          f'{curr_good_quantity_sum} шт., стоимость {curr_good_prices_sum} руб.')
