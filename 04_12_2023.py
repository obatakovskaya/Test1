import numpy as np #Массивы (float, int) объект array

# a = np.array([1, 2, 3, 8], float)
# # print(a)
# # print(type(a))
# # print(a[:2])
# # print(a[3])
# # a[0] = 5
# # print(a)

# принцип: элемент--элемент.
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

# Создайте массив 100х100 из нулей, массив 100х100 из  единиц, массив 100х100 где по главной диагонали единицы, а все прочие элементы – нули.

zero = np.zeros((100, 100))
print(zero)

one = np.ones((100,100))
print(one)

diag = np.diag(np.ones(100))
print(diag)

# Посчитайте суммы элементов всех массивов.

sum_zeros = np.sum(zero)
sum_one = np.sum(one)
sum_diag = np.sum(diag)

print(sum_zeros + sum_one + sum_diag)

# Создайте массив, где каждый элемент – это сумма соответствующих элементов предыдущих 3 массивов.
sum_all = zero + one + diag
print(sum_all)

# Посчитайте среднее значение элемента в этом новом массиве
print(np.mean(sum_all))