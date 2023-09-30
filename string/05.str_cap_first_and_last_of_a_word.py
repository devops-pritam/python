# Problem Statement
'''capitalize the first and last character of each word in a string'''
import string
def capWord(str):
    str1 = ''
    s = str.title().split(" ")
    for i in s:
        str1 += (i[:-1] + i[-1].upper()) + ' '
    return print("original string was : {} and the converted string is : {}".format(str,str1))

# Driver code
capWord('my name is pritam kumar dey')
capWord('Murder for a jar of red rum')
