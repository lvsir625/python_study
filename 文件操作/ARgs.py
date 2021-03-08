import sys,os
old_str = sys.argv[1]
new_str = sys.argv[2]
filename = sys.argv[3]
filename_new = "./1.new"
f = open(filename,"r")
f_new = open(filename_new,"w")
for line in f:
    if old_str in line:
        line = line.replace(old_str,new_str)
    f_new.write(line)
f.close()
f_new.close()

os.remove(filename)
os.rename(filename_new,filename)

