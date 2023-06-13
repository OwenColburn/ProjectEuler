"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
from time import time

t = time()

collatz_list = []

def collatz(num):
    chain = 1
    while num != 1:
        if num % 2 == 0:
            num = num/2
            chain += 1
        else:
            num = (3*num) + 1
            chain += 1

    collatz_list.append(chain)

def main():
    for i in range(1, 1000000):
        collatz(i)

    maximum = max(collatz_list)

    for i in range(len(collatz_list)-1):
        if collatz_list[i] == maximum:
            print(i+1)
            print(collatz_list[i])
            break

    tt = time() - t

    print(f"Time taken: {tt} seconds")

main()