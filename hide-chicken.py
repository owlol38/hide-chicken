import tkinter as tk
from tkinter import *
from tkinter import filedialog

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.gif;*.bmp")])
    if file_path:
        file_label.config(text=file_path)

    return file_path

def save_text():
    file_path = filedialog.asksaveasfilename()
    if file_path:
        with open(file_path, 'w') as file:
            file.write(text_input.get('1.0', tk.END))

app = tk.Tk()
app.title("hide chicken")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack()

browse_button = tk.Button(frame, text="Browse image", command=browse_file)
browse_button.pack()

file_label = tk.Label(frame, text="")
file_label.pack()

text_input = tk.Text(frame, wrap=tk.WORD, width=25, height=15)
text_input.pack()

save_button = tk.Button(frame, text="Save text", command=save_text)
save_button.pack()

app.mainloop()