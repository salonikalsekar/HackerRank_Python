# Sample Input
#
# 2
# 9587456281
# 1252478965
# Sample Output
#
# YES
# NO


import re

n = int(input())

for i in range(n):
    str = input()
    if re.match(r'[789]\d{9}$',str):
        print('YES')
    else:
        print('NO')
