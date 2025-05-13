import tkinter as tk

def say_hello():
    name = entry.get()
    label_result.config(text=f"Hello, {name}!")

# Create main window
window = tk.Tk()
window.title("Simple GUI Example")
window.geometry("300x150")

# Create a label
label = tk.Label(window, text="Enter your name:")
label.pack(pady=5)

# Create an entry (text input)
entry = tk.Entry(window)
entry.pack(pady=5)

# Create a button
button = tk.Button(window, text="Greet", command=say_hello)
button.pack(pady=5)

# Create a label to show the result
label_result = tk.Label(window, text="")
label_result.pack(pady=5)

# Start the GUI loop
window.mainloop()
