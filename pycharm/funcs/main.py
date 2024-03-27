from funcs.add import *
from funcs.help import *
from funcs.list import *
from funcs.error import *



def main():
    """"
    Главная функция программы.
    """
    print("Список команд:\n")
    print("add - добавить студента;")
    print("list - вывести список студентов;")

    print("help - отобразить справку;")
    print("exit - завершить работу с программой.")
    # Список работников.
    students = []
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
                students.append(i)
                # Отсортировать список в случае необходимости.
                if len(students) > 1:
                    students.sort(key=lambda item: item.get('fullname', ''))

            case 'list':
                list1(students)

            case 'help':
                help1()

            case _:
                error1()


if __name__ == '__main__':
    main()




