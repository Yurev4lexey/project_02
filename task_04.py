# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random


import random

choice_list =[]



my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

while random.choice(my_favorite_songs):
    i = random.choice(my_favorite_songs)
    choice_list.append(i)

    if len(choice_list) == 3:
            break

s1 = float(choice_list[0][1])
s2 = float(choice_list[1][1])
s3 = float(choice_list[2][1])

print('Три случайных песни звучат:',round(s1 + s2 + s3, 4))
