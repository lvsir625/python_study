data_list=[]
f=open("data.txt", "r", encoding='utf-8')
for line in f:
    l= ",".join(line.split())
    data_list.append(l)
print(data_list)