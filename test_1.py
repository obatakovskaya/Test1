# # Полиндром - это слово или фраза которая одинаково читается слева напрвао или справа налево
# )word = input("введите слово")
#
# if word == word[::-1]:
#     print(f'{word}является плиндромом')
# else:
#     print(f'{word}не является плиндромом'

#
# word = input("введите слово")
# word = word[::-1]
# if word == word:
#     print(word, "палиндром")
# else:
#     print(word, "не палиндром")

string = input ("Введите строку: ")
reversed_string = string[::-1]
if string == reversed_string:
    print(string, "палиндром")
else:
    print(string, "не палиндром")


