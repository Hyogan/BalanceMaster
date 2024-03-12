import os
import customtkinter as mctk
# Common functions for our projects


def get_parent_path():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    path = os.path.join(parent_dir, 'assets', 'images')
    return path


def set_theme(master):
    if master._get_appearance_mode() == 'dark':
        print(master._get_appearance_mode())
        mode = 'light'
        master._set_appearance_mode('light')
        mctk.set_appearance_mode('light')
    else:
        mode = "dark"
        print(master._get_appearance_mode())
        master._set_appearance_mode('dark')
        mctk.set_appearance_mode('dark')

