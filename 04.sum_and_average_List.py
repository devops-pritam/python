# Find sum and average of List in Python
# input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output:
# sum =  55
# average =  5.5

import statistics
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
 
# using sum() method
sum1 = sum(my_list)
 
# finding average
avg = statistics.mean(my_list)
 
print("sum = ", sum1)
print("average = ", avg)
