import sys
from bdata.get_goods import get_goods
from bdata.display_goods import display_goods
from bdata.select_goods import select_goods

def main():
    # Список товаров.
    goods = []

    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()

        # Выполнить действие в соответствие с командой.
        if command == 'exit':
            break

        elif command == 'add':
            # Запросить данные о товаре.
            good = get_goods()

            # Добавить словарь в список.
            goods.append(good)
            # Отсортировать список в случае необходимости.
            if len(goods) > 1:
                goods.sort(key=lambda item: item.get('name', ''))

        elif command == 'list':
            # Отобразить все товары.
            display_goods(goods)

        elif command.startswith('select '):
            # Разбить команду на части для выделения стажа.
            parts = command.split(' ', maxsplit=1)
            # Получить требуемые товары.
            shop = parts[1]

            # Выбрать товары магазина.
            selected = select_goods(goods, shop)
            # Отобразить выбранные товары.
            display_goods(selected)

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить товар;")
            print("list - вывести список товаров;")
            print("select <имя магазина> - запросить товары магазина;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)