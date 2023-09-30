#Problem Statement :
'''Uppercase Half String'''

def halfUpper(str):
    l = len(str)
    half_l = l//2
    str1 = str[0:half_l]
    str2 = str[half_l:l+1]
    return print('The half upper case of {} is : {}'.format(str,str1+str2.upper()))

# Driver code
halfUpper('my name is pritam kumar dey')
halfUpper('I am a devops consultant')
