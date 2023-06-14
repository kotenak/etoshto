# Задача 1
sales = {}
for _ in range(int(input())):
	name, item, count = input().split()
	sales[name][item] = sales.setdefault(name, {}).setdefault(item, 0) + int(count)
for key in sorted(sales):
	print(f'{key}:')
	for i in sorted(sales[key].items()):
		print(*i)


# Задача2
countries = dict()
country = input()
str_number = 0
while country != "СТОП":
    if country not in countries:
        countries[country] = [str_number]
    else:
        countries[country].append(str_number)
    str_number += 1
    country = input()
for country in countries:
    print(f"{country}: {countries[country]}")

# Задача3
a = [int(i) for i in input().split()]
counter = 0
for i in range(1, len(a) - 1):
    if a[i - 1] < a[i] > a[i + 1]:
        counter += 1
print(counter)

# Задача4
a = [int(s) for s in input().split()]
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(' '.join([str(i) for i in a]))

# Задача5
n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    a[i][n - i - 1] = 1
for i in range(n):
    for j in range(n - i, n):
        a[i][j] = 2
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()

# Задача6
def read_last(lines, file):
	if lines > 0:
		with open(file, encoding='utf-8') as text:
			file_lines = text.readlines()[-lines:]
		for line in file_lines:
			print(line.strip())
		else:
			print('Количество строк может быть только целым положительным')


#Задача7
def fib(n):
	fib0 = 1
	yield fib0
	fib1 = 1
	yield fib1
	for i in range(n - 2):
		fib0, fib1 = fib1, fib0 + fib1
		yield fib1


# Задача 8
import re
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))
points_en = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
points_ru = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
text = input().upper()
if isCyrillic(text):
	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
else:
	print(sum([k for i in text for k, v in points_en.items() if i in v]))

#Задача9
def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st

# Задача 10
def set_gen(lst):

    index = 0
    while index < len(lst):
        cnt = lst.count(lst[index])
        if cnt > 1:
            lst[index] = str(lst[index]) * cnt
        index += 1

    return set(lst)


# Задача 12
y, x = map(int, input().split())

x, y = x - 1, y - 1

board = [[0]*8 for i in range(8)]

board[x][y] = 1

for i in range(x, 7):

   board[i+1][0] += board[i][1]

   for j in range(1, 7):

       board[i+1][j] += board[i][j-1] + board[i][j+1]

   board[i+1][7] += board[i][6]

print(sum(board[7]))

# Задача 13
def lcm(a, b):
	m = a * b
	while a != 0 and b != 0:
		if a > b:
			a %= b
		else:
			b %= a
	return m // (a + b)


while 1:
	try:
		x = int(input('a = '))
		y = int(input('b = '))
		print('НОК:', lcm(x, y))
	except ValueError:
		break

# Задача 14
def GCD_Loop( a, b):
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if(( a % i == 0) and(b % i == 0 )):
            gcd = i
    return gcd
x = int(input(" Enter the first number: ") )
y =int(input(" Enter the second number: "))
num = GCD_Loop(x, y)
print("GCD of two number is: ")
print(num)


