""" def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)

    print(f"Your BMI is: {bmi:.2f}")

    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Overweight")
    else:
        print("Obese")


# Function call (outside the function)
calculate_bmi(70, 1.75)
 """

def check_age(age):
    if age >= 18:
        return "Eligible"
    else:
        return "Not Eligible"
