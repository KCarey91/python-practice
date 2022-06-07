# Defining a string that can accept four arguments
formatter = "{} {} {} {}"

# pass ints to formatter string
print(formatter.format(1, 2, 3, 4))
#
test = formatter.format(1, 2, 3, 4)
print(type(test))
print(test)
# Pass 4 separate strings into the formatter
print(formatter.format("one", "two", "three", "four"))
# Pass booleans into string fomratter
print(formatter.format(True, False, False, True))
# Passes itself inside the string with the .format
print(formatter.format(formatter, formatter, formatter, formatter))
# Strings on different lines can be seperated with a , and then next line
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
name = "Kevin"

# 2 different ways to use format.
print("hello" + format(name))
print("hello", format(name))
print(f"hello{name}")


