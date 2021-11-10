#  File: Adjacency.py

#  Description: Converts an edge list into an adjacency matrix

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610
        
# Given an edge list of a weighted directed graph where each edge is provided as [src, dest, weight],
# return the corresponding adjancency matrix as a 2D list of INTEGERS where the columns and rows are
# sorted by vertex label. Labels may be provided as strings or integers.


def edge_to_adjacency(edge_list):
    adjMat = [[0 for i in range(len(edge_list))] for j in range(len(edge_list))]

    

    for edges in edge_list: 
        start = edges[0]
        end = edges[1]
        weight = edges[2]

        


# ------ DO NOT CHANGE BELOW HERE ------ #
import ast

def main():
    matrix = edge_to_adjacency(ast.literal_eval(input()))

    print('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix]))

if __name__ == "__main__":
    main()

# python3 Adjacency.py < R.txt