#
# @author:SRvSaha
# next_round.py
# Description : http://codeforces.com/problemset/problem/158/A
#

n, k = input().strip().split(' ') # Throws a list of 2 string elements which are initialised to n and k
n = int(n) # n and k are in string format so must be converted to int for furthur works
k = int(k)
count = 0 #this variable counts the number of times
output_list = [] # a final list is taken that holds the overall data of score by all N participants
string = input()
for item in string.strip().split(' ') : #For every item in the list
    output_list.append(int(item))  # Output list is initialised with the integer values, since the previous list throws list of strings
for element in output_list :
    if element != 0 and element >= output_list[k-1] : # Now if the element is non-zero and the element is greater than or equal to the element in the kth place then count is incremented. Else count remains 0 if all are 0 else count is equal to counted value by previous if condition
        count += 1
print(count) # finally printing the result of how many participants will go the next round
