# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек



sites = ['Tambov', 'Novgorod', 'Yaroslavl', 'Tver', 'Kostroma']

people = [287407, 224286, 601403, 424969, 277393]

empt = []
empt.append(sites)
empt.append(people)
goroda = empt

#print(goroda[1][1])

print('Население города',(goroda[0][1]),
        '-', (goroda[1][1]), 'человек')