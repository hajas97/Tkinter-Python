import tkinter as tk
from tkinter import messagebox


class MyGUI:
    def __init__(self):
        
        self.root = tk.Tk()
        
        self.label = tk.Label(self.root, text="Your message", font=("Arial", 18))
        self.label.pack(padx=10, pady=10)
        
        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(padx=10, pady=10)
        
        self.check_state = tk.IntVar()
        
        self.check = tk.Checkbutton(self.root, text="Show messagebox", font=('Arial', 16), variable = self.check_state)
        self.check.pack(padx=10, pady=10)
        
        self.button = tk.Button(self.root, text="Show Message", font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)
        
        
        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title="Message", message=self.textbox.get('1.0', tk.END))
            
    def shortcut(self, event):
        # bitmask az enternek 8 
        if event.state == 8 and event.keysym == "Return":
            self.show_message()
        
MyGUI()
        
        