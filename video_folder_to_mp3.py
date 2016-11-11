from Tkinter import *
import tkFileDialog
import tkMessageBox
from subprocess import Popen

master = Tk()

def filen(flag):
    directory = tkFileDialog.askdirectory()
    if flag == 1:
        ffmpegpath.delete(0,END)
        ffmpegpath.insert(1,directory)
    if flag == 2:
        folderpath.delete(0,END)
        folderpath.insert(1,directory)
    if flag == 3:
        destpath.delete(0,END)
        destpath.insert(1,directory)
        
def convert():
    str1 = "cd /D %s \n" % (folderpath.get())
    str2 = r'for bba in ("*.*") do %s\ffmpeg -i "bba" -f mp3 "%s\bb~na.mp3' % (ffmpegpath.get(),destpath.get())
    str2 = str2.replace("bb","%%")
    str4 = "\n @echo Off "
    str3 = "\npause"
    batch_command = str1+str2+str4+str3
    f = open("simple.bat","w")
    f.write(batch_command)
    f.close()
    p = Popen("simple.bat")
    stdout, stderr = p.communicate()


text1 = Label(master,text="Select folder where FFMPEG is")
text1.grid(row=0,padx=10,pady=10)

ffmpegpath = Entry(width=25)
ffmpegpath.grid(row=0,column=1,padx=20,pady=20,ipadx=5,ipady=3)


ffmpeg_path_button = Button(master, text="...",command=lambda : filen(1))
ffmpeg_path_button.grid(row=0,column=2,padx=10)

text2 = Label(master,text="Select folder where your videos are stored")
text2.grid(row=1,padx=10,pady=10)

folderpath = Entry(width=25)
folderpath.grid(row=1,column=1,padx=20,pady=20,ipadx=5,ipady=3)

folder_path_button = Button(master, text="...",command=lambda : filen(2))
folder_path_button.grid(row=1,column=2,padx=10)

text3 = Label(master,text="Select folder to store audios")
text3.grid(row=2,padx=10,pady=10)

destpath = Entry(width=25)
destpath.grid(row=2,column=1,padx=20,pady=20,ipadx=5,ipady=3)

dest_path_button = Button(master, text="...",command=lambda : filen(3))
dest_path_button.grid(row=2,column=2,padx=10)

convert_button = Button(master,text="Convert",fg="brown",font=2,command=convert)
convert_button.grid(row=4,column=1,columnspan=2,ipadx=28,ipady=3,pady=5)

master.iconbitmap(bitmap="favicon.ico")
master.minsize(width=510,height=300)
master.maxsize(width=510,height=300)
master.resizable(width=FALSE,height=FALSE)
master.title("Convert To mp3")

mainloop()
