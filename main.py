import tkinter as tk

root = tk.Tk()

root.geometry("800x600")
root.title("My first GUI app")

label = tk.Label(root, text="Hello World!", font=('Arial', 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=('Times New Roman', 16))
textbox.pack()

myentry = tk.Entry(root)
myentry.pack()


root.mainloop()