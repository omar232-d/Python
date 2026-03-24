import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime


def sort_files(mode):
    folder = filedialog.askdirectory(title="Select Folder")

    if not folder:
        return

    try:
        for file in os.listdir(folder):
            path = os.path.join(folder, file)

            if os.path.isfile(path):
                time = os.path.getmtime(path)
                date = datetime.fromtimestamp(time)

                if mode == "year":
                    folder_name = str(date.year)

                elif mode == "month":
                    folder_name = f"{date.year}-{date.month:02d}"

                new_folder = os.path.join(folder, folder_name)
                os.makedirs(new_folder, exist_ok=True)

                shutil.move(path, os.path.join(new_folder, file))

        messagebox.showinfo("Success", "Files sorted successfully!")

    except Exception as e:
        messagebox.showerror("Error", str(e))


# GUI
root = tk.Tk()
root.title("Auto File Sorter")
root.geometry("300x200")

label = tk.Label(root, text="Choose Sorting Method", font=("Arial", 12))
label.pack(pady=10)

btn1 = tk.Button(root, text="Sort by Year", width=20, command=lambda: sort_files("year"))
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Sort by Month", width=20, command=lambda: sort_files("month"))
btn2.pack(pady=5)

root.mainloop()