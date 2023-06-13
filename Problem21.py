import time
"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

1. Calculate divisors of n
2. Sum divisors
3. Find the divisors of the sum of n's divisors.
4. If they are the same, add to total sum
"""
def get_divisors(num):
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
    factors.remove(factors[len(factors)-1])
    return factors

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

def main():
    t = time.time()
    total = 0
    found = False
    amicable_pairs = []
    for i in range(1,10001):
        a=i
        b=get_divisors(a)
        c=get_divisors(sum(get_divisors(a)))
        # If the sum of the divisors of the sum of the divisors of i equals i, 
        # then i and the sum of the divisors of the sum of the divisors of i are 
        # an amicable pair
        if sum(c) == a and b != c and (sum(c) not in amicable_pairs):
            print(f"{sum(c)} and {sum(b)} are an amicable pair")
            amicable_pairs.append(sum(c))
            amicable_pairs.append(sum(b))
            found = True

    if not found:
        print("No amicable pairs found. Increase range")

    print(amicable_pairs)
    print(sum(amicable_pairs))
    tt= time.time()
    print(f"This took {(tt - t)} seconds")

main()