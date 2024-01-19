# while - мы не знаем количество повторений, будет поторяться цикл пока условие истинно


#while условие:
    #блок кода

# True/False

# i = 0
# while i < 10:
#     print('Привет')
#     i += 1

# num = int(input())
# while num != -1:
#     print('Квадрат вашего числа  равен:', num * num)
#     num = int(input())
#
# while True:
#     num = input()
#     if num == 'stop':
#         break

# i = 0
# total = 0
# while i < 10:
#     total += i
#
# result = 0
# for i in range(10):
#     num = int(input())
#     if num < 0:
#         break
#     result += num
#     print(result)
#
# n = int(input())
# flag = False
# while n != 0:
#     last_diqit = n % 10
#     if last_diqit == 7:
#         flag = True
#         break
#     n //= 10
# if flag == True:
#     print('число n содержит 7')
# else:
#     print('число n не содержит 7')

for i in range(1, 101):
    if i == 7 or i == 9:
        continue
    print(i)




