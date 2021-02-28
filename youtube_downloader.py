import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox


def createWidgets():

    link_label = Label(root, text="Youtube URL: ", bg='#CC0000')
    link_label.grid(row=1, column = 0, pady= 5, padx = 5)

    root.link_text = Entry(root, width=60, textvariable= video_link)
    root.link_text.grid(row=1, column = 1, pady=5, padx=5)

    destination_label = Label(root, text = 'Destionation: ', bg='#CC0000')
    destination_label.grid(row = 2, column =0, pady=15, padx=5)

    root.dest_button = Entry(root, width= 60, textvariable = download_path)
    root.dest_button.grid(row=2, column=1, pady=15, padx=5)

    browse_button = Button(root, text='Browse', command=browse, width=10, bg='#CC0000')
    browse_button.grid(row=2, column=2, pady=1, padx=1)

    download_button = Button(root, text='Download', command=download, width=10, bg='#CC0000')
    download_button.grid(row=3, column=2, pady=15, padx=1)


def browse():
    download_dir = filedialog.askdirectory(initialdir = '')
    download_path.set(download_dir)


def download():

    url = video_link.get()
    folder=download_path.get()

    get_video = YouTube(url)
    get_stream = get_video.streams.first()
    get_stream.download(folder)
    messagebox.showinfo ('success', 'Download successful!')


root = tk.Tk()

root.geometry('600x150')
root.resizable(False, False)
root.title('Pytube')

root.config(background = '#000000')

video_link = StringVar()
download_path = StringVar()


createWidgets()

root.mainloop()