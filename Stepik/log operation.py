# a = int(input())
# if a >= 2 and a <= 17:
#     b = 3
#     p = a * a + b * b
# else:
#     b = 5
# p = (a + b) * (a + b)
# print(p)
#
# a = int(input())
# if -1 < a < 17:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# a = int(input())
# if -30 < a <= -2 or 7 < a <= 25:
#     print('Принадлежит')
# else:
#     print('Не принадлежит')


# a = int(input())
# if 0 < a // 1000 < 10 and (a % 7 == 0 or a % 17 == 0):
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# b = int(input())
# c = int(input())
# if a + b > c and a + c > b and b + c > a:
#     print('YES')
# else:
#     print('NO')

# year = int(input())
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print('YES')
# else:
#     print('NO')

# a = input()
# b = input()
# if a == 'красный' and b == 'синий' or b == 'красный' and a == 'синий':
#     print('фиолетовый')
# elif a == 'красный' and b == 'желтый' or b == 'красный' and a == 'желтый':
#     print('оранжевый')
# elif a == 'синий' and b == 'желтый' or b == 'синий' and a == 'желтый':
#     print('зеленый')
# elif a == 'синий' and b == 'синий':
#     print('синий')
# elif a == 'красный' and b == 'красный':
#     print('красный')
# elif a == 'желтый' and b == 'желтый':
#     print('желтый')
# else:
#     print("ошибка цвета")


# a = int(input())
# if a == 0:
#     print('зеленый')
# elif 1 <= a <= 10 or 19 <= a <= 28:
#     if a % 2 == 0:
#         print('черный')
#     else:
#         print("красный")
# elif 0 <= a <= 36:
#     if a % 2 != 0:
#         print('черный')
#     else:
#         print("красный")
# else:
#     print('ошибка ввода')

# a1 = int(input())
# b1 = int(input())
# a2 = int(input())
# b2 = int(input())
# if a1 < a2 and b1 < b2 and a2 < b1:
#     print(a2, b1)
# elif a1 < a2 and b1 > b2:
#     print(a2, b2)
# elif a1 > a2 and b1 > b2 and a1 < b2:
#     print(a1, b2)
# elif a1 > a2 and b1 < b2:
#     print(a1, b1)
# elif a1 == a2 and b1 == b2:
#     print(a1, b1)
# elif a1 == a2 and b1 < b2:
#     print(a1, b1)
# elif a1 == a2 and b1 > b2:
#     print(a2, b2)
# elif a1 > a2 and b1 == b2:
#     print(a1, b1)
# elif a1 < a2 and b1 == b2:
#     print(a2, b2)
# elif b1 == a2:
#     print(a2)
# elif b2 == a1:
#     print(a1)
# else:
#     print('пустое множество')

# year = int(input())
# if year % 100 == 0:
#     print('YES')
# else:
#     print('NO')

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a % 2 != 0 and b % 2 != 0 or a % 2 == 0 and b % 2 == 0:
#     if c % 2 != 0 and d % 2 != 0 or c % 2 == 0 and d % 2 == 0:
#         print('YES')
#     else:
#         print('NO')
# elif a % 2 != 0 and b % 2 == 0 or a % 2 == 0 and b % 2 != 0:
#     if c % 2 == 0 and d % 2 != 0 or c % 2 != 0 and d % 2 == 0:
#         print('YES')
#     else:
#         print('NO')

# age = int(input())
# sex = input()
# if 10 <= age <= 15 and sex == 'f':
#     print('YES')
# else:
#     print('NO')

# a = int(input())
# if a == 1:
#     print('I')
# elif a == 2:
#     print('II')
# elif a == 3:
#     print('III')
# elif a == 4:
#     print('IV')
# elif a == 5:
#     print('V')
# elif a == 6:
#     print('VI')
# elif a == 7:
#     print('VII')
# elif a == 8:
#     print('VIII')
# elif a == 9:
#     print('IX')
# elif a == 10:
#     print('X')
# else:
#     print('ошибка')

# n = int(input())
# if n % 2 != 0:
#     print('YES')
# elif n % 2 == 0 and 2 <= n <= 5:
#     print('NO')
# elif n % 2 == 0 and 6 <= n <= 20:
#     print('YES')
# elif n % 2 == 0 and n > 20:
#     print('NO')

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a - 2 == c and b + 1 == d or a - 1 == c and b + 2 == d:
#     print('YES')
# elif a + 1 == c and b + 2 == d or a + 2 == c and b + 1 == d:
#     print('YES')
# elif a + 2 == c and b - 1 == d or a + 1 == c and b - 2 == d:
#     print('YES')
# elif a - 1 == c and b - 2 == d or a - 2 == c and b - 1 == d:
#     print('YES')
# else:
#     print('NO')

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (c - d) == (a - b) or (c + d) == (a + b) or c == a or d == b:
#     print('YES')
# else:
#     print('NO')










