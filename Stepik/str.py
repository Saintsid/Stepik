# небольшой комментарий на тему комментариев
# s = 'abcdef'
# for r in s:
#     print(r)

# s = 'abcdefg'
# print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)

# s = '01234567891011121314151617'
# for i in range(0, len(s), 5):
#     print(s[i], end='')

# s = "In 2010, someone paid 10k Bitcoin for two pizzas."
# for i in range(len(s)):
#     if s[i] == 'w':
#         print(s[i])

# s = input()
# for i in range(len(s)):
#     if i % 2 == 0:
#         print(s[i])

# s = input()
# for i in range(-1, -len(s) - 1, -1):
#     print(s[i])

# name = input()
# surname = input()
# parentname = input()
# print(surname[0], name[0], parentname[0], sep='')

# s = input()
# total = 0
# for i in range(len(s)):
#     total += int(s[i])
# print(total)

# s = input()
# flag = False
# for i in range(len(s)):
#     if s[i] == '0123456789':
#         flag = True
# if flag == True:
#     print('Цифра')
# else:
#     print('Цифр нет')

s = input()
l = s.lower()
print('Аденин:', l.count('a'))
print('Гуанин:', l.count('г'))
print('Цитозин:', l.count('ц'))
print('Тимин:', l.count('т'))


























