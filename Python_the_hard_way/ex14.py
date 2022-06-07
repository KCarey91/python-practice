from sys import argv

script, user_name, number = argv
prompt = "--->"

print(f"Hi {user_name}, Im the {script} script.")
print("Id like to ask you a few questions")
print(f"Do you like me {user_name}?")
likes = input(prompt)

dogs = input(f"Do you have {number} dogs\n{prompt}")

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me. 
You live in {lives}. Not sure where that is. 
And you have a {computer} computer. Nice. 
Also, you said {dogs} to having a dog. 
""")