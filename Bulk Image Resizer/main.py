import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    folder = filedialog.askdirectory()
    
    if not folder:
        return
    
    try:
        for file in os.listdir(folder):
            path = os.path.join(folder, file)

            if os.path.isfile(path):
                ext = file.split('.')[-1]

                if ext in ['jpg', 'png']:
                    new_folder = os.path.join(folder, 'Images')
                elif ext in ['mp4', 'mkv']:
                    new_folder = os.path.join(folder, 'Videos')
                elif ext in ['pdf', 'docx']:
                    new_folder = os.path.join(folder, 'Documents')
                else:
                    new_folder = os.path.join(folder, 'Others')

                os.makedirs(new_folder, exist_ok=True)
                shutil.move(path, os.path.join(new_folder, file))

        messagebox.showinfo("Success", "Files organized successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x150")

btn = tk.Button(root, text="Select Folder & Organize", command=organize_files)
btn.pack(pady=40)

root.mainloop()