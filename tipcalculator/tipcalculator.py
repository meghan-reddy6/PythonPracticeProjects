while True:
    print("Welcome to the TIP CALCULATOR")
    total_bill = float(input("What was the total bill? $"))
    tip_percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    number_of_people = int(input("How many people to split the bill? "))
    tip_amount = total_bill * (tip_percentage / 100)
    total_bill_with_tip = total_bill + tip_amount
    amount_per_person = total_bill_with_tip / number_of_people
    final_amount = "{:.2f}".format(amount_per_person)
    print(f"Each person should pay: ${final_amount}")
    another_calculation = input("Would you like to perform another calculation? (yes/no): ").strip().lower()
    if another_calculation != 'yes':
        break