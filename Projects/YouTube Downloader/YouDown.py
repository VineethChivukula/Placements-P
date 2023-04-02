import tkinter as tk
from pytube import YouTube

def download():
    url = entry.get()
    resolution = resolution_var.get()
    try:
        yt = YouTube(url)
        streams = yt.streams.filter(progressive=True)
        for stream in streams:
            print(stream.resolution)
        stream = streams.filter(res=resolution).first()
        stream.download()
        status_label.config(text="Download successful!")
    except Exception as e:
        status_label.config(text="Error: " + str(e))

# Create the tkinter GUI
root = tk.Tk()
root.title("YouTube Video Downloader")

# Create the input field for the YouTube URL
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack()
entry = tk.Entry(root, width=50)
entry.pack()

# Create a dropdown menu for selecting the video resolution
resolution_label = tk.Label(root, text="Select video resolution:")
resolution_label.pack()
resolution_var = tk.StringVar(root)
resolution_choices = ["1080p", "720p", "480p", "360p", "240p", "144p"]
resolution_menu = tk.OptionMenu(root, resolution_var, *resolution_choices)
resolution_menu.pack()

# Create the download button
download_button = tk.Button(root, text="Download", command=download)
download_button.pack()

# Create a label for displaying the download status
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()