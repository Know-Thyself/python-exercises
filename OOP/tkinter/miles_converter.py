from tkinter import *

# Window
window = Tk()
window.geometry("600x400")
window.title("Miles to Kilometers Converter")
# Label
label = Label(text="Miles to Kilometers Converter", font=("", 16))
label.pack(pady=10)


def convert(val):
    print(val.startswith("Enter number of miles: "))
    miles = entry.get()
    print(miles.startswith("Enter number of miles: "))
    num = miles.replace("Enter number of miles: ", "")
    print(int(num))
    # miles = int(user_input.get().split(' ')[1])
    # km = round(miles * 1.609344, 2)
    # label["text"] = f"{miles} miles is {km} km"
    # mi = spinbox.get()
    # km = round(int(mi) * 1.609344, 2)
    # label["text"] = f"{mi} miles is {km} km"


# Entry

# valid = window.register(convert)
# user_input = Entry(window, validate="key", validatecommand=(valid, "%P"))
# # user_input.insert(END, string="Enter miles: ")
# # Gets text in user_input
# user_input.insert(END, string="Enter miles:>>> ")

window.geometry("500x500")
entry = Entry()
entry.pack(side="top", fill="x")
entry.insert(END, "Enter number of miles: ")

validate_cmd = (window.register(convert), '%v')
entry.config(validate='key', validatecommand=validate_cmd)

entry.pack()

# Button
button = Button(text="Calculate", command=convert)
button.pack(pady=10)

window.mainloop()
