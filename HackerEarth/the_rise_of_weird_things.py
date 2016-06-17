#
# @author:SRvSaha
# the_rise_of_weird_things.py
# Description :https://www.hackerearth.com/problem/algorithm/the-rise-of-the-weird-things-1/
#

N = input()
string = raw_input().split(" ")
array =[int(data) for data in string]
zombie_array = []
sum_zombie = 0
vampire_array = []
sum_vampire = 0
for number in array:
    if number % 2 == 0 :
        sum_zombie += number
        zombie_array.append(number)
    else:
        sum_vampire += number
        vampire_array.append(number)
zombie_array = sorted(zombie_array)
zombie_array.append(sum_zombie)
vampire_array = sorted(vampire_array)
vampire_array.append(sum_vampire)
zombie_array.extend(vampire_array)
print " ".join(str(item) for item in zombie_array)
    
