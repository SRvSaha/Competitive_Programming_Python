#
# @author:SRvSaha
# what_is_string_made_of.py
# Description :https://www.hackerearth.com/problem/algorithm/what-is-the-string-made-of-2/
#

sum = 0
string = raw_input()
list_from_string = list(string)
list_from_string = [int(item) for item in list_from_string]
dictionary = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
for element in list_from_string:
    if element in dictionary:
        sum += dictionary[element]
print sum
