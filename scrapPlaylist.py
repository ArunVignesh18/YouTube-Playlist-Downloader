from tkinter import *
from pytube import YouTube
from pytube import Playlist

root = Tk()
root.title("YouTube Playlist Downloader")
root.iconbitmap("YTPLDL.ico")

root.geometry("400x400")

# v = Scrollbar(root, orient='vertical')
# v.config(command=t.yview) #for vertical scrollbar

myimg = PhotoImage(file="background.png")
myLabel3 = Label(root, image=myimg)
myLabel3.place(x=0,y=61)

# root.wm_attributes('-transparentcolor','white')

myLabel2 = Label(root, text = "Welcome to YouTube Playlist Downloader")
myLabel2.pack()

myLabel1 = Label(root, text = "Enter The Playlist Link")
myLabel1.pack()

e = Entry(root, width=100)
e.pack()

error = False
buttons = []
buttons_index = []

# def thanksf(downloading = False, totalvideos = None, videosdownloaded = None, error = False, downloaded = False):
    
#     if downloaded:
#         thanks.config(text = "Thanks for using YouTube Playlist Downloader\nTry again with another link")
#         print("Inside Downloaded")

#     elif error:
#         thanks.config(text = "The link you entered is not valid\nTry again with a valid link")
#         print("Inside Error")

#     elif downloading:
#         thanks.config(text = str(videosdownloaded) + "/" + str(totalvideos) + " videos downloaded")
#         print("Inside Downloading")

#     thanks.pack()


def download_single(video):

    YouTube(video).streams.filter(progressive=True, file_extension='mp4').first().download()
    
    for button in buttons:
        
        if button["text"] == YouTube(video).title:
            print(YouTube(video).title)
            button["text"] = "downloaded"
            button["bg"] = '#ee9527'
            button["state"] = DISABLED
            buttons_index.append(buttons.index(button))

    if len(buttons) == len(buttons_index):
        myLabel4 = Label(root, text = "Thanks for using YouTube Video Downloader")
        myLabel4.pack()
        buttons_index = []
        buttons = []

def download_all(videos2download):

    for video in videos2download:
        if videos2download.index(video) not in buttons_index:
            download_single(video)
        
    download_all_button["text"] = "Downloaded All"
    download_all_button["state"] = DISABLED


def load_playlist():

    global videos2download
    videos2download = Playlist(e.get())

    for video in videos2download.video_urls:

        global download_single_button
        download_single_button = Button(root, text=YouTube(video).title, width = 50, command = lambda video = video : download_single(video), bg="#5783db", fg="white", highlightbackground="red", activebackground="yellow")
        download_single_button.pack()
        buttons.append(download_single_button)

    v = Scrollbar(root)
    v.pack(side = RIGHT, fill = Y)
    v.config(command=download_single_button.yview)

    global download_all_button
    download_all_button = Button(root, text = "Download All", width = 30, command = lambda videos2download = videos2download : download_all(videos2download), bg="#5dbea3", fg="white", highlightbackground="red", activebackground="yellow")
    download_all_button.pack()


submit_button = Button(root, text="Submit", padx = 40, command=load_playlist, bg = "green", fg="white")
submit_button.pack()


root.mainloop()