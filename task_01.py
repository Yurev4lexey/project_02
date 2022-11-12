# Задача 1
# Есть строка с перечислением песен
from pprint import pprint


from pprint import pprint
my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

#Var 1_______________________________
song = my_favorite_songs[0:23] + my_favorite_songs[24:]
print(song[:14],'\n',
      song[-14:],'\n',
      song[15:29],'\n',
      song[-27:-15])

#Var 2________________________________  
print(my_favorite_songs[:14]
 + my_favorite_songs[-14:] 
 + my_favorite_songs[15:23]
 + my_favorite_songs[24:30]
 + my_favorite_songs[-27:-15])

# Хорошо. вот еще решение

# Решение с помощью индекции строк

first_song = my_favorite_songs [
    : my_favorite_songs.find(',')
]

last_song = my_favorite_songs [
    my_favorite_songs.rfind('A') :
]

second_song = my_favorite_songs[
     my_favorite_songs.find('N') : 
     my_favorite_songs.find(', S')
]

previous_song = my_favorite_songs [
    my_favorite_songs.rfind('O') : my_favorite_songs.rfind(',')
    ]

print(first_song, last_song, second_song, previous_song)


# Второй вариант, мы можем воспользоваться методом разделения строк по символам. split.
# Полученный в результате список проиндексируем по песням

# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])

