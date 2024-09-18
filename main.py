import random


def get_random(level):
    if level == 1:
        result = random.randint(0, 11)
        print("Загадано число от 0 до 10")
        return result
    elif level == 2:
        result = random.randint(0, 51)
        print("Загадано число от 0 до 50")
        return result
    else:
        result = random.randint(0, 101)
        print("Загадано число от 0 до 100")
        return result


def get_level():
    level = int(input("Выбери уровень от 1 до 3"))
    print('')

    if level >= 1 and level <= 3:
        print("Уровень принят")
        return level
    else:
        print("Введено неверное число, попробуете еще раз")
        get_level()


def attempts(numb):

    status = True
    while status:
        man_numb = int(input("Введите свое число"))

        if numb == man_numb:
            print("Вы угадали!")
            status = False
        elif man_numb == 999:
            print("Успешно вышли!")
            break
        else:
            print("Вы не угадали, попробуйте еще раз")
            print("Введите 999 чтобы выйти")


lvl = get_level()
rand_number = get_random(lvl)
attempts(rand_number)
