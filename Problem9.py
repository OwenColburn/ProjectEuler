# Solved at https://www.desmos.com/calculator/wmmiukvi9r

"""
A pythagorean triple is any set of numbers a < b < c such that a^2 + b^2 = c^2

There exists exactly one Pythagorean triple where a + b + c = 1000.
Find the product abc

1. Find a pythagorean triple
2. While da + db + dc < 1000
    2a. Keep multiplying a, b, c by some number d
    2b. Increase d every iteration
3. If da + db + dc = 1000
    3a. Return abc
"""

def find_pythag_triples():
    found = False
    answer = 0
    for c in reversed(range(997)):
        for b in reversed(range(1000-c-1)):
            a = 1000 - c - b
            if isPythagoreanTriple(a, b, c):
                found = True
                answer = a * b * c
                print(a, b, c)

    if found:
        print(answer)

    else:
        print("Your program kinda tweakin' bruh")

def isPythagoreanTriple(a, b, c):
    return a**2 + b**2 == c**2

def main():
    find_pythag_triples()

main()
