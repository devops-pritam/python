# problem Statement : 
'''Python program to print even length words in a string'''

def findEven(str):
    s = str.split(" ")
    print([x for i,x in enumerate(s) if len(x)%2==0])

# Driver code
findEven('My Name is Pritam Kumar Dey')
findEven('Print the list of even length words')
