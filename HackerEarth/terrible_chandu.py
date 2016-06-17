#
# @author:SRvSaha
# terrible_chandu.py
# Description : https://www.hackerearth.com/problem/algorithm/terrible-chandu/
#
test_cases = input()
while test_cases > 0:
    reversed_string = ''
    string = raw_input()
    for i in xrange(len(string)-1,-1, -1):
        reversed_string += string[i]
    print reversed_string
    test_cases -= 1
