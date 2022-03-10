def select_goods(goods, shop):
    """
    Выбрать товары магазина.
    """

    # Счетчик записей.
    count = 0

    # Сформировать список товаров.
    result = []

    for good in goods:
        if shop == good.get('shop', shop):
            count += 1
            result.append(good)

    # Проверка на отсутствие товаров или выбранного магазина.
    if count == 0:
        print("Такого магазина не существует либо нет товаров.")
    else:
        # Возвратить список выбранных товаров.
        return result
