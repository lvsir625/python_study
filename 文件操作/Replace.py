import sys,os,io
f1 = open("1.txt", "r")
f2 = open("./1.txt.new","w")
old_str="167"
new_str="180"
for line in f1:
    if old_str in line:
        line = line.replace(old_str,new_str)
    f2.write(line)


f1.close()
f2.close()
os.rename("1.txt", "./1.txt.bak")
os.rename("./1.txt.new", "1.txt")