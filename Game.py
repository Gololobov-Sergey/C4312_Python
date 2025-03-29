import tkinter as tk

time = 100
score = 0
press_enter = True

window = tk.Tk()
window.geometry("600x600+600+100")
window.title("C4312 - Clicker")
window.resizable(False, False)

label = tk.Label(window, text="Для початку гри натисніть [ENTER]", font=('Comic Sans MS', 12, 'bold'))
label.pack()

label_time = tk.Label(window, text=f"Залишок часу {time}", font=('Comic Sans MS', 16, 'bold'))
label_time.pack()

label_score = tk.Label(window, text=f"Набрані бали {score}", font=('Comic Sans MS', 16, 'bold'))
label_score.pack()



window.mainloop()