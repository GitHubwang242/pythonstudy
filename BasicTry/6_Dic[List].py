pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
#
# print(f"You ordered a {pizza['crust']}-crust pizza "
#       "with the following toppings:")
# for topping in pizza['toppings']:
#     print(f"\t"+topping)


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
# for name, languages in favorite_languages.items():
#
#     if len(languages) >1:
#         print(f"\n{name.title()}'s favorite languages are:")
#         for language in languages:
#             print(f"\t{language.title()}")
#     else:
#         print(f"\n{name.title()}'s favorite languages is:")
#         print(f"\t{languages[0]}")


# 练习6-7 人们
people = {
    'wang':{
        'age': 1,
        'sex': 'nan',
    },
    'miao':{
        'age': 2,
        'sex': 'nv',
    },
    'ban': {
        'age':3,
        'sex': 'nv',
    },
}

# for name, name_info in people.items():
#     print(f"name is : {name}")
#     age = name_info['age']
#     sex = name_info['sex']
#     print(f"the age is {age}")
#     print(f"the sex is {sex}")


# 练习6-8
cat = {'name':'mimi','host_name': 'miaomiao'}
dog = {'name':'wangwang', 'host_name': 'banban'}
duck = {'name':'gaga', 'host_name': '17'}
pets = [ cat, dog, duck]
# for pet in pets:
    # print(pet)
    # print(pet['name'])
    # print(pet['host_name'])
    # print(pet.items())
    # print(pet.keys())
    # print(pet.values())
    # for name,host_name in pet.items():
    #     print(f"\n name is {name[0]},host_name is {host_name[0]}")
        # print(f"host_name is {host_name}")
        # print(f"\n name is {name[1]},host_name is {host_name[1]}")

print("**********************************")
# print(pets[0].keys())

# 练习6-9

favorite_places1 = {
    'zhao':{
        'f':'beijing',
        's':'tianjin',
        't':'hebei',
    },
    'qian':{
        'f':'beijing',
        's':'tianjin',
        't':'hebei',
    },
    'sun':{
        'f':'beijing',
        's':'tianjin',
        't':'hebei',
    },
}
favorite_places2 = {
    'zhao':['beijing','tianjin','hebei'],
    'qian':['beijing','tianjin','hebei'],
    'sun':['beijing','tianjin','hebei'],
}

for name,place in favorite_places1.items():
    print(name)
    place1 = place['f'],
    place2 = place['s'],
    place3 = place['t'],
    print(place1)
    print(place2)
    print(place3)
    print("******************")

for name,value in favorite_places2.items():
    print("-------------------------")
    print(name)
    for va in value:
        print(va)

# 练习6-10
num_dic = {
    'Zhao' : [1,2,3,4],
    'Qian' : [5,6,7,8],
}

# 练习6-11
cities = {
    'beijing1':{
        'country':'China',
        'population':1000000,
        'fact':"capital",
    },
    'beijing2':{
        'country':'China',
        'population':2000000,
        'fact':"capital",
    },
    'beijing3':{
        'country':'China',
        'population':3000000,
        'fact':"capital",
    },
}
print('++++++++++++++++++++++++++++++++')
for name,info in cities.items():
    print(name)
    print(info['country'])
    print(info['population'])
    print(info['fact'])


















