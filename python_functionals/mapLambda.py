# Let's learn some new Python concepts! You have to generate a list of the first  fibonacci numbers,  being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

# Concept

# The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables. 
# Let's say you are given a list of names, and you have to print a list that contains the length of each name.

# >> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
# [4, 3, 3]  
# Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.

# >> sum = lambda a, b, c: a + b + c
# >> sum(1, 2, 3)
# 6
# Note:

# Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries.

# Input Format

# One line of input: an integer .

# Constraints


# Output Format

# A list on a single line containing the cubes of the first  fibonacci numbers.

# Sample Input

# 5
# Sample Output

# [0, 1, 1, 8, 27]

cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    sum_res = 0
    list1 = []
    for i in range(n):
        if len(list1) < 2:
            sum_res = i
        else:
            sum_res= list1[-1] + list1[-2]
        list1.append(sum_res)
    return list1
    # return a list of fibonacci numbers

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


    # OR

cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    a = 0
    b = 1
    list1 = [a, b]

    if n == 1:
        return [a]
    elif n == 0:
        return []
    else:
        for i in range(n - 2):
            c = a + b
            a = b
            b = c
            list1.append(c)
        return list1


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))