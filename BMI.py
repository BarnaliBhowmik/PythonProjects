# Calculate the BMI
height = float(input("Enter your height(in cms): "))
weight = float(input("Enter your weight(in kgs): "))

bmi = weight/(height**2)

print(round(bmi))
# print(round(bmi, 2)) - It round's BMI to 2 decimal places


# BMI CALCULATOR WITH INTERPRETATIONS 👇🏻

weight1 = 85
height2 = 1.85

BMI = weight1 / (height2 ** 2)
if BMI < 18.85:
    print("underweight")
elif 18.5 <= BMI < 25:
    print("normal weight")
else:
    print("overweight")