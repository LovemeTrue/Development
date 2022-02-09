print("Welcome to the Pizza Deliveries!\n")

size = input("What size of pizza do you prefer? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
add_extra_cheese = input("Extra cheese? Y or N ")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

pepperoni_small = 2
pepperoni_medium = 3
pepperoni_large = 4

extra_cheese = 1

# Ordering S pizza
if size == "S" and add_extra_cheese == "Y" and add_pepperoni == "Y":
    bill = small_pizza + pepperoni_small + extra_cheese
    print(f"Your bill is: ${bill}")

elif size == "S" and add_pepperoni == "N" and add_extra_cheese == "Y":
    bill = small_pizza + extra_cheese
    print(f"Your bill is: ${bill}") 

elif size == "S" and add_pepperoni == "Y" and add_extra_cheese == "N":
    bill = small_pizza + pepperoni_small
    print(f"Your bill is: ${bill}")

elif size == "S" and add_extra_cheese == "N" and add_pepperoni == "N":
    bill = small_pizza
    print(f"Your bill is: ${bill}")

# Ordering M size pizza
if size == "M" and add_extra_cheese == "Y" and add_pepperoni == "Y":
    bill = medium_pizza + pepperoni_medium + extra_cheese
    print(f"Your bill is: ${bill}")

elif size == "M" and add_pepperoni == "N" and add_extra_cheese == "Y":
    bill = medium_pizza + extra_cheese
    print(f"Your bill is: ${bill}") 

elif size == "M" and add_pepperoni == "Y" and add_extra_cheese == "N":
    bill = medium_pizza + pepperoni_medium
    print(f"Your bill is: ${bill}")

elif size == "M" and add_extra_cheese == "N" and add_pepperoni == "N":
    bill = medium_pizza
    print(f"Your bill is: ${bill}")

# Ordering L pizza

if size == "L" and add_extra_cheese == "Y" and add_pepperoni == "Y":
    bill = large_pizza + pepperoni_large + extra_cheese
    print(f"Your bill is: ${bill}")

elif size == "L" and add_pepperoni == "N" and add_extra_cheese == "Y":
    bill = large_pizza + extra_cheese
    print(f"Your bill is: ${bill}") 

elif size == "L" and add_pepperoni == "Y" and add_extra_cheese == "N":
    bill = large_pizza + pepperoni_large
    print(f"Your bill is: ${bill}")

elif size == "L" and add_extra_cheese == "N" and add_pepperoni == "N":
    bill = large_pizza
    print(f"You have ordered large pizza! Your bill is: ${bill}")