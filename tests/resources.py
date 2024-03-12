from tkinter import *
from tkinter import messagebox
import customtkinter as mctk
from PIL import Image as im, ImageTk



def setTheme() :
    if(root._get_appearance_mode() == 'dark') :
        mode = 'light'
    else : 
        mode = "dark"
    # root._set_appearance_mode(f"{mode}")
    mctk.set_appearance_mode(mode)
    root._set_appearance_mode(mode)
    toogleThemeButton.configure(text = f"{mode.upper()} mode")


root = mctk.CTk
root.title("BalanceMaster")
root.geometry("925x500+300+200")
root.configure(bg='#FFFFF')
root._set_appearance_mode("light")
root.resizable(False,False)
root.iconify()
bg = mctk.CTkImage(light_image=im.open("background-light.jpeg"), dark_image=im.open("background.jpg"),size=(925,500))
icon = mctk.CTkImage(light_image=im.open("logo_trial.png"), dark_image=im.open("logo_trial.png"),size=(925,500))
my_label = mctk.CTkLabel(root,image=bg,text="")
# my_label.place(x=0,y=0,relwidth=1,relheight=1)
my_label.place(x=0,y=0)
toogleThemeButton = mctk.CTkButton(master=root,text="LIGHT mode",bg_color="transparent")
toogleThemeButton.configure(command=setTheme())
toogleThemeButton.pack()
