"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

1. Sort alphabetical
2. Parse through the word to find "sum of word". 
3. Find what line that word is on in the new file
4. Multiply line number by sum of word.
"""

name_list = []
alphabet = ['a', 'b', 'c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
names_sum = 0
sum_of_name = 0

with open("Problem22Names.txt") as file:
    for line in file:
        name_list.append(line.removesuffix("\",\n").strip("\""))

def alphabetize(list):
    list.sort()
    return list

name_list = alphabetize(name_list)

for name in name_list:
    for letter in name.lower():
        sum_of_name += alphabet.index(letter)+1
        names_sum += sum_of_name * (name_list.index(name)+1)
        sum_of_name = 0

print(names_sum)
