import tkinter as tk

def click():
    label.config(text="Hello " + text.get())

window = tk.Tk()
window.geometry("600x400+600+200")
window.title("C4312 - Clicker")
window.minsize(400, 400)
window.resizable(False, False)

label = tk.Label(text="Hello Python!", font=('Comic Sans MS', 20, 'bold'), fg='DarkBlue', width=16, bg='yellow', height=2)
label.pack()

button = tk.Button(text="Click", font=('Comic Sans MS', 20, 'bold'), command=click)
button.pack()

text = tk.Entry()
text.pack()

window.mainloop()