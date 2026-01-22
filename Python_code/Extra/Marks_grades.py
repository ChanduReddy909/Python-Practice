print()
kannada = float(input("Enter kannada marks: "))
english = float(input("Enter Englisg marks: "))
hindi = float(input("Enter Hindi marks: "))
maths = float(input("Enter Maths marks: "))
science= float(input("Enter Science marks: "))
social= float(input("Enter Social marks: "))

total = kannada + english + hindi + maths + science + social
print(f"Total Marks: {int(total)}")

max_total = 125 + 100 + 100 + 100 + 100 + 100

percentage = (total / max_total) * 100
print(f"Percentage: {percentage:.2f}\n")

print("Grade")
if percentage > 85:
    print("Distiction")
elif percentage > 60:
    print("First Class")
elif percentage > 35:
    print("Second Class")
elif percentage == 35:
    print("Just Pass")
else:
    print("Fail")                