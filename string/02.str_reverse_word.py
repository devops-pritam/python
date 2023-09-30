# Problem Statement
'''Reverse Words in a Given String in Python'''

def reverseWord(str):
    str = str.lower()
    words = str.split(' ')
    words.reverse()
    # using list comprehension
    listToStr = ' '.join([(elem) for elem in words])
    print(listToStr)

# Driver code
reverseWord('my name is Pritam Kumar Dey')
reverseWord('Pritam python string quiz practice code')
