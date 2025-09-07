# Calculate the BMI
height = float(input("Enter your height(in cms): "))
weight = float(input("Enter your weight(in kgs): "))

bmi = weight/(height**2)

print(round(bmi))
# print(round(bmi, 2)) - It round's BMI to 2 decimal places