# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f'{magician.title()}, that was a great trick!')
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")
#
# #练习4-1
# pizzas = ['A', 'B', 'C']
# for pizza in pizzas:
#     print(f'I like {pizza} pizza.')
# print("I really love pizza!")

# 4.3创建数值列表
# range()函数
for value in range(1,5):
    print(value)

print('\n')
for value in range(6):
    print(value)

print('\n')
# 使用range创建数字列表
squares = []
numbers = list(range(7,10))
for num in numbers:
    num = num ** 2
    squares.append(num)
    print(num)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))

adm = [value ** 2 for value in range(1,11)]
print(adm)

# 练习4-3
for value in range(1,21):
    print(value)
# 练习4-4
users = [value for value in range(1,1000001)]
# for user in users:
#     print(user)

print(min(users))
print(max(users))
print(sum(users))

# 练习4-6
jishus = [value for value in range(1,21,2)]
for js in jishus:
  print(js)

# 练习4-7
shu3 = [value for value in range(3,31,3)]
for s3 in shu3:
  print(s3)

# 练习4-8
shu3 = [value**3 for value in range(1,11)]
for s3 in shu3:
  print(s3)

# 练习4-9
shu3 = [value for value in range(3,31,3)]
for s3 in shu3:
  print(s3)




















