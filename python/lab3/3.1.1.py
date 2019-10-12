import sys

fname = sys.argv[1]
lines = 0
words = 0
letters = 0
mostLine = "";
counter = 0;
tempForAlphabet = []
row = []
answer = []
punctuation = ['.', ',', ':', ';', '!', '?', '(', ')','\n']
for line in open(fname):
    lines += 1
    letters += len(line)
    if counter < len(line):
        counter = len(line)
        mostLine = line
    pos = 'out'
    for letter in line:
        if letter != ' ' and pos == 'out':
            words += 1
            pos = 'in'
        elif letter == ' ':
            pos = 'out'
        if letter !=' ' and letter not in punctuation:
            row.append(letter)
    print(row)
    tempForAlphabet.append(row)
    row = []
print("print", tempForAlphabet)
for i in tempForAlphabet:
     answer.append(''.join(sorted(i)))
print(answer)
f = open(fname, 'w')
for i in range(len(answer)):
   f.write(answer[i] + '\n')
print("Lines:", lines)
print("Words:", words)
print("Letters:", letters)
print("Longest line:", mostLine, "\t\t\t(", counter, ")")



