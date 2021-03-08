f = open("user_info.txt", "r")
login_name = input("请输入用户名：")
for line in f:
    if login_name in line:
        for i in range(3):
            login_passwd = input("请输入密码：")
            if login_passwd != line.split()[1]:
                continue
            else:
                print("welcome!")
                break
        print("用户锁定状态")
        break





