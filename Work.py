
#  File: Work.py

#  Description: This program uses linear search and binary search to 
#  determine the minimal lines to write each time before falling asleep
#  /drinking coffee. The output returns the time values for each method.

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 6/27/2021

#  Date Last Modified: 6/28/2021

import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
  p = 0
  sum = 0
  while (v//k**p) != 0:
    sum += (v//k**p)
    p += 1
  return sum


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
  for num in range(1, n+1):
    if sum_series(num,k) >= n: 
      return num


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
  low = 1
  high = n
  while low <= high:
    mid = (low + high) // 2
    # returns mid if sum_series uses minimum "v" to write lines
    if (sum_series(mid, k) > n):
      if (sum_series(mid-1, k) < n):
        return mid
      else:
        high = mid - 1
    # moves search range up if sum_series returns too little lines
    elif (sum_series(mid, k) < n):
      low = mid + 1
    # if sum_series is equal to "n" lines to write
    else:
      return mid 


def main():
  # read number of cases
  line = sys.stdin.readline()
  line = line.strip()
  num_cases = int (line)

  for i in range (num_cases):
    line = sys.stdin.readline()
    line = line.strip()
    inp =  line.split()
    n = int(inp[0])
    k = int(inp[1])

    start = time.time()
    print("Binary Search: " + str(binary_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()

    start = time.time()
    print("Linear Search: " + str(linear_search(n, k)))
    finish = time.time()
    print("Time: " + str(finish - start))

    print()
    print()

if __name__ == "__main__":
  main()

