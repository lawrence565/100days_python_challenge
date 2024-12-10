import tkinter

window = tkinter.Tk()
window.title("Mile to KM Converter")
window.minsize(width=200, height=150)
window.config(padx=20, pady=20)

# Label
equal = tkinter.Label(text="is equal to",font=("Arial", 18, "normal"))
equal.grid(column=0, row=1)

miles = tkinter.Label(text="Miles",font=("Arial", 18, "normal"))
miles.grid(column=2, row=0)

km = tkinter.Label(text="Km",font=("Arial", 18, "normal"))
km.grid(column=2, row=1)

km_value = tkinter.Label(text="0" ,font=("Arial", 18, "normal"))
km_value.grid(column=1, row=1)

# Button
def button_clicked():
    value = miles_input.get()
    km_value.config(text=str(int(value) * 1.609))

calculate = tkinter.Button(text="calculate", command=button_clicked)
calculate.grid(column=1, row=2)

# Entry
miles_input = tkinter.Entry(width=10)
miles_input.grid(column=1, row=0)

window.mainloop()