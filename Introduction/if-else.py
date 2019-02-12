# Check Tutorial tab to know how to to solve.

# Task 
# Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of  to , print Not Weird
# If n is even and in the inclusive range of  to , print Weird
# If n is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints
# 1 <= n <= 100
# Output Format

# Print Weird if the number is weird; otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird
# Explanation 0

# n=3 
# n is odd and odd numbers are weird, so we print Weird.

# Sample Input 1

# 24
# Sample Output 1

# Not Weird
# Explanation 1
# n=24

 
#  n > 20 and n is even, so it isn't weird. Thus, we print Not Weird.



N = int(input())

if N%2 is 1:
    print("Weird")

elif N%2 is 0 and N in range(2,6):
    print("Not Weird")
elif N%2 is 0 and N in range(6,21):
    print("Weird")
else:
    print("Not Weird")