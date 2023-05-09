# import tkinter as tk
# import  ticktak
# def start():
#     ticktak.tictactoe()
#
# def about():
#     label.config(text="This is a sample application created with tkinter.")
#
# # Create the main window
# root = tk.Tk()
# root.title("My Application")
#
# # Create the label
# label = tk.Label(root, text="")
# label.pack()
#
# # Create the menu bar
# menu_bar = tk.Menu(root)
#
# # Create the "File" menu
# file_menu = tk.Menu(menu_bar, tearoff=0)
# file_menu.add_command(label="Start", command=start)
# file_menu.add_command(label="About", command=about)
# menu_bar.add_cascade(label="File", menu=file_menu)
#
# # Add the menu bar to the main window
# root.config(menu=menu_bar)
#
# # Run the main loop
# root.mainloop()
import tkinter as tk

# Create a dictionary to map key presses to button widgets
#button_map = {'a': button_a, 'b': button_b, 'c': button_c, 'd': button_d, 'e': button_e, 'f': button_f, 'g': button_g, 'h': button_h, 'i': button_i, 'j': button_j}

# Define a function to change the color of the button corresponding to the pressed key to red and then back to white after a short delay
def on_key_press(event):
    key = event.char.lower()
    if key in button_map:
        button = button_map[key]
        button.config(bg='red')
        button.after(500, lambda: button.config(bg='white'))

# Create the main window and buttons
root = tk.Tk()

button_a = tk.Button(root, text='A')
button_a.pack(side='left', padx=5)

button_b = tk.Button(root, text='B')
button_b.pack(side='left', padx=5)

button_c = tk.Button(root, text='C')
button_c.pack(side='left', padx=5)

button_d = tk.Button(root, text='D')
button_d.pack(side='left', padx=5)

button_e = tk.Button(root, text='E')
button_e.pack(side='left', padx=5)

button_f = tk.Button(root, text='F')
button_f.pack(side='left', padx=5)

button_g = tk.Button(root, text='G')
button_g.pack(side='left', padx=5)

button_h = tk.Button(root, text='H')
button_h.pack(side='left', padx=5)

button_i = tk.Button(root, text='I')
button_i.pack(side='left', padx=5)

button_j = tk.Button(root, text='J')
button_j.pack(side='left', padx=5)
button_map = {'a': button_a, 'b': button_b, 'c': button_c, 'd': button_d, 'e': button_e, 'f': button_f, 'g': button_g, 'h': button_h, 'i': button_i, 'j': button_j}

# Bind the key press event to the main window
root.bind('<KeyPress>', on_key_press)

# Start the main event loop
root.mainloop()
