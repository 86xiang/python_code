fi = open("ex0701.py", 'r')
fo = open("f2.txt", 'w')
for line in fi:
    line = line.upper()
    fo.write(line)

fi.close()
fo.close()
