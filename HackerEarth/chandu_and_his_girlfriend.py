#
# @author:SRvSaha
# chandu_and_his_girlfriend.py
# Description :https://www.hackerearth.com/problem/algorithm/chandu-and-his-girlfriend/
#

test_case = input()
while test_case > 0 :
	array_size = input()
	array = raw_input().split(" ")
	array = [int(a) for a in array]
	for item in sorted(array, reverse = True):
		print item,
	print 
	test_case -= 1
