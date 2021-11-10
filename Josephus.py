#  File: Josephus.py

#  Description: This program creates a circular linked list to determine the 
#  order in which the soldiers will be killed off. The output returns each 
#  soldier's number, and the last number denotes the soldier that escapes 
#  and survives.  

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/21/2021

#  Date Last Modified: 7/23/2021

import sys


class Link(object):
    # constructor 
    def __init__(self, data, next = None):
        self.data = data
        self.next = next 


class CircularList(object):
    # Constructor
    def __init__ ( self ): 
        self.first = None

    # Insert an element (value) in the list
    def insert ( self, data ):
        new_data = Link(data)
        curr = self.first
        # if list is empty
        if curr == None:
            self.first = new_data
            new_data.next = new_data
        # list not empty, moves through to last node before circles to first
        else:
            while curr.next != self.first:
                curr = curr.next
            curr.next = new_data
            new_data.next = self.first 
        return 

    # Find the Link with the given data (value)
    # or return None if the data is not there
    # Link returns as a node, not an int
    def find ( self, data ):
        curr = self.first
        # list is empty 
        if curr == None:
            return None
        # first value is the targeted value 
        elif data == curr.data:
            return curr
        # list not empty, moves through to last node before circles to first
        else:
            while data != curr.data:
                # went through whole list, value not found
                if curr.next == self.first:
                    return None
                curr = curr.next
        return curr

    # Delete a Link with a given data (value) and return the Link
    # or return None if the data is not there
    # Link is returned as a node, not an int
    def delete ( self, data ):
        prev, curr = self.first, self.first 
        target_data = self.find(data)

        # list is empty or value not in list:
        if curr == None or target_data == None:
            return None
        # value is in a non-empty list
        else:
            # value is the only node in list
            if data == curr.data and curr.next == self.first:
                self.first = None
                return curr
            # value is the head of the list that contains more than 1 node
            elif data == curr.data and curr.next != self.first:
                last_node = self.first
                while last_node.next != self.first:
                    last_node = last_node.next
                self.first = curr.next
                last_node.next = self.first
                return curr
            # value in list and is not the head
            else:
                while data != curr.data:
                    prev = curr 
                    curr = curr.next
                prev.next = curr.next
                return curr

    # Delete the nth Link starting from the Link start 
    # Return the data of the deleted Link AND return the
    # next Link after the deleted Link in that order
    def delete_after ( self, start, n ):
        curr = start
        # iterates until target number is found 
        for i in range(n-1):
            curr = curr.next 
        # stores next value after deleted value 
        next_node = curr.next 
        
        # returns a tuple of an int value, and a node 
        return self.delete(curr.data).data, next_node
    
    # Return a string representation of a Circular List
    # The format of the string will be the same as the __str__ 
    # format for normal Python lists
    def __str__ ( self ):
        curr = self.first 
        store = []
        if curr == None:
            return str(store)
        else:
            while curr.next != self.first:
                store.append(curr.data)
                curr = curr.next
            store.append(curr.data)
        return str(store) 


def main():
    # read number of soldiers
    line = sys.stdin.readline()
    line = line.strip()
    num_soldiers = int (line)
    
    # read the starting number
    line = sys.stdin.readline()
    line = line.strip()
    start_count = int (line)

    # read the elimination number
    line = sys.stdin.readline()
    line = line.strip()
    elim_num = int (line)

    # creates a new circular list to hold soldiers 
    circle_lst = CircularList()

    # fill list with number of soldiers 
    for i in range(1, num_soldiers+1):
        circle_lst.insert(i)

    # finds current node to start removing soldiers 
    curr_node = circle_lst.find(start_count)
    for i in range(1, num_soldiers + 1):
        to_delete = circle_lst.delete_after(curr_node, elim_num)
        # prints soldier that is deleted
        print(to_delete[0])
        # prepares to calculate the next soldier to delete
        curr_node = to_delete[1]
    
if __name__ == "__main__":
    main()

# python3 Josephus.py < josephus.in.txt