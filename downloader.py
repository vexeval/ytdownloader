from tkinter import *
from tkinter import filedialog
from pytube import YouTube
from pytube import Playlist

import os
import sys
import requests, json
import time

# version control
try:
    latestVersion = requests.get("https://api.github.com/repos/vexeval/ytdownloader/tags")
    versionData = json.loads(latestVersion.text)
    versionName = versionData[0]['name']
    print(versionName)
except:
    latestVersion = "Unable to load version"

if versionName == "v1.1.0-beta":
    versionIndicator = "Up to date!"
else:
    versionIndicator = "Update available!"
    print("Update Available! Check the github releases page for an update.")
    print("https://github.com/vexeval/ytdownloader/releases")
    

# select download path
def select_path():
    #allows the user to select the path
    path = filedialog.askdirectory()
    path_label.config(text=path)
    screen.title('Youtube Download Tool v1.0.1')

# download mp4 video
def download_file():
    try:
        #get user path
        get_link = link_field.get()
        
        #get selected path
        user_path = path_label.cget("text")
        
        #get video
        screen.title('Identifying Content...')
        yt = YouTube(get_link)
        # print(content.streams.filter(progressive=True))
        video = yt.streams.get_highest_resolution()
        
        #download video
        screen.title('Downloading...')
        video.download(str(user_path))
        
        #move file to selected location
        # shutil.move(mp4_video, user_path)
        screen.title('Download Complete!')
        print("Downloaded \""+yt.title+"\" Successfully")
        
    except:
        screen.title("An error has occured :/")
        print("Error",sys.exc_info(),"occured.")
    
def download_mp3_file():
    try:
        #get user path
        get_link = link_field.get()
        user_path = path_label.cget("text")
        
        #Get video
        screen.title('Indentifying Content...')
        yt = YouTube(get_link)
        
        #Download mp3
        screen.title('Downloading...')
        audio_file = yt.streams.filter(only_audio=True).first().download(str(user_path))
        base, ext = os.path.splitext(audio_file)
        new_file = base + '.mp3'
        os.rename(audio_file, new_file)
        
        screen.title('Download Complete!')
        print("Downloaded \""+yt.title+"\" Successfully")
    except:
        screen.title("An error has occured!")
        print("Error",sys.exc_info(),"occured.")

def download_playlist_file():
    try:
        #get user path
        get_link = link_field.get()
        user_path = path_label.cget("text")
        
        #get link information
        screen.title('Indentifying Content...')
        plist = Playlist(get_link)
        
        #download playlist
        for video in plist.videos:
            try:
                screen.title("Downloading \""+video.title+"\"")
                video.streams.get_highest_resolution().download(str(user_path))
                time.sleep(5)
            except:
                screen.title("An error has occured while downloading \""+video.title+"\". Skipping...")
                print("Error",sys.exc_info(),"occured. Skipping...")
        
        screen.title('Download Complete!')
        print("Downloaded \""+plist.title+"\" Successfully")

    except:
        screen.title("An error has occured! Make sure you have a valid playlist link, not a video within a playlist.")
        print("Error",sys.exc_info(),"occured.")

def download_playlist_mp3():
    try:
        #get user path
        get_link = link_field.get()
        user_path = path_label.cget("text")
        
        #get link information
        screen.title('Indentifying Content...')
        plist = Playlist(get_link)
        
        #download playlist
        for video in plist.videos:
            try:
                screen.title("Downloading \""+video.title+"\"")
                audio_file = video.streams.filter(only_audio=True).first().download(str(user_path))
                base, ext = os.path.splitext(audio_file)
                new_file = base + '.mp3'
                os.rename(audio_file, new_file)
                
                time.sleep(2.5)
            except:
                screen.title("An error has occured while downloading \""+video.title+"\". Skipping...")
                print("Error",sys.exc_info(),"occured. Skipping...")
        
        screen.title('Download Complete!')
        print("Downloaded \""+plist.title+"\" Successfully")

    except:
        screen.title("An error has occured! Make sure you have a valid playlist link, not a video within a playlist.")
        print("Error",sys.exc_info(),"occured.")

screen = Tk()

# screen favicon
screen.iconbitmap("shoe.ico")

# disable resizing of the window
screen.resizable(0,0)

title = screen.title('Youtube Download Tool')
canvas = Canvas(screen, width=500, height=600)  
canvas.pack()

# image
logo_img = PhotoImage(file='ytimage.png')

# resize
logo_img = logo_img.subsample(3, 3)

canvas.create_image(250, 150, image=logo_img)

# link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Link", font=('Segoe UI', 12))

# footer text
footer_label = Label(screen, text="Note: Overwriting a file with another is not \ncurrently supported and will result in an issue.\n\nAlso, downloading without a specified path will result in the file \nbeing downloaded in the source files of this project.", font=('Segoe UI', 8))
footer_label.pack(side=BOTTOM)

# update label
update_label = Label(screen, text=versionIndicator, font=('Segoe UI', 7))
update_label.pack(side=LEFT)

# select path for saving the file
path_label = Label(screen, text="Select Save Location", font=('Segoe UI', 11))
select_btn = Button(screen, text="Browse", command=select_path)

# add to window
canvas.create_window(250, 320, window=path_label)
canvas.create_window(250, 350, window=select_btn)

# add widgets to window
canvas.create_window(250, 260, window=link_label)
canvas.create_window(250, 290, window=link_field)

# download btns
download_btn = Button(screen, text="Download (mp4)", command=download_file)
download_playlist_btn = Button(screen, text="Download playlist (mp4)", command=download_playlist_file)
download_playlist_mp3_btn = Button(screen, text="Download playlist (mp3)", command=download_playlist_mp3)
download_mp3_btn = Button(screen, text="Download (mp3)", command=download_mp3_file)


# add to canvas
canvas.create_window(250, 400, window=download_btn)
canvas.create_window(250, 450, window=download_mp3_btn)
canvas.create_window(250, 500, window=download_playlist_btn)
canvas.create_window(250, 550, window=download_playlist_mp3_btn)

# download_mp3_btn["state"] = 'disabled'


screen.mainloop()