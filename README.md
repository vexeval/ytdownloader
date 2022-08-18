# Vex's Youtube Downloader

Hey! This is a simple python project I made so that I, along with others, wouldn't have to navigate sketchy websites when just trying to download a video off of Youtube they find enjoyable. This project is still pretty bear-bones in the releases, so suggestions on how to improve it are greatly appreciated.

# Installation & Operation

Everything should launch from running the batch file, but if it doesn't, modifiying a couple documented variables inside the file may be necessary.

When the download button is pressed in the interface, the title of the window will change to reflect the status of the download.

YTDownloader.bat is the file you will run to start the program. If you want to move the executable, it is recommended to create a shortcut of the
bat file and move the shortcut elsewhere. Make sure all the source files for this project are in their own folder (or just leave them in the folder they are downlodaed in) before running.

**Python is required.** If your installation of python is not in the `AppData/Local/Programs` directory, open the batch file and modify the path.

### One last thing..

My project uses the pytube library, which is currently capped at a maximum of 720p resolutions for video downloads. Unfortunately I haven't found a workaround for this, so downloads within my project are also capped at 720p.

**That should be all, enjoy!**

v1.1.0-beta
