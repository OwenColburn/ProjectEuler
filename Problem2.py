"""
Find the sum of all the Fibonacci numbers whose values do not exceed four million and that are even numbers
1. Generate all the Fibonacci numbers with values less than four million
2. Find the sum
"""

list_of_fibbers = []
sum_ = 0
nums_to_remove = []

def generate_Fibonacci(num):
    if (num == 1 or num == 0):
        return num
    
    fbm2 = 0
    fbm1 = 1
    fib = fbm2 + fbm1

    for i in range(num-2):
        fbm2 = fbm1
        fbm1 = fib
        fib = fbm2 + fbm1

    return fib

for i in range(100000):
    list_of_fibbers.append(generate_Fibonacci(i))

    if list_of_fibbers[i] >= 4000000:
        list_of_fibbers.remove(list_of_fibbers[i])
        break

for i in list_of_fibbers:
    if (i % 2 == 0):
        sum_ += i

print("The sum of all even Fibonacci Numbers whose values do not exceed four million is", sum_)