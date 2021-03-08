#将gbk编码的文件内容转换为utf-8的格式，思路就是先将gbk转换为unicode格式，再由unicode编码的格式转换为utf-8格式
f=open("win_data.txt", "rb")   #以gbk编码 二进制格式打开文件
bytes_f = f.read()
unicode_f = bytes_f.decode("gbk")  #将文件的二进制内容以gbk进行解码为unicode字符串
f.close()
utf8_f = unicode_f.encode("utf-8")  #将unicode字符串的内容以utf-8的格式的编码为二进制格式
f= open("win_data.txt", "wb")
f.write(utf8_f)
# print(type(utf8_f))
f.close()
