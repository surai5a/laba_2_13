def display_goods(goods):
    """
    Отобразить список товаров.
    """
    print(goods)
    # Проверить, что список товаров не пуст.
    if goods:
        # Заголовок таблицы.
        line = '+-{}-+-{}-+-{}-+-{}-+'.format(
            '-' * 4,
            '-' * 30,
            '-' * 20,
            '-' * 8
        )
        print(line)
        print(
            '| {:^4} | {:^30} | {:^20} | {:^8} |'.format(
                "№",
                "Название",
                "Магазин",
                "Цена"
            )
        )
        print(line)
        # Вывести данные о всех товарах.
        for idx, good in enumerate(goods, 1):
            print(
                '| {:>4} | {:<30} | {:<20} | {:>8} |'.format(
                    idx,
                    good.get('name', ''),
                    good.get('shop', ''),
                    good.get('price', 0)
                )
            )
        print(line)

    else:
        print("Список товаров пуст.")
