# s = input()
# flag = False
# for i in range (0, 10):
#     for j in range(0, len(s)):
#         if str(i) == s[j]:
#             flag = True
# if flag == True:
#     print('Цифра')
# else:
#     print("Цифр нет")

# totalp, totalz = 0, 0
# for j in input():
#     if j == '+':
#         totalp += 1
#     if j == '*':
#         totalz += 1
# print('Символ + встречается', totalp, 'раз')
# print('Символ * встречается', totalz, 'раз')

# total = 0
# s = input()
# for i in range(1, len(s)):
#     if s[i] == s[i - 1]:
#         total += 1
# print(total)

# totals = 0
# totalg = 0
# # for i in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
# #     for j in range(len(s)):
# #         if s[j] == i:
# #             totalg +=1
# # for i in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
# #     for j in range(len(s)):
# #         if s[j] == i:
# #             totals +=1
# for i in input():
#     if i in 'ауоыиэяюёеАУОЫИЭЯЮЁЕ':
#         totalg += 1
#     if i in 'бвгджзйклмнпрстфхцчшщБВГДЖЗЙКЛМНПРСТФХЦЧШЩ':
#         totals += 1
# print('Количество гласных букв равно', totalg)
# print('Количество согласных букв равно', totals)

# s = int(input())
# chislo = ''
# while s > 0:
#     chislo = str(s % 2) + chislo
#     s //= 2
# print(chislo)
































