from sys import argv

script, filename = argv
# Open a new file and allow writing and reading
target = open(filename, 'x+')

print("Now im going to ask you for three lines")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3)
target.close()

print("\n The new file has the following")

new_output = open(filename, 'r')
print(new_output.read())



