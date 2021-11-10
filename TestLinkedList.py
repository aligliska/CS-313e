#  File: TestLinkedList.py

#  Description: This program uses two classes to work with linked lists. 
#  The class develops functions that allow the user to manipulate the 
#  list in certain ways. 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 7/21/2021

#  Date Last Modified: 7/22/2021

import random


class Link (object):
    # constructor
    def __init__ (self, data, next = None):
        self.data = data
        self.next = next


class LinkedList (object):
    # create a linked list
    # you may add other attributes
    def __init__ (self):
        self.first = None

    # get number of links 
    def get_num_links (self):
        count = 0
        curr = self.first
        while curr != None:
            count += 1
            curr = curr.next
        return count 
    
    # add an item at the beginning of the list
    def insert_first (self, data): 
        new_data = Link(data)
        new_data.next = self.first
        self.first = new_data

    # add an item at the end of a list
    def insert_last (self, data): 
        new_data = Link(data)
        curr = self.first
        if curr == None:
            self.first = new_data
            return 
        else:
            while curr.next != None:
                curr = curr.next
            curr.next = new_data
        return 

    # add an item in an ordered list in ascending order
    # assume that the list is already sorted
    def insert_in_order (self, data): 
        curr = self.first
        if curr == None or data <= curr.data:
            self.insert_first(data)
            return 
        else:
            while curr.next != None and data >= curr.next.data:
                curr = curr.next
            new_data = Link(data, curr.next)
            curr.next = new_data
            return 

    # search in an unordered list, return None if not found
    def find_unordered (self, data): 
        curr = self.first
        if curr == None:
            return None
        else:
            while curr != None:
                if data == curr.data:
                    return curr
                curr = curr.next
            return None

    # Search in an ordered list, return None if not found
    def find_ordered (self, data): 
        curr = self.first
        while curr != None and data >= curr.data:
            if data == curr.data:
                return curr
            curr = curr.next
        return None

    # Delete and return the first occurrence of a Link containing data
    # from an unordered list or None if not found
    def delete_link (self, data):
        prev, curr = self.first, self.first
        if curr == None:
            return None
        
        while data != curr.data:
            if curr.next == None:
                return None
            else:
                prev = curr
                curr = curr.next
        if curr == self.first:
            self.first = self.first.next
        else:
            prev.next = curr.next
        return curr

    # String representation of data 10 items to a line, 2 spaces between data
    def __str__ (self):
        string = ""
        count = 0
        curr = self.first
        if curr == None:
            return string

        while curr.next != None:
            string += str(curr.data)
            count += 1
            if count != 10:
                string += "  "
            else:
                string += "\n"
                count = 0
            curr = curr.next
        string += str(curr.data)
        return string 

    # Copy the contents of a list and return new list
    # do not change the original list
    def copy_list (self):
        copy_linked_list = LinkedList()
        curr = self.first 
        if self.is_empty():
            return copy_linked_list
        else:
            while curr != None:
                copy_linked_list.insert_last(curr.data)
                curr = curr.next
        return copy_linked_list

    # Reverse the contents of a list and return new list
    # do not change the original list
    def reverse_list (self): 
        copy_linked_list = LinkedList()
        curr = self.first 
        if self.is_empty():
            return copy_linked_list
        else:
            while curr != None:
                copy_linked_list.insert_first(curr.data)
                curr = curr.next
        return copy_linked_list

    # Sort the contents of a list in ascending order and return new list
    # do not change the original list
    def sort_list (self): 
        copy_linked_list = LinkedList()
        curr = self.first
        if self.is_empty():
            return copy_linked_list
        else:
            while curr != None:
                copy_linked_list.insert_in_order(curr.data)
                curr = curr.next
        return copy_linked_list

    # Return True if a list is sorted in ascending order or False otherwise
    def is_sorted (self):
        curr = self.first
        if self.is_empty() or self.get_num_links() == 1:
            return True
        else:
            while curr.next != None:
                if curr.data > curr.next.data:
                    return False
                curr = curr.next
            return True

    # Return True if a list is empty or False otherwise
    def is_empty (self): 
        if self.first == None:
            return True
        return False 

    # Merge two sorted lists and return new list in ascending order
    # do not change the original lists
    def merge_list (self, other): 
        new_list = LinkedList()
        curr_self = self.first
        curr_other = other.first
        # add list one in order
        while curr_self != None:
            new_list.insert_in_order(curr_self.data)
            curr_self = curr_self.next
        # add list two in order 
        while curr_other != None:
            new_list.insert_in_order(curr_other.data)
            curr_other = curr_other.next
        return new_list

    # Test if two lists are equal, item by item and return True
    def is_equal (self, other):
        curr_self = self.first
        curr_other = other.first
        if self.get_num_links() == other.get_num_links():
            while curr_self != None and curr_other != None:
                if curr_self.data == curr_other.data:
                    curr_self = curr_self.next
                    curr_other = curr_other.next
                else:
                    return False
            return True
        return False 

    # Return a new list, keeping only the first occurence of an element
    # and removing all duplicates. Do not change the order of the elements.
    # do not change the original list
    def remove_duplicates (self):
        copy_linked_list = LinkedList()
        curr = self.first
        if self.is_empty():
            return copy_linked_list
        else:
            while curr != None:
                if copy_linked_list.find_unordered(curr.data):
                    curr = curr.next
                    continue
                copy_linked_list.insert_last(curr.data)
                curr = curr.next
        return copy_linked_list


def main():
    # Test methods insert_first() and __str__() by adding more than
    # 10 items to a list and printing it.
    linked_List = LinkedList()
    for i in range(9, -1, -1):
        linked_List.insert_first(i)
    print(linked_List)

    # Test method insert_last()
    linked_List.insert_last(10)
    print(linked_List)

    # Test method insert_in_order()
    linked_List.insert_in_order(5)
    print(linked_List)

    # Test method get_num_links()
    num_links = linked_List.get_num_links()
    print(num_links)

    # Test method find_unordered() 
    # Consider two cases - data is there, data is not there 
    print(linked_List.find_unordered(3))
    print(linked_List.find_unordered(11))

    # Test method find_ordered() 
    # Consider two cases - data is there, data is not there 
    print(linked_List.find_ordered(6))
    print(linked_List.find_ordered(12))

    # Test method delete_link()
    # Consider two cases - data is there, data is not there 
    print(linked_List.delete_link(5))
    print(linked_List.delete_link(11))

    # Test method copy_list()
    copy_list = linked_List.copy_list()
    print(copy_list)

    # Test method reverse_list()
    reversed_list = linked_List.reverse_list()
    print(reversed_list)
    
    # Test method sort_list()
    new_list = LinkedList()
    for i in range(10):
        new_list.insert_last(random.randint(1,20))
    sorted_new_list = new_list.sort_list()
    print(sorted_new_list)

    # Test method is_sorted()
    # Consider two cases - list is sorted, list is not sorted
    print(new_list.is_sorted())
    print(sorted_new_list.is_sorted())

    # Test method is_empty()
    emp_list = LinkedList()
    print(linked_List.is_empty())
    print(emp_list.is_empty())

    # Test method merge_list()
    merged_list = linked_List.merge_list(new_list)
    print(merged_list)

    # Test method is_equal()
    # Consider two cases - lists are equal, lists are not equal
    print(linked_List.is_equal(copy_list))
    print(linked_List.is_equal(new_list))

    # Test remove_duplicates()
    linked_List.insert_in_order(5)
    linked_List.insert_in_order(5)
    print("******")
    print(linked_List)
    print(linked_List.remove_duplicates())


if __name__ == "__main__":
    main()

# python3 TestLinkedList.py