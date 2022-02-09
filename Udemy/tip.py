print("Welcome to the tip calculator!","\n")

while True:
    bill_input = input("What was the total bill?: ")
    if (bill_input.isnumeric()):
        bill_input = int(bill_input)
        break
    else:
        print("An error has occurred! Type a whole number")
while True:
    tip_input = input("What percentage tip would you like to give? 10, 15, or 12? ")
    if (tip_input.isnumeric()):
        tip_input = int(tip_input)
        break
    else:
        print("An error has occurred! Type a whole number")
while True:
    people_input = input("How many people would you like to split the bill? ")
    if (people_input.isnumeric()):
        people_input = int(people_input)
        break
    else:
        print("An error has occurred! Type a whole number")

tip_amount = float(tip_input)/100

tip_sum = (bill_input + tip_amount) / people_input
print(round(tip_sum, 2))