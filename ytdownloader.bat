@echo off
echo Downloading Packages...
call pip install tkinter
call pip install moviepy
call pip install pytube
echo Packages Installed Successfully!

@REM If there's an error with the installation and the cmd closes, uncomment every "pause" line to troubleshoot.
@REM pause

cls

@REM ===================================== - USER INPUTS

@rem | Important: You will need python 3.10 installed. If your python is installed somewhere different than the quotes at the bottom of the program,
@rem | change the path at the bottom to correct it.
@rem | Make sure all the source files for this project are in their own folder before running.
@rem | Python download: https://www.python.org/downloads/

@REM The %USERNAME% variable should work, but if it doesn't, insert pc name below:
set pcname=%USERNAME%

@REM Insert path to downloader.py. Typically this can be left alone, or set manually if issues are encountered. (EXAMPLE: c:/Users/rickastley/Documents/vex-ytdownloader-portable/downloader.py)
set path=downloader.py

@REM =====================================

@REM If there was a problem, remove the "rem" from the line below to diagnose the issue. The most common issue is that there is a space in the path to the script, so ensure there are no spaces in the path you've selected.
@REM pause

@REM If the downloader.py script is moved or renamed, this file will need to be edited with the updated path.

@REM - Everthing below can be ignored.


@echo YT Downloader v1.0.0 by Vexeval opened
"C:/Users/%pcname%/AppData/Local/Programs/Python/Python310/python.exe" "%path%"