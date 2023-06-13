"""
Starting in the top left corner of a 2 x 2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20 x 20 grid?

6 = (2+1)!

A 2x2 grid has 9 vertices
A 3x3 grid has 16 vertices
A nxn grid has (n+1)^2 vertices
A 20x20 grid has 441 vertices

A 2x2 grid has 6 possible paths
A 3x3 grid has 20 possible paths
A 4x4 grid has 70 possible paths
A nxn grid has a (2n)!/(n!)(n!) number of possible paths
A 20x20 grid has 137846528820 possible paths
"""
import math, time

def binom(n):
    try:
        return int(math.factorial(2*n)//(math.factorial(n)**2))
    except ValueError:
        print("Please pass in a positive number")
        main()
def main():
    t = time.time()
    try:
        num = int(input("Please give a number (0-1073741823): "))
        print(binom(num))
        tt = time.time() - t
        print(f"Execution time: {tt} seconds")
    except ValueError:
        print("Please enter a positive, whole number")
        main()
    except OverflowError:
        print("Please enter a number between 0 and 1073741823")
        main()

main()