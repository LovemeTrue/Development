print("Welcome to the rolercoaster!","\n")

height = int(input("What is your height?"))

bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5. ")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7. ")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us! ")
        bill = 0
    else:
        bill = 12
        print("Adult tickets are $12. ")

wants_photo = input("Do you want a photo taken? Y or N ")
if wants_photo == "Y":
    bill += 3

print(f"Your final bill is: ${bill}")