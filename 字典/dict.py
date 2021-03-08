#字典是python中唯一的映射关系
#定义：{k1:v1,k2:v2}
#特性： k-v结构；key必须为不可变数据类型，必须唯一；可存放任意多个value，可修改，可以不唯一；无序；查询速度快，且不受dict大小影响


#字典的创建
person = {"name":"alec","age":20}
#获取键值
for k,v in person.items():
    print(k,v)
#或
person = dict(name="alec",age=20)
#获取键值
for k,v in person.items():
    print(k,v)
#或
person = dict({"name":"asd","age":20})
#获取键值
for k,v in person.items():
    print(k,v)

#增加键值操作
#方式一
person["job"]="IT"
print(person)
#方式二:比较安全添加kv的操作，假如字典中已经有了要添加的key，则不会之前的值不会被修改，可与方式一的对比
person.setdefault("job","teacher")  #dict.setdefault(k,v)
print(person)

#删除指定的键
person.pop("job")
print(person)

#清空字典
# person.clear()
# print(person)

#修改操作
#方式一：
person["name"]="lvsir"
print(person)
#方式二,将字典2的键值更新到字典一，
person2={"age":18,"job":"teacher"}
person.update(person2)
print(person)

#查操作
#方式一：
print(person["age"])
#方式二：第二个参数是查不到值时返回的
print(person.get("agee",-1))
#查看所有key
print(person.keys())
#查看所有有value
print(person.values())
#查看所有键值对
print(person.items())

#循环
#只打印key
for k in person.keys():
    print(k)

#只打印value
for v in person.values():
    print(v)

#同时打印key，value
#方式一：
for k,v in person.items():
    print(k,v)

#方式二：这种方式效率 最快,推荐用这种
for k in person:
    print(k,person[k])