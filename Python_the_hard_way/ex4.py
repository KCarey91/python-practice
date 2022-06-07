cars = 100
space_in_a_car = 4.0
space_in_a_car2 = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
carpool_capacity2 = cars_driven * space_in_a_car2
average_passengers_per_car = passengers / cars_driven

x2 = 2
x = 5

if(x2 != 5):
    print("please check again. score does not equal 5")


print("There are", cars, "cars available")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("we have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
print("without floating point", carpool_capacity2, "used 4 instead of 4.0")
print("With floating point", carpool_capacity, "used 4.0 in this one")
print("single equals", x, "Double equals", x2)