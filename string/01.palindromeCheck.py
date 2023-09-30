# Problem Statement :
'''Python program to check whether the string is Palindrome'''

# code
import string

#function
def checkPalindrome(str):
    s = str
    # all char Lower case
    str = str.lower()
    #replacing the whitespaces
    str = str.replace(" ", "")
    #removing the punctuation
    for char in string.punctuation:
      str = str.replace(char, '')
  
    
    #Validation
    print("{} : is a palindrome".format(s) if str==str[::-1] else "{} : is not a palindrome".format(s))

# Driver code
checkPalindrome('able was I ere I saw Elba')
checkPalindrome('khokho')
checkPalindrome('amaama')
checkPalindrome('wow')
checkPalindrome('Murder for a jar of red rum')
checkPalindrome('No, it can, as it is, it is a war. Raw as it is, it is an action')
checkPalindrome('Some men interpret nine memos')
checkPalindrome('Eva, can I see bees in a cave?')
checkPalindrome('Gert, I saw Ron avoid a radio-van, or was it Reg?')
