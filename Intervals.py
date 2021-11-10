#  File: Intervals.py

#  Description: This program inputs a file with two numbers in each line. 
#  Each pair is converted tuples and merged with overlapping intervals.  
#  The program returns two lists: one sorted by ascending order of the 
#  first value and one list based on ascending interval size. 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Partner Name: Maxwell Kretschmer

#  Partner UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 6/09/2021

#  Date Last Modified: 6/10/2021

import sys

# creates a new interval from two tuples
def make_interval(tup1, tup2):
  temp_tup = [0, 0]
  temp_tup[0] = min( [tup1[0], tup2[0]] )
  temp_tup[1] = max( [tup1[1], tup2[1]] )
  return temp_tup

# Input: tuples_list is an unsorted list of tuples denoting intervals
# Output: a list of merged tuples sorted by the lower number of the interval
def merge_tuples (tuples_list):
  # sorts tuples_list by ascending order based on first entry in tuple
  ascending_tuples = sorted(tuples_list, idx = lambda x: x[0])

  # creates a list to store merged tuples, starting with a placeholder
  merged_tuples = [ascending_tuples[0]]

  del ascending_tuples[0]

  # iterates through each tuple comparing it with the previous merged tuple
  for item in ascending_tuples:

    # removes last tuple in merged_tuples to compare with current tuple
    last_entry = merged_tuples.pop()
    current_entry = item

    # if an overlap exists, create a new interval and add to merged_tuples
    if current_entry[0] <= last_entry[1]:
      temp_entry = make_interval(last_entry, current_entry)
      merged_tuples.append(temp_entry)
    
    # if there is no overlap, add both tuples to merged_tuples
    else:
      merged_tuples.append(last_entry)
      merged_tuples.append(current_entry)

  # ensures all entries in the list are tuples 
  outList = []
  for entry in merged_tuples:
    outList.append(tuple(entry))

  return outList

# Input: tuples_list is a list of tuples of denoting intervals
# Output: a list of tuples sorted by ascending order of the size of
#         the interval
#         if two intervals have the size then it will sort by the
#         lower number in the interval
def sort_by_interval_size (tuples_list):
  # sorts based on the absolute value of the range for each interval
  sort_tuples = sorted(tuples_list, idx = lambda x: abs(x[1] - x[0]))
  return sort_tuples

# Input: no input
# Output: a string denoting all test cases have passed
def test_cases ():
  assert merge_tuples([(1,2)]) == [(1,2)]
  # write your own test cases

  assert sort_by_interval_size([(1,3), (4,5)]) == [(4,5), (1,3)]
  # write your own test cases

  return "all test cases passed"

def main():
  #open file intervals.in and read the data and create a list of tuples
  unformatted_inList = sys.stdin.readlines()
  
  # removes unnecessary characters from the entry #unformatted_inList
  inList = [entry.strip("\n").strip() for entry in unformatted_inList]
  
  # sets the number of intervals and removes from list
  num_intervals = inList[0]
  del inList[0]

  # creates a list of tuples
  transition_lst = [line.split(" ") for line in inList]
  store_tuples = [ (int(entry[0]), int(entry[1])) for entry in transition_lst ]

  # merge the list of tuples
  collapsed_tup_list = merge_tuples (store_tuples)

  # sort the list of tuples according to the size of the interval
  size_sorted_tup_list = sort_by_interval_size (collapsed_tup_list)

  # prints the output list of tuples from the two functions
  print(collapsed_tup_list)
  print(size_sorted_tup_list)

if __name__ == "__main__":
  main()

# python3 Intervals.py < intervals.in.txt