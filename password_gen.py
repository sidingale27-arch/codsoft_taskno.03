
from customtkinter import *
import string
import random

def password_gen():
    s = []
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    if not (upper.get() or lower.get() or digits.get() or punctuation.get()):
        screen.delete(0, END)
        screen.insert(0, "Select at least one option")
        return

    if lower.get():
        s.extend(s1)
    if upper.get():
        s.extend(s2)
    if digits.get():
        s.extend(s3)
    if punctuation.get():
        s.extend(s4)
    passlen = length.get()
    random.shuffle(s)
    password = "".join(random.choices(s, k=passlen))
    screen.delete(0, END)
    screen.insert(0, password)


def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(screen.get())
    window.update()


def slider_event(value):
    value_label.configure(text=f"{int(value)}")


def change_theme():
    if switch.get() == 1:
        set_appearance_mode("dark")
        switch.configure(text="Light Mode")
        
    else:
        set_appearance_mode("light")
        switch.configure(text="Dark Mode")


def center_window(win, width=300, height=200):
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    win.geometry(f'{width}x{height}+{x}+{y}')


window = CTk()
set_appearance_mode("light")
center_window(window, 400, 600)
window.title("Password Generator")
window.geometry("400x500")
window.resizable(0, 0)

# Frames
frame1 = CTkFrame(master=window, fg_color="transparent", corner_radius=0)
frame = CTkFrame(master=frame1, fg_color="grey", corner_radius=10)
frame12 = CTkFrame(master=frame1)
frame2 = CTkFrame(master=window, fg_color="transparent", corner_radius=0)
frame3 = CTkFrame(master=window, fg_color="transparent", corner_radius=0)

# Dark Mode Switch
switch = CTkSwitch(master=frame, text=("Dark Mode"), command=change_theme,
                   text_color=("white"), fg_color="white", font=("arial", 12, "bold"))

# Label
label = CTkLabel(master=frame1, text="ENTER PASSWORD LENGTH",
                 fg_color="transparent", text_color=("black", "white"),
                 font=('arial', 20, 'bold'))

# Slider
length = IntVar(value=8)
slider = CTkSlider(master=frame12, from_=8, to=32, number_of_steps=24, variable=length,
                   command=slider_event, progress_color=("blue", "white"), button_color="blue")
value_label = CTkLabel(frame12, text="Select Length", text_color=("black", "white"), font=('collosalis', 15, "bold"))

# Checkboxes
upper = BooleanVar()
lower = BooleanVar()
digits = BooleanVar()
punctuation = BooleanVar()
variables = [upper, lower, digits, punctuation]
labels = ["UpperCase", "LowerCase", "Digits", "Punctuation"]
checkbox_widgets = []

for i in range(len(labels)):
    checkbox = CTkCheckBox(master=frame2, text=labels[i], text_color=("black", "white"),
                           font=("Helvetica", 15, "bold"), variable=variables[i])
    checkbox_widgets.append(checkbox)

# Grid placement of checkboxes
count = 0
for i in range(1, 3):
    for j in range(1, 3):
        checkbox_widgets[count].grid(row=i, column=j, sticky="SNEW")
        count += 1


btn_gen = CTkButton(master=frame3, text=" Generate ",
                    text_color=("white"), fg_color="#3d59f5", command=password_gen,
                    border_color=("black", "white"), height=30, border_width=2,
                    corner_radius=10, hover_color="#8b9bf7", font=("collosalis", 18))


screen = CTkEntry(master=frame3, corner_radius=15, text_color=("black", "white"),
                  border_color=("black", "white"), height=40, width=300)


copy_btn = CTkButton(master=frame3, text="Copy", fg_color="#115ffa", hover_color="#6d9bf7",
                     text_color=("white"), font=("Courier New", 15, "italic"),
                     command=copy_to_clipboard)


window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)

frame1.grid(row=0, column=0, sticky="SNEW")
frame2.grid(row=1, column=0, sticky="SNEW")
frame3.grid(row=2, column=0, sticky="SNEW")

frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)
frame1.rowconfigure(1, weight=1)
frame1.rowconfigure(2, weight=1)

frame2.columnconfigure(0, weight=1, uniform='c')
frame2.columnconfigure(1, weight=1, uniform='a')
frame2.columnconfigure(2, weight=1, uniform='a')
frame2.rowconfigure(0, weight=1, uniform='c')
frame2.rowconfigure(1, weight=1, uniform='b')
frame2.rowconfigure(2, weight=1, uniform='b')

frame3.columnconfigure(0, weight=1)
frame3.rowconfigure(0, weight=1)
frame3.rowconfigure(1, weight=1)
frame3.rowconfigure(2, weight=1)

frame12.columnconfigure(0, weight=1)
frame12.rowconfigure(0, weight=1)
frame12.rowconfigure(1, weight=1)


frame.grid(row=0, column=0, sticky="E", padx=5)
frame.columnconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
switch.grid(row=30, column=0, padx=5, pady=5)
label.grid(row=1, column=0)
frame12.grid(row=2, column=0)
slider.grid(row=1, column=0)
value_label.grid(row=0, column=0)


btn_gen.grid(row=0, column=0)
screen.grid(row=1, column=0)
copy_btn.grid(row=2, column=0)

window.mainloop()