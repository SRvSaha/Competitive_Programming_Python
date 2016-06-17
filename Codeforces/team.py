#
# @author:SRvSaha
# decision_string.py
# Description :http://codeforces.com/problemset/problem/231/A
#

n = int(input())
count = 0
while n > 0:
    sum = 0
    decision_string = input()
    for i in range(3):
        sum += int(decision_string[2 * i])
    if sum >= 2:
        count += 1
    n -= 1
print(count, end=None)
