# input()
# In Python 2, the expression input() is equivalent to eval(raw _input(prompt)).
#
# Code
#
# >>> input()
# 1+2
# 3
# >>> company = 'HackerRank'
# >>> website = 'www.hackerrank.com'
# >>> input()
# 'The company name: '+company+' and website: '+website
# 'The company name: HackerRank and website: www.hackerrank.com'



x,y = map(int, input().split())
exp = input()

res = eval(exp);

if res == y:
    print('True')
else:
    print('False')

