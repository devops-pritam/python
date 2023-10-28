# Reversing a List in Python
# input: list = [1,2,3,4,5]
# output: [5,4,3,2,1] 

def reverse_list(input_list):
    rev_list = input_list[::-1]
    return rev_list

my_list = [1,2,3,4,5]
print(reverse_list(my_list))
