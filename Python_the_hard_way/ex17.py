from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Printing {from_file} to {to_file}")

# We could do these two in one line
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

# Does the output file exist

print("Press RETURN to proceed and ctrl c to cancel")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()