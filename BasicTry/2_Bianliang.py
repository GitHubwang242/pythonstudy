
# 去掉首尾的空白
favorite_language = ' python '
# print(favorite_language)
#
# print(favorite_language.lstrip())
#
# print(favorite_language.rstrip())
#
# print(favorite_language.strip())


# 练习2-3
name = "Eric"
sentence = f'Hello {name}, would you like to learn some Python today?'
print(sentence)

# 练习2-4

name2 = "Mia"
print(name2.lower())
print(name2.upper())
print(name2.title())

# 练习2-5
name3 = "Albert Einstein"
sentence2 = '"A person who never made a mistake never tried anything new."'
sentence3 = f'{name3} once said,{sentence2}'
print(sentence3)

# 练习2-6
famous_person = "Albert Einstein"
sentence2_1 = '"A person who never made a mistake never tried anything new."'
message = f'{name3} once said,{sentence2_1}'
print(message)

# 练习2-7
person = "\tAlbert Einstein\n"
print(person)

print("looklook")

print(person.strip())
print(person.lstrip())
print(person.rstrip())
print("looklook")