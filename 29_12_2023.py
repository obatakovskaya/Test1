import numpy as np
import pandas as pd


# HW#1 Преобразуйте список чисел в список кортежей (число, квадрат числа) с помощью генераторного выражения.
# numbers = [1, 2, 3, 4, 5]
# result = [(num, num ** 2) for num in numbers]
# print(result)
#
# num = [int(i) for i in input("Введите число:" ).split()]
# tup = [(x, x*x) for x in num]
# print(tup)

# HW#2Выберите из предложенных наборов данных наиболее интересный для вас, и выполните исследовательский анализ данных, следуя шагам, описанным в лекции.

# cereal = pd.read_csv('cereal.csv', sep=',')
# print(cereal)
# print(cereal.head(5))
# print(cereal.tail(5))
# print(cereal.info())
# print(cereal.describe())

#HW3 Сгруппируйте клиентов по стране и посчитайте количество клиентов и средний возраст клиентов для каждой из стран.
# cereal_data = pd.read_csv('cereal.csv')

# Расчет среднего, минимума и максимума
# mean_values = cereal_data.mean(numeric_only=True)
# min_values = cereal_data.min(numeric_only=True)
# max_values = cereal_data.max(numeric_only=True)
#
# # Вывод результатов
# print("Средние значения:")
# print(mean_values)
# print("\nМинимальные значения:")
# print(min_values)
# print("\nМаксимальные значения:")
# print(max_values)