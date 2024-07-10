from Bubble_And_Selection_Sorting import selection_sort
import random

ls = list(range(0, 10001, 3))
random.shuffle(ls)
# print(ls)
target_search = random.randint(0,10001)
sorted_ls = selection_sort(ls)

def search(ls, target):
    lower_bound = 0
    upper_bound = len(ls)
    while not (upper_bound -1) == lower_bound:
        mid_point = (upper_bound + lower_bound) // 2
        if ls[mid_point] > target:
            upper_bound = mid_point
            # print(mid_point)
        elif ls[mid_point] < target:
            lower_bound = mid_point
            # print(mid_point) 
        else:
            return mid_point
        
    else:
        return "Not found"
        
print("Target is:", target_search)
pos = search(sorted_ls, target_search)
print("Position in list:", pos)
exit()
