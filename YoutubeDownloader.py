from tkinter import *
from tkinter import filedialog
import webbrowser
import pytube.exceptions
from pytube import YouTube
import win32com.client
import os
import json
from pytube import Playlist
import urllib.request as request
from PIL import ImageTk,Image


def callback(url):
    webbrowser.open_new_tab(url)
def select_pathv():

    path = filedialog.askdirectory()
    with open("data.json", "r") as file:
        filep = json.load(file)
    filep["path"] = path 
    with open("data.json", "w") as file:
        json.dump(filep, file, indent=4)
def hide_option():
    option_can.place_forget()
    option_but_can.place(rely=0.07, relx=0.07, anchor=E)
def open_option():
    option_can.place(relx=0.27,rely=0.5,anchor=E)
    option_can.config(bg='grey')
    option_but_can.place_forget()
def download_video():
    vcanvas.pack_forget()
    with open("data.json", "r") as file:
        filep = json.load(file)
    pathu =filep["path"]
    if len(pathu) >= 20:
        pathu = pathu[:20] +"..."
    pathlabel.config(text=pathu)

    qucanves.place(relx=0.23,rely=0.5, anchor=W)
    # screen.title("Please select a resolution")
    # get_link = link_field.get()
    # get_link.title
    # get_link.thumbnail_url
    
    
    # mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
def close_qu():
    qucanves.place_forget()
    vcanvas.pack()
def change_window_to_playlist():
    vcanvas.pack_forget()
    pcanvas.pack()
    option_can.place_forget()
    option_but_can.place(relx=0.07 , rely=0.07, anchor=E)
    mcanves_change_but.config(text="Open Video Downloader", command=change_window_to_video)

