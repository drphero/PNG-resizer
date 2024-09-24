# Image Resizer GUI

A simple and user-friendly application that resizes all PNG images in a selected folder to sizes specified by you. The application allows you to enter multiple sizes and processes all images accordingly, saving the resized images in a designated subfolder.

## Features

- **Easy to Use GUI:** Interact through a straightforward graphical interface without the need for command-line usage.
- **Customizable Sizes:** Specify any number of sizes to resize your images to, with default sizes provided.
- **Batch Processing:** Automatically processes all PNG images in the selected folder.
- **Organized Output:** Resized images are saved in a separate subfolder, keeping your original images untouched.

## System Requirements

- **Operating System:** Windows 7, 8, 10, or 11
- **No Additional Software Needed:** The application is a standalone executable; no installation of Python or other dependencies is required.

## Installation

1. **Download the Executable**

   - Download the `ImageResizerGUI.exe` file from the provided link or source.

2. **Save the Executable**

   - Place the `ImageResizerGUI.exe` file in any folder on your computer. You can create a dedicated folder for the application if you wish.

## Usage

1. **Launch the Application**

   - Double-click on `ImageResizerGUI.exe` to open the application.

2. **Select the Folder Containing Images**

   - Click on the **"Browse..."** button.
   - Navigate to the folder that contains the PNG images you want to resize.
   - Select the folder and click **"OK"** or **"Select Folder"**.

3. **Enter Desired Sizes**

   - In the field labeled **"Enter sizes (comma-separated):"**, input the sizes you want.
   - **Default Sizes:** The field is pre-filled with `72,36,18`.
   - **Format:** Enter sizes as integers separated by commas (e.g., `100,50,25`).

4. **Start Resizing**

   - Click the **"Start Resizing"** button.
   - The application will process all PNG images in the selected folder.
   - A progress indicator or message will notify you when resizing is complete.

5. **Access the Resized Images**

   - A new subfolder named `resized` will be created inside your original image folder.
   - The resized images will be saved in this subfolder.
   - Each resized image will have its original filename appended with the new size (e.g., `image_72x72.png`).

## Notes

- **Supported Image Format:** The application currently supports PNG images.
- **Original Images Remain Unchanged:** Your original images will not be modified.
- **Multiple Sizes:** You can enter as many sizes as you like; the application will resize each image to all specified sizes.