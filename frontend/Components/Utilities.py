import os
import customtkinter as mctk

# CONSTANTS AND LOGIN METHODS DEFINITIONS
ERRORS = {
    "empty_fields": "Vous devez remplir tous les champs !",
    "login_failed": "Les informations de connexion ne correspondent pas !"
}


# Common functions for our projects


def get_parent_path2():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    path = os.path.join(parent_dir, 'assets', 'images')
    return path


def set_theme(master):
    mode = "light"
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


