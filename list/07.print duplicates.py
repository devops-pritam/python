# write a Program to print duplicates from a list of integers
# input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# output : output_list = [20, 30, -20, 60]

from collections import Counter
 
my_list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
d = Counter(my_list)
# print(d)
 
new_list = list([item for item in d if d[item]>1])
print(new_list)
