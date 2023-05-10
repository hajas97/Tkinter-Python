import tkinter as tk

root = tk.Tk()

root.geometry("800x600")
root.title("My first GUI app")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack()

root.mainloop()