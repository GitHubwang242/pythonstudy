# 列表排序
cars = ['bmw', 'audi', 'toyota', 'subaru']   #字母正序
cars.sort()
print(cars)


# 字幕反序，永久修改
cars.sort(reverse= True)
print(cars)

# sorted临时排序
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the Fsorted list:")
cars_sorted = sorted(cars,reverse=True)    #永久排序
print(cars_sorted)

print("\nHere is the original list again:")
print(cars)


# 倒序打印列表
print("倒序输出")
cars.reverse()
print(cars)



# 确定列表长度
print(len(cars))


# 练习3-8
print(f'我会邀请{len(cars)}位客人')




















