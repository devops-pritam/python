# Write a Python program to to Swap Two Elements in a List
# input : [1, 2, 3, 4] : position_1 = 1 , position_2 = 3 (Swap these 2 positional elements))
# output : [3, 2, 1, 4]

my_list = [1, 2, 3, 4]

def swapPositions(lis, pos1, pos2):
    for i, x in enumerate(lis):
        if i == pos1:
            elem1 = x
        if i == pos2:
            elem2 = x
    lis[pos1] = elem2
    lis[pos2] = elem1
    return lis
 
pos1, pos2 = 1, 3
print(swapPositions(my_list, pos1-1, pos2-1))
