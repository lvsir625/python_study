#集合和列表有点像，也是可以存一堆数据，不过他有几个单独的特点，令其在整个python语言中占有一席之地
# 1：里面的元素不可改变，代表不能存一个list，dict在里面，字符串，数字，元组等不可变类型可以存
#2：天生去重，在集合里没办法存重复的元素
#3： 无序，不想列表一样通过索引来标记在列表中的位置，元素是无序的，集合中的元素没有先后之分

#去重
s1 = {1,2,3,4,3,"alec","su",2}
print(s1)
#通过集合去重将列表里的重复元素去重
l1 = [1,2,3,4,3,"alec","su",2]

l2=list(set(l1))
print(l2)

#增加元素
s1.add(5)
print(s1)

#删除元素
#方式一：删除指定元素，不存在的话不报错
s1.discard(3)
#方式二： 随机删除并返回
s1.pop()
#方式三：删除指定元素，不存在的报错
#s1.remove(6)


#查元素  ，in
print("alec"  in s1)

#关系运算

s2 = {"yanguo","guojing","huangyaoshi","duanyu","qiaofeng"}
s3 = {"qiaofeng","jiumozhi","zhangwuji","duanyu","dignbusan"}
#交集
print(s2&s3)
#=或，并集或合集
print(s2|s3)
#在s2中不在s3，差集
print(s2-s3)
#既不在s2中也不在s3中的元素
print(s2^s3)


#两个集合之间一般有三种关系，相交，包含，不相交

#判断两个集合是不是相交
print(s2.isdisjoint(s3))
#判断s2是不是s3的子集
print(s2.issubset(s3))
#判读s2是不是s3d的父集
print(s2.issuperset(s3))