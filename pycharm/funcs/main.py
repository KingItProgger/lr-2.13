from funcs.add import *
from funcs.help import *
from funcs.select import *
from funcs.list import *
from funcs.error import *



def main():
    """"
    Главная функция программы.
    """
    print("Список команд:\n")
    print("add - добавить рейс;")
    print("list - вывести список рйсов;")
    print("select <тип> - вывод на экран пунктов назначения и номеров рейсов для данного типа самолёта")
    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    # Список работников.
    aircrafts = []
    # Организовать бесконечный цикл запроса команд.
    while True:
        # Запросить команду из терминала.
        command = input(">>> ").lower()
        # Выполнить действие в соответствие с командой.

        match command:
            case 'exit':
                break

            case 'add':
                # Добавить словарь в список.
                i = add1()
                aircrafts.append(i)
                # Отсортировать список в случае необходимости.
                if len(aircrafts) > 1:
                    aircrafts.sort(key=lambda item: item.get('name', ''))

            case 'list':
                list(aircrafts)

            case 'select':
                select(command, aircrafts)

            case 'help':
                help1()

            case _:
                error1()



