import customtkinter as mctk


class Account(mctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.lower(parent.sidebar)
        self.place(relx=0.015, rely=0.05, relwidth=0.97, relheight=0.90)
        self.label1 = mctk.CTkLabel(self, text='Hello Account', font=("Arial", 11))
        self.label1.place(relx=1, rely=1, relwidth=1, relheight=1)
        #self.pack(after=parent.sidebar)
