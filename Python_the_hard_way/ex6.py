# setting a variable to 10
types_of_people = 10
# variable with formatted string
x = f"There are {types_of_people} types of people"
# variables
binary = "binary"
do_not = "dont"
# another variable with a formatted string.
y = f"Those who know {binary} and those who {do_not}"

# print results of two variables
print(x)
print(y)
# print function with variables () are needed in this unlike variables
print(f"I said: {x}")
print(f"I also said: '{y}'")
# Variables
hilarious = True
# Curly brackets allow you to leave a string with a blank variable, essentially you can pass anything to this with the .format after the variable name
joke_evaluation = "Isn't that joke so funny?! {}"

# print with just variables amd pass in another variable with .format
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

# combine to variables with + sign
print(w + e)

# Simple example of how to do this

a = "hello {}"
b = "Kevin"

print(a.format(b))


