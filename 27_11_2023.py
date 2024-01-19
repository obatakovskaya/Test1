# a = [1, 2, 'ольга', 'иван', True, False]
#
# a = []# c 0
# list()

# append - добавить в конец списка
# remove - удалить первый совпадающий элемент списка
# pop - удалить элемент по индексу с возможностью сохранить значение в переменной
# clear - очистить список
# sort - отсортировать список
# extend - объединить списки
# index - найти индекс элемента
# insert - вставить элемент по индексу


# 1. append
# a = [1, 2, 3]
# a.append(4)
# print(a)

#
# #2. remove
# a = [1, 2, 3]
# # a.remove(2)
# print(a)

# values = [a[0], a[2]]
# for v in values:
#     a.remove(v)
#     print(a)

# # 3.pop
# a = [1, 2, 3]
# a.pop(1)
# print(a)
#
#  # 4.clear
# a = [1, 2, 3]
# a.clear()
# print(a)


# #5.sort
# a = [1, 5, 3]
# a.sort()
# print(a)

# #6.extend
# a = [1, 2, 3]
# b = [15, 12, 13]
# b.extend(a)
# print(b)
#
# #7.index
# a = [1, 2, 3, 4, 5]
# print(a.index(5))

# #8.insert
# a = [1, 2, 3]
# a.insert(2, 6)
# print(a)

# # Словари {"x": "e", 1: 2, 1: "z"}

# a = {'x': 1, 'y': 2}
# a = dict([(1, 2), [2, 3]])
# print(a)
#
# a_1 = {'a': 1}
# a_1['a'] = 4
# a_1['b'] = 5
# print(a_1)

# clear() - очищает словарь.
# copy() - возвращает копию словаря.
# get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).
# items() - возвращает пары (ключ, значение).
# keys() - возвращает ключи в словаре.
# pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).
# popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError.
# setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).
# update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).
# values() - возвращает значения в словаре.

#clear
# a = {2: 1}
# print(a)
# a.clear()
# print(a)

#copy
# a = {2: 1}
# b = a.copy()
# c = a
# print(b)
# print(a is b) #не является
# print(c is a) #является

# get
# a = {2: 1}
# print(a.get(3, 3))
# print(a.get(1, 3))

# items
# a = {2: 1}
# print(a.items())

#keys
# a = {2: 1, 3: 2}
# print(a.keys())

#pop
# a = {2: 1, 3: 2}
# b = a.pop(3)
# print(b)
# print(a)

# popitem
# a = {2: 1, 'a': 2}
# b = a.popitem()
# print(a)
# print(b)

#setdefault
# a = {2: 1, 'a': 4}
# a.setdefault(3)
# print(a)


#update
# a = {2: 1}
# a.update({'a': 2})
# print(a)

#values
# a = {2: 1, 'a': 4}
# print(a.values())

# Множества
# a = {1, 2, 3}
# a = set()
# print(a)


# Выберите из списка элементы с 4го по предпоследний включительно и выведите на экран
# a = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in range(4, 8):
#     print(i)



# Создайте список словарей, в котором каждый словарь ключами содержит строки, а значениями – множества.


# a = [{"a":(1, 1)}, {"b": (2, 2)}]
# print(a)

# Напишите программу, считающую, сколько раз в строке встречается слово «кот»,
# написанное либо целиком заглавными буквами (КОТ), либо целиком прописными (кот), либо с заглавной буквы (Кот), но не учитывая прочие варианты (кОТ и т. д.).

# sentence = input('Введите строку: ')
#
# total = sentence.count('кот') + sentence.count('КОТ') + sentence.count('Кот')
# print(total)

# Напишите программу, которая превратит список списков списков в одноуровневый список, где все элементы предыдущего списка идут в том же порядке.

# complex_list = [
#     [[1, 2, 3], [4, 5, 6]],
#     [[7, 8, 9], [0, 1, 2]],
#     [[3, 4, 5], [6, 7, 8]],
#     [[9, 0, 1], [2, 3, 4]],
# ]
#
# flat_list = []
#
# for i in complex_list:
#     for j in i:
#         for k in j:
#             flat_list.append(k)
# print(flat_list)
#
# def spisok(listq):
#     listw = []
#     for q1 in listq:
#         for q2 in q1:
#             listw.append(q2)
#
#     return listw
#
# listq = [[1,2], [3,4], [2,3]]
# listw = spisok(listq)
# print(listw)

# for i in range(4):
#     num = int(input())
#     print( 'квадрат вашего числа равен: ' , num * num)
# print('цикл закончился')

# StudensName = ['РРІР°РЅ', 'РђР»РёСЃР°', 'РџРµС‚СЂ', 'РћР»СЊРіР°', 'Р•РІРіРµРЅРёСЏ', 'Р”РјРёС‚СЂРёР№', 'Р›Рё']
# for i in enumerate(sorted(StudensName), start=1):
#     print(*i)


# def flatten_list(nested_list):
#     flattened_list = []
#     for sublist in nested_list:
#         flattened_list.extend(sublist)
#     return flattened_list
# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# flattened_list = flatten_list(nested_list)
# print(flattened_list)
#
# names = ['РРІР°РЅ', 'РђР»РёСЃР°', 'РџРµС‚СЂ', 'РћР»СЊРіР°', 'Р•РІРіРµРЅРёСЏ', 'Р”РјРёС‚СЂРёР№', 'Р›Рё']
# names.sort()
# for a in range(len(names)):
#     print((a + 1), names[a])

# lst = [[1, 2, 3, 4], [5, 6, 7, 8]]
# flat_lst = []
# for i in lst:
#     for j in i:
#         flat_lst.append(j)
# print(flat_lst)

# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# a = a[0] + a[1] + a[2]
# print(a)

# names = ['РРІР°РЅ', 'РђР»РёСЃР°', 'РџРµС‚СЂ', 'РћР»СЊРіР°', 'Р•РІРіРµРЅРёСЏ', 'Р”РјРёС‚СЂРёР№', 'Р›Рё']
#
# sorted_names = sorted(names)
# print('РћС‚СЃРѕСЂС‚РёСЂРѕРІР°РЅРЅС‹Рµ РёРјРµРЅР°:')
# for i, name in enumerate(sorted_names, 1):
# #     print(f'{i}. {name}')
#
# names = ['РРІР°РЅ', 'РђР»РёСЃР°', 'РџРµС‚СЂ', 'РћР»СЊРіР°', 'Р•РІРіРµРЅРёСЏ', 'Р”РјРёС‚СЂРёР№', 'Р›Рё']
# sorted_names = sorted(names)
# for i, name in enumerate(sorted_names, 1):
#     print(f"{i} {name}")

# names = ['Иван', 'Алиса', 'Петр', 'Ольга', 'Евгения', 'Дмитрий', 'Ли']
# sorted_names = sorted(names)
# for i in range(1, len(sorted_names)+1):
#     print(i, sorted_names[i-1])