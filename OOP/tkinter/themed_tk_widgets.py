# from tkinter.ttk import *
from tkinter import ttk

style = ttk.Style()
style.configure("BW.TLabel", foreground="black", background="white")

ttk.Label(text="Test", style="BW.TLabel")
ttk.Label(text="Miles to Kilometers Converter", style="BW.TLabel")

window = ttk.Frame(width=600, height=400)
# window.title("Miles to Kilometers Converter", style="BW.TLabel")

window.mainloop()
