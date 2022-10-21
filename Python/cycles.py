# for i in range(10):
#     print('Python is awesome!')

# a = input()
# b = int(input())
# for i in range(b):
#     print(a)

# for i in range(6):
#     print('AAA')
# for i in range(5):
#     print('BBBB')
# print('E')
# for i in range(9):
#     print('TTTTT')
# print('G')

# a = int(input())
# for i in range(a):
#     print('*' * 19)

# a = input()
# for i in range(10):
#     print(i, a)

# a = int(input())
# for i in range(a + 1):
#     print('Квадрат числа', i, 'равен', i ** 2)

# a = int(input())
# for i in range(a):
#     print('*' * (a - i))

# m, p, n = int(input()), int(input()), int(input())
# for i in range(n):
#     print(i + 1, m * (1 + p / 100) ** i)

# m, n = int(input()), int(input())
# if m < n:
#     for i in range(m, n + 1):
#         print(i)
# else:
#     for i in range(m, n - 1, -1):
#         print(i)

# m, n = int(input()), int(input())
# if m % 2 == 0:
#     for i in range(m - 1, n - 1, -2):
#         print(i)
# else:
#     for i in range(m, n - 1, -2):
#         print(i)

# m, n = int(input()), int(input())
# for i in range(m, n + 1):
#     if i % 17 == 0 or i % 10 == 9 or i % 3 == 0 and i % 5 == 0:
#         print(i)

# n = int(input())
# for i in range(1, 11):
#     print(n, 'x', i, '=', n * i)

# counter = 0
# for i in range(10):
#     num = int(input())
#     if num > 10:
#         counter = counter + 1
# print('Было введено', counter, 'чисел, больших 10.')

# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False

# if num == 1:
#     print('Это единица, она не простая и не составная')
# elif flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# a, b = int(input()), int(input())
# counter = 0
# for i in range(a, b + 1):
#     if i ** 3 % 10 == 9 or i ** 3 % 10 == 4:
#         counter += 1
# print(counter)

# n = int(input())
# counter = 1
# for i in range(1, n + 1):
#     counter *= i
# print(counter)

# counter = 1
# for i in range(1, 11):
#     proiz = int(input())
#     if proiz != 0:
#         counter *= proiz
# print(counter)

# counter = 0
# n = int(input())
# for i in range(1, n + 1):
#     if n % i == 0:
#         counter += i
# print(counter)

# counter = 0
# n = int(input())
# for i in range(1, n + 1):
#     counter += (-1) ** (i + 1) * i
# print(counter)

# max1 = 0
# max2 = 0
# n = int(input())
# for i in range(n):
#     num = int(input())
#     if num > max1:
#         max2 = max1
#         max1 = num
#     elif num > max2 :
#         max2 = num
# print(max1, max2, sep='\n')

# flag = True
# for i in range(10):
#     num = int(input())
#     if num % 2 != 0:
#         flag = False
# if flag == True:
#     print('YES')
# else:
#     print('NO')

# a, b = 0, 1
# n = int(input())
# print(1, end=' ')
# for i in range(1, n):
#     c = a + b
#     print(c, end=' ')
#     a, b = b, c

# text = input()
# total = 0
# while text != 'stop':
#     num = int(text)
#     total += num
#     text = input()
# print('Сумма чисел равна', total)


# i = 7
# a = 5
# while i < 11:
#     a += i
#     i += 2
# print(a)

# text = input()
# while text != 'КОНЕЦ' or text !='конец':
#     print(text)
#     text = input()

# text = input()
# counter = 0
# while text != 'стоп' and text !='хватит' and text !='достаточно':
#     counter += 1
#     text = input()
# print(counter)

# n = int(input())
# counter = 0
# while n < 0:
#     counter += n
#     n = int(input())
# print(counter)


# n = int(input())
# counter = 0
# while 0 <= n <= 5:
#     if n == 5:
#         counter += 1
#     n = int(input())
# print(counter)

# n = int(input())
# counter = 0
# for i in 25, 10, 5, 1:
#     while n - i >= 0:
#         counter += 1
#         n -= i
# print(counter)

# num = int(input())
# while num != 0:
#     print(num % 10, end='')
#     num = num // 10

# num, mi, ma = int(input()), 0, 10
# num1 = num
# while num != 0:
#     if num % 10 > mi:
#         mi = num % 10
#     num = num // 10
# print("Максимальная цифра равна",mi)
# while num1 != 0:
#     if num1 % 10 < ma:
#         ma = num1 % 10
#     num1 = num1 // 10
# print('Минимальная цифра равна', ma)

# num, summa, kol, proiz, perv = int(input()), 0, 0, 1, 0
# posl = num % 10
# while num != 0:
#     summa += num % 10
#     kol += 1
#     proiz *= num % 10
#     perv = num
#     num = num // 10
# print(summa, kol, proiz, summa / kol, perv, perv + posl, sep='\n')

# num = int(input())
# while num > 99:
#     num = num // 10
# print(num % 10)

# num, flag = int(input()), True
# while num > 9 and flag == True:
#     if num % 10 == num % 100 // 10:
#         flag = True
#     else:
#         flag = False
#     num = num // 10
# if flag:
#     print('YES')
# else:
#     print('NO')

# num, flag = int(input()), True
# while num > 9 and flag == True:
#     if num % 10 <= num % 100 // 10:
#         flag = True
#     else:
#         flag = False
#     num = num // 10
# if flag:
#     print('YES')
# else:
#     print('NO')

# n = int(input())
# i = 2
# while i != n:
#     if n % i == 0:
#         break
#     i += 1
# print(i)

# n = int(input())
# for i in range(1, n + 1):
#     if 5 <= i <= 9 or 17 <= i <= 37 or 78 <= i <= 87:
#         continue
#     print(i)
#     i += 1

# num = int(input())
# flag = True
#
# for i in range(2, num):
#     if num % i == 0:
#         flag = False
# if num > 1 and flag == True:
#     print('Число простое')
# else:
#     print('Число составное')

# count = 0
# p = 1                   # two
# for i in range(1, 11):  # one
#     x = int(input())
#     if x >= 0:          # three
#         p = p * x
#         count = count + 1
# if count > 0:
#     print(count)        # four
#     print(p)
# else:
#     print('NO')

# mx = -10000000
# s = 0
# for i in range(10):     # three
#     x = int(input())
#     if x < 0:
#         s += x          # one
#         if mx < x:          # two
#             mx = x
# if mx != -10000000:
#     print(s)
#     print(mx)
# else:                   # four
#     print('NO')

# s = 0                   # three
# for i in range(7):      # one
#     n = int(input())    # two
#     if n % 2 == 0:
#         s = s + n
# print(s)

# n = int(input())
# max_digit = -1                       # one
# while n > 0:
#     digit = n % 10
#     if digit % 3 == 0:
#         if digit > max_digit:       # two
#             max_digit = digit       # three
#     n = n // 10                     # four
# if max_digit == -1:                 # five
#     print('NO')
# else:
#     print(max_digit)

# n = int(input())
# product = 1
# while n != 0:
#     digit = n % 10
#     product = product * digit
#     n = n // 10
# print(product)

# n = int(input())
# counter = 1
# for i in range(n):
#     for j in range(5):
#         print(counter, end=' ')
#     counter += 1
#     print()

# counter = 0
# for i in range(99, 102):
#     temp = i
#     while temp > 0:
#         counter += 1
#         temp //= 10
# print(counter)

# n = int(input())
# for j in range(1, n+1):
#     for i in range(9):
#         print(j, '+', i + 1, '=', j + i + 1)
#     print()

# n = int(input())
# for i in range(n):
#     k = (n // 2 + 1) - abs(n // 2 - i)
#     for i in range(k):
#         print('*', end='')
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(i + 1):
#         print(i + 1, end='')
#     print()

# for a in range(1, 151):
#     for b in range(a, 151):
#         for c in range(b, 151):
#             for d in range(c, 151):
#                 for e in range(d, 151):
#                     if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
#                         print('сумма равна', a + b + c + d + e)
#                         break

# n = int(input())
# counter = 1
# for i in range(n):
#     print()
#     for j in range(i + 1):
#         print(counter, end=' ')
#         counter += 1

# n = int(input())
# counter = 1
# print(1)
# for i in range(n-1):
#     while counter <= i + 1:
#         print(counter, end='')
#         counter += 1
#     while counter > 0:
#         print(counter, end='')
#         counter -= 1
#     print()
#     counter += 1

# a = int(input())
# b = int(input())
# summa = 0
# maxsumma = 0
# nashechislo = 0
# for j in range(a, b + 1):
#     # print('число', j)
#     for i in range(1, j + 1):
#         if j % i == 0:
#             summa += i
#             if maxsumma <= summa:
#                 maxsumma = summa
#                 nashechislo = j
#             # print(i)
#     # print('summa', j, 'равна', summa)
#     summa = 0
# print(nashechislo, maxsumma)

# n = int(input())
# counter = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         counter += 1
#     print(i, '+', '+' * counter)
#     counter = 0

# a = int(input())
# b = int(input())
# for i in range(a, b + 1):
#     for j in range(a, i):
#         if i % j == 0:
#             print(j)

# i = 4
# counter = 0
# while i <= 10:
#     print ('Python!')
#     i += 1
#     counter += 1
# print(counter)

# n = int(input())
# s = 0
# while n > 0:
#     if n % 2 == 0:
#         s += n % 10
#     n //= 10
# print(s)

# n = 8
# count = 0
# maximum = -10 ** 12
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 4 == 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = 4
# count = 0
# maximum = -10 ** 8
# for i in range(1, n + 1):
#     x = int(input())
#     if x % 2 != 0:
#         count += 1
#         if x > maximum:
#             maximum = x
# if count > 0:
#     print(count)
#     print(maximum)
# else:
#     print('NO')

# n = int(input())
# print('*' * 19)
# for i in range(1, n - 1):
#     print('*', ' ' * 17, '*')
# print('*' * 19)

# n = int(input())
# while n > 99:
#     chislo = n % 10
#     n //= 10
# print(chislo)

# n = int(input())
# count3 = 0
# countlastdigit = 0
# lastdigit = n % 10
# countchet = 0
# countchiselb5 = 0
# countchiselb7 = 1
# countchiselot0do5 = 0
# while n > 0:
#     if n % 10 == 3:
#         count3 += 1
#     if n % 10 == lastdigit:
#         countlastdigit += 1
#     if n % 2 == 0:
#         countchet += 1
#     if n % 10 > 5:
#         countchiselb5 += n % 10
#     if n % 10 > 7:
#         countchiselb7 *= n % 10
#     if n % 10 == 0 or n % 10 == 5:
#         countchiselot0do5 += 1
#     n //= 10
#
# print(count3, countlastdigit, countchet, countchiselb5, countchiselb7, countchiselot0do5, sep='\n')

# import timeit
#
# code_to_test = """
# for a in range(1, 100):
#     for c in range(1, a):
#         for d in range(1, c+1):
#             for b in range(1, d):
#                 if a**3 + b**3 == d**3 + c**3:
#                     print(a**3+b**3)
# """
# elapsed_time = timeit.timeit(code_to_test, number=1)
# print(elapsed_time)

# import timeit
#
# code_to_test = """
# n = 50000
# for i in range(1, n + 1):
# 	count = 0
# 	for x in range(1, int(i**(1/3)) + 1):
# 		for y in range(x, int(i**(1/3)) + 1):
# 			if x**3 + y**3 == i:
# 				count += 1
# 			elif x**3 + y**3 > i:
# 				break
# 	if count >= 2:
# 		print(i)
# """
# elapsed_time = timeit.timeit(code_to_test, number=1)
# print(elapsed_time)














