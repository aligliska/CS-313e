#  File: Triangle.py

#  Description: This program compares different methods of calculating
#  the greatest path down a triangle of integers. The output compares 
#  the maximum sum found and the time taken to run each method. 

#  Student Name: Alice Gee 

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/08/2021

#  Date Last Modified: 7/09/2021

import sys
from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force (grid):
  store = []
  idx, row, curr_sum = 0, 0, 0
  brute_helper(row, idx, curr_sum, grid, store)
  return max(store)


def brute_helper(row, idx, curr_sum, grid, store):
  # base case if row is out of index
  if row == len(grid):
    store.append(curr_sum)
    return 
  else:
    curr_sum += grid[row][idx]
  # recursive call, choose bottom left or bottom right value 
  return brute_helper(row + 1, idx, curr_sum, grid, store) or \
    brute_helper(row + 1, idx + 1, curr_sum, grid, store)


# returns the greatest path sum using greedy approach
def greedy (grid):
  path_num = [grid[0][0]]
  idx = 0
  # adds larger number into the path 
  for row in range(1, len(grid)):
    if grid[row][idx] > grid[row][idx + 1]:
      path_num.append(grid[row][idx])
    elif grid[row][idx] < grid[row][idx + 1]:
      path_num.append(grid[row][idx + 1])
      idx += 1
  return sum(path_num)


# returns the greatest path sum using divide and conquer (recursive) approach
def divide_conquer (grid):
  row, idx = 0, 0
  return divide_helper(row, idx, grid)

def divide_helper(row, idx, grid):
  if row == len(grid) - 1:
    return grid[row][idx]
  else:
    next_value = max(divide_helper(row + 1, idx, grid), 
                    divide_helper(row + 1, idx + 1, grid))
  return grid[row][idx] + next_value
                  

# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog (grid):
  new_array = []
  # creates an empty array to store sum values
  for i in range(len(grid)-1):
      column = []
      for j in range(len(grid)):
          column.append(0)
      new_array.append(column)
  new_array.append(grid[-1])

  for i in range (len(grid)-2, -1, -1):
    for j in range(i + 1):
      # compares bottom left and bottom right values to add to above number
      if new_array[i+1][j+1] > new_array[i+1][j]:
        new_array[i][j] = grid[i][j] + new_array[i+1][j+1]
      else:
        new_array[i][j] = grid[i][j] + new_array[i+1][j]
  return new_array[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file ():
  # read number of lines
  line = sys.stdin.readline()
  line = line.strip()
  n = int (line)

  # create an empty grid with 0's
  grid = [[0 for i in range (n)] for j in range (n)]

  # read each line in the input file and add to the grid
  for i in range (n):
    line = sys.stdin.readline()
    line = line.strip()
    row = line.split()
    row = list (map (int, row))
    for j in range (len(row)):
      grid[i][j] = grid[i][j] + row[j]

  return grid 

def main ():
  # read triangular grid from file
  grid = read_file()

  # output greatest path from exhaustive search
  times = timeit ('brute_force({})'.format(grid), 'from __main__ import brute_force', number = 10)
  times = times / 10
  # print time taken using exhaustive search
  print("The greatest path sum through exhaustive search is")
  print(brute_force(grid))
  print("The time taken for exhaustive search in seconds is")
  print(times)
  print()

  # output greatest path from greedy approach
  times = timeit ('greedy({})'.format(grid), 'from __main__ import greedy', number = 10)
  times = times / 10
  # print time taken using greedy approach
  print("The greatest path sum through greedy search is")
  print(greedy(grid))
  print("The time taken for greedy approach in seconds is")
  print(times)
  print()

  # output greatest path from divide-and-conquer approach
  times = timeit ('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number = 10)
  times = times / 10
  # print time taken using divide-and-conquer approach
  print("The greatest path sum through recursive search is")
  print(divide_conquer(grid))
  print("The time taken for recursive search in seconds is")
  print(times)
  print()

  # output greatest path from dynamic programming 
  times = timeit ('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number = 10)
  times = times / 10
  # print time taken using dynamic programming
  print("The greatest path sum through dynamic programming is")
  print(dynamic_prog(grid))
  print("The time taken for dynamic programming in seconds is")
  print(times)
  print()

if __name__ == "__main__":
  main()

# python3 Triangle.py < triangle.in.txt