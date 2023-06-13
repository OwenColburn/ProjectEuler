"""
The series 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317

Find the last ten digits of the series 1^1 + 2^2 + 3^3 + ... + 1000^1000
"""

def summation(start, end):
    total = 0
    for i in range(start,end+1):
        total += i**i

    return total

def main():
    start = 1
    end = 1000
    sum_string = str(summation(start,end))
    print(sum_string[len(sum_string)-10:len(sum_string)])
    print(sum_string[-10:len(sum_string)])

main()