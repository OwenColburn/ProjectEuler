"""By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

              75     
             95 64
            17 47 82
           18 35 87 10
          20 04 82 47 65
         19 01 23 75 03 34
        88 02 77 73 07 63 67
       99 65 04 28 06 16 70 92
      41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

1. Store triangle as an array, if possible. 
2. Starting at bottom, find sum of current number and number above. For example, if array[i][j] = 3 and array[i-1][j] = 4, the sum would be 7. 
3. Move to array[i][j+1]. Find the sum of current number and number above. If array[i][j+1] = 4 and array[i-1][j-1] = 4, the sum would be 8.
4. Check which sum is greater and set array[i-1][j] to that sum. array[i-1][j] would be set to 8 because 8 > 7.
5. Do this for every row until you've done the top row.
6. Return the value of the top row.
"""

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


test_array = [[3],[7,4],[2,4,6],[8,5,9,3]]
real_array = [[75],
              [95,64],
              [17, 47, 82],
              [18, 35, 87, 10],
              [20, 4, 82, 47, 65],
              [19, 1, 23, 75, 3, 34],
              [88, 2, 77, 73, 7, 63, 67],
              [99, 65, 4, 28, 6, 16, 70, 92],
              [41, 41, 26, 56, 83, 40, 80, 70, 33],
              [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
              [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
              [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
              [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
              [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
              [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]
sum_list = []

for i in reversed(range(len(real_array))):
   for j in range(len(real_array[i])):
      # Handle the last item in the row
      if j == len(real_array[i]) -1 and i != 0:
          sum_list.append(real_array[i][j] + real_array[i-1][j-1])
      # Handle the first item in the row
      elif j == 0 and i != 0:
         sum_list.append(real_array[i][j] + real_array[i-1][j])
      # Handle all other "in between" items in the row
      elif j > 0 and j < len(real_array[i]) - 1 and i-j != 0:
         sum_list.append(real_array[i][j] + real_array[i-1][j-1])
         sum_list.append(real_array[i][j] + real_array[i-1][j])

   if check_stop(sum_list, i):
      index = 0
      row = i

      while index <= row-1:
         real_array[row-1][index] = compare(sum_list[0:2])
         sum_list.pop(0)
         sum_list.pop(0)
         index+=1

print("The maximum sum from top to bottom is:", real_array[0][0])
