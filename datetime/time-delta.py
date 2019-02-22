# When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

# Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

# Day dd Mon yyyy hh:mm:ss +xxxx

# Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

# Input Format

# The first line contains , the number of testcases. 
# Each testcase contains  lines, representing time  and time .

# Constraints

# Input contains only valid timestamps
# .
# Output Format

# Print the absolute difference  in seconds.

# Sample Input 0

# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0

# 25200
# 88200
# Explanation 0

# In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is  seconds or  seconds.

# Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 

# https://www.hackerrank.com/challenges/python-time-delta/problem


for i in range(int(input())):
    arr = input().split()
    try:
        print(int(arr[0]) // int(arr[1]))
    except Exception as e:
        print("Error Code:", e)