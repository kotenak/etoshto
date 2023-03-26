# 1
'''a = [1, 2, 3, 4, 5]
print(a[0], a[2], a[-2])'''

# 2
'''a=[1,2,3,4,5,6,7,8,9]
N=int(input())
if N<=len(a):
    print(a[N]**N)
else:
    print(-1)'''

# 3
'''a='flashfufel'
s='f'
k=0
for i in range (0, len(a)):
    if a[i]==s:
        k+=1
    if k==2:
        print(i)
        break'''


# 4
'''num = '01000110010000'
num = num[::-1]
print(num)
b = 0
for n in num:
    if n == '0':
        b += 1
    else:
        break
print(b)'''

#5
'''n= input()[::-1]
print(n)'''

# 6
'''a = input()
v = False
for i in range(0, len(a)-1):
    if b[i] == b[i+1]:
        v = True
    else:
        v = False
        break
print(c)'''

#7
'''p = str(input())
while len(p) < 16:
    p = input()
a, b, c, d = False, False, False, True
for m in p:
    if m.isupper():
        a = True
    elif m.islower():
        b = True
    elif m.isnumeric():
        c = True
    else:
        d = False
if a and b and c and d:
    print('Безопасный пароль')
else:
    print('Небезопасный пароль')'''

#8
'''def F(d):
    for i in d:
        if type(i) is list:
            F(i)
        else:
            print(i,end=' ')
    return
n=[1,[2,3],[4,[5,6]]]
F(n)'''

#9
'''a = {'Один': 1,'Четыре': 4, 'Два': 2, 'Три': 3}
max=0
for k, с in a.items():
    if с > max:
        max=с
        key=k
print(key)'''


#10
'''def F(a):
    X = []
    for i in a:
        if a.count(i)>1:
            X.append(i)
    return X

print(F([1,2,2,2,5,8,1]))'''


