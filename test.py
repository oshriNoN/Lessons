
# odd list signature
# from random import randint
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
# new_list = []
# for x in range(1, len(my_list), 2):
#     new_list.append(my_list[x])
# print(new_list)
def square(num):
    return num**2

m_list = [1,2,3,4,5]
for item in map(square, m_list):
    print(item)

