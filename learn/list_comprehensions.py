nums =  [1,2,3,4,5,6,7,8,9,10]

# my_list = []
# for n in nums:
#     my_list.append(n)
# print(my_list)

# my_list = [num for num in nums]
# print(my_list)


# my_list = []
# for n in nums:
#     my_list.append(n*n)
# print(my_list)


# my_list = [n*n for n in nums]
# print(my_list)

# my_list = []
# for n in nums: 
#     if n%2 == 0:
#         my_list.append(n)
# print(my_list)

# my_list2 = [n for n in nums if n%2 ==0]
# print(my_list2)

# my_list = filter(lambda n: n%2 == 0, nums)
# print(my_list)

# my_list = []
# for letter in 'abcd':
#     for num in range(4):
#         my_list.append((letter, num))
# print(my_list)

# my_list2 = [(letter, num) for letter in 'abcd' for num in range(4)]
# print(my_list2)


names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']

my_dict = {}
for name, hero in zip(names, heros):
    my_dict[name] = hero
print(my_dict)

my_dict2 = {name: hero for name,hero in zip(names, heros)}
print(my_dict2)