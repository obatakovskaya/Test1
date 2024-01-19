import numpy as np

#Массивы (float, int)
# Массив из списка

# a = np.array([1, 2, 3, 8], float)
# print(a)
# print(type(a))
# print(a[:2])
# print(a[3])
# a[0] = 5
# print(a)
#
# # элемент- элемент
#
# a = np.array([1, 2, 3], float)
# b = np.array([5, 2, 6], float)
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b)
# print(a**b)

# a = np.array([[1, 2], [1, 3]], float)
# b = np.array([[5, 2], [1, 3]], float)
# print(a*b)
# ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (2,) + inhomogeneous part.

#Создать массив 100*100 из нулей, массив 100*100 из единиц, массив 100*100 где по главной диагонали еденицы а все прочие элементы нули


zero = np.zeros((10, 10))
# print(zero)

one = np.ones((100,100))
# print(one)

diag = np.diag(np.ones(10))
# print(diag)

s = np.sum(one)
print(s)
s_1 = np.sum(zero)
print(s_1)
s_2 = np.sum(diag)
print(s_2)


# array = [[0 for _ in range(100)] for _ in range(100)]
# print(array)
# Посчитайте суммы элементов всех массивов.

# Создайте массив, где каждый элемент – это сумма соответствующих элементов предыдущих 3 массивов.

sum_all = s + s_1 + s_2
print(sum_all)

# Посчитайте среднее значение элемента в этом новом массиве.
print(np.mean(sum_all))
