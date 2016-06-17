#
# @author:SRvSaha
# small_factorials_recursive.py
# Description :
#

test_cases = input()
def factorial(n):
    if n == 0 :
        return 1
    else:
        return n*factorial(n-1)
while test_cases > 0 :
    number = input()
    factorial = factorial(number)
    print factorial
    test_cases -= 1
