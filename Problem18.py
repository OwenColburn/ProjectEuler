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
test_array = [[3],[7,4],[2,4,6],[8,5,9,3]]

print(test_array[3][3])

def main():
    for i in reversed(range(len(test_array))):
        sum_list = []
        for j in range(0,len(test_array[i])-1):
            # if array[i][j] is the first item in the array (j=0), compare it to i-1,j
            # if array[i][j] is the last item in the array (j=len(array[i])-1), compare to i-1, j-1
            # if array[i][j] is in the middle (0 < j < len(array[i])-1), compare to i-1, j and i-1, j-1;
            print(f"i={i}, j={j}")
            print(f"array[i][j] = {test_array[i][j]}")
            try:
                print(f"array[i-1][j] = {test_array[i-1][j]}")
                print(f"sum = {test_array[i][j]+test_array[i-1][j]} \n")
            except ValueError:
                print(f"array[i-1][j-1] = {test_array[i-1][j-1]}")
            if j == 0:
                sum_list.append(test_array[i][j] + test_array[i-1][j])

            elif j == len(test_array[i])-1:
                sum_list.append(test_array[i][j] + test_array[i-1][j-1])

            elif 0 < j and j < len(test_array[i]):
                sum_list.append(test_array[i][j] + test_array[i-1][j]) 
                sum_list.append(test_array[i][j] + test_array[i-1][j-1])

        print(f"sum_list: {sum_list} \n")

#main()