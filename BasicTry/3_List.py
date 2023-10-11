bicycle = ['trek', 'cannondale', 'redline', 'specialized']

# 打印列表，输出['trek', 'cannondale', 'redline', 'specialized']
print(bicycle)


# 根据值删除
# bicycle.remove('trek')
print(bicycle)

# 练习3-4
print(f'welcome ****,{bicycle[0]}')
print(f'welcome ****,{bicycle[1]}')
print(f'welcome ****,{bicycle[2]}')
print(f'welcome ****,{bicycle[3]}')

# 练习3-5
print(f'welcome ****,{bicycle[0]}')
print(f'welcome ****,{bicycle[1]}')
print(f'welcome ****,{bicycle[2]}')
print(f'{bicycle[3]} can not -*---')

bicycle.remove("specialized")
bicycle.append("Mia")
print(f'{bicycle[3]} will *******')

bicycle.insert(0,"Tom")
bicycle.insert(3,"Jeery")
print(bicycle)
