from sys import argv

script, from_file, to_file = argv

# open the new file for writing
# write to it by opening the old file and reading from it
open(to_file, 'w').write(open(from_file).read())

print("complete")