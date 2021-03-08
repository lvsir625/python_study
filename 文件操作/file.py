# f = open("./1.txt","w")
# f.write("这是一个测数\n")
#f.flush() #将数据从内存刷新到磁盘
#f.truncate(n)  #按指定长度截断文件，不给指定值n的话默认从当前位置截断到文件尾部
# f.close()
"""
f1 = open("1.txt", "r")
# print(f1.read())
f1.seek(n) #n代表邹多少个字节
f1.readlines()

f1.close()
"""
# f2 = open("./1.txt","a")
# f2.write("a b\n")
# f2.close()

#文件是可以以混合模式操作的：如r+   w+  a+
#t是文本默认的编辑模式
#1：读写都以str(unicode)为单位的；读的时候在内存中，数据是utf-8格式的二进制，t模式会将二进制数据解码为unicode格式，即str

with open("./2.txt", "rt", encoding="utf-8") as f:
    read = f.read()
    print(read)
    print("第一次读".center(50,'*'))

















