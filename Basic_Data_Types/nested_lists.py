# Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

# Input Format

# The first line contains an integer, N , the number of students. 
# The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

# Constraints

# There will always be one or more students having the second lowest grade.
# Output Format

# Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry
# Explanation 0

# There are 5 students in this class whose names and grades are assembled to build the following list:

# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of 37.2 belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

if __name__ == '__main__':
    students=[]
    for _ in range(int(input())):
        list_1 = []
        name = input()
        score = float(input())
        students.append([name, score])

minElem = min(students,key= lambda x:x[1])
for i in sorted(students, key = lambda x:x[1]):
    if i[1] > minElem[1]:
        minValue = i[1]
        break

result = []
for i,x in enumerate(sorted(students, key = lambda x:x[1])):
    if x[1] == minValue:
        result.append(x)
        
for i in sorted(result):
    print(i[0])
    
    
    # you can also solve it by:

    if __name__ == '__main__':
    result=list()
    list2 = list()
    for _ in range(int(input())):
        list1 = list()
        name = input()
        score = float(input())
        list1.append(name)
        list1.append(score)
        list2.append(list1)


minData = min(list2, key= lambda x:x[1] )


for i in sorted(list2, key=lambda x:x[1]):
    if i[1] > minData[1]:
        result.append(i);
        break;

for i in sorted(list2, key=lambda x:x[1]):
    if i[0] != result[0][0]:
        if i[1] == result[0][1] :
            result.append(i);
for i in sorted(result):
    print(i[0])


