import customtkinter as mctk
from frontend import Login as LoginScreen
from frontend import Dashboard
import os
from PIL import Image as Im
from frontend.Components.Utilities import get_parent_path, set_theme


class MainApplication(mctk.CTk):
    def __init__(self):
        mctk.CTk.__init__(self)

        mctk.set_appearance_mode('light')
        mctk.set_default_color_theme('blue')

        self.geometry("925x500+300+200")
        self.configure(bg='#FFFFF')
        self._set_appearance_mode("light")
        self._apply_appearance_mode('light')
        self.resizable(False, False)
        self.iconify()

        light_mg = os.path.join(get_parent_path(), 'background-light.jpeg')
        dark_mg = os.path.join(get_parent_path(), 'background.jpg')

        bg = mctk.CTkImage(light_image=Im.open(light_mg), dark_image=Im.open(dark_mg), size=(925, 500))
        my_label = mctk.CTkLabel(self, image=bg, text="")
        my_label.place(x=0, y=0)
        toggle_theme_button = mctk.CTkButton(master=self, command=set_theme(self), text="LIGHT mode", bg_color="transparent")
        toggle_theme_button.pack()

        self.login_frame = LoginScreen(self, on_login=self.on_login)
        self.login_frame.pack()

    def on_login(self):
        # Hide the login screen and show the dashboard screen
        self.login_frame.pack_forget()
        self.dashboard_frame.pack()

    def on_logout(self):
        # Hide the dashboard screen and show the login screen
        self.dashboard_frame.pack_forget()
        self.login_frame.pack()


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
