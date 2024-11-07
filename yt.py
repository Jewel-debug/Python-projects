# from pytube import YouTube
# imort tk
# url = input("enter youy url > ")

# video = YouTube(url)

# downloader = video.streams.get_highest_resolution()

# downloader.download()

import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    if url:
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download()
            messagebox.showinfo("Success", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    else:
        messagebox.showwarning("Input Error", "Please enter a YouTube URL")

# Create the main window
root = tk.Tk()
root.title("YouTube Downloader")
root.geometry("400x200")

# Create and place URL label and entry
url_label = tk.Label(root, text="Enter YouTube URL:")
url_label.pack(pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create and place the download button
download_button = tk.Button(root, text="Download", command=download_video)
download_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
