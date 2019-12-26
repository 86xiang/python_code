fi = open("ex0702.py", 'r')
fo = open("f2.txt", 'w')
deleteword = "line"
for line in fi:
    line1 = line.replace(deleteword, "")
    # print(line1)
    fo.write(line1)
fi.close()
fo.close()
