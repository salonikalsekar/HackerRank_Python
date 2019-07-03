# Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer N. You have to print a list of all possible coordinates(i,j,k) given by  on a 3D grid where the sum i+j+k of is not equal to N.
#
# Input Format
#
# Four integers  and  each on four separate lines, respectively.
#
# Constraints
#
# Print the list in lexicographic increasing order
#
# Sample
# Input
# 0
#
# 1
# 1
# 1
# 2
# Sample
# Output
# 0
#
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

arr = [[ i, j, k] for i in range( x + 1) for j in range(y+1) for k in range(z+1) if ( ( i + j + k ) != n )]

print(arr)