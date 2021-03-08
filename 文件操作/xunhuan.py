# f = open("./1.txt","r")
# for line in f.readlines():
#     print(line)
# f.close()
#
# with open("./1.txt","r") as f:
#     for line in f.readlines():
#         print(line)
name_list=[]
#默认使用t模式编辑文本
with open("1.txt", "rt") as f:
    for line in f.readlines():
        if int(line.split()[2]) >= 175:
            name_list.append(line.split()[0])
print(name_list)