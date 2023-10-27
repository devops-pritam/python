# Write a Python program to interchange first and last elements in a list
# Input : [1, 2, 3, 4, 5]
# Output : [5, 2, 3, 4, 1]

my_list = [1, 2, 3, 4, 5]

def item_interchange(input_list):
    if len(input_list) > 2 :
        new_list = input_list[-1:] + input_list[1:-1] + input_list[:1]
    return new_list

print(item_interchange(my_list))
