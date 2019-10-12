import sys

fname = sys.argv[1]
f = open(fname)
symbols = []
lines = f.readlines()
f.close()
f = open(fname, 'w')
for line in lines:
    if len(line.strip('\n').replace(' ','')) != 0:
        f.write(line)
        print(line)
f.close()