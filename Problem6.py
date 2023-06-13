"""
The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... +10^2 = 385

The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sum_of_squares(limit):
    sum_of = 0
    for i in range(limit+1):
        sum_of += i**2

    print("The sum of squares is", sum_of)
    return sum_of

def square_of_sum(limit):
    sum = 0
    for i in range(limit+1):
        sum += i

    square_of = sum**2

    print("The square of sums is", square_of)
    return square_of

def main():
    print("The difference in the square of sums and sum of squares for all natural numbers less than 100 is", square_of_sum(100) - sum_of_squares(100))

main()