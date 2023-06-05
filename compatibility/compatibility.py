# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
combined_names = name1 + name2
true_count = sum(map(combined_names.lower().count, ["t", "r", "u", "e"]))
love_count = sum(map(combined_names.lower().count, ["l", "o", "v", "e"]))

combined_count_str = str(true_count) + str(love_count)
combined_count_num = int(combined_count_str)

if combined_count_num < 10 or combined_count_num > 90:
    print(f"Your score is {combined_count_num}, you go together like coke and mentos.")
elif 40 < combined_count_num < 50:
    print(f"Your score is {combined_count_num}, you are alright together.")
else:
    print(f"Your score is {combined_count_num}.")
