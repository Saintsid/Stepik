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

# s = input()
# print(s[2], s[-2], s[0:5], s[0:-2], s[0::2], s[1::2], s[::-1], s[::-2], sep='\n')

# s = input()
# pol = int((len(s) + 1) / 2)
# print(s[pol:] + s[:pol])

# s = input()
# if s == s.title():
#     print('YES')
# else:
#     print('NO')

# s = input()
# print(s.swapcase())

# s = input()
# if 'хорош' in s.lower():
#     print('YES')
# else:
#     print('NO')
# print('YES' if 'хорош' in input().lower() else 'NO')

# s = input()
# count = 0
# for i in range(len(s)):
#     if "a" <= s[i] <= "z":
#         count +=1
# print(count)
# print(sum(s.islower() for s in input()))

print(sum(s.islower() for s in input()))
123








