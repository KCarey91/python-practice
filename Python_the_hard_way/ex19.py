from sys import argv

script_name, in_file, out_file_name = argv


def read_and_write_to_new_file(fromFile, toFile):
    open(toFile, 'w').write(open(fromFile).read())
    print(f"Completed copying from {fromFile} to {toFile} it is {len(toFile)} long")


def read_new_file(outfile):
    print(f"Printing contents of {outfile}\n")
    print(open(outfile).read())


def truncate_file(filename):
    # Now open the file again and specify write this time
    print("Opening the file...")
    target = open(filename, 'a')

    # This empties the file
    print("Truncating the file", "Goodbye")
    target.truncate(0)
    target.close()

read_and_write_to_new_file(in_file, out_file_name)
read_new_file(out_file_name)
truncate_file(out_file_name)

"""
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers")


print("We can just give the numbers directly")
cheese_and_crackers(20,30)

print("Or we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("We can even do math inside too")
cheese_and_crackers(25 * 3, 79 % 3)

print("You can also combine variables and numbers")
cheese_and_crackers(amount_of_crackers + 10, amount_of_cheese * 4)

"""

