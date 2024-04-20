from tkinter import filedialog


def read_file():
    file_path = filedialog.askopenfilename(filetypes=[("RLE jeserna", "*.rlej"), ("All files", "*.*")])
    content = ''
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            print("File content:")
    return content


def write_file(text_to_save):
    file_path = filedialog.asksaveasfilename(defaultextension=".rlej",
                                             filetypes=[("RLE jeserna", "*.rlej"), ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text_to_save)
