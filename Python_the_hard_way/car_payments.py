

def car_payments():
    while True:
        try:
            # Read the amount borrowed, interest rate and loan duration from the user.
         loan_amt = float(input("How much are you borrowing? "))
         rate = float(input("\nWhat is the interest rate you are getting "))
         years = float(input("How many years are your borrowing for? "))

        except ValueError:
           print("Error, This is not a number. Try again.")

        else:
            # Get interest rate per month in decimal format interest rate divided by months and then divded by 100 to get decimal
            rate_per_month = rate / 12 / 100
            # Compute the interest rate per payment period and the number of payments
            num_payments = years * 12

            # Compute the payment amount (loan_amount)(rate_per_month)(1 + rate_per_month)^60 Divide that by (1 + rate_per_month)^ 60 - 1
            payment_amt = rate_per_month * loan_amt / (1 - (1 + rate_per_month) ** -num_payments)

            # Compute the total cost of borrowing
            total_cost = (num_payments * payment_amt - loan_amt)

            # Display Results
            print("The payment amount will be £" + format(payment_amt, ",.2f"), "per month.")
            print("The total cost of borrowing will be £" + format(total_cost, ",.2f"))

        break

car_payments()
