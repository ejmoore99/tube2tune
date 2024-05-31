# YouTube to MP3 Converter

![Screenshot (97)](https://github.com/ejmoore99/tube2tune/assets/155325780/5392fa45-56b2-40bb-a849-d6f9037b1d33)

This is an open-source YouTube to MP3 converter program written in Python. It allows users to download YouTube videos as MP3 files and stores the downloaded files directly in the user's Downloads folder.

## Features

- Convert YouTube videos to MP3 format
- Automatically save the downloaded MP3 files to the user's Downloads folder
- Simple and intuitive graphical user interface (GUI)

## Requirements

- Python 3.6+
- `pytube` library
- `customtkinter` library

## Installation

1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install the required libraries using pip:
    ```bash
    pip install pytube customtkinter
    ```

## Usage

1. Run the program using Python:
    ```bash
    python main.py
    ```
2. A GUI will appear. Insert the YouTube link in the provided text field.
3. Click the "Download" button to start the download process.
4. The downloaded MP3 file will be saved in your Downloads folder.

## Code Overview

### Imports

The following libraries are used in the program:

```python
import tkinter
import customtkinter
from pytube import YouTube
import os
Functions
startDownload()
This function handles the downloading of the YouTube video. It extracts the link from the input field, downloads the video in the highest resolution, and saves it in the Downloads folder.

python
def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        video.download(output_path=downloads_path)
        print('Download Complete!')
    except Exception as e:
        print(f'Error: {e}')
        print('Link invalid or issue with downloading the video.')
on_progress(stream, chunk, bytes_remaining)
This function updates the progress of the download and displays it in the GUI.

python
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100 
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    progressBar.set(float(percentage_of_completion) / 100)
GUI Setup
The GUI is created using customtkinter and includes elements such as labels, text entry fields, buttons, and a progress bar.

python
# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme('green')

# Our App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title('YouTube To Audio')

# UI Elements
title = customtkinter.CTkLabel(app, text="Insert A YouTube Link")
title.pack(padx=10, pady=10)
header = customtkinter.CTkLabel(app, text="Use CTRL + C for Copy & CTRL + V for paste!")
header.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
button = customtkinter.CTkButton(app, text="Download", command=startDownload)
button.pack(padx=10, pady=10)

# Progress Bar
pPercentage = customtkinter.CTkLabel(app, text='0%')
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, orientation="horizontal", width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Run app
app.mainloop()

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.
