import tkinter as tk
from tkinter import messagebox

# Create a tkinter window
window = tk.Tk()

# Hide the main window
window.withdraw()

# Create a warning message box
messagebox.showwarning("Warning", "This is a warning message!")

# Start the tkinter event loop
window.mainloop()