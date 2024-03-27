import sys

def add1():
    """"
        Функция для добавления информации о новых студентах
        """
    fullname=input('введите фамилию , имя и отчества студента: ')
    try:
        group=int(input('введите номер группы '))
    except ValueError:
        print('номер должен быть числом',file=sys.stderr)
        exit(1)

    lessons=['математика', 'информатика','экономика','программирование','философия']
    res={}
    res['marks'] = []
    res['fullname']=fullname
    res['group']=group


    for i in range(0,5):
        a=int(input(f'оценка по {lessons[i]}: '))
        res['marks'].append(a)

    return res
