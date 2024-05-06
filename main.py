from tkinter import *

window = Tk()
window.title("Mile to Kilometers")
window.minsize(width=600, height=400)

screen_has_value = False
answer_label = None


def on_button_click():
    global screen_has_value, answer_label
    value = int(input_field.get())
    if value and screen_has_value is False:
        new_value = value * 1.609344
        answer_label = Label(text=f"{new_value} km", font=("Ariel", 20, "bold"))
        answer_label.pack()
        screen_has_value = True


def clear_screen():
    global screen_has_value, answer_label
    if screen_has_value is True:
        screen_has_value = False
        input_field.delete(0, END)
        if answer_label is not None:
            answer_label.destroy()


label = Label(text="Enter miles:", font=("Ariel", 20, "bold"))
label.pack()

input_field = Entry(width=50)
input_field.pack()

button_frame = Frame(window)
button_frame.pack()

submit_btn = Button(button_frame, text="Convert", command=on_button_click)
submit_btn.pack(side="left")

clear_btn = Button(button_frame, text="Clear", command=clear_screen)
clear_btn.pack(side="left")


window.mainloop()

