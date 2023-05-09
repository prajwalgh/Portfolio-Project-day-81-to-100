# Create the main window
def tictactoe():
    root = tk.Tk()
    root.geometry("180x90")

    # Create a label widget and add it to the window
    label = tk.Label(root)
    label.pack()

    #entry field for tic tac toe   3 coloum
    #first coloum

    entry = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry)
    entry.place(x=1,y=1)
    entry.bind("<KeyRelease>", say_hello)

    entry2 = tk.StringVar()
    entry2 = tk.Entry(root, textvariable=entry2)
    entry2.place(x=1,y=30)
    entry2.bind("<KeyRelease>", say_hello)

    entry3 = tk.StringVar()
    entry3 = tk.Entry(root, textvariable=entry3)
    entry3.place(x=1,y=60)
    entry3.bind("<KeyRelease>", say_hello)

    #secodn coloume


    entry4 = tk.StringVar()
    entry4 = tk.Entry(root, textvariable=entry4)
    entry4.place(x=60,y=1)
    entry4.bind("<KeyRelease>", say_hello)

    entry5 = tk.StringVar()
    entry5 = tk.Entry(root, textvariable=entry5)
    entry5.place(x=60,y=30)
    entry5.bind("<KeyRelease>", say_hello)

    entry6 = tk.StringVar()
    entry6 = tk.Entry(root, textvariable=entry6)
    entry6.place(x=60,y=60)
    entry6.bind("<KeyRelease>", say_hello)

    #third colum

    entry7 = tk.StringVar()
    entry7 = tk.Entry(root, textvariable=entry7)
    entry7.place(x=120,y=1)
    entry7.bind("<KeyRelease>", say_hello)


    entry8 = tk.StringVar()
    entry8 = tk.Entry(root, textvariable=entry8)
    entry8.place(x=120,y=30)
    entry8.bind("<KeyRelease>", say_hello)


    entry9 = tk.StringVar()
    entry9 = tk.Entry(root, textvariable=entry9)
    entry9.place(x=120,y=60)
    entry9.bind("<KeyRelease>", say_hello)


    # Start the main event loop to display the window
    root.mainloop()


from tkinter import messagebox


matrix=[[" "]*3 for _ in range(3)]
print(matrix)

#following code creata list of entry keys and index of matrix and map them in dictionary
entrylist=['.!entry']
for i in range(2,10):
    entrylist.append(f'.!entry{i}')
indexlist=[]
for i in range(3):
    for j in range(3):
        indexlist.append([j,i])
dict={}
for i in range(9):
    dict[entrylist[i]]=indexlist[i]
print(dict)
print(entrylist)
print(indexlist)
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Import the tkinter library
import tkinter as tk



# Define a function to be called when the button is clicked this will update matrix
def say_hello(a):
    entry_name = a.widget
    value = entry_name.get()
    y=str(entry_name)
    x1=dict[y][0]
    x2 = dict[y][1]
    matrix[x1][x2]=value
    print(entry_name,value)
    check(x1,x2)
root = tk.Tk()
# Create the main window
def tictactoe():
    root.geometry("180x90")

    # Create a label widget and add it to the window
    label = tk.Label(root)
    label.pack()

    #entry field for tic tac toe   3 coloum
    #first coloum

    entry = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry)
    entry.place(x=1,y=1)
    entry.bind("<KeyRelease>", say_hello)

    entry2 = tk.StringVar()
    entry2 = tk.Entry(root, textvariable=entry2)
    entry2.place(x=1,y=30)
    entry2.bind("<KeyRelease>", say_hello)

    entry3 = tk.StringVar()
    entry3 = tk.Entry(root, textvariable=entry3)
    entry3.place(x=1,y=60)
    entry3.bind("<KeyRelease>", say_hello)

    #secodn coloume


    entry4 = tk.StringVar()
    entry4 = tk.Entry(root, textvariable=entry4)
    entry4.place(x=60,y=1)
    entry4.bind("<KeyRelease>", say_hello)

    entry5 = tk.StringVar()
    entry5 = tk.Entry(root, textvariable=entry5)
    entry5.place(x=60,y=30)
    entry5.bind("<KeyRelease>", say_hello)

    entry6 = tk.StringVar()
    entry6 = tk.Entry(root, textvariable=entry6)
    entry6.place(x=60,y=60)
    entry6.bind("<KeyRelease>", say_hello)

    #third colum

    entry7 = tk.StringVar()
    entry7 = tk.Entry(root, textvariable=entry7)
    entry7.place(x=120,y=1)
    entry7.bind("<KeyRelease>", say_hello)


    entry8 = tk.StringVar()
    entry8 = tk.Entry(root, textvariable=entry8)
    entry8.place(x=120,y=30)
    entry8.bind("<KeyRelease>", say_hello)


    entry9 = tk.StringVar()
    entry9 = tk.Entry(root, textvariable=entry9)
    entry9.place(x=120,y=60)
    entry9.bind("<KeyRelease>", say_hello)


    # Start the main event loop to display the window
    root.mainloop()



# this function will check if ther is any winner
def check(i,j):
    print(matrix,i,j)
    current_input=matrix[i][j]
    counti=0
    for k in range(3):
        if matrix[k][j]==current_input:
            counti+=1
    countj = 0
    for k in range(3):
        if matrix[i][k] == current_input:
            countj += 1
    if counti==3 or countj==3:
        print("worked")
        messagebox.showinfo("winner is ", f"{current_input}")
        root.destroy()
    notdignol=[[0,1],[1,1],[1,3],[3,1]]
    if [i,j]  in notdignol:
        print("dont check digonal")
        return
    d1=[matrix[0][0],matrix[1][1],matrix[2][2]]
    d2=[matrix[0][2],matrix[1][1],matrix[2][0]]
    if d1[0]==d1[1] and d1[1]==d1[2] and d1[0]!=' ':
        print("worked")
        messagebox.showinfo("winner is ", f"{current_input}")
        root.destroy()
    if d2[0] == d2[1] and d2[1] == d2[2] and d2[0]!=' ':
        print("worked")
        messagebox.showinfo("winner is ", f"{current_input}")
        root.destroy()
    return 0