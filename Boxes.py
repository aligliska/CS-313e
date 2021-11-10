
#  File: Boxes.py

#  Description: This program checks if a series of boxes can fit
#  into one another. To check for all possible combinations, all subsets
#  are checked. The program outputs the longest chain of nested boxes 
#  and the occurance of that length of nested boxes. 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/05/2021

#  Date Last Modified: 7/05/2021

import sys


# returns True if box1 fits inside box2
def does_fit (box1, box2):
  '''
  Returns a boolean for whether box 1 fits in box 2
  '''
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  '''
  Creates a list of all subsets through recursion
  '''
  # base case when index is out of range 
  if idx == len(box_list):
    all_box_subsets.append(sub_set)
    return 
  # recursion case to create subsets following 2 different paths 
  else:
    copy_sub_set = sub_set[:]
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
    sub_sets_boxes(box_list, copy_sub_set, idx + 1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets):
  '''
  Returns length of largest nesting boxes and frequency of that size
  '''
  nested_boxes = []
  
  # finds all subsets where boxes are nested 
  for box in all_box_subsets:
    if len(box) != 0:
      curr, next = 0, 1
      curr_subsets = [box[curr]]
      is_nesting_boxes(curr, next, box, curr_subsets, nested_boxes)
    
  # finds the largest size of subset[s]
  nested_boxes.sort(key = len, reverse = True)
  largest_subsets = len(nested_boxes[0])

  # finds the occurance of the largest subset size
  count = 0
  for i in range(len(nested_boxes)-1, -1, -1):
    if len(nested_boxes[i]) == largest_subsets:
      count += 1

  return largest_subsets, count

# returns all subsets where boxes can next within one another
def is_nesting_boxes(curr, next, box, curr_subsets, nested_boxes):
  '''
  Compares if current box can nest into following boxes through recursion
  '''
  # base case if next is out of index
  if next >= len(box):
    # adds the current subset into total subset list
    if curr_subsets not in nested_boxes:
      nested_boxes.append(curr_subsets)

  else:
    # current box fits into the next box
    if does_fit(box[curr], box[next]):
      curr = next
      curr_subsets.append(box[curr])
      # checks if next box fits into the following box (through recursion)
      is_nesting_boxes(curr, next + 1, box, curr_subsets, nested_boxes)
    # curent box does not fit into next box, try with following box
    else:
      is_nesting_boxes(curr, next + 1, box, curr_subsets, nested_boxes)


def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # sort the box list
  box_list.sort()

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes (box_list, sub_set, 0, all_box_subsets)

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = largest_nesting_subsets (all_box_subsets)

  # prints largest number of nesting boxes and its occurance
  for output in all_nesting_boxes:
    print(output)


if __name__ == "__main__":
  main()

# python3 Boxes.py < boxes.in.txt