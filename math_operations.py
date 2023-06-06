# priorities:- high to low (), * and /, + and -
# print(3 * (3 + 3 / 3 - 3))
# Calculating BMI / Body-Mass_index
# Formula: BMI = Weight / Height ** 2
print("Welcome to the BMI calculator!")
weight = input("What is your weight in kg?\n")
height = input("What is your height in meters?\n")
bmi = float(weight) / float(height) ** 2
print("Your BMI is " + str(int(bmi)))
