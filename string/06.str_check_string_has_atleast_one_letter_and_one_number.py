# problem Statement
'''check if a string has at least one letter and one number'''
def checkLetterNeumber(str):
    checkString = lambda s: any(c.isalpha() for c in str) and any(c.isdigit() for c in str)
    print('the input {} contain at least one letter and one number is :'.format(str))
    print(checkString(str))
   

# driver code
checkLetterNeumber('pretam.365.devops')
checkLetterNeumber('keepsmilingsimi')
