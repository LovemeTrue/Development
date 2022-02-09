while True:
    ageInput = input("What is your current age?: ")
    if (ageInput.isnumeric()):
        ageInput = int(ageInput)
        break
    else:
        print ('Ошибка! Введите целое число')

daysYear = 365
weeksYear = 52
monthsYear = 12

yearRemaining = 90 - ageInput

currentDays = ageInput * daysYear
currentWeeks = ageInput * weeksYear
currentMonths = ageInput * monthsYear

message = f"You have {yearRemaining} years remaining, and {currentDays} days, and {currentWeeks} weeks, and {currentMonths} months passed by"
print(message)