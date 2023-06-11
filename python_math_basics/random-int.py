import random

# random_integer = random.randint(0, 1)
# print(random_integer)
# random_float = random.random() * 5
# print(random_float)
# Import the random module here

# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
number_of_people = len(names)
randomly_picked_to_pay = random.randint(0, number_of_people - 1)
print(f"{names[randomly_picked_to_pay]} is going to buy the meal today!")
