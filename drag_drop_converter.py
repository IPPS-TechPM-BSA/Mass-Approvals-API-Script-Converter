import json
import tkinter as tk
from tkinter import filedialog, messagebox

def process_file(file_path):
    try:
        # Read space-separated numbers from file
        with open(file_path, 'r') as f:
            data = f.read()

        # Convert to list of integers
        ids = list(map(int, data.strip().split()))
        output = [{"id": i, "request_status": 1} for i in ids]

        # Save as output.json in the same directory
        output_path = file_path.rsplit("/", 1)[0] + "/output.json"
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
root.title("Text to JSON Converter")
root.geometry("350x200")
root.resizable(False, False)

label = tk.Label(root, text="Drag or click to select a .txt file\nwith space-separated numbers",
                 pady=30, font=("Arial", 12))
label.pack()

button = tk.Button(root, text="Select File", command=select_file, font=("Arial", 11))
button.pack()

# Enable drag and drop if needed
def drop(event):
    file_path = event.data
    if file_path.startswith('{') and file_path.endswith('}'):
        file_path = file_path[1:-1]  # remove curly braces added on macOS
    process_file(file_path)

# macOS drag-and-drop support (requires `tkdnd` installed, or use click instead)
try:
    import tkinterdnd2 as tkdnd
    root = tkdnd.TkinterDnD.Tk()
    root.drop_target_register(tkdnd.DND_FILES)
    root.dnd_bind('<<Drop>>', drop)
except:
    pass  # fallback to button-only if tkdnd is not available

root.mainloop()