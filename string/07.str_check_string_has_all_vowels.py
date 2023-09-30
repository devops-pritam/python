#Problem Statement
'''Given a string, the task is to check if every vowel is present or not.
 We consider a vowel to be present if it is present in upper case or lower case. '''

# Python program for the above approach
def checkVowels(str):
	if len(set(str.lower()).intersection("aeiou")) >= 5:
		return ('String has all vowels')
	else:
		return ("String does not contains all vowels")


# Driver code
if __name__ == "__main__":
	string = "My Name Is Pritam Kumar Dey"
	print(checkVowels(string))
