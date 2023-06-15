"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""
import time

# Should take adjacent items in a list and compare them, returning the larger value
def compare(list):
   compare_one = list[0]
   compare_two = list[1]

   if compare_one >= compare_two:
      return compare_one
   else:
      return compare_two
   
def check_stop(list, row):
   if len(list) == row*2:
      return True
   return False

start = time.time()
f = open("0067_triangle.txt", "r").readlines()
values =  []
for line in f:
    temp = []
    for token in line.replace("\n", "").split(' '):
        temp.append(int(token))
    values.append(temp)

sum_list = []

for i in reversed(range(len(values))):
   for j in range(len(values[i])):
      # Handle the last item in the row
      if j == len(values[i]) -1 and i != 0:
          sum_list.append(values[i][j] + values[i-1][j-1])
      # Handle the first item in the row
      elif j == 0 and i != 0:
         sum_list.append(values[i][j] + values[i-1][j])
      # Handle all other "in between" items in the row
      elif j > 0 and j < len(values[i]) - 1 and i-j != 0:
         sum_list.append(values[i][j] + values[i-1][j-1])
         sum_list.append(values[i][j] + values[i-1][j])

   if check_stop(sum_list, i):
      index = 0
      row = i

      while index <= row-1:
         values[row-1][index] = compare(sum_list[0:2])
         sum_list.pop(0)
         sum_list.pop(0)
         index+=1

print("The maximum sum from top to bottom is:", values[0][0])
print(f"Total time: {time.time() - start}")