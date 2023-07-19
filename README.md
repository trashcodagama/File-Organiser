# File Organizer Script

This script organizes files in a specified directory into different folders based on their file types. It helps in categorizing and managing files more efficiently.

## Usage

1. Clone the repository or download the script file.

2. Modify the script:

   - Set the target directory path by updating the `os.chdir()` function call at the beginning of the script.
   - Optionally, update the list of folders to be created if you want different folder names.

3. Run the script using Pythons


4. The script will categorize and move files into their respective folders based on their file extensions. Folders that already exist in the target directory will not be modified or moved.

5. Once the script completes, it will display the count of successfully moved files and folders.

## Supported File Types

The script currently supports the following file types for categorization:

- Audio: `.3ga`, `.aac`, `.ac3`, `.aif`, `.aiff`, `.alac`, `.amr`, `.ape`, `.au`, `.dss`, `.flac`, `.flv`, `.m4a`, `.m4b`, `.m4p`, `.mp3`, `.mpga`, `.ogg`, `.oga`, `.mogg`, `.opus`, `.qcp`, `.tta`, `.voc`, `.wav`, `.wma`, `.wv`

- Video: `.webm`, `.MTS`, `.M2TS`, `.TS`, `.mov`, `.mp4`, `.m4p`, `.m4v`, `.mxf`

- Image: `.jpg`, `.jpeg`, `.jfif`, `.pjpeg`, `.pjp`, `.png`, `.gif`, `.webp`, `.svg`, `.apng`, `.avif`

- Executable Files: `.exe`

- Compressed Files: `.zip`, `.rar`

- PDF and Word Documents: `.pdf`, `.docx`


Feel free to customize and modify it to fit your specific requirements.

