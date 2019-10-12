import random as rand

def phone(fname):
    file = open(fname)
    lines = file.readlines()
    file.close()
    abonents = []
    for line in lines:
        phone = []
        bill = 0
        phone.append(line[:6])
        phoneStr =str( ''.join(phone))
        bill = bill + int(line[7:])
        abonent = {'phone': phoneStr, 'bill': bill}
        abonents.append(abonent)
    number = input('input phone number ypu want to find: ')
    answ = 0
    for i in abonents:
        if i['phone'] == number:
            answ += i['bill']

    return answ

def generate(fname):
    f = open(fname, 'w')
    for i in range(1, 1000):
        row = []
        for k in range(6):
            row.append(str(rand.randint(0,9)))
        row.append(":")
        row.append(str(rand.randint(0,100)))
        f.write(''.join(row)+'\n')

file = ('phone.txt')
print(phone(file))