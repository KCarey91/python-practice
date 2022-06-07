# remember this is called a module or libraries if you are importing something
from sys import argv
#  read the WYSS section for how to run this
hello, first, second, third = argv
# pydoc is like man tells you what an inbuilt function or module can do
print("The script is called:", hello)
print("another way to print the file name is by just passing argv[0] see.. " + argv[0])

print("The first variable is:", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)


