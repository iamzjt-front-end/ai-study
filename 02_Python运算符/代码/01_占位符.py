# f-string (重点掌握)
name = "杰伦"
age = 45
salary = 1.4567

# print("大家好，我是杰伦，我今年45，我的年薪1.4567亿")


# 占位符：（建议掌握）
#   %s : 字符串
#   %d : 整数
#   %f : 小数   %.4f表示保留4位小数，四舍五入
#   %% : 百分号
print("大家好，我是%s，我今年%d，我的年薪%.4f亿" % (name, age, salary))
num = 3.1415926


# 花括号占位符.format() （了解）
print("大家好，我是{}，我今年{}，我的年薪{}亿".format(name, age, salary))

print("我叫{0}，今年{1}岁。{0}喜欢Python。".format(name, age))
print("我叫{name}，今年{age}岁。".format(name="王五", age=22))


# 练习：
# 请输入您的姓名，年龄，身高，体重，其中姓名是字符串，年龄是整数，身高和体重是小数类型，
# 要求分别使用上面3种占位符方式输出内容：
#    "大家好，我是xxx, 今年xxx岁，我身高是xx.xcm，体重是xx.xkg"
#
#  例如："大家好，我是Jack, 今年25岁，我身高是177.5cm，体重是75.2kg"

name = input("姓名:")
age = int(input("年龄:"))
height = float(input("身高："))
weight = float(input("体重："))
print(
    "大家好，我是%s, 今年%d岁，我身高是%dcm，体重是%.1fkg" % (name, age, height, weight)
)
print(
    "大家好，我是{}, 今年{}岁，我身高是{}cm，体重是{}kg".format(
        name, age, height, weight
    )
)
print(
    "大家好，我是{name}, 今年{age}岁，我身高是{height}cm，体重是{weight}kg".format(
        name="Jack", age="25", height="177.5", weight="75.2"
    )
)

print(f"我叫{name}，今年{age}岁")
