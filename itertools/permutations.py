#
# itertools.permutations(iterable[, r])
#
# This tool returns successive  length permutations of elements in an iterable.
#
# If  is not specified or is None, then  defaults to the length of the iterable, and all possible full length permutations are generated.
#
# Permutations are printed in a lexicographic sorted order. So, if the input iterable is sorted, the permutation tuples will be produced in a sorted order.
#
# Sample Code
#
# >>> from itertools import permutations
# >>> print permutations(['1','2','3'])
# <itertools.permutations object at 0x02A45210>
# >>>
# >>> print list(permutations(['1','2','3']))
# [('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
# >>>
# >>> print list(permutations(['1','2','3'],2))
# [('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
# >>>
# >>> print list(permutations('abc',3))
# [('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]


# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import permutations

s = input().split(" ")

print(*[''.join(i) for i in permutations(sorted(s[0]),int(s[1]))], sep = "\n")
