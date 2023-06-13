"""
Find the largest prime factor of 600851475143
1. Find the factors
2. Determine which of those factors are prime
3. Find the largest of those prime factors
"""

from math import sqrt

big_int = 600851475143
factors = []
primes = []
prime_factors = []

def find_factors(num):
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
            next_factor = num//i
            factors.append(next_factor)
            quicksort(factors, 0, len(factors)-1)
    
        if remove_duplicates(factors):
            break

    remove_duplicates(factors)
    


def partition(num, low, high):
    pivot = num[high]
    i = low-1
    for j in range(low, high):
        if num[j] <= pivot:
            i = i + 1
            (num[i], num[j]) = (num[j], num[i])
        
    (num[i+1], num[high]) = (num[high], num[i+1])

    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)

        quicksort(array, low, pi-1)

        quicksort(array, pi+1, high)

def remove_duplicates(array):
    for i in range(len(array)-1):
            if i == 0:
                continue
            elif ((array[i] == array[i-1]) or (array[i] == array[i+1])):
                array.remove(array[i])
                return True
    
def find_primes(num):
    prime_flag = 0
    if (num > 1):
        for i in range(2, int(sqrt(num))+1):
            if (num % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            primes.append(num)
            return True

def largest_in_list(array):
    highest = array[0]
    for i in range(len(array)):
        if array[i] > highest:
            highest = array[i]
    return highest

def smallest_in_list(array):
    lowest = array[0]
    for i in range(len(array)):
        if array[i] < lowest:
            lowest = array[i]

    return lowest

def main():
    find_factors(big_int)
    for i in factors:
        find_primes(i)
        if find_primes(i):
            prime_factors.append(i)

    print(f"The highest prime factor of {big_int} is {largest_in_list(prime_factors)}")


main()