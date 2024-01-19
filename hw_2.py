# count = [x for x in range(10)]
# s = [(a, a ** 2) for a in count]
# s = list(s)
# print(s)
#
# my_list = [1, 2, 3, 4, 5, 6]
# my_list = list((x, x ** 2) for x in my_list)
# print(my_list)

# names = ['РРІР°РЅ', 'РђР»РёСЃР°', 'РџРµС‚СЂ', 'РћР»СЊРіР°', 'Р•РІРіРµРЅРёСЏ', 'Р”РјРёС‚СЂРёР№', 'Р›Рё']
# names.sort()
# for i in names:
#     a = ''
#     a += str(i)
#     print(names.index(a) + 1, a)

numbers = [1, 2, 3, 4, 5]

squares = tuple(x**2 for x in numbers)

print(squares)

# РЎРѕР·РґР°С‚СЊ РіРµРЅРµСЂР°С‚РѕСЂ, РєРѕС‚РѕСЂС‹Р№ Р±СѓРґРµС‚ РіРµРЅРµСЂРёСЂРѕРІР°С‚СЊ РєРІР°РґСЂР°С‚С‹ С‡РёСЃРµР» РѕС‚ 1 РґРѕ 10
squares = (x**2 for x in range(1, 11))
# for square in squares:
#     print(square)