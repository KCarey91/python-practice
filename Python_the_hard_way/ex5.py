name = "Zed A. Shaw"
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
cm_per_in = 2.54


print(f"Lets talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} lbs")
print("Actually thats not too heavy")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee")

# this line is tricky, try to get it exactly correct
total = age + height + weight
calculation_for_height = height * cm_per_in
calculation_for_weight = weight / 2.20
print(f"If I add {age}, {height}, and my {weight} I get {total}")
print(f"There are 2.54 cm in 1 inch, you are {height} in inches, you are {calculation_for_height} cm tall")
print(f"You weigh {weight} lbs, you are", format(calculation_for_weight, ",.2f"), "in kg")
print(f"you might aswel round up your {weight} lbs", round(calculation_for_weight), "kg is what you are really")


