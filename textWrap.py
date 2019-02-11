# You are given a string S and width w. 
# Your task is to wrap the string into a paragraph of width w.

# Input Format

# The first line contains a string, S. 
# The second line contains the width, w.

# Constraints

# Output Format

# Print the text wrapped paragraph.

# Sample Input 0

# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4
# Sample Output 0

# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ

import textwrap
def wrap(string, max_width):
    # without using textwrap
    finalResult = ""

    for i in range(0, len(string), max_width): 
        str1 = ""
        for j in range(i, i + max_width):
            if j >= len(string):
                break;
            str1 = str1 + string[j] 
        if len(finalResult) == 0:
            finalResult = str1
        else:
            finalResult = finalResult + "\n" + str1
    return finalResult
    
    # Using textwrap
    # return textwrap.fill(string, max_width)

    # Alternate Method
    # return "\n".join([string[i:i+max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)