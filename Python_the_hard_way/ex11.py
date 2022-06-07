# end=' ' just makes it so the input is on the same line and not the next line
print("How old are you?", end=' ')
# you can add int in front to force a number
age = int(input())
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh? ", end=' ')
weight = input()

print(f"So, you're {age}& {height} and {weight}")
