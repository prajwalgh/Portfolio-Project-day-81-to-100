import tkinter as tk
from main import *

window = tk.Tk()


def print_tk():
    for i in range(9):
        for j in range(9):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
            frame.grid(row=i, column=j)

            label = tk.Label(master=frame, text=f"{bord[i][j]} ")  # Row {i}\nColumn {j}

            label.config(bg="red")
            label.pack()


solve(bord)
print_tk()
window.mainloop()
