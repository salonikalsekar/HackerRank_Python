# Sample Input
#
# 11
# #BED
# {
#     color: #FfFdF8; background-color:#aef;
#     font-size: 123px;
#     background: -webkit-linear-gradient(top, #f9f9f9, #fff);
# }
# #Cab
# {
#     background-color: #ABC;
#     border: 2px dashed #fff;
# }
# Sample Output
#
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff
# Explanation
#
# #BED and #Cab satisfy the Hex Color Code criteria, but they are used as selectors and not as color codes in the given CSS.
#
# Hence, the valid color codes are:
#
# #FfFdF8
# #aef
# #f9f9f9
# #fff
# #ABC
# #fff

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

n = int(input())

for i in range(n):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')