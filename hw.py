# a = input()
# if a == '12' or a == '1' or a == '2':
#     print('Зима')
# elif a == '3' or a == '4' or a == '5':
#     print('Весна')
# elif a == '6' or a == '7' or a == '8':
#     print('Лето')
# elif a == '9' or a == '10' or a == '11':
#     print('Осень')
# else:
#     print('такого месяца нет')
#
# month = input('Введите номер месяца:')
# if int(month)<=0 or int(month)>12:
# print('Неверное номер месяца')
# elif int(month) > 2 and int(month) < 6:
# print ('Весна')
# elif int(month) >5 and int(month) <9:
# print('Лето')
# elif int(month) >8 and int(month) <12:
# print('Осень')
# else:
# print('Зима')

# a = int(input('Р’РІРµРґРёС‚Рµ С‡РёСЃР»Рѕ: '))
# word = 'СЂСѓР±Р»РµР№'
# if a // 10 != 1:
#     if a % 10 in (2, 3, 4):
#         word = 'СЂСѓР±Р»СЏ'
#     elif a % 10 == 1:
#         word = 'СЂСѓР±Р»СЊ'
# print(f'{a} {word}')

#

# fib1 = 1
# fib2 = 1

# rub = input("РџРѕР»СЊР·РѕРІР°С‚РµР»СЊ, РІРІРѕРґРё С‡РёСЃР»Рѕ: ")
# long = len(rub)
# long2 = long - 2
# long1 = long - 1
# rub2 = rub[long2::]
# rub1 = rub[long1::]
# if rub2 in ("11","12","13","14"):
#    print(f'{rub} СЂСѓР±Р»РµР№')
#    exit(0)
# if rub1 in "1":
#    print(f'{rub} СЂСѓР±Р»СЊ')
#    exit(0)
# if rub1 in ("2", "3", "4"):
#    print(f'{rub} СЂСѓР±Р»СЏ')
#    exit(0)
# if rub1 in ("5", "6", "7", "8", "9", "0"):
#    print(f'{rub} СЂСѓР±Р»СЏ')
#    exit(0)
# #

# n = input("Номер элемента ряда Фибоначчи: ")
# n = int(n)
#
# i = 0
# while i < n - 2:
#     fib_sum = fib1 + fib2
#     fib1 = fib2
#     fib2 = fib_sum
#     i = i + 1
#
# print("Значение этого элемента:", fib2)

# num = int(input('Р’С‹Р±РёСЂРµС‚Рµ С‡РёСЃР»Рѕ'))
# if (num == 1):
#     print(num, ' СЂСѓР±Р»СЊ ')
# elif (num == 2 or num == 3 or num == 4):
#     print(num, ' СЂСѓР±Р»СЏ')
# else:
#         print(num, ' СЂСѓР±Р»РµР№')

# n = int(input())
# num_1 = 1
# num_2 = 1
# res = 0
# for i in range(3, n + 1):
#     num_3 = num_1 + num_2
#     res = num_3

#     num_2 = num_1
#     num_1 = num_3

# print(res)

list_listov = [[1, 2], [3, 4], [5, 6]]
onelevle_list = []

# for i in list_listov:
#     onelevle_list.extend(i)
#
# print(onelevle_list)

# names = ['РРІР°РЅ', 'РђР»РёСЃР°', 'РџРµС‚СЂ', 'РћР»СЊРіР°', 'Р•РІРіРµРЅРёСЏ', 'Р”РјРёС‚СЂРёР№', 'Р›Рё']
# names.sort()
#
# for index, name in enumerate(names):
#     print(f"{index+1}. {name}")
#
#
# names = ['РРІР°РЅ', 'РђР»РёСЃР°', 'РџРµС‚СЂ', 'РћР»СЊРіР°', 'Р•РІРіРµРЅРёСЏ', 'Р”РјРёС‚СЂРёР№', 'Р›Рё',]
# names.sort()
# for i in range(len(names)):
#     print(i, names[i])

names = ['РРІР°РЅ', 'РђР»РёСЃР°', 'РџРµС‚СЂ', 'РћР»СЊРіР°', 'Р•РІРіРµРЅРёСЏ', 'Р”РјРёС‚СЂРёР№', 'Р›Рё',]
names.sort()
for i in range(len(names)):
    print(i, names[i])