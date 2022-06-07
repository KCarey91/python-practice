from sys import argv

# this will print the filename
print(argv[0])
# this will print the first argument that is passed after that
print(argv[1])

# these are place holders so instead of calling the posisiton in the array you can just call the names in the print statement.
script, filename = argv

# This script allows you to pass a file to read from it

answer = input(f"Is this the correct file you would like to read from: {filename} type yes to confirm")
# This we can just say open that file and store it in a variable

if answer == "yes":
    # this creates a file object
    txt = open(filename)
    print("\n", txt.read())
    txt.close()

print("print the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
txt_again.close()




