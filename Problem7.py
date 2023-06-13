"""
Find the 10001st prime number

Sieve of Eratosthenes? 

def SieveOfEratosthenes(num, count):
    prime = [True for i in range(num+1)]
    counter = 0
# boolean array
    p = 2
    while (p * p <= num and counter < count):
  
        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):
  
            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
  
    # Count all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            counter+=1
    return counter


def main():
    num = 104743
    count = 10001
    print(f"There are {SieveOfEratosthenes(num, count)} prime numbers less than or equal to {num}")

"""

import time, math

s = time.time()


def isprime(n):
    if n == 2:
        return 1
    elif n % 2 == 0:
        return 0

    i = 3
    range = int(math.sqrt(n)) + 1
    while (i < range):
        if (n % i == 0):
            return 0
        i += 1
    return 1


N, T = 1, 3
while N < 6:
    if isprime(T):
        N += 1
    T += 2
print(T - 2)
print(time.time() - s)