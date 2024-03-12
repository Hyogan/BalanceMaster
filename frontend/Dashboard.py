# SYSTEM IMPORTS
from tkinter import *
from tkinter import messagebox
import customtkinter as mctk
from PIL import Image as im
import os


def get_parent_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    path = os.path.join(parent_dir, 'assets', 'images')
    return path


class DashboardGUI(mctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("BalanceMaster - Client Dashboard")

        light_mg = os.path.join(get_parent_path(), "transparent-login.png")
        dark_mg = light_mg

        img = mctk.CTkImage(light_image=im.open(light_mg), dark_image=im.open(dark_mg), size=(400, 400))
        my_label2 = mctk.CTkLabel(master, image=img, bg_color="transparent", fg_color="transparent", text="")
        my_label2.place(x=50, y=60)

        frame = mctk.CTkFrame(master, width=360, height=400, bg_color="transparent")
        frame.place(x=480, y=60)

        heading = mctk.CTkLabel(frame, text="WELCOME SIR", font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=8)



# if __name__ == "__main__":
#    mctk.set_appearance_mode('light')
#   mctk.set_default_color_theme('blue')
#  root = mctk.CTk()
# root.geometry("925x500+300+200")
# root.configure(bg='#FFFFF')
# root._set_appearance_mode("light")
# root._apply_appearance_mode('light')
# root.resizable(False, False)
# root.iconify()

# light_mg = os.path.join(get_parent_path(), 'background-light.jpeg')
# dark_mg = os.path.join(get_parent_path(), 'background.jpg')

# bg = mctk.CTkImage(light_image=im.open(light_mg), dark_image=im.open(dark_mg), size=(925, 500))
# my_label = mctk.CTkLabel(root, image=bg, text="")
# my_label.place(x=0, y=0)
# toggle_theme_button = mctk.CTkButton(master=root, command=set_theme(root), text="LIGHT mode",
#                                    bg_color="transparent")
# toggle_theme_button.pack()
