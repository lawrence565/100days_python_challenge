import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = tkinter.Label(text="The first label.",font=("Arial", 24, "bold"))
my_label.grid(column=0, row=0) # pack() accept arg to specify the place label shows, like pack(side="left")

my_label["text"] = "Let's try a new word." # Change single attribute
my_label.config(text="New York") # Change multiple attribute

# Button
def button_clicked():
    print("I got clicked.")
    new_text = input_text.get()
    my_label.config(text=new_text)

button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

new_button = tkinter.Button(text="new button")
new_button.grid(column=2, row=0)

# Entry
input_text = tkinter.Entry(width=10)
input_text.grid(column=3, row=2)

window.mainloop()