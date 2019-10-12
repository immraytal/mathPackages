import math as ma

def distance(x1,y1,x2,y2):
    return ma.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1) )

x1 = int(input("введите x1: "))
y1 = int(input("введите y1: "))
x2 = int(input("введите x2: "))
y2 = int(input("введите y2: "))

print(distance(x1,y1,x2,y2))

def power(a,n):
    p = 1.0
    for i in range(n):
        p = p*a
    return p

print(power(2,3))

def capitalize(str):
    str = list(str)
    str[0] = chr(ord(str[0])-32)
    str = ''.join(str)
    return str

def capitalizeAll(str):
    words = str.split()
    for i in range(len(words)):
        words[i] = capitalize(words[i])
    return ' '.join(words)

print(capitalizeAll('erik pasha alex masha sasha'))

def powerRec(a,n):
    return a*power(a, n-1)

print(powerRec(4,3))

def rec():
    n = int(input("rec:"))
    if n != 0:
        rec()
    print(n)

rec()

def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(int(input("Inout n: "))))


