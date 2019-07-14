
# Your task is to sort the string  in the following manner:
#
# All sorted lowercase letters are ahead of uppercase letters.
# All sorted uppercase letters are ahead of digits.
# All sorted odd digits are ahead of sorted even digits
# Sample Input
#
# Sorting1234
# Sample Output
#
# ginortS1324

s = input()
list_lower = []
list_upper = []
list_digit = []


for i in range(len(s)):
    if s[i].isupper():
        list_upper.append(s[i])
    elif s[i].islower():
        list_lower.append(s[i])
    elif s[i].isdigit():
        list_digit.append(s[i])

print(''.join(sorted(list_lower)+ sorted(list_upper) + sorted([i for i in list_digit if int(i)%2!=0]) + sorted([i for i in list_digit if int(i)%2==0])))