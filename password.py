import tkinter as tk
from tkinter import messagebox
from getpass import getpass
import shutil
import cv2
import os

class CyberNumberPasswordLock:
    def __init__(self, master, password):
        self.master = master
        self.master.title("PASSWORD PLEASE")
        self.master.geometry("600x800")
        self.master.configure(bg='#121212')

        self.password = password
        self.current_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.create_entry_display()
        self.create_numeric_keypad()

    def create_entry_display(self):
        entry_display = tk.Entry(self.master, textvariable=self.current_input, font=('Courier', 24),
                                 justify='center', state='normal', bg='#2b2b2b', fg='#ffffff')
        entry_display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, ipady=20, sticky='nsew')

    def create_numeric_keypad(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', 'Enter', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            tk.Button(self.master, text=button, width=6, height=3, command=lambda b=button: self.button_click(b),
                      font=('Courier', 14, 'bold'), bg='#2b2b2b', fg='#00ff00', bd=2, relief='ridge').grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid weights for responsiveness
        for i in range(5):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i, weight=1)

    def button_click(self, button):
        if button == 'C':
            self.current_input.set('')
        elif button == 'Enter':
            self.check_password()
        else:
            current_value = self.current_input.get()
            self.current_input.set(current_value + button)

    def check_password(self):
        entered_password = self.current_input.get()
        try:
            if entered_password == self.password:
                messagebox.showinfo("Success", "Access Granted! Welcome to the Cyber World.")
                self.current_input.set('')
                self.open_locked_directory()
            else:
                self.capture_image()
                messagebox.showerror("Error", "Access Denied. Intruder Alert!")
                self.current_input.set('')

        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric digits.")
            self.current_input.set('')

    def open_locked_directory(self):
        locked_dir_path = "LOCKED DIR"
        os.makedirs(locked_dir_path, exist_ok=True)
        os.startfile(locked_dir_path)  # Open the directory
        messagebox.showinfo("Locked Directory", f"Locked directory opened at {locked_dir_path}")

    def capture_image(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        cv2.imwrite("intruder.jpg", frame)
        messagebox.showinfo("Intruder Alert", "Intruder image captured and saved as intruder.jpg")

if __name__ == "__main__":
    password = '1234'

    root = tk.Tk()
    root.configure(bg='#121212')
    app = CyberNumberPasswordLock(root, password)
    root.mainloop()



