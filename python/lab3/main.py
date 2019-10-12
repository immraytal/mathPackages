import math as ma
import random as rand


def countOddAndEvenDigits(arr):
    odd = 0
    even = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            even += 1
        else:
            odd += 1
    print("even = ", even)
    print("odd = ", odd)

arr1 = []
for i in range(rand.randint(1, 25)):
    arr1.append(rand.randint(-25, 25))
print("arr1", arr1)
countOddAndEvenDigits(arr1)

def plusAndMinus(arr):
    plus = []
    minus = []
    for i in range(len(arr)):
        if arr[i] < 0:
            minus.append(arr[i])
        else:
            plus.append(arr[i])
    print("plus" ,plus)
    print("minus", minus)

plusAndMinus(arr1)

def replace(arr):
    answer = []
    for i in range(len(arr)):
        if arr[i] < 0:
            answer.append(-1)
        elif arr[i] > 0:
             answer.append(1)
        else:
             answer.append(0)
    print("replace", answer)

replace(arr1)

def deletePoints(str):
    punctuation = ['.', ',', ':', ';', '!', '?', '(', ')']
    wordList = str.split()
    i = 0
    for word in wordList:
        if word[-1] in punctuation:
            wordList[i] = word[:-1]
            word = wordList[i]
        if word[0] in punctuation:
            wordList[i] = word[1:]
        i += 1

    i = 0
    while i < len(wordList):
        print(wordList[i], end=' ')
        i += 1

str = "one (two) three, four! five."
deletePoints(str)

def columnWithMax(matrix):
    maxRow = 0
    idRow = 0
    i = 0
    for row in matrix:
        if sum(row) > maxRow:
            maxRow = sum(row)
            idRow = i
        i += 1

    print(idRow, '-', maxRow)

    maxCol = 0
    idCol = 0
    for i in range(5):
        colSum = 0
        for j in range(5):
            colSum += matrix[j][i]
        if colSum > maxCol:
            maxCol = colSum
            idCol = i

    print(idCol, '-', maxCol)

print()

matrix = []

for i in range(5):
    row = []
    for j in range(5):
        row.append(rand.randint(1, 5))
    matrix.append(row)

for row in matrix:
    print(row)

columnWithMax(matrix)

def existNumber(matrix):
    item = int(input("Number range(1,5): "))

    print("index(i,j):", end=" ")
    for i in range(5):
        for j in range(5):
            if matrix[i][j] == item:
                print(i, j, end="   ")
    print()

existNumber(matrix)


def mostCommon(a):

    a_set = set(a)

    most_common = None
    qty_most_common = 0

    for item in a_set:
        qty = a.count(item)
        if qty > qty_most_common:
            qty_most_common = qty
            most_common = item

    print("most common", most_common)

a=[1, 2, 2, 2, 1, 3, 2, 0, 2, 1, 3, 2, 4, 0, 4]
mostCommon(a)

