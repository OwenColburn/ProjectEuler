"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

Can count up by 5, as each number must be divisble by 5. 
If number is not even, skip it as number must be divisible by 2. 
Only have to search even numbers that can be multiplied by 5. 
The only numbers that satisfy this condition are 10, 20, 30, 40, etc. 
"""
import time

def is_even(num):
    return num % 2 == 0

def five_multiple(num):
    return num % 5 == 0

def find_num(limit):
    i = 0
    potential_num = []
    while True:
        i += 10 # increment i by 10, as these are the only numbers that satisfy is_even and five_multiple
        if is_even(i) and five_multiple(i):
            for j in range(1,limit): # starting at 1, go through the limiting number
                if i % j != 0: # If not an even division
                    if len(potential_num) > 0: # empty potential_num
                        try:
                            while True:
                                potential_num.remove(i)

                        except ValueError:
                            pass
                    break
                else:
                    potential_num.append(i) # if i % j == 0, it is a potential solution
        
        if len(potential_num) > 0: # after the for loop, if potential_num has an item in it, return the item
            return potential_num[0]


def main():
    print(f"The smallest positive number that can be evenly divided by all numbers 1-20 is {find_num(20)}") # 1-20 is what every number will be divided by

main()
