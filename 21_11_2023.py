# if
# elif
# else

# x = int(input())
# if x == 5:
#     print('x равно')
# else:
#     print('x не равно')


# x == 5
# x >= 5
# x <= 5
# x != 5

# and логическое умножение
# or логическое сложение
# not логическое отрицание
#in  []

# Напишите условие , проверяющее что число находится в диапозоне от 1 до 100.

# numbers = [i for i in range(1, 101)]
# n = int(input())
# if n in numbers:
#     print("yes")
# else:
#     print("no")

# num = int(input('Введите число: '))
# if 1 <= num <= 100:
#     print('Ваше число от 1 до 100')
# else:
#     print('Ваше число не входит в диапазон от 1 до 100')

# user_input = int(input("Введите число: "))
# if user_input % 10 == 1 and user_input % 100 != 11:
#     print(f'{user_input}рубль')
# elif user_input % 10 in [2, 3, 4] and user_input % 100 not in [12, 13, 14]:
#     print(f'{user_input}рубля')
# else:
#     print(f'{user_input}рублей')

# Перебор строки:
# word = "hello"
# for char in word:
#     print(char)

# Конкатенация(обьединение строк)
# word = 'hello'
# print(word + ' ', 'world')

#Нахождение длины строки
# word = 'hell'
# print(len(word))

# Проверка вхождения в строку:
# word = 'pencil'
# if 'pen' in word:
#     print('yes')

# #Умножение строки на число
# a = 'hello'
# print(a * 3)

#Срезы строк
# s = 'abcdefghij'
# print(s[:-2])
# print(s[5:6])

# a = 1
# print (f'{a} рубль')
# upper - верхний регистр
# lower - нижний регистр
#find -подстрока, ищет в строке подстроку

# words = input('Введите предложение: ').split()
# count = 0
# for word in words:
#     if word == 'кот':
#         count += 1
# print(f'Слово "кот" встречается в строке {count} раз(а)')

# amount_of_rubles = input()
# last_digit = int(amount_of_rubles[-1])
#
# exceptions = ['11', '12', '13', '14']
#
# if not amount_of_rubles in exceptions:
#     if last_digit == 1:
#         print(amount_of_rubles, 'СЂСѓР±Р»СЊ')
#     elif 1 < last_digit <= 4:
#         print(amount_of_rubles, 'СЂСѓР±Р»СЏ')
#     else:
#         print(amount_of_rubles, 'СЂСѓР±Р»РµР№')
# else:
#         print(amount_of_rubles, 'СЂСѓР±Р»РµР№')

# fib1 = 1
# fib2 = 1
#
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

# N = int(input())
# fibonache = 0
# Num = 1
# summa = 1
# for i in range(1, N + 1):
#     print(summa, end=' ')
#     summa = summa + fibonache
#     fibonache = Num
#     Num = summa

