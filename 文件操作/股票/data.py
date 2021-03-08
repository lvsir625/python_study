import sys



print("""
    请选择使用的选项：
    1：输入要查询的股票代码
    2：输入要查询的股票名称关键字
    3：按照价格
    4：按照涨跌幅
    5：按照市盈率
""")



def codechaxun():
    while True:
        codeid = input("请输入要查询的股票代码：")
        f = open("data.txt", "r", encoding='utf-8')
        if len(codeid) == 0:
            print("请输入内容：")
            continue
        elif codeid == "q" or codeid == "Q":
            f.close()
            break
        for line in f:
            if codeid == str(line.split()[1]):
                print(line)


def  namechaxun():
    while True:
        name_key = input("请输入要查询的股票名称关键字：")
        f = open("data.txt", "r", encoding='utf-8')
        for line in f:
            if name_key in str(line.split()[2]):
                print(line)

        if name_key == "q" or name_key == "Q":
            f.close()
            break
def pricechaxun():
    while True:
        pricestr = input("请输入要查询的股票价格条件：")
        f = open("data.txt", "r", encoding='utf-8')
        if "价格" not in pricestr:
            print("请输入价格关键字！")
        elif ">" not in pricestr and "<" not in pricestr:
            print("请输入带有>或者<的符号！")
        elif ">" in pricestr:
            price = int(pricestr.split(">")[1])
            for line in f:
                if int(float(line.split()[6])) > price:
                    print(line)
        elif "<" in pricestr:
            price = int(pricestr.split("<")[1])
            for line in f:
                if int(float(line.split()[6])) < price:
                    print(line)
        elif pricestr == "q" or pricestr == "Q":
            f.close()
            break

while True:
    in_put = int(input("请输入你的选项："))
    if in_put == 1:
        codechaxun()
    elif in_put == 2:
        namechaxun()
    elif in_put == 3:
        pricechaxun()
#    elif str(in_put) == 'q'or str(in_put) == 'Q':
#        break
