# 🚨 Don't change the code below 👇
student_heights = input(
    "Input a list of student heights separated by a comma and a space \n"
).split(", ")
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_heights = 0
number_of_students = 0
for height in student_heights:
    total_heights += height
    number_of_students += 1

average_height = total_heights / number_of_students
print(round(average_height))
