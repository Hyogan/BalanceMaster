# SYSTEM IMPORTS
# from tkinter import *
# from tkinter import messagebox
import customtkinter as mctk
from PIL import Image as Im
import os

from Controllers.DashboardController import DashboardController
from frontend.Components.DashboardInstance import DashboardInstance
from frontend.Components.Sidebar import Sidebar


def get_parent_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    path = os.path.join(parent_dir, 'assets', 'images')
    return path


class DashboardGUI(mctk.CTkFrame):
    def __init__(self, master, on_logout):
        super().__init__(master)
        # self.configure(width=1000)
        # self.configure(height=600)
        self.configure(fg_color='transparent')
        self.set_frame_size(master)
        self.on_logout = on_logout
        self.master = master
        master.title("BalanceMaster - Client Dashboard")
        # self.dashboard_instance = DashboardInstance(self)
        self.dashboard_instance = DashboardController(self)
        self.sidebar = Sidebar(self, on_logout, self.dashboard_instance.current_frame, switch_page=self.dashboard_instance.switch_page)
        # self.sidebar.lift(self.dashboard_instance.current_frame)
        # self.place(relx=0.21, rely=0.125, relwidth=0.78, relheight=0.94)
        toggle_menu_btn = mctk.CTkButton(master=self, height=40, text="MENU", bg_color='transparent', command=lambda: self.toggle_menu(self.sidebar))
        toggle_menu_btn.place(x=5, y=5)
        toggle_menu_btn.lift(self.sidebar)
        self.lift()

    def set_frame_size(self, master):
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        self.configure(width=screen_width)
        self.configure(height=screen_height)

    def button_click_callback(self, message):
        print(message)

    def toggle_menu(self, sidebar):
        sidebar.toggle_sidebar()
        # screen_width = login.winfo_screenwidth()
        # screen_height = login.winfo_screenheight()
        # screen_height = str(screen_height)
        # screen_width = str(screen_width)
        # screen = screen_width + "x" + screen_height
        # login.geometry(screen)
