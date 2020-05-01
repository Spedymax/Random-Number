import random


def random_number():
    number = input('Нажмите Enter чтобы крутить кубик: ')
    print(number)
    if number == "":
        rand_number = random.randint(1, 6)
        print(rand_number)


random_number()
