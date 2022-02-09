year = int(input("Which year you want to check? "))

if year % 4 == 0 or year % 100 == 0 and year % 400 == 0:
    print("This is a leap year!")
else:
    print("This is NOT a leap year!")