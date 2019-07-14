# any()
# This expression returns True if any element of the iterable is true.
# If the iterable is empty, it will return False.
#
# Code
#
# >>> any([1>0,1==0,1<0])
# True
# >>> any([1<0,2<1,3<2])
# False
# all()
# This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.
#
# Code
#
# >>> all(['a'<'b','b'<'c'])
# True
# >>> all(['a'<'b','c'<'b'])
# False
# Task
#
# You are given a space separated list of integers. If all the integers are positive
# then you need to check if any integer is a palindromic integer.

n = int(input())

list1 = list(map(int, input().split()))

print(all(i> 0 for i in list1) and any(str(j) == str(j)[::-1] for j in list1))
