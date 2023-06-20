import tkinter

window = tkinter.Tk()

window.title("Experimental Window")
window.minsize(width=500, height=400)

# Label
window_label = tkinter.Label(text="This is a label", font=("", 24))
window_label.pack()
window_label["text"] = "New Label"
window_label.config(text="Updated Label")


def print_status():
    print("Clicked")
    window_label["text"] = "Button Got Clicked"


# Button
button = tkinter.Button(text="I am a Button", command=print_status)
button.pack()


def input_handler():
    value = user_input.get()
    print(value)
    window_label.config(text=value)


# Entry
user_input = tkinter.Entry()
user_input.insert(tkinter.END, string="Enter a text")
# Gets text in user_input
input_value = user_input.get()
print(input_value)
user_input.pack()
button2 = tkinter.Button(text="Submit Input", command=input_handler)
button2.pack()

# Text
text = tkinter.Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry.")
# Gets current value in textbox at line 1, character 0
print(text.get("1.0", tkinter.END))
text.pack()


def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


# Spinbox
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
# Called with current scale value.


def scale_used(value):
    print(value)


scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

# Checkbutton


def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()

# Radiobutton


def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()
