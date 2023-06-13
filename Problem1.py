"""
Find the sum of all the multiples of 3 and 5 below 1000

1. Identify all multiples of 3 less than 1000
2. Identify all multiples of 5 less than 1000
3. Sum together
"""
three_multiples = []
five_multiples = []
s = 0

for i in range(1000):
    if i % 3 == 0:
        three_multiples.append(i)

    elif i % 5 == 0:
        five_multiples.append(i)

    else:
        continue

for i in range(len(three_multiples)):
    s += three_multiples[i]

for i in range(len(five_multiples)):
    s += five_multiples[i]

print("The sum of all multiples of 3 and 5 less than 1000 is", s)

print(f"This is the same answer, just reached differently, in one line of code: {sum(filter(lambda x: x % 5 == 0 or x % 3 == 0, range(1000)))}")