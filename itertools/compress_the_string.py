# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .
#
# You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
#
# For a better understanding of the problem, check the explanation.
#
# Input Format
#
# A single line of input consisting of the string .
#
# Output Format
#
# A single line of output consisting of the modified string.

from itertools import groupby


n = list(input())

# for i,j in groupby(n):
#     print(int(i))
#     print(len(list(j)))

print(*[(len(list(j)), int(i)) for i,j in groupby(n)])