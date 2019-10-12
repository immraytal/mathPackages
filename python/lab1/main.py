import math
import random

def number():
    x = int(input("Pls input number in range from 1 to 9: \n"))
    if (x > 0 and x < 4):
        s = input("Pls input string\n")
        n = int(input("n?\n"))
        for m in range (0,n):
            print(s)
    elif (x > 3 and x < 7):
        m = int(input("Pls input deg\n"))
        print(x**m)
    elif (x > 6  and x < 10):
        for i in range(0,10):
            x = 1 + x
            print(x)
    else:
        print("Error")

number()

def age():
    print("\t\t\t\t\tОбщество в начале XXI века")
    age = int(input("Возраст\n"))
    if (age >= 0 and age <= 6):
        print("Вам в детский сад")
    elif (age >= 7 and age <= 18):
        print("Вам в школу")
    elif (age >= 19  and age <= 25):
            print("Вам в профессиональное учебное заведение")
    elif (age >= 26  and age <= 60):
        print("Вам на работу")
    elif (age >= 61  and age <= 120):
        print("Вам предоставляется выбор")
    else:
        for i in range(5):
            print("Ошибка! Это программа для людей!")

age()


def Fact():
    x = int(input("Plz input number in range from 1 to 100(FACTORIAL)\n"))
    for i in range(1,x):
        x = x*i
    print(x)

Fact()

def Fi():
    print("Fi:")
    a=1
    b=1
    for i in range(1,50):
        print(a)
        print(b)
        a = a + b
        b = b + a
Fi()

def fib (n):
    fi = (1+math.sqrt(5))/2
    Fn = (fi**n-(-fi)**(-n))/(2*fi-1)
    return int(Fn)

n = int(input("input n(n fibonachi)\n"))
print(fib(n))


def Summofdigits():
    print("summ of digits:")
    x = str(random.randint(100, 999))
    print(x)
    summ = 0
    for i in x:
        summ = summ + int(i)
    return summ

print(Summofdigits())

def CelsInFar():
    temp = input("Введите градусы с обозначением шкалы в конце: ")
    x = temp[-1]
    if (x == 'c' or x == 'C'):
        return (9/5)*float(temp[0:-1]) + 32
    elif (x == 'f' or x == 'F'):
        return (5/9)*(float(temp[0:-1]) - 32)
    else:
        print("Не возможно распознать шкалу")

print(CelsInFar())

def Vis():
    y = int(input('Введите год: '))
    unusual = 'Високосный'
    usual = 'обычный'
    if ( y%4 != 0):
        return usual
    elif ( y%100  == 0):
        if( y%400 == 0 ):
            return unusual
        else:
            return usual
    else:
        return unusual

print(Vis())

def NoD():
    print("NoD: ")
    a = int(input("Введите а: "))
    b = int(input("Введите b: "))

    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a

    return a+b

print(NoD())

def MaxNumber(array):
    print("Search:")
    n = int(input("Какую цифру вы хоитите найти ?: "))
    answarrayind = []
    for i in range(len(array)):
        if(array[i] == n):
            answarrayind.append(i)
    print("Индекс элемента который вы выбрали: ")
    if len(answarrayind)!=0:
        for i in answarrayind:
            print(i + 1)
    else:
        print("Здесь нет вашего числа")

array = [1,3,3,8,15,25,44,45,76,88,99]
print(array)
MaxNumber(array)


def SquareEq():
    print("sq eq:")
    a = []
    b = []
    c = []
    for i in range(int(input("a start: ")), int(input("a finish: "))):
        a.append(i)
    for i in range(int(input("b start: ")), int(input("b finish: "))):
        b.append(i)
    for i in range(int(input("c start: ")), int(input("c finish: "))):
        c.append(i)
    i = 0;
    for i in a:
        for n in b:
            for m in c:
                if (i*i-4*(n*m)>0):
                    print("Комбинации с решением: ", i, "x^2 + ", n, "x + ", m)

SquareEq()

def MaxDigit():
    n = input("Введите цифру(Max digit): ")
    max = -1
    for i in n:
        if(i=='-'):
            continue
        elif(i=='.'):
            continue
        else:
            if(int(i) > max):
                max = int(i)
    return max

print(MaxDigit())

def Palindrom():
    a = input("Введите слово(Palindrom): ")
    b = a[::-1]
    if (a == b):
        print('Yes')
    else:
        print('No')

Palindrom()

def ReplaceString():
    str = input("Введите вашу строку: ")
    old = input("Что надо заменить: ")
    new = input("Чем: ")
    lenold = len(old)

    while str.find(old) > 0:
        i = str.find(old)
        str = str[:i] + new + str[i + lenold:]

    return str

print(ReplaceString())

def LongestWord():
    str = (input("введите строку(longest): "))
    strsplit = str.split()
    longestWord = ''
    for i in strsplit:
        if(len(i) > len(longestWord)):
            longestWord = i
    return longestWord

print(LongestWord())
