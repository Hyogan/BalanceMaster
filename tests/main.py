from tkinter import *  
from tkinter import messagebox
import customtkinter as mctk
from PIL import Image as im, ImageTk
import json

ERRORS = {
    "empty_fields" : "Vous devez remplir tous les champs !",
    "login_failed" : "Les informations de connexion ne correspondent pas !"
}
with open('colors.json') as f:
    colorsa = json.load(f)
colors = colorsa['colors']

mctk.set_appearance_mode('light')
mctk.set_default_color_theme('blue')

root = mctk.CTk()
root.title("BalanceMaster - Login")
root.geometry("925x500+300+200")
root.configure(bg='#FFFFF')
root._set_appearance_mode("light")
root.resizable(False,False)
bg = mctk.CTkImage(light_image=im.open("background-light.jpeg"), dark_image=im.open("background.jpg"),size=(925,500))
# bg = mctk.CTkImage(light_image=im.open("logo_trial.png"), dark_image=im.open("logo_trial.png"),size=(925,500))
my_label = mctk.CTkLabel(root,image=bg,text="")
# my_label.place(x=0,y=0,relwidth=1,relheight=1)
my_label.place(x=0,y=0)


def setTheme() :
    if(root._get_appearance_mode() == 'dark') :
        mode = 'light'
    else : 
        mode = "dark"
    # root._set_appearance_mode(f"{mode}")
    mctk.set_appearance_mode(mode)
    root._set_appearance_mode(mode)
    toogleThemeButton.configure(text = f"{mode.upper()} mode")

def login(username_ent,password_ent,secretQuestion_ent,error_msg) :
    login_elements = recoverInput(username_ent,password_ent,secretQuestion_ent,error_msg)
    if(login_elements == FALSE) : 
        return
    if not (login_elements['Iusername'] == "john" and login_elements["Ipassword"] == "mon password" and login_elements["IsecretQuest"] == "Tobi\n") :
        setError(ERRORS['login_failed'])
        return 
    else :
        open_home_window()

def recoverInput(username_ent,password_ent,secretQuestion_ent,error_msg) :
    Iusername = username_ent.get()
    Ipassword = password_ent.get()
    IsecretQuest = secretQuestion_ent.get('1.0',END)
    if len(Iusername) == 0 or len(Ipassword) == 0 or len(IsecretQuest) <= 2 :
        setError(error_msg,ERRORS['empty_fields'])
        return FALSE
    user = {
            "Iusername" : Iusername,
            "Ipassword" : Ipassword,
            "IsecretQuest" : IsecretQuest
        }
    return user

def setError(error_msg,error) :
    error_msg.configure(text=error)

def show_hide_password(password_ent,show_password_button) :
    if password_ent.cget('show') == '*' :
        password_ent.configure(show='') 
        show_password_button.configure(text="hide")
    else :
        password_ent.configure(show="*")
        show_password_button.configure(text="show")
        
def open_home_window() :
    root.destroy()
    main_window = mctk.CTk()
    main_window.title("Balance Master - Main Window")
    root.title("BalanceMaster - Login")
    root.geometry("925x500+300+200")
    root.configure(bg='#FFFFF')
    root._set_appearance_mode("light")
    root.resizable(False,False)
    toogleThemeButton1 = mctk.CTkButton(master=main_window,text="LIGHT mode",command=setTheme,bg_color="transparent")
    toogleThemeButton1.pack()
    main_window.mainloop()


def main_window() :
    img = mctk.CTkImage(light_image=im.open("transparent-login.png"),dark_image=im.open("transparent-login.png"),size=(400,400))
    my_label2 = mctk.CTkLabel(root,image=img,bg_color="transparent",fg_color="transparent",text="").place(x=50,y=60)

    frame = mctk.CTkFrame(root,width=360,height=400,bg_color="transparent")
    frame.place(x=480,y=60)

    heading = mctk.CTkLabel(frame,text="Inscription",font=('Microsoft YaHei UI Light',23,'bold'))
    heading.place(x=100,y=8)

    error_msg = mctk.CTkLabel(frame,fg_color='transparent',bg_color='transparent',text="",text_color='red',font=('Microsoft YaHei UI Light',12,'bold'))
    error_msg.place(relx=0.5,anchor="center")
    error_msg.configure(wraplength=250)
    error_msg.place_configure(y=50)

    username_ent = mctk.CTkEntry(frame, corner_radius=None,placeholder_text="Enter your Username",width=250,height=35,border_width=0,font=('Microsoft UI Light',13,'bold'))
    username_ent.place(x=50,y=70)
    # mctk.CTkFrame(frame,width=250,height=2,fg_color=colors['primary']).place(x=50,y=107)

    password_ent = mctk.CTkEntry(frame,corner_radius=None,placeholder_text="Enter your Password",show="*",width=250,height=35,border_width=0,font=('Microsoft UI Light',13,'bold'))
    password_ent.place(x=50,y=130)

    show_password_button = mctk.CTkButton(master=frame,text="Show",width=45,height=35,command=show_hide_password(password_ent,show_password_button),bg_color="transparent")
    show_password_button.place(x=305,y=130)

    # mctk.CTkFrame(frame,width=250,height=4,fg_color=('red',colors['primary'])).place(x=50,y=180)
    # password.focus(corder_radius=2)
    question = "What is your pet name ?"
    secretQuestionLabel = mctk.CTkLabel(frame,text=f"{question}",width=250,height=35,font=('Microsoft UI Light',13,'bold'))
    secretQuestionLabel.place(x=50,y=170)
    secretQuestion_ent = mctk.CTkTextbox(frame,width=250,height=150)
    secretQuestion_ent.place(x=50,y=200)

    loginButton = mctk.CTkButton(master=frame,text="Login",bg_color='transparent', command=login(username_ent,password_ent,secretQuestion_ent,error_msg))
    loginButton.place(x=50,y=355)



    img = mctk.CTkImage(light_image=im.open("logo_trial.png"),dark_image=im.open("logo_trial.png"),size=(250,250))
    # img = mctk.CTkImage(light_image=im.open("logo_trial-removebg-preview.png"),dark_image=im.open("logo_trial-removebg-preview.png"),size=(250,250))
    my_label2 = mctk.CTkLabel(root,image=img,bg_color="transparent",fg_color="transparent",text="").place(x=0,y=250)
  
# img = PhotoImage(file='transparent-login.png')
# img = mctk.CTkImage(light_image=im.open("transparent-login.png"), dark_image=im.open("transparent-login.png"),size=(400,400))


main_window()
toogleThemeButton = mctk.CTkButton(master=root,text="LIGHT mode",command=setTheme,bg_color="transparent")
toogleThemeButton.pack()
root.mainloop()
