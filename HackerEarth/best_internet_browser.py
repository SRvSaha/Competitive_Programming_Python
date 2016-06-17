#! /usr/bin/python
#
# @author:SRvSaha
# best_internet_browser.py
# Description : https://www.hackerearth.com/problem/algorithm/the-best-internet-browser-3/description/
#
test_cases = input()
while test_cases > 0:
    count = 0
    website = raw_input()
    website_mofified = website[4:-4]
    for alphabet in list(website_mofified.lower()):
        if alphabet in ['a', 'e', 'i', 'o', 'u']:
            continue
        else:
            count += 1
    print str(count + 4) + '/' + str(len(website))
    test_cases -= 1
