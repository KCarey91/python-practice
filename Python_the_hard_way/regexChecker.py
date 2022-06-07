from sys import argv
import re

#Check if the string starts with "The" and ends with "Spain":
regex = input("Enter regex: ")
txt = str(input("Enter Text to check: "))


print(f"Regex is {regex} and the text to check is {txt}")

x = re.search(regex, txt)

if x:
  print(f" YES! We have a match! {regex} matches {txt}")
else:
  print("No match")