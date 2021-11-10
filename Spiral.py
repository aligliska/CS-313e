#  File: Spiral.py

#  Description: The program accepts a file and accepts the first line as the 
#  dimensions for a spiral of numbers. The program creates and stores a 
#  generated spiral and takes additional input values to calculate the sum of
#  the adjacent values. The output is printed individually on a new line. 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Partner Name: Maxwell Kretschmer

#  Partner UT EID: mtk739

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 6/07/2021

#  Date Last Modified: 6/17/2021

# Input: n is an odd integer between 1 and 100
# Output: returns a 2-D list representing a spiral
#         if n is even add one to n

import sys

def create_spiral ( n ):
    int(n)

    num_rows, num_cols = n, n
    spiral = []

    # creates a spiral of correct dimensions 
    for i in range(num_cols):
        column = []
        for j in range(num_rows):
            column.append(0)
        spiral.append(column)
    
    # spiral begins in the center (middle of row and columns)
    current_value = 1
    y, x = (num_rows // 2), (num_cols // 2)

    # max number of entries in the matrix
    num_total_entry = num_rows ** 2
    
    increment = 1

    # adds replaces the zeros to the ascending values 
    while current_value < num_total_entry:
        
        # rightward movements 
        for count in range(increment, 0, -1):
            spiral[y][x] = current_value
            x += 1
            current_value += 1
            
        # downward movements
        for count in range(increment, 0, -1):
            spiral[y][x] = current_value
            y += 1
            current_value += 1

        # increase increment amount
        increment += 1
            
        # leftward movements
        for count in range(increment, 0, -1):
            spiral[y][x] = current_value
            x -= 1
            current_value += 1
            
        # upward movements
        for count in range(increment, 0, -1):
            spiral[y][x] = current_value
            y -= 1
            current_value += 1
            
        # last rightward movement 
        if increment == num_total_entry - current_value:
            increment += 1
            for count in range(increment, 0, -1):
                spiral[y][x] = current_value
                x += 1
                current_value += 1
            current_value = num_total_entry + 1
            
        # increase increment amount 
        increment += 1
    
    return spiral

# finds the indices of a value in a 2D list
def index_2d(lst, n):
    for i, j in enumerate(lst):
        if n in j:
            return [i, j.index(n)]

def sum_adjacent_numbers (spiral, n):
    # finds location of index
    location = index_2d(spiral, n)
    x, y = location[0], location[1]
    dimension = len(spiral)
    
    # initializes the sum of adjacent numbers 
    adjacent_sum = 0

    # adds value from all adjacent values if value exists in spiral
    if (x+1) in range(dimension) and y in range(dimension):
        adjacent_sum += spiral[x+1][y]
    if (x-1) in range(dimension) and y in range(dimension):
        adjacent_sum += spiral[x-1][y]
    if (x) in range(dimension) and (y+1) in range(dimension):
        adjacent_sum += spiral[x][y+1]
    if (x) in range(dimension) and (y-1) in range(dimension):
        adjacent_sum += spiral[x][y-1]
    if (x+1) in range(dimension) and (y+1) in range(dimension):
        adjacent_sum += spiral[x+1][y+1]
    if (x-1) in range(dimension) and (y-1) in range(dimension):
        adjacent_sum += spiral[x-1][y-1]
    if (x+1) in range(dimension) and (y-1) in range(dimension):
        adjacent_sum += spiral[x+1][y-1]
    if (x-1) in range(dimension) and (y+1) in range(dimension):
        adjacent_sum += spiral[x-1][y+1]

    return adjacent_sum


def main():
    # reads the input file from the command line/terminal 
    unformatted_inFile = sys.stdin.readlines()
    inFile= []
    for num in unformatted_inFile:
        inFile.append(int(num.strip("\n")))

    # checks if dimensions of the spiral is odd and within range            
    if inFile[0] % 2 != 0 and inFile[0] in range(2, 100):
        spiralNumber = inFile[0] 

    del inFile[0]

    # creates a spiral 
    spiral = create_spiral(spiralNumber)

    outFile = []

    # generates sum of adjacent values for each input value 
    for i in inFile:
        if i in range(spiralNumber **2):
            adjacentNumbers = sum_adjacent_numbers (spiral, i)
            outFile.append(adjacentNumbers)

    # prints results on individual lines 
    for element in outFile:
        print(element)
        

if __name__ == "__main__":
    main()

