#
# @author:SRvSaha
# roy_and_profile_picture.py
# Description :https://www.hackerearth.com/problem/algorithm/roy-and-profile-picture/
#

L = input()
test_cases = input()
while test_cases > 0:
    W, H = raw_input().split(' ')
    W, H = [int(W),int(H)]
    if W < L or H < L:
        print "UPLOAD ANOTHER"
    else :
        if W == H :
            print "ACCEPTED"
        else :
            print "CROP IT"
    test_cases -= 1
