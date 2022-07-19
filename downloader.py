from tkinter import *
from tkinter import filedialog
from moviepy import *
from pytube import YouTube

import os
import sys
# import shutil


#Functions
def select_path():
    #allows the user to select the path
    path = filedialog.askdirectory()
    path_label.config(text=path)
    screen.title('Youtube Download Tool v1.0.0')

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
        screen.title("An error has occured! Duplicate files may have been downloaded.")
        print("Error",sys.exc_info(),"occured.")

screen = Tk()

#screen favicon
screen.iconbitmap("shoe.ico")

title = screen.title('Youtube Download Tool')
canvas = Canvas(screen, width=500, height=500)  
canvas.pack()

#image logo
logo_img = PhotoImage(file='ytimage.png')

#resize
logo_img = logo_img.subsample(3, 3)

canvas.create_image(250, 150, image=logo_img)

#link field
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Link", font=('Segoe UI', 12))

#footer text
footer_label = Label(screen, text="Note: Overwriting a file with another is not \ncurrently supported and will result in an issue.\n\nAlso, downloading without a specified path will result in the file \nbeing downloaded in the source files of this project.", font=('Segoe UI', 8))
footer_label.pack(side=BOTTOM)

#Select path for saving the file
path_label = Label(screen, text="Select Save Location", font=('Segoe UI', 11))
select_btn = Button(screen, text="Browse", command=select_path)

#Add to window
canvas.create_window(250, 320, window=path_label)
canvas.create_window(250, 350, window=select_btn)

#add widgets to window
canvas.create_window(250, 260, window=link_label)
canvas.create_window(250, 290, window=link_field)

#Download btns
download_btn = Button(screen, text="Download (mp4) (720p max)", command=download_file)
download_mp3_btn = Button(screen, text="Download (mp3)", command=download_mp3_file)
#add to canvas
canvas.create_window(250, 410, window=download_btn)
canvas.create_window(250, 460, window=download_mp3_btn)
# download_mp3_btn["state"] = 'disabled'


screen.mainloop()