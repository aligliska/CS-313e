#  File: Radix.py

#  Description: This program creates a queue list to sort a 
#  list of strings that contain numbers and lowercase letters. 
#  The order of the sorted list follows that of ascii characters
#  and the created dictionary that contains the numeric orders.

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/12/2021

#  Date Last Modified: 7/14/2021

import sys


class Queue (object):
  def __init__ (self):
    self.queue = []

  # add an item to the end of the queue
  def enqueue (self, item):
    self.queue.append (item)

  # remove an item from the beginning of the queue
  def dequeue (self):
    return (self.queue.pop(0))

  # check if the queue if empty
  def is_empty (self):
    return (len(self.queue) == 0)

  # return the size of the queue
  def size (self):
    return (len(self.queue))


# Input: a is a list of strings that have either lower case
#        letters or digits
# Output: returns a sorted list of strings
def radix_sort (a):
  '''
  Sorts the list of string based on a dictionary of numbers/letters with keys
  '''
  # creates and populates a dictionary with numbers and letters as keys
  store_dict = {}
  for i in range(10):
    store_dict[str(i)] = i
  for i in range(97, 123):
    store_dict[chr(i)] = i - 87
  
  # creates a queue list 
  queue_list = [Queue() for i in range(len(store_dict))]

  # gets length of longest string; sets maximum number of iterations
  longest_char = len(max(a, key = len))

  # equalizes the length of each string 
  for i in range(len(a)):
    a[i] = a[i].ljust(longest_char, "-")

  # queueing and dequeueing
  for i in range(longest_char-1, -1, -1):
    for strng in a:
      # adds strings into queue list by comparing characters in reverse order
      if strng[i] == "-":
        queue_list[0].enqueue(strng)
        continue
      queue_key = int(store_dict[strng[i]])
      queue_list[queue_key].enqueue(strng)

    a.clear()
    # dequeues queue list for next iteration 
    for slot in queue_list:
      while not slot.is_empty():
        a.append(slot.dequeue())

  # removes dashes from string
  for i in range(len(a)):
    a[i] = a[i].replace("-", "")

  return a


def main():
  # read the number of words in file
  line = sys.stdin.readline()
  line = line.strip()
  num_words = int (line)

  # create a word list
  word_list = []
  for i in range (num_words):
    line = sys.stdin.readline()
    word = line.strip()
    word_list.append (word)

  # use radix sort to sort the word_list
  sorted_list = radix_sort (word_list)

  # print the sorted_list
  print (sorted_list)

if __name__ == "__main__":
  main()

# python3 Radix.py < radix.in.txt

    