def write(data, filename="data.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
def one_hundred_forty_four_p_download():
    with open("num.json", "r") as file:
        getnum = json.load(file)
    numvalue = getnum["lastnumber"]
    if numvalue <= 2:
        path = filedialog.askdirectory()
        pathlabel.config(text=path)

    else: 
        with open("data.json", "r") as file:
            fileu = json.load(file)
        path = fileu["path"]
        pathlabel.config(text=path)
    try:
            
        request.urlopen("https://www.google.com", timeout=2)
        get_link = link_field.get()
    
    
        try:
                title = get_link.title()

                videosize = YouTube(get_link).streams.filter(res="144p").first().filesize 
                print(videosize)


                with open("data.json", "r") as file:
                    fileu = json.load(file)
                user_path = fileu["path"]
                # print(user_path)
                qucanves.place_forget()
                vcanvas.pack()
                # YouTube(get_link).register_on_progress_callback(on_progress)
                YouTube(get_link).streams.filter(res="144p").first().download(path)
                with open("num.json", "r") as file:
                    dato = json.load(file)
                num = dato["lastnumber"]
                dato["lastnumber"] = num + 1
                useput = num + 1
                print(useput)
                a = "video_"
                b = useput
                c = a + str(b)
                with open("num.json", "w")as file:
                    json.dump(dato, file)
                with open("data.json") as file:
                    data = json.load(file)
                    temp = data["videos"]
                    datu ={c:{"videolink": title , "thumbnail_link":"test" , "quality":"140p", "Downloaded Path": user_path}, }
                    temp.append(datu)
                write(data)
                print(title)
                screen.title('Downloading...')
                status.config(text="Downloading...")
                screen.title('Download Complete! Download Another File...')
                status.config(text="Download Complete! Download Another File")
        except pytube.exceptions.RegexMatchError:
                error_box1 = Tk()
                error_box1.geometry("300x200")
                error_box1.title("Error")
                error_can = Canvas(error_box1 , width=300, height=200)
                error_can.config(bg="red")
                error_label1 = Label(error_box1, text="Error : Please put a valid or accessable link", font=('Arial', 11))
                error_can.create_window(150,100,window=error_label1)
                error_can.pack()
                qucanves.place_forget()
                vcanvas.pack()
        except pytube.exceptions.VideoUnavailable:
                error_box2 = Tk()
                error_box2.geometry("300x200")
                error_box2.title("Error")
                error_can = Canvas(error_box2 , width=300, height=200)
                error_can.config(bg="red")
                error_label2 = Label(error_box2, text="Error : The Video is removed by the author", font=('Arial', 11))
                error_can.create_window(150,100,window=error_label2)
                error_can.pack()
                qucanves.place_forget()
                vcanvas.pack()   
    except :
            error_box3 = Tk()
            error_box3.geometry("300x200")
            error_box3.title("Error")
            error_can = Canvas(error_box3, width=300, height=200)
            error_can.config(bg="red")
            error_label3 = Label(error_box3, text="Error : Poor or no Internet connection", font=("Arial", 11))
            error_can.create_window(150, 100, window=error_label3)
            error_can.pack()
            qucanves.place_forget()
            vcanvas.pack()

def three_sixty_p_download():
    try:
            
            request.urlopen("https://www.google.com", timeout=2)
            get_link = link_field.get()
    
    
            try:
                title = get_link.title()

                videosize = YouTube(get_link).streams.filter(res="360p").first().filesize 
                print(videosize)


                with open("data.json", "r") as file:
                    fileu = json.load(file)
                user_path = fileu["path"]
                # print(user_path)
                qucanves.place_forget()
                vcanvas.pack()
                # YouTube(get_link).register_on_progress_callback(on_progress)
                YouTube(get_link).streams.filter(res="360p").first().download(user_path)
                with open("num.json", "r") as file:
                    dato = json.load(file)
                num = dato["lastnumber"]
                dato["lastnumber"] = num + 1
                useput = num + 1
                
                a = "video_"
                b = useput
                c = a + str(b)
                with open("num.json", "w")as file:
                    json.dump(dato, file)
                with open("data.json") as file:
                    data = json.load(file)
                    temp = data["videos"]
                    datu ={c:{"videolink": title , "thumbnail_link":"test" , "quality":"360p", "Downloaded Path": user_path}, }
                    temp.append(datu)
                write(data)
                print(title)



                screen.title('Downloading...')
                status.config(text="Downloading...")
                screen.title('Download Complete! Download Another File...')
                status.config(text="Download Complete! Download Another File")
            except pytube.exceptions.RegexMatchError:
                error_box1 = Tk()
                error_box1.geometry("300x200")
                error_box1.title("Error")
                error_can = Canvas(error_box1 , width=300, height=200)
                error_can.config(bg="red")
                error_label1 = Label(error_box1, text="Error : Please put a valid or accessable link", font=('Arial', 11))
                error_can.create_window(150,100,window=error_label1)
                error_can.pack()
                qucanves.place_forget()
                vcanvas.pack()
            except pytube.exceptions.VideoUnavailable:
                error_box2 = Tk()
                error_box2.geometry("300x200")
                error_box2.title("Error")
                error_can = Canvas(error_box2 , width=300, height=200)
                error_can.config(bg="red")
                error_label2 = Label(error_box2, text="Error : The Video is removed by the author", font=('Arial', 11))
                error_can.create_window(150,100,window=error_label2)
                error_can.pack()
                qucanves.place_forget()
                vcanvas.pack()   
    except :
            error_box3 = Tk()
            error_box3.geometry("300x200")
            error_box3.title("Error")
            error_can = Canvas(error_box3, width=300, height=200)
            error_can.config(bg="red")
            error_label3 = Label(error_box3, text="Error : Poor or no Internet connection", font=("Arial", 11))
            error_can.create_window(150, 100, window=error_label3)
            error_can.pack()
            qucanves.place_forget()
            vcanvas.pack()
def audio_only():
    try:
            request.urlopen("https://www.google.com", timeout=10)
            get_link = link_field.get()
    
    
            try:
                title = get_link.title()

                # videosize = YouTube(get_link).streams.filter(only_audio=True).filesize 
                # print(videosize)


                with open("data.json", "r") as file:
                    fileu = json.load(file)
                user_path = fileu["path"]
                # print(user_path)
                qucanves.place_forget()
                vcanvas.pack()
                #YouTube(get_link).register_on_progress_callback(on_progress)
                you = YouTube(get_link).streams.filter(only_audio=True).first()
                you2 =  you.download(user_path)
                base = os.path.splitext(you2)
                # new_file = base + ".mp3"
                # os.rename(you2, new_file)
                with open("num.json", "r") as file:
                    dato = json.load(file)
                num = dato["lastnumber"]
                dato["lastnumber"] = num + 1
                useput = num + 1
                print(useput)
                a = "video_"
                b = useput
                c = a + str(b)
                with open("num.json", "w")as file:
                    json.dump(dato, file)
                with open("data.json") as file:
                    data = json.load(file)
                    temp = data["videos"]
                    datu ={c:{"videolink": title , "thumbnail_link":"test" , "quality":"audio only (.mp3)", "Downloaded Path": user_path}, }
                    temp.append(datu)
                write(data)
                print(title)



                screen.title('Downloading...')
                status.config(text="Downloading...")
                screen.title('Download Complete! Download Another File...')
                status.config(text="Download Complete! Download Another File")
            except pytube.exceptions.RegexMatchError:
                error_box1 = Tk()
                error_box1.geometry("300x200")
                error_box1.title("Error")
                error_can = Canvas(error_box1 , width=300, height=200)
                error_can.config(bg="red")
                error_label1 = Label(error_box1, text="Error : Please put a valid or accessable link", font=('Arial', 11))
                error_can.create_window(150,100,window=error_label1)
                error_can.pack()
                qucanves.place_forget()
                vcanvas.pack()
            except pytube.exceptions.VideoUnavailable:
                error_box2 = Tk()
                error_box2.geometry("300x200")
                error_box2.title("Error")
                error_can = Canvas(error_box2 , width=300, height=200)
                error_can.config(bg="red")
                error_label2 = Label(error_box2, text="Error : The Video is removed by the author", font=('Arial', 11))
                error_can.create_window(150,100,window=error_label2)
                error_can.pack()
                qucanves.place_forget()
                vcanvas.pack()   
    except :
            error_box3 = Tk()
            error_box3.geometry("300x200")
            error_box3.title("Error")
            error_can = Canvas(error_box3, width=300, height=200)
            error_can.config(bg="red")
            error_label3 = Label(error_box3, text="Error : Poor or no Internet connection", font=("Arial", 11))
            error_can.create_window(150, 100, window=error_label3)
            error_can.pack()
            qucanves.place_forget()
            vcanvas.pack()



screen = Tk()
title = screen.title('Youtube Downloader')

vcanvas = Canvas(screen, width=1000, height=600)
pcanvas = Canvas(screen, width=1000, height=600)
option_can = Canvas(screen, width=270, height=600, border='2', relief="solid")
option_but_can = Canvas(screen, width=20, height=25)
qucanves = Canvas(screen, height=400,width=500, border='2', relief="solid" )
option_but_can.place(relx=0.07 , rely=0.07, anchor=E)
no_int = Canvas(screen, width=400, height=300)

pcanvas.pack_forget()
vcanvas.pack()
mainpath = os.path.abspath("YoutubeDownloader.exe")
# pythoncom.CoInitialize() # remove the '#' at the beginning of the line if running in a thread.
desktop = str(os.path.join(os.environ["HOMEPATH"], "Desktop")) # path to where you want to put the .lnk
st_text = "C:"
moddesktop = desktop.replace('\\','//')

mix_text = st_text + moddesktop
path = os.path.join(mix_text, 'YoutubeDownloader.lnk')
target = mainpath
icon = r'C:\\Program Files\\YoutubeDownloader\\logo.png' # not needed, but nice 

shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(path)
shortcut.Targetpath = target
# shortcut.IcmmonLocation = icon
shortcut.WindowStyle = 1 # 7 - Minimized, 3 - Maximized, 1 - Normal
shortcut.save()
#################################################Video Downloader canves##################################################################
copyrightv = Label(screen , text="AryanXP Youtube Downloader" , font=('Arial' , 20))
link_field = Entry(screen, width=40, font=('Arial', 15), relief="solid", border="2" )
link_labelv = Label(screen, text="Enter Download Link: ", font=('Arial', 15))
status = Label(screen, font=('Arial', 15))
infolabel = Label(screen, text="Hello This is Aryan, To run this program you \n need a Youtube video link avalible in \nWeb Browser like this:-", font=("Arial", 11))
versionareav = Label(screen, text="Version:1.3", font=('Arial', 10))
# img = Image.open("LabelforYD.jpg")
# img = img.resize((300,100))
# img = ImageTk.PhotoImage(img)

# vcanvas.create_image(650, 450, anchor=NW, image=img)
select_btn =  Button(screen, text="Select Path", bg='red', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=select_pathv)
download_btnv = Button(screen, text="Download video",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_video)
# audio_download_button = Button(screen, text=" Download audio only", bg='green', padx='22', pady='5', font=('Arial', 15), fg="#fff")
option_can_but = Button(screen, text='=', padx='5', pady='5', font=('Arial',15),background='gray',border='2', relief='solid',command=open_option)
option_but_can.create_window(  1 ,1,window=option_can_but)
vcanvas.create_window(800, 400, window=infolabel)
vcanvas.create_window(970, 590, window=versionareav)
vcanvas.create_window(500, 150, window=copyrightv)

vcanvas.create_window(500, 380, window=select_btn)
status_win = vcanvas.create_window(300, 500, window=status)
status_win
vcanvas.create_window(500, 210, window=link_labelv)
vcanvas.create_window(500, 260, window=link_field)
vcanvas.create_window(500, 360, window=download_btnv)
# vcanvas.create_window(380, 440, window=audio_download_button)

##########################################################
def download_playlist():
    pl = Playlist(playlist_field.get())
    purl = pl.videos
    print(purl)
    statusp.configure(text="Downloading...")
    for video in pl.videos:
        print(video.title)
        st = video.streams.get_lowest_resolution()
        st.download(path)
        print('video downloaded' + video.title)
    statusp.configure(text="Downloaded")

def change_window_to_video():
    pcanvas.pack_forget()
    vcanvas.pack()
    option_can.place_forget()
    option_but_can.place(relx=0.07 , rely=0.07, anchor=E)
    mcanves_change_but.config(text="Open Video Downloader", command=change_window_to_playlist)

##################################################playlist downloader canves###############################################################
copyrightp = Label(screen , text="AryanXP Youtube Playlist Downloader", font=('Arial', 20))
playlist_field = Entry(screen, width=40, font=('Arial', 15))
link_labelp = Label(screen, text="Enter Download Link: ", font=('Arial', 15))
statusp= Label(screen, text="No Download Pending", font=('Arial', 15))
versionareap = Label(screen, text="Version:1.3", font=('Arial', 10))
download_btnp = Button(screen, text="Download File",bg='green', padx='22', pady='5',font=('Arial', 15), fg='#fff', command=download_playlist)

pcanvas.create_window(500, 260, window=playlist_field) 
pcanvas.create_window(970, 590, window=versionareap)
pcanvas.create_window(500, 150, window=copyrightp)
pcanvas.create_window(500, 380, window=select_btn)
pcanvas.create_window(500,440, window=download_btnp)
status_win = pcanvas.create_window(500, 500, window=statusp)
pcanvas.create_window(500, 210, window=link_labelp)

############################################################ quality canves #################################################
#option_can
close_but = Button(screen, text='X', padx='5', pady='3', font=('Arial',15), command=hide_option, border=2, relief='solid')
mcanves_change_but = Button(screen, text="Open Playlist Downloader", padx='16', pady='5', font=('Arial', 14), command=change_window_to_playlist, border=2, relief='solid')
select_pathb = Button(screen, text="          Select a Path           ",padx="16", pady="5", font=("Arial", 14), command=select_pathv, border=2, relief='solid')
option_can.create_line(0,5000,400,0)
option_can.create_window(137, 100, window=mcanves_change_but)
option_can.create_window(137, 150, window=select_pathb)
option_can.create_window(240,30, window=close_but)

toplabel = Label(screen, text="Pease select a Resolution :", font=('Arial', 12))
close_but = Button(screen, text="X", font=('Arial',15), pady='1', padx='1',command=close_qu)
#quality = str
label_video = Label(screen, text="video with audio : ")
label_audio = Label(screen, text="Only audio track : ")
value_buttton1 = Button(screen, text="144p",command=one_hundred_forty_four_p_download, pady='5', padx='5')
value_buttton2 = Button(screen, text="360p", command=three_sixty_p_download, pady="5" , padx="5")
audio_vlaue_button1 = Button(screen, text="but1", command=audio_only, padx='5' , pady='5')
qulabel = Label(screen, text="Please Choose a Rsolution \n for your Video or Audio :\n\n\n\nVideo Will be Downloaded in :")
pathlabel = Label(screen, font=('Arial', 12))
qunote1 = Label(screen, text=" Note : Sometimes at the time of\n downloading the window might freeze \nand show not responding\nJUST IGNORE IT\n the file will be downloaded in the\n selected path", border=2, relief="solid")
qucanves.create_window(100, 150, window=qulabel)
qucanves.create_window(250, 25, window=toplabel)
qucanves.create_window(470, 30, window=close_but)
qucanves.create_window(400, 75, window=value_buttton1)
qucanves.create_window(400, 125, window=value_buttton2)
qucanves.create_window(400, 250, window=audio_vlaue_button1)
qucanves.create_window(300, 75, window=label_video)
qucanves.create_window(300, 250, window=label_audio)
qucanves.create_window(100, 160,window=pathlabel)
qucanves.create_window(150, 320, window=qunote1)

screen.mainloop()
