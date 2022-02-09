height = input("enter your height in m: ").strip()
weight = input("enter your weight in kg: ").strip()



bmi = int(weight) / float(height) ** 2

bmi_as_int = int(bmi)

if bmi_as_int < 18.5:
    print(f"Your BMI is: {bmi_as_int}, It's underweight!")

if  18.5 < bmi_as_int <= 25:
    print(f"Your BMI is: {bmi_as_int}, It's normalweight!")

if  25 < bmi_as_int <= 30:
    print(f"Your BMI is: {bmi_as_int}, It's overweight!")

if  30 < bmi_as_int <= 35:
    print(f"Your BMI is: {bmi_as_int}, It's obese!")

if bmi_as_int >= 30:
    print(f"Your BMI is: {bmi_as_int}, It's clinically obese!")
