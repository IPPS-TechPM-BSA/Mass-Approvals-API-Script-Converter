import json
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from datetime import datetime

def process_file(file_path):
    try:
        # Read space-separated numbers from file
        with open(file_path, 'r') as f:
            data = f.read()

        # Convert to list of integers
        ids = list(map(int, data.strip().split()))
        output = [{"id": i, "request_status": 1} for i in ids]

        # Generate output filename
        base_dir = os.path.dirname(file_path)
        base_name = os.path.splitext(os.path.basename(file_path))[0]
        date_str = datetime.now().strftime("%m-%d-%Y")
        output_filename = f"{base_name}_output_{date_str}.json"
        output_path = os.path.join(base_dir, output_filename)

        # Save as JSON
        with open(output_path, 'w') as out:
            json.dump(output, out, indent=4)

        messagebox.showinfo("Success", f"✅ JSON saved to:\n{output_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def select_file():
    file_path = filedialog.askopenfilename(
        title="Select .txt file",
        filetypes=[("Text files", "*.txt")]
    )
    if file_path:
        process_file(file_path)

# GUI setup
root = tk.Tk()
root.title("Drag & Drop Converter")
root.geometry("400x200")

select_button = tk.Button(root, text="Select File", command=select_file, width=20, height=2)
select_button.pack(expand=True)

root.mainloop()
