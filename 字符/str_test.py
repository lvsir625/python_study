#说明，strip() 默认是将字符串的开头和结尾的空格去掉，也可以指定strip('#')
# user=input("输入用户名>>:").strip()
# pwd = input("输入密码>>:")
# if user == "lvsir" and pwd == "123":
#     print("登录成功")
# else:
#     print("用户名或密码错误")

# str = "*****/#alecv****a*****&"
# str=str.strip('*/#&')
# print(str)

#分别去掉左测和右侧指定的字符
# str = "*******asdasd**"
# print(str.lstrip('*'))
# print(str.rstrip('*'))

#分别将字符串转为大写和小写
# str ="alec"
# print(str.upper())
# print(str.lower())

#分别判断字符串是否以指定的字符开头或者结尾，返回bool值
# str = "hello good time ,how are you"
# print(str.startswith("hello"))
# print(str.endswith("you"))

str = "you can you up"
print(str.replace("you","YOU"))


#说明：split后返回一个列表，默认空格是分隔符
# str = "alec:lv:hello:world"
# print(str.split(':'))

#正向取，反向取

str = "alec:lv:hello:world"
#正向取，加上步长
print(str[:5:2])
#反向取，加上步长
print(str[::2])