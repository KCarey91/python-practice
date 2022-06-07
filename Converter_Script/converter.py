import sys
import time


def feet_to_mm(feet):
    conversion_to_mm = feet * 304.8
    return conversion_to_mm


def mm_to_feet(mm):
    conversion_to_feet = mm * 0.0032808
    return conversion_to_feet


def celsius_to_fahrenheit(c):
    fahrenheit = (c * 1.8) + 32
    return fahrenheit


def fahrenheit_to_celsius(f):
    celsius = (f - 32) / 1.8
    return celsius


def quit():
    print("shutting downn...")
    time.sleep(1)
    sys.exit()


def menu():

    while True:
        try:
            print("**** Main Menu ****")
            time.sleep(1)

            # Read the selection and make sure
            print("\nPlease select the number of the operation would like to run from the below menu:")

            selection = int(input(""" 
            1: Convert feet to mm 
            2: Convert mm to feet
            3: Convert Celsius to Fahrenheit 
            4: Convert Fahrenheit to Celsius 
            5: Quit\n   
            """))

        except ValueError:
             print("Error, This is not a number. Try again.")

        else:
            if selection == 1:
                feet_total = float(input("Enter the amount of feet you would like converted to mm, you can use a decimal point to represent inches ex: 12.6: "))
                total = feet_to_mm(feet_total)
                # Format result to one decimal point
                formatted_total = round(total, 1)
                print(f"\n{feet_total}ft is {formatted_total}mm\n")
                # Sleep and show the menu again
                time.sleep(2)
                menu()
            elif selection == 2:
                mm_total = float(input("Enter the amount of mm you would like converted to feet: "))
                total = mm_to_feet(mm_total)
                # Format result to one decimal point
                formatted_total = round(total, 1)
                print(f"{mm_total}mm is {formatted_total}ft")
                # Sleep and show the menu again
                time.sleep(1)
                menu()
            elif selection == 3:
                celsius = float(input("Temperature value in degree Celsius: "))
                total = celsius_to_fahrenheit(celsius)
                # Format result to one decimal point
                formatted_total = round(total, 2)
                print(f"{celsius} degrees celsius is {formatted_total} degrees Fahrenheit")
                # Sleep and show the menu again
                time.sleep(1)
                menu()
            elif selection == 4:
                fahrenheit = float(input("Temperature value in degree Fahrenheit: "))
                total = fahrenheit_to_celsius(fahrenheit)
                # Format result to one decimal point
                formatted_total = round(total, 2)
                print(f"{fahrenheit} degrees fahrenheit is {formatted_total} degress celsius")
                # Sleep and show the menu again
                time.sleep(1)
                menu()
            elif selection == 5:
                quit()
            else:
                print("You did not select a valid option")
                time.sleep(1)
                menu()
        break


menu()