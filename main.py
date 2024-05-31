import tkinter
import customtkinter
from pytube import YouTube
import os 

def startDownload():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()
        #Directs download to Download folder
        downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        video.download(output_path=downloads_path)
        print('Download Complete!')
    except Exception as e:
        print(f'Error: {e}')
        print('Link invalid or issue with downloading the video.')

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100 
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()

# Update progress bar
    progressBar.set(float(percentage_of_completion) / 100)

# system settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme('green')

#Our App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title('Youtube To Audio')

# UI Elements
title = customtkinter.CTkLabel(app, text="Insert A Youtube Link")
title.pack(padx=10, pady=10)
header = customtkinter.CTkLabel(app, text="Use CTRL + C for Copy & CTRL + V for paste!")
header.pack(padx=10, pady=10)


#link input
url_var= tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

#Download Button
button = customtkinter.CTkButton(app, text="Download", command=startDownload)
button.pack()
button.pack(padx=10, pady=10)

# Progress Bar
pPercentage = customtkinter.CTkLabel(app, text='0%')
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, orientation="horizontal", width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)


progressBar.pack()

# Run app
app.mainloop();