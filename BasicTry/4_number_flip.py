players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[0:3])
# print(players[1:3])
# print(players[:4])
# print(players[2:])
# print(players[-3:])

# 遍历切片
print("Here are the first three players on my team!")
# for player in players[:3]:
    # print(player)
    # print(player.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

# print(f'my food are{my_foods}')
# print(f'firens’s food are {friend_foods}')
#
# print('\n')
my_foods.append("cannoli")
friend_foods.append('ice cream')
# print(f'my food are{my_foods}')
# print(f'firens’s food are {friend_foods}')


# 两个变量名关联到同一个地址，指向同一个列表
her_foods = my_foods
my_foods.append("meat")
her_foods.append('grass')
# print(f'my food are{my_foods}')
# print(f'her food are {her_foods}')

# 练习4-10
# print(f'The first three items in the list are:')
# print(my_foods[:3])
#
# print(f'Three items from the middle of the list are:')
# print(my_foods[2:5])

# print(f'The last three items in the list are:')
# print(my_foods[-3:])

# 练习4-11
pizzas = ['A', 'B', 'C']
friend_pizzas = pizzas[:]
pizzas.append("D")
friend_pizzas.append("E")

print(pizzas)
print(friend_pizzas)

print("My favorite pizzas are:")
for me in pizzas:
    print(me)

print("Her favorite pizzas are:")
for me in friend_pizzas:
    print(me)

















