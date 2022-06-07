from sys import argv

script, filename = argv

print(f"We're going to erase {filename}")
print("If you dont want that, hit CTRL-C (ˆC")
print("If you do want that, hit RETURN.")

input("?")


# Get the contents of the current file
current_file = open(filename)
current_file_contents = current_file.read()
current_file.close()

# Now open the file again and specify write this time
print("Opening the file...")
target = open(filename, 'a')

# This empties the file
print("Truncating the file", "Goodbye")
target.truncate()

# Write three lines to the newly emptied file
print("Now im going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3)
target.close()

print(f"\nYou are about to print the following file {filename} it previously had \n")
# print out the old contents
print(current_file_contents)

# open a new file object again , read print and close.
print("\n The new file has the following")
new_file = open(filename)
print(new_file.read())
new_file.close()




