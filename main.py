import tkinter
import customtkinter
from pytube import YouTube
from pytubefix import YouTube
from pytubefix.cli import on_progress

def startDownload():
    try:
        youtube_link = link.get()
        youtube_obj = YouTube(youtube_link,on_progress_callback=on_progress)
        print(youtube_obj.title)
        audio = youtube_obj.streams.get_audio_only()
        audio.download()
    except:
        print("Invalid Link")    
    print("Download Complete")   
   


# system settings

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")


# app frame 

app = customtkinter.CTk()
app.geometry("720x580")
app.title("Youtube Audio Downloader")

# adding UI elements

title = customtkinter.CTkLabel(app,text="Insert a YouTube link.")
title.pack(padx=10,pady=10)


#link input area
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app,width=350,height=40,textvariable= url_var)
link.pack()


# download button

download = customtkinter.CTkButton(app,text="Download",command=startDownload)
download.pack(padx = 10, pady = 10)

#Run app

app.mainloop()