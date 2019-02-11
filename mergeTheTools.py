# Consider the following:

# A string, s, of length 
# An integer, k, where k is a factor of n.
# We can split s into n/k subsegments where each subsegment, ti, consists of a contiguous block of k characters in s. Then, use each ti to create string ui such that:

# The characters in  are a subsequence of the characters in .
# Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
# Given  and , print  lines where each line  denotes string .

# Input Format

# The first line contains a single string denoting . 
# The second line contains an integer, , denoting the length of each subsegment.

# Constraints

# It is guaranteed that k is a multiple of n.
# Output Format

# Print n/k lines where each line  contains string ui.

# Sample Input

# AABCAAADA
# 3   
# Sample Output

# AB
# CA
# AD
# Explanation

# String  is split into  equal parts of length . We convert each  to  by removing any subsequent occurrences non-distinct characters in :

# We then print each  on a new line.

def merge_the_tools(string, k):
    # your code goes here
    num = int(len(string) / int(k))
    print(type(num))
    for i in range(0, len(string), num):
        str1 = ""
        for j in range(i, i+num):
            if string[j] in str1:
                str1 = str1
            else:
                str1= str1 + string[j]
        print(str1)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)