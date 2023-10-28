# Python program to Convert List to List of dictionaries
# input : my_list = [“Pritam”, 1990, 'Swagata'. 1990, 'Edhikaa'. 2022], key_list = [“name”, “year”] 
# output :
# [{'name': 'Pritam', 'year': 1990}, {'name': 'Swagata', 'year': 1990}, {'name': 'Edhikaa', 'year': 2022}]

# initializing lists
my_list = ['Pritam', 1990, 'Swagata', 1990, 'Edhikaa', 2022]
 
# printing original list
print("The original list : " + str(my_list))
 
# initializing key list 
key_list = ["name", "year"]
 
# using list comprehension to perform as shorthand
n = len(my_list)
res = [{key_list[0]: my_list[idx], key_list[1]: my_list[idx + 1]}
       for idx in range(0, n, 2)]
 
# printing result 
print("The constructed dictionary list : " + str(res))
