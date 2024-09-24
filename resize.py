import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

def resize_images(folder_path, sizes):
    # Create a 'resized' subfolder if it doesn't exist
    resized_folder = os.path.join(folder_path, 'resized')
    if not os.path.exists(resized_folder):
        os.makedirs(resized_folder)

    # Iterate over all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.png'):
            filepath = os.path.join(folder_path, filename)
            try:
                # Open the image file
                img = Image.open(filepath)
                for size in sizes:
                    # Resize the image
                    img_resized = img.resize((size, size), Image.LANCZOS)
                    # Construct the new filename
                    base, ext = os.path.splitext(filename)
                    new_filename = f"{base}_{size}x{size}{ext}"
                    new_filepath = os.path.join(resized_folder, new_filename)
                    # Save the resized image
                    img_resized.save(new_filepath)
                print(f"Processed {filename}")
            except Exception as e:
                print(f"Error processing {filename}: {e}")

def start_resizing():
    folder_path = folder_entry.get()
    sizes_str = sizes_entry.get()
    if not folder_path:
        messagebox.showwarning("No Folder Selected", "Please select a folder containing PNG images.")
        return
    if not sizes_str:
        messagebox.showwarning("No Sizes Entered", "Please enter at least one size.")
        return
    try:
        sizes = [int(size.strip()) for size in sizes_str.split(',') if size.strip().isdigit()]
        if not sizes:
            raise ValueError
    except ValueError:
        messagebox.showerror("Invalid Sizes", "Please enter sizes as comma-separated integers.")
        return
    # Run the resizing function in a separate thread to prevent GUI freezing
    threading.Thread(target=resize_and_notify, args=(folder_path, sizes)).start()

def resize_and_notify(folder_path, sizes):
    resize_images(folder_path, sizes)
    messagebox.showinfo("Resizing Complete", "Images have been resized successfully.")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_selected)

# Set up the main application window
root = tk.Tk()
root.title("Image Resizer")

# Folder selection
folder_label = tk.Label(root, text="Folder containing PNG images:")
folder_label.pack(pady=5)

folder_frame = tk.Frame(root)
folder_frame.pack(pady=5)

folder_entry = tk.Entry(folder_frame, width=50)
folder_entry.pack(side=tk.LEFT, padx=5)

browse_button = tk.Button(folder_frame, text="Browse...", command=browse_folder)
browse_button.pack(side=tk.LEFT)

# Sizes entry
sizes_label = tk.Label(root, text="Enter sizes (comma-separated):")
sizes_label.pack(pady=5)

sizes_entry = tk.Entry(root, width=50)
sizes_entry.insert(0, "72,36,18")
sizes_entry.pack(pady=5)

# Start button
start_button = tk.Button(root, text="Start Resizing", command=start_resizing)
start_button.pack(pady=20)

# Run the GUI event loop
root.mainloop()