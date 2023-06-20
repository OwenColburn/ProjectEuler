"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are:
    1/2 = 0.5
    1/3 = 0.(3)
    1/4 0 0.25
    1/5 = 0.2
    1/6 = 0.1(6)
    1/7 = 0.(142857)
    1/8 = 0.125
    1/9 = 0.(1)
    1/10 = 0.1

Where 0.1(6) means 0.1666666..., and has a 1 digit recurring cycle. It can be seen that 7 has a 6 digit recurring cycle.
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part

1. Find out how the hell Python handles repeating digits in a fraction
2. Use my new knowledge to code a great program.

If n is relatively prime (coprime) to base b, the multiplicative order exists. 
The multiplicative order of 10 % n coprime to 10 equals the period of the repeated portion of the decimal expansion of the reciporical of n
Multiplicative order is given by the smallest exponent e for which b^e % n = 1
We want the maximum multiplicative order for b = 10 and n < 1000.
"""

def Euclid_algo(num1, num2):
    remainder = num1 % num2

    while remainder != 0:
        num1 = num2
        num2 = remainder

        remainder = num1 % num2

    return num2

def main():
    b = 10
    e = 1

    power_list = []
    order_list = []
    for n in range(1,1001):
        if Euclid_algo(b, n) == 1 and b**e % n == 1:
            power_list.append(e)
            order_list.append(n)
            e = 1
        else:
            e += 1

    print(max(power_list))
    print(max(power_list))
    print(order_list)

main()