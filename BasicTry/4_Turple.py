#定义元组
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# dimensions[2] = 250   元组禁止修改
my_t = (3)
my_t2 = (3,)
# print(my_t[0])  没有逗号，加上（）也只是int型数据，

for dimension in dimensions:
    print(dimension)

dimensions = (400,100)
for dimension in dimensions:
    print(dimension)


# 练习4-13
foods = ('Guobaorou', 'wuxie', 'wangpangzi', 'zhangqiling', 'wusanxing')
for food in foods:
    print(food)

# foods[1] = "heixiazi"

foods = ('A', 'B', 'C', 'D', 'E')
for f in foods:
    print(f)

