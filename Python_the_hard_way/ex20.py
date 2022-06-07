from sys import argv

script, input_file = argv


# This prints the file, basically all we do is open the file first in {current_file} and then pass it in to be read
def print_all(f):
    print(f.read())


"""
Files are like old Tapes that need to be rewound after being read, the cursor is at the bottom in this case
In Python, seek() function is used to change the position of the File Handle to a given specific position. 
seek() function is dealing in bytes, not lines. The code seek(0) moves the file to the 0 byte (first byte)
File handle is like a cursor, which defines from where the data has to be read or written in the file.
0: sets the reference point at the beginning of the file
1: sets the reference point at the current file position
2: sets the reference point at the end of the file
"""


def rewind(f):
    f.seek(0)


# Takes the line number and reads the file at that line, in this case the cursor is at the top since we set seek to 0.
def print_a_line(line_count_number, f):
    print(line_count_number, f.readline())


# Global variable instead of having to open the file in each function
current_file = open(input_file)

print("First let's print the whole file \n")

print_all(current_file)

print("Now lets rewind, kind of like a tape")

rewind(current_file)

print("Lets print 3 lines")
# line number counter variable, we can add to this to keep track of where we are.
current_line = 1
print_a_line(current_line, current_file)
# short hand for adding to the count
current_line += 1
print_a_line(current_line, current_file)
# long way of adding to the count
current_line = current_line +1
print_a_line(current_line, current_file)


