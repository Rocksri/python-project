import tkinter as tk

root = tk.Tk()
root.title("Option button")

var = tk.StringVar(value="Option 1")


def change_option(*args):
    print(var.get())


option1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=change_option)
option2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=change_option)
option3 = tk.Radiobutton(root, text="Option 3", variable=var, value="Option 3", command=change_option)

option1.pack()
option2.pack()
option3.pack()

root.mainloop()
