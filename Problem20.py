"""
Find the sum of the digits in the number 100!
"""

import math

total = 0

for i in range(0,len(str(math.factorial(100)))-1):
    total += int(str(math.factorial(100))[i])

print(total)
