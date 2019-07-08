# Sample Input
#
# 3 1000
# 2 5 4
# 3 7 8 9
# 5 5 7 8 9 10
# Sample Output
#
# 206
#
# Input Format
#
# The first line contains 2 space separated integers  K and M.
# The next K lines each contains an integer Ni, denoting the number of elements in the ith list, followed by Ni space separated integers denoting the elements in the list.

# # Enter your code here. Read input from STDIN. Print output to STDOUT
from math import pow


from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(pow(i,2) for i in x)%M, product(*N))
print(max(results))