# Python program to count Even and Odd numbers in a List
# input: list1 = [8, 7, 13, 64, 14, 19]
# output: Even = 3, odd = 3

import numpy as np
 
# list of numbers
List = [8, 7, 13, 64, 14, 19]
 
# using numpy Array
list1 = np.array(List)
Even_list = list1[list1 % 2 == 0]
 
print("Even numbers in the list: ", len(Even_list))
print("Odd numbers in the list: ", len(list1)-len(Even_list))
