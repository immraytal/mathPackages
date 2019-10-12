import sys
fname = sys.argv[1]
fname2 = sys.argv[2]
fname3 = sys.argv[3]

def lenfile(fname):
    lines = 0
    letters = 0
    for line in open(fname):
        lines += 1
        letters += len(line)
    return letters




min= ""
max= ""

len1 = lenfile(fname)
len2 = lenfile(fname2)
len3 = lenfile(fname3)

print(len1, len2, len3)

files = []

files.append(len1)
files.append(len2)
files.append(len3)

files.sort()

if files[0]==len1:
    min = fname
elif files[0]==len2:
    min = fname2
else:
    min = fname3

if files[2]==len1:
    max = fname
elif files[2]==len2:
    max = fname2
else:
    max = fname3


print(max, min)


bufMax = open(max).readlines()
bufMin = open(min).readlines()


for i in bufMax:
    open(min, 'w').write(i)

for i in bufMin:
    open(max, 'w').write(i)



