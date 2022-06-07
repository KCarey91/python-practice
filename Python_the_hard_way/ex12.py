# when you do it like this you don't need the end=' ' to get the answer on the same line
age = input("How old are you ")
height = input("How tall are you ")
# This is the old way
print("How much do you weight?", end=' ')
weight = input()
print(f"I am {age} {height} {weight}")