#
# @author:SRvSaha
# chandu_and_consecutive_letters.py
# Description :https://www.hackerearth.com/problem/algorithm/chandu-and-consecutive-letters/
#

test_cases = input()
while test_cases > 0 :
    output_string = ""
    string = raw_input()
    for i in xrange(len(string)-1):
        if i != len(string)-2:
            if string[i] == string[i+1]:
                continue
            else:
                output_string += string[i]
        else :
            if string[i] == string[i+1]:
                output_string += string[i]
            else:
                output_string += string[i] + string[i+1]
    print output_string
    test_cases -= 1
