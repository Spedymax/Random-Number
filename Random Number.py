import random


my_list = []
imovirnist = []
n = 0
o = 0
i = 0
number5 = 0
while n < 6:
    while i < 6:
        number = random.randint(1, 6)
        my_list.append(number)
        if number == 5:
            number5 += 1
        i += 1
        imovirnist.append(number5 / len(my_list))

    n += 1
p = 2
imovirnist2 = imovirnist[p]
print(my_list)
print(number5)
print(imovirnist)
print(imovirnist2)

