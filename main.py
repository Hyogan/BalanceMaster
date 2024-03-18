import customtkinter as mctk
from tkinter import messagebox
from frontend.Login import LoginGUI as LoginScreen
from frontend.Dashboard import DashboardGUI as DashboardScreen
import os
from PIL import Image as Im
from frontend.Components.Utilities import set_theme


def get_parent_path():
    path = os.path.join('assets', 'images')
    return path


class MainApplication(mctk.CTk):
    def __init__(self):
        mctk.CTk.__init__(self)
        self.login_frame = LoginScreen(self, on_login=self.on_login)
        self.dashboard_frame = DashboardScreen(self, on_logout=self.on_logout)

        mctk.set_appearance_mode('light')
        mctk.set_default_color_theme('blue')

        # self.geometry("925x500+300+200")
        self.set_windows_size()
        self.configure(bg='#FFFFF')
        self._set_appearance_mode("light")
        self._apply_appearance_mode('light')
        self.resizable(True, True)
        self.iconify()

        light_mg = os.path.join(get_parent_path(), 'background-light.jpeg')
        dark_mg = os.path.join(get_parent_path(), 'background.jpg')

        size_w = self.winfo_screenwidth()
        size_h = self.winfo_screenheight()
        bg = mctk.CTkImage(light_image=Im.open(light_mg), dark_image=Im.open(dark_mg), size=(size_w, size_h))
        my_label = mctk.CTkLabel(self, image=bg, text="")
        my_label.place(x=0, y=0)
        my_label.lower()

        toggle_theme_button = mctk.CTkButton(master=self, command=set_theme(self), text="LIGHT mode",
                                             bg_color="transparent")
        toggle_theme_button.pack()

        self.login_frame.pack()
        # self.dashboard_frame.pack()

    def on_login(self):
        # Hide the login screen and show the dashboard screen
        self.login_frame.pack_forget()
        self.dashboard_frame.pack()

    def on_logout(self):
        # Hide the dashboard screen and show the login screen
        messagebox.showinfo("balancemaster", f"You are about to logout")
        self.dashboard_frame.pack_forget()
        self.login_frame.pack()

    def set_windows_size(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        screen_height = str(screen_height)
        screen_width = str(screen_width)
        screen = screen_width + "x" + screen_height
        self.geometry(screen)


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()

