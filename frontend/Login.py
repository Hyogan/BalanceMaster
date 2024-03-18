# SYSTEM IMPORTS 
from tkinter import *
from tkinter import messagebox
import customtkinter as mctk
from PIL import Image as Im
import os


# IMPORTS ABOUT DIRECTORIES ORGANISATIONS
from Controllers.AuthController import login
from Models.Customer import Customer
from frontend.Components.Utilities import ERRORS

# UTILITIES


def get_parent_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    path = os.path.join(parent_dir, 'assets', 'images')
    return path


class LoginGUI(mctk.CTkFrame):
    def __init__(self, master, on_login):
        super().__init__(master)
        self.configure(width=1000)
        self.configure(height=600)
        # self.geometry("925x500+300+200")
        self.on_login = on_login
        self.master = master
        master.title("BalanceMaster - Login")

        light_mg = os.path.join(get_parent_path(), "transparent-login.png")
        dark_mg = light_mg

        img = mctk.CTkImage(light_image=Im.open(light_mg), dark_image=Im.open(dark_mg), size=(400, 400))
        my_label2 = mctk.CTkLabel(self, image=img, bg_color="transparent", fg_color="transparent", text="")
        my_label2.place(x=50, y=60)

        frame = mctk.CTkFrame(self, width=360, height=400, bg_color="transparent")
        frame.place(x=480, y=60)

        heading = mctk.CTkLabel(frame, text="Inscription", font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=8)

        self.error_msg = mctk.CTkLabel(frame, fg_color='transparent', bg_color='transparent', text="", text_color='red',
                                       font=('Microsoft YaHei UI Light', 12, 'bold'))
        self.error_msg.place(relx=0.5, anchor="center")
        self.error_msg.configure(wraplength=250)
        self.error_msg.place_configure(y=50)

        self.username_ent = mctk.CTkEntry(frame, corner_radius=None, placeholder_text="Enter your Username",
                                          width=250, height=35, border_width=0, font=('Microsoft UI Light', 13, 'bold'))
        self.username_ent.place(x=50, y=70)

        self.password_ent = mctk.CTkEntry(frame, corner_radius=None, placeholder_text="Enter your Password", show="*",
                                          width=250, height=35, border_width=0, font=('Microsoft UI Light', 13, 'bold'))
        self.password_ent.place(x=50, y=130)

        self.show_password_button = mctk.CTkButton(master=frame, text="Show", width=45, height=35,
                                                   bg_color="transparent", command=self.show_hide_password)
        self.show_password_button.place(x=305, y=130)

        question = "What is your pet name ?"
        secret_question_label = mctk.CTkLabel(frame, text=f"{question}", width=250, height=35,
                                              font=('Microsoft UI Light', 13, 'bold'))
        secret_question_label.place(x=50, y=170)

        self.secretQuestion_ent = mctk.CTkTextbox(frame, width=250, height=150)
        self.secretQuestion_ent.place(x=50, y=200)

        light_mg = os.path.join(get_parent_path(), "logo_trial.png")
        dark_mg = light_mg

        img = mctk.CTkImage(light_image=Im.open(light_mg), dark_image=Im.open(dark_mg), size=(450, 250))
        my_label2 = mctk.CTkLabel(self, image=img, bg_color="transparent", fg_color="transparent", text="")
        my_label2.place(x=0, y=250)

        login_button = mctk.CTkButton(master=frame, text="Login", bg_color='transparent', command=lambda: self.login_logic())
        login_button.place(x=50, y=355)

    def set_error(self, error):
        self.error_msg.configure(text=error)

    def show_hide_password(self):
        if self.password_ent.cget('show') == '*':
            self.password_ent.configure(show='')
            self.show_password_button.configure(text="hide")
        else:
            self.password_ent.configure(show="*")
            self.show_password_button.configure(text="show")

    def recover_input(self):
        my_username = self.username_ent.get()
        my_password = self.password_ent.get()
        my_secret_quest = self.secretQuestion_ent.get('1.0', END)

        if len(my_username) == 0 or len(my_password) == 0 or len(my_secret_quest) <= 2:
            self.set_error(ERRORS['empty_fields'])
            return False

        user = {
            "my_username": my_username,
            "my_password": my_password,
            "my_secret_quest": my_secret_quest
        }

        return user

    def set_frame_size(self, master):
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        self.configure(width=screen_width)
        self.configure(height=500)

    def login_logic(self):
        login_elements = self.recover_input()
        if not login_elements:
            return
        else:
            customer_data = Customer(username=login_elements['my_username'], password=login_elements['my_password'])
            result = login(customer_data)
            # print(customer_data)
            if result is not None:
                # print('all fine')
                name_to_welcome = self.username_ent.get()
                messagebox.showinfo("balancemaster", f"Welcome Mr / Mrs {name_to_welcome}")
                self.on_login()
            else:
                self.set_error(ERRORS['login_failed'])
                return


def set_theme(master):
    if master._get_appearance_mode() == 'dark':
        print(master._get_appearance_mode())
        mode = 'light'
        master._set_appearance_mode('light')
        mctk.set_appearance_mode(mode)
    else:
        mode = "dark"
        print(master._get_appearance_mode())
        master._set_appearance_mode('dark')
        mctk.set_appearance_mode(mode)

    # root._set_appearance_mode(f"{mode}")
    # mctk.set_appearance_mode(mode)
    # master._set_appearance_mode(mode)
    # global toggleThemeButton
    # toggleThemeButton.configure(text = f"{mode.upper()} mode")
