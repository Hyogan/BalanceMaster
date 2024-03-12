import customtkinter as mctk
from PIL import Image as im, ImageTk
from frontend.Login import Login
import json

with open('colors.json') as f:
    colorsa = json.load(f)
colors = colorsa['colors']

mctk.set_appearance_mode('light')
mctk.set_default_color_theme('blue')


class BalanceMaster():
    def __init__(self,master):
        self.root = mctk.CTk()
        self.root.title("BalanceMaster")
        self.root.geometry("925x500+300+200")
        self.root.configure(bg='#FFFFF')
        self.root._set_appearance_mode("light")
        self.root.resizable(False, False)
        self.root.iconify()
        self.bg = mctk.CTkImage(light_image=im.open("background-light.jpeg"), dark_image=im.open("background.jpg"),
                                size=(925, 500))
        self.icon = mctk.CTkImage(light_image=im.open("logo_trial.png"), dark_image=im.open("logo_trial.png"),
                                  size=(925, 500))
        self.my_label = mctk.CTkLabel(self.root, image=self.bg, text="")
        # my_label.place(x=0,y=0,relwidth=1,relheight=1)
        self.my_label.place(x=0, y=0)
        self.toogleThemeButton = mctk.CTkButton(master=self.root, text="LIGHT mode", bg_color="transparent")
        self.toogleThemeButton.configure(command=self.setTheme())
        self.toogleThemeButton.pack()

    def setTheme(self):
        if (self.root._get_appearance_mode() == 'dark'):
            mode = 'light'
        else:
            mode = "dark"
        # root._set_appearance_mode(f"{mode}")
        mctk.set_appearance_mode(mode)
        self.root._set_appearance_mode(mode)
        self.toogleThemeButton.configure(text=f"{mode.upper()} mode")


# login = Login(root)

app = BalanceMaster()
login = Login(app)
app.mainloop()

# def open_home_window(root) :
#     root.destroy()
#     main_window = mctk.CTk()
#     main_window.title("Balance Master - Main Window")
#     root.title("BalanceMaster - Login")
#     root.geometry("925x500+300+200")
#     root.configure(bg='#FFFFF')
#     root._set_appearance_mode("light")
#     root.resizable(False,False)
#     toogleThemeButton1 = mctk.CTkButton(master=main_window,text="LIGHT mode",command=set_theme,bg_color="transparent")
#     toogleThemeButton1.pack()
#     main_window.mainloop()
