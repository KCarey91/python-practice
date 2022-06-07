# Argv takes command line arguments input takes in application arguments
from sys import argv
# the first argument will always be the file name, the 2nd will be what you type after that
# delete = argv[1]
# file = argv[0]
# so you can just make a list of variable like below or specify it above with list position
file, flag = argv
# You can use argv[0] or file here, both the same
question = str(input("Do you want to delete:\t" + argv[0] + " "))

if question == "yes":
    print("You answered ", question, " and you set the flag", flag, "self destructing now")
else:
    print("That was close you almost deleted", file)