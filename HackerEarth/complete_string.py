#
# @author:SRvSaha
# complete_string.py
# Description :https://www.hackerearth.com/problem/algorithm/complete-string-4/
#

test_cases = input()
list_of_alphabet = list('abcdefghijklmnopqrstuvwxyz')
while test_cases > 0:
    string = raw_input()
    list_set_from_string = sorted(list(set(string)))
    if list_set_from_string == list_of_alphabet :
        print "YES"
    else:
        print "NO"
    test_cases -=1
