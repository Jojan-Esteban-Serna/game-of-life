from tkinter import filedialog, simpledialog


def read_file():
    file_path = filedialog.askopenfilename(filetypes=[("RLE jeserna", "*.rlej"), ("All files", "*.*")])
    content = ''
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
    return content


def write_file(text_to_save):
    file_path = filedialog.asksaveasfilename(defaultextension=".rlej",
                                             filetypes=[("RLE jeserna", "*.rlej"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_to_save)

def read_input(message):
    text_to_save = simpledialog.askstring("Ingresa", f"{message}:\t\t\t\t\t\t\t\t")
    return text_to_save
