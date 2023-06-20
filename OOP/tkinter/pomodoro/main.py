import tkinter as tk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✅"

keep_timer_going = True


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown_with_timeout(sec, is_working_hour):
    if keep_timer_going:
        if sec == 0 and is_working_hour:
            completed_cycles["text"] += CHECKMARK
            completed_rounds = len(completed_cycles["text"])
            if completed_rounds % 4 == 0:
                print('4 x 25 minutes work done. Enjoy your 20 minutes break!')
                long_break()
            else:
                print('25 minutes Completed. Enjoy your 5 minutes break!')
                short_break()
        elif sec == 0 and not is_working_hour:
            countdown()
        minutes, seconds = divmod(sec, 60)
        timer = '{:02d}:{:02d}'.format(minutes, seconds)
        print(f"00:{timer}")
        canvas.itemconfig(canvas_text, text=f"00:{timer}")
        if sec > 0:
            root.after(1000, countdown_with_timeout, sec - 1, is_working_hour)


def short_break():
    seconds = SHORT_BREAK_MIN * 60
    countdown_with_timeout(seconds, False)


def long_break():
    seconds = LONG_BREAK_MIN * 60
    countdown_with_timeout(seconds, False)


def countdown():
    time_in_seconds = WORK_MIN * 60
    countdown_with_timeout(time_in_seconds, True)


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global keep_timer_going
    keep_timer_going = False
    canvas.itemconfig(canvas_text, text="00:00:00")
    completed_cycles["text"] = ""


# ---------------------------- UI SETUP ------------------------------- #
root = tk.Tk()
root.title("Pomodoro Technique")
root.config(padx=100, pady=40, bg=YELLOW)
label = tk.Label(text="Timer", font=(FONT_NAME, 32, "bold"), fg=GREEN)
label.pack()
tomato_img = tk.PhotoImage(file="tomato.png")
canvas = tk.Canvas(root, width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_img)
canvas_text = canvas.create_text(102, 132, text="00:00:00", font=(FONT_NAME, 24, "bold"), fill="white")
canvas.pack()

# Buttons
start_countdown = tk.Button(root, text="Start", font=(FONT_NAME, 16, "bold"), bg="red", fg="white", command=countdown)
start_countdown.pack(padx=20, ipadx=10, pady=10, side=tk.LEFT, fill="x")
reset_timer = tk.Button(text="Reset", font=(FONT_NAME, 16, "bold"), command=reset_timer)
reset_timer.pack(padx=20, ipadx=10, pady=20, side=tk.RIGHT, fill="x")

# Label
cycles = tk.Label(text="Completed Cycles:", font=(FONT_NAME, 16, "bold"), fg=GREEN)
cycles.pack(padx=5, pady=20, side=tk.LEFT)
completed_cycles = tk.Label(text="", font=(FONT_NAME, 12, "bold"), bg=YELLOW, fg="green")
completed_cycles.pack(padx=2, pady=60, side=tk.LEFT)

root.mainloop()