#
# @author:SRvSaha
# string_task.py
# Description :http://codeforces.com/problemset/problem/118/A
#

input_string = input() #taking the user input of a string
input_string = input_string.lower() #Converting the input string into lower case since the answer must be in lowercase
output_string = "" #Empty string for output purpose
length = len(input_string) # taking the length of the string in a variable named length
for i in range(length) : # from 0 to length-1 i.e, first to last of string
	if input_string[i] in ['a','e','i','o','u','y']: #if the character is a vowel then continue : pass it
			continue
	else :
		output_string += '.' + input_string[i]  # Else append that character to the output string with a period before it.
print(output_string) #final printing out the lowercased output.
