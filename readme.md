# File Copier Utility

This code was created out of a real-world need for controlled file management. The owner of this application does not want offshore developers to push directly to the git repository. Instead of manually copying files one by one—navigating through multiple directories and using copy-paste, I wanted a simple UI where I could:

- Set the destination folder
- Set the root folder of the source files
- Select files to copy, and have the tool automatically preserve the folder structure

Although I don't know Python that well, this tool allowed me to quickly create the UI elements I needed for this workflow.

## Features

- Select a destination folder for copied files
- Select a root folder to preserve the source folder structure
- Add multiple files to be copied in one go
- Simple, responsive UI (built with tkinter)
- No need to manually copy files or use the command line

## Usage

1. Set the **Destination Folder** (where files will be copied to).
2. Set the **Root Folder** (the base directory whose structure you want to preserve).
3. Add files to be copied (they must be inside the root folder).
4. Click **Copy Files**.

The files will be copied to the destination, preserving their paths relative to the root folder.
