#
# @author:SRvSaha
# caps_lock.py
# Description :http://codeforces.com/problemset/problem/231/A
#

word = input()
output = ''
if len(word) == 1 and word.islower():
	output = word.upper()
	print(output) 
elif (word[0].islower() and word[1:].isupper()) :
    output = word[0].upper() + word[1:].lower()
    print(output)
elif word.isupper():
	output = word.lower();
	print(output)
else :
    print(word)
