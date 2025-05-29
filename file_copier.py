import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
from pathlib import Path

class FileCopierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Copier")
        self.root.geometry("600x400")
        
        # Variables
        self.destination_path = tk.StringVar()
        self.selected_files = []
        self.root_folder_path = tk.StringVar()
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        main_frame.columnconfigure(0, weight=0)
        main_frame.columnconfigure(1, weight=1)  # Entry expands
        main_frame.columnconfigure(2, weight=0)
        main_frame.columnconfigure(3, weight=0)
        main_frame.columnconfigure(4, weight=1)
        main_frame.columnconfigure(5, weight=0)

        # Make main frame and listbox row expand
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)  # Let the listbox row expand vertically
        
        # Destination folder selection (row 0)
        ttk.Label(main_frame, text="Destination Folder:").grid(row=0, column=0, sticky=tk.W)
        self.dest_entry = ttk.Entry(main_frame, textvariable=self.destination_path, state='readonly')
        self.dest_entry.grid(row=0, column=1, padx=0, sticky="ew")
        ttk.Button(main_frame, text="Browse", command=self.select_destination).grid(row=0, column=2, padx=(3, 0))

        # Root folder selection (row 1)
        ttk.Label(main_frame, text="Root Folder:").grid(row=1, column=0, sticky=tk.W)
        self.root_entry = ttk.Entry(main_frame, textvariable=self.root_folder_path, state='readonly')
        self.root_entry.grid(row=1, column=1, padx=(3, 0), sticky="ew")
        ttk.Button(main_frame, text="Set Root", command=self.select_root_folder).grid(row=1, column=2, padx=(3, 0))

        # File selection (row 2+)
        ttk.Label(main_frame, text="Select Files:").grid(row=2, column=0, sticky=tk.W)
        self.file_listbox = tk.Listbox(main_frame, selectmode=tk.MULTIPLE, width=70, height=10)
        self.file_listbox.grid(row=3, column=0, columnspan=3, pady=10, sticky="ew")

        ttk.Button(main_frame, text="Add Files", command=self.add_files).grid(row=4, column=0)
        ttk.Button(main_frame, text="Remove Selected", command=self.remove_selected).grid(row=4, column=1)

        # Copy button
        ttk.Button(main_frame, text="Copy Files", command=self.copy_files).grid(row=5, column=0, columnspan=3, pady=20)
        
    def select_destination(self):
        """Open directory selection dialog for destination folder"""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.destination_path.set(folder_selected)

    def select_root_folder(self):
        """Open directory selection dialog for root folder"""
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.root_folder_path.set(folder_selected)
    
    def add_files(self):
        """Open file selection dialog"""
        files = filedialog.askopenfilenames()
        if files:
            for file in files:
                if file not in self.selected_files:
                    self.selected_files.append(file)
                    self.file_listbox.insert(tk.END, os.path.basename(file))
    
    def remove_selected(self):
        """Remove selected files from listbox"""
        selected_indices = self.file_listbox.curselection()
        if selected_indices:
            selected_indices = sorted(selected_indices, reverse=True)
            for index in selected_indices:
                self.selected_files.pop(index)
                self.file_listbox.delete(index)
    
    def copy_files(self):
        """Copy selected files to destination, preserving structure relative to the root folder"""
        dest_path = self.destination_path.get()
        root_folder = self.root_folder_path.get()
        if not dest_path:
            messagebox.showerror("Error", "Please select a destination folder")
            return
        if not root_folder:
            messagebox.showerror("Error", "Please select a root folder")
            return
        if not self.selected_files:
            messagebox.showerror("Error", "Please select files to copy")
            return
        try:
            for file_path in self.selected_files:
                relative_path = os.path.relpath(file_path, root_folder)
                dest_file_path = os.path.join(dest_path, relative_path)
                os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                shutil.copy2(file_path, dest_file_path)
            messagebox.showinfo("Success", "Files copied successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileCopierApp(root)
    root.mainloop()
