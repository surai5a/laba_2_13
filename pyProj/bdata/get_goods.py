def get_goods():
    """
    Запросить данные о товаре.
    """

    name = input("Название товара: ")
    shop = input("Название магазина: ")
    price = float(input("Стоимость: "))

    # Создать словарь.
    return {
        'name': name,
        'shop': shop,
        'price': price,
    }
