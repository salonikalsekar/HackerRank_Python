# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.

# Input Format

# The first line contains an integer, n , denoting the number of commands. 
# Each line i of the n subsequent lines contains one of the commands described above.

# Constraints

# The elements added to the list must be integers.
# Output Format

# For each command of type print, print the list on a new line.

# Sample Input 0

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print
# Sample Output 0

# [6, 5, 10]
# [1, 5, 9, 10]
# [9, 5, 1]

if __name__ == '__main__':
    N = int(input())


list1=[]
for i in range(N):
    inputData = input().split()
    inputLen = len(inputData)
    if(inputLen == 3):
        eval("list." + inputData[0]+ "(" + inputData[1] + "," + inputData[2] + ")")
    elif(inputLen == 2):
        eval("list." + inputData[0]+ "(" + inputData[1] + ")")
    elif(inputData[0] == "print"):
        print(list)
    elif(inputLen == 1):
        eval("list." + inputData[0] +"()")


###############Alternate Way##############
# for i in range(N):
#     command, *line = input().split()
#     if(command == "insert"):
#         list1.insert(int(line[0]), int(line[1]))
#     elif(command == "print"):
#         print(list1)
#     elif(command == "remove"):
#         list1.remove(int(line[0]))
#     elif(command == "append"):
#         list1.append(int(line[0]))
#     elif(command == "pop"):
#         list1.pop()
#     elif(command == "reverse"):
#         list1.sort(reverse=True)
#         # print(list1)
#     elif(command == "sort"):
#         list1.sort()

    




