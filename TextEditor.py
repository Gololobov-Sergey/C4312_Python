import tkinter as tk
from tkinter import filedialog

def save_file():
    file_name = filedialog.asksaveasfilename(title="C4312 Save File", defaultextension='txt',
                                           filetypes=(('Text file', '*.txt'),("All Files", '*.*')))
    if file_name:
        f = open(file_name, 'w', encoding='utf-8')
        f.write(text.get(1.0, 'end'))
        f.close()


def open_file(event=None):
    file_name = filedialog.askopenfilename(title="C4312 Open File", defaultextension='txt',
                                           filetypes=(('Text file', '*.txt'),("All Files", '*.*')))
    if file_name:
        f = open(file_name, 'r', encoding='utf-8')
        txt_read = f.read()
        if txt_read != None:
            text.delete(1.0, 'end')
            text.insert('end', txt_read)
        f.close()


window = tk.Tk()
window.geometry("600x400+400+200")
window.minsize(200,200)
window.title("C4312 - TextEditor")

menu = tk.Menu(window)
window.config(menu=menu)

img1 = tk.PhotoImage(file='pics/folder-open-outline-custom.png')
img2 = tk.PhotoImage(file='pics/content-save-outline-custom.png')

file_menu = tk.Menu(menu, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_command(label="Open...", image=img1, compound='left', accelerator='Ctrl+O', command=open_file)
file_menu.add_command(label="Save As", image=img2, compound='left', command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit")
menu.add_cascade(label="File", menu=file_menu)


about_menu = tk.Menu(menu, tearoff=0)
about_menu.add_command(label="Help")
about_menu.add_command(label="About")
menu.add_cascade(label="About", menu=about_menu)

text = tk.Text(window)
text.pack(fill='both', expand=1)

window.bind("<Control-o>", open_file)

window.mainloop()