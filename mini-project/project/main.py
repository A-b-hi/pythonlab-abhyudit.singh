from tkinter import *
from tkinter import filedialog, messagebox
import subprocess

root = Tk()
root.geometry('450x300')
root.title("YouTube Video Downloader")  # Title of the program

Label(root, text='YouTube Video Downloader', font='arial 15 bold').pack()

link = StringVar()  # Variable to store the link of the video
folder_path = StringVar()  # Variable to store the download folder path

# Input field for the link
Label(root, text='Paste Link Here:', font='arial 13 bold').place(x=160, y=40)
Entry(root, width=45, textvariable=link).place(x=50, y=90)

# Function to browse for a download folder
def browse_folder():
    path = filedialog.askdirectory()
    if path:
        folder_path.set(path)

# Button to browse folder
Button(root, text="Choose Folder", command=browse_folder, font='arial 10').place(x=160, y=120)

# Function to download the video using yt-dlp
def Download():
    try:
        video_url = link.get()
        output_folder = folder_path.get()

        if not video_url:
            messagebox.showerror("Error", "Please enter a valid YouTube link!")
            return

        if not output_folder:
            messagebox.showerror("Error", "Please select a folder to save the video!")
            return

        Label(root, text='Downloading...', font='arial 13').place(x=180, y=210)

        # Use yt-dlp to download the video
        command = f'yt-dlp -o "{output_folder}/%(title)s.%(ext)s" {video_url}'
        subprocess.run(command, shell=True, check=True)

        Label(root, text='Downloaded!', font='arial 15').place(x=180, y=240)
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Download Error", f"An error occurred:\n{str(e)}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred:\n{str(e)}")

# Download button
Button(root, text='Download', font='arial 15 bold', padx=2, command=Download).place(x=180, y=150)

root.mainloop()
