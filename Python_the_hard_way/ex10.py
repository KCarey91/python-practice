quote = "Joe"
print(f"my name is \"{quote}\"")  # Escape variable with double quotes
print("I am 6\'2\" tall.")  # Escape double quotes
print('I am 6\'2\" tall.')  # Escape single quotes

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
# This is a double escape, the second backslash will show
backslash_cat = "I'm \\ a \\ cat."
# /t does a tab * is just a way to make a bullet point
fat_cat = """
I'll do a list:
\t* Cat Food 
\t* Fishies 
\t* Catnip\n\t* Grass 
"""

asciiBell = "\aHowya\rasciiBell"
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)
print(asciiBell)
