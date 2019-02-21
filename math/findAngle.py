# Examples: 
# If angle is 56.5000001°, then output 57°. 
# If angle is 56.5000000°, then output 57°. 
# If angle is 56.4999999°, then output 56°.


# Sample Input

# 10
# 10
# Sample Output

# 45°

import math
AB = int(input())
BC = int(input())

print(int(round(math.degrees(math.atan2(AB,BC)))), end="°")