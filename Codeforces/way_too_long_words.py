#
# @author:SRvSaha
# way_too_long_words.py
# Description : http://codeforces.com/problemset/problem/71/A
#

n = int(input().strip()) #input number of cases. Strip method is used to remove leading and trailing white spaces.
while n > 0 :
    word = input() #Taking the word input from the user
    length = len(word) #finding the length of the word
    if length < 11 :
        print(word)
    else :
        word = word[0] + str(length-2) +word[-1] #condition required for the output of the string
        print(word)
    n -= 1
