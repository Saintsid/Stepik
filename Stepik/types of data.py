# a = float(2)
# print(a)

# a, b = input(), input()
# s = float(a) * float(b) / 2
# print(s)

# s, a, b = float(input()), float(input()), float(input())
# result = s / (a + b)
# print(result)

# a = float(input())
# if a != 0:
#     print(1 / a)
# else:
#     print('Обратного числа не существует')

# f = float(input())
# c = 5 * (f - 32) / 9
# print(c)

# age = float(input())
# a, b = 10.5, 4
# if 0 < age <= 2:
#     print(age * a)
# else:
#     print(2 * a + (age - 2) * 4)

# a = float(input())
# print(int(a * 10 % 10))

# a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
# print("Наименьшее число =", min(a, b, c, d, e))
# print("Наибольшее число =", max(a, b, c, d, e))

# a, b, c = int(input()), int(input()), int(input())
# minim = min(a, b, c)
# maxim = max(a, b, c)
# if minim < a < maxim:
#     print(maxim, a, minim, sep='\n')
# elif minim < b < maxim:
#     print(maxim, b, minim, sep='\n')
# elif a == b:
#     print(a, b, c, sep='\n')
# else:
#     print(maxim, c, minim, sep='\n')

# a = int(input())
# b = a // 100
# c = a // 10 % 10
# d = a % 10
# minim = min(b, c, d)
# maxim = max(b, c, d)
#
# print(b, c, d)
# print(maxim - minim)
#
# #if minim - maxim == b or minim - maxim == c or minim - maxim == d:
#     # print('Число интересное')
# #else:
#     # print("Число неинтересное")

# a, b, c, d, e = float(input()), float(input()), float(input()), float(input()), float(input())
# print(abs(a) + abs(b) + abs(c) + abs(d) + abs(e))

# p1, p2, q1, q2 = int(input()), int(input()), int(input()), int(input())
# print(abs(p1 - q1) + abs(p2 - q2))

#print('"Python is a great language!", said Fred. ', '"I don', "'", 't ever remember having this much fun before."', sep='')

#print('Hello ', input(),' ', input(),'! You just delved into Python', sep='')

# a = input()
# print('Футбольная команда', a, 'имеет длину', len(a), 'символов')

# a, b, c = input(), input(), input()
# if min(len(a), len(b), len(c)) == len(a):
#     print(a)
# elif min(len(a), len(b), len(c)) == len(b):
#     print(b)
# else:
#     print(c)
# if max(len(a), len(b), len(c)) == len(a):
#     print(a)
# elif max(len(a), len(b), len(c)) == len(b):
#     print(b)
# else:
#     print(c)

# a, b, c = len(input()), len(input()), len(input())
# if a - b == b - c or a - c == c - b or c - a == a - b:
#     print('YES')
# elif c - b == b - a or b - c == c - a or b - a == a - c:
#     print('YES')
# else:
#     print('NO')

# a = input()
# if '@' in a and '.' in a:
#     print('YES')
# else:
#     print('NO')

# from math import sqrt, pow
# x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
# print(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

# from math import pi
# r = float(input())
# print(pi * r ** 2, 2 * pi * r, sep='\n')

# from math import sqrt
# a, b = float(input()), float(input())
# print((a + b)/ 2, sqrt(a * b), 2 * a * b / (a + b), sqrt((a ** 2 + b ** 2) / 2), sep='\n')

# from math import *
# x = float(input())
# print(sin(radians(x)) + cos(radians(x)) + tan(radians(x)) ** 2)

# from math import *
# a, b, c = float(input()), float(input()), float(input())
# D = b ** 2 - 4 * a * c
# if D > 0:
#     print(min(((-b + sqrt(D)) / (2 * a)), (-b - sqrt(D)) / (2 * a)))
#     print(max(((-b + sqrt(D)) / (2 * a)), (-b - sqrt(D)) / (2 * a)))
# elif D == 0:
#     print(-b / (2 * a))
# elif D < 0:
#     print('Нет корней')

from math import *
n, a = float(input()), float(input())
print(n * a ** 2 / (4 * tan(pi/n)))














