#  File: Cipher.py

#  Description: This program inputs a file with two strings. The first string
#  is to be encrypted while the second string is to be decrypted. The 
#  encryption occurs by rotating an array by 90º while the decryption 
#  undos this by rotating -90º (or 270º). 

#  Student Name: Alice Gee

#  Student UT EID: ag67642

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 06/14/2021

#  Date Last Modified: 6/17/2021

import sys
import math 


#  adds astericks to string so that the length is a perfect square
#  returns as a list of characters, so input is mutable
def fill_astericks_encrypt(strng): 
    store_astericks = ""

    #  checks if length of string is a perfect square
    if math.sqrt(len(strng)) != math.ceil(math.sqrt(len(strng))):
        next_square = (math.ceil(math.sqrt(len(strng))))**2

        #  adds astericks to make length a perfect square
        for i in range(next_square - len(strng)):
            store_astericks += "*"
        return list(strng + store_astericks)
    else: 
        return list(strng)

# creates an array with placeholding "*" and 0's
def fill_astericks_decrypt(strng): 
    store_astericks = ""

    # creates number of "*" needed to make a square array 
    next_square = (math.ceil(math.sqrt(len(strng))))**2
    dimension = int(math.sqrt(next_square))
    num_astericks = next_square - len(strng)
    store_astericks = "*" * num_astericks
    store_astericks = list(store_astericks)

    # creates an empty array with all 0's 
    new_array = []
    for i in range (dimension):
        column = []
        for j in range (dimension):
            column.append(0)
        new_array.append(column)

    # replaces 0's with "*" from bottom to top, left to right
    for j in range(dimension):
        for i in range (dimension -1, -1, -1):
            try: 
                new_array[i][j] = store_astericks.pop()
            except:
                continue
    
    return new_array


#  creates a square 2d list of the characters from the input string 
def make_array_encrypt(strng):
    new_string = list(strng)
    dimensions = int(math.sqrt(len(new_string)))

    filler_array = []
    for i in range(dimensions):
        column = []
        for j in range(dimensions):
            column.append( new_string.pop(0) )          
        filler_array.append(column)
    
    return filler_array

# fills in remaining spots in array that are not "*" with characters
def make_array_decrypt(strng):
    asterick_array = fill_astericks_decrypt(strng)
    new_string = list(strng)

    # replaces 0's with characters from input string 
    filled_array = []
    for row in asterick_array:
        column = []
        for entry in row:
            if entry != "*":
                column.append(new_string.pop(0))
            else:
                column.append(entry)
        filled_array.append(column)
        
    return filled_array


#  Input: strng is a string of 100 or less of upper/lower case & digits
#  Output: function returns an encrypted string 
def encrypt(strng):

    #  adds astericks to make length of string a perfect square
    new_string = fill_astericks_encrypt(strng)

    #  creates a 2d list with characters from new_string 
    filler_array = make_array_encrypt(new_string)

    #  rotates filler_array by 90º
    rotated_array = list(zip(*filler_array[::-1]))

    encrypted_strng = ""
    
    #  concatonates the characters to form encrypted_string
    for row in rotated_array:
        for column in row:
            if column != "*":
                encrypted_strng += column

    return encrypted_strng


#  Input: strng is a string of 100 or less of upper/lower case & digits
#  Output: function returns an encrypted string 


def decrypt(strng):

    #  creates a 2d list with characters from new_string
    filler_array = make_array_decrypt(strng)

    #  rotates filler_array by 270º ≈ -90º 
    rotated_array = list(zip(*filler_array[::-1]))
    rotated_array = list(zip(*rotated_array[::-1]))
    rotated_array = list(zip(*rotated_array[::-1]))

    decrypted_strng = ""
    
    #  concatonates the characters to form decrypted_string
    for row in rotated_array:
        for column in row:
            if column != "*":
                decrypted_strng += column

    return decrypted_strng


def main():

    #  opens file reads the data to create a list of strings
    unformatted_inList = sys.stdin.readlines()

    #  removes unnecessary characters from unformatted_inList
    inList = [line.strip("\n").strip() for line in unformatted_inList]

    #  assigns which line gets encrypted and which gets decrypted
    to_encrypt = inList[0]
    to_decrypt = inList[1]

    #  creates encrypted string if input string is a string of 100 or  
    #  less of upper/lower case and digits
    if to_encrypt.isalnum() and len(to_encrypt) in range(1, 101):
        encrypted_line = encrypt(to_encrypt)
        print(encrypted_line)
        
    #  creates decrypted string if input string is a string of 100 or  
    #  less of upper/lower case and digits
    if to_decrypt.isalnum() and len(to_decrypt) in range(1, 101):
        decrypted_line = decrypt(to_decrypt)
        print(decrypted_line)


if __name__ == "__main__":
  main()
