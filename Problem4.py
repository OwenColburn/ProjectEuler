"""
Find the largest palindrome product of two 3-digit numbers

A palindromic number is a number that reads the same forwards and backwards. 
The largest palindromic number that can be created by multipliying two 2-digit numbers together is 9009 = 91x99

Cannot generate a complete list of all multiples of two 3-digit numbers. Simply too many answers. Would take O(n^2)

Two three digit numbers multiplied together cannot produce anything larger than 998001 = 999x999. 

Transform number into string. Check if palindrome

"""

start_int = 998001
high_palindrome = start_int


def is_palindrome(str):
    return str == str[::-1]

def find_palindrome():
    for i in reversed(range(start_int)):
        if is_palindrome(str(i)):
            if check_length_factors(find_factors(i)):
                high_palindrome = i
                break
    return high_palindrome

def find_factors(num):
    factors = []
    if len(factors) > 0:
        factors = []
    for i in range(1, num+1):
        if num % i == 0:
           factors.append(i)
           next_factor = num//i
           factors.append(next_factor)
           quicksort(factors, 0, len(factors)-1)
    
        if remove_duplicates(factors):
           break

    remove_duplicates(factors)

    return factors

def remove_duplicates(array):
    for i in range(len(array)-1):
            if i == 0:
                continue
            elif ((array[i] == array[i-1]) or (array[i] == array[i+1])):
                array.remove(array[i])
                return True

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

def check_length_factors(array):

    for i in range(len(array)):
        if len(str(array[i]))==3 and len(str(array[len(array)-i-1]))==3:
            return True
        
    return False


def main():
    print(find_palindrome())

main()
