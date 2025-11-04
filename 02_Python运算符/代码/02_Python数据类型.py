# 数据类型：
#   int, float【数字类型：整型int，浮点型[小数]float，复数类型complex 】， 如： 100,  3.14
# 	str【字符串】， 如："hello",  '张三'
# 	bool【布尔类型】：  True真（1）， Flase假（0）
# 	NoneType【空值】 : None
#
# 	list【列表】 类似c语言的数组array， 如： [1, 2, 3]
# 	tuple【元组】 不可改变的列表,  如： (1, 2, 3)
# 	dict【字典】由键值对组成的，如： {"name": "张三",  "age": 30}
# 	set【集合】(了解) ，如： {1, 2, 3}
# 	bytes【字节】二进制， 如：b'hello'

# int 整数
a = 10
print(a, type(a))

# float: 小数
b = 3.14
print(b, type(b))

# str: 字符串 string
c = "hello"
print(c, type(c))

# bool: 布尔类型, True(1), False(0)
d = True
e = False
print(d, type(d))
print(e, type(e))

# NoneType: 空, None
f = None
print(f, type(f))

# list：列表，数组
g = [1, 2, 3]
print(g, type(g))

# tuple： 元组，不可变的列表
h = (1, 2, 3)
print(h, type(h))

# dict: 字典，dictionary
#     key: value  : 键值对
i = {"a": 1, "b": 2.22, "c": "你好"}
print(i, type(i))

# set: 集合（了解）,唯一
j = {1, 2, 3, 3, 3, 4}
print(j, type(j))

# bytes: 字节类型，二进制类型
k = b"hello"
print(k, type(k))
