import customtkinter as mctk

from frontend.pages.Beneficiary import Beneficiary


class DashboardContent(mctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.015, rely=0.125, relwidth=0.97, relheight=0.85)
        self.dashboard_beneficiary = Beneficiary(self)
    def button1_click(self):
        print('Dashboard button 1 clicked ')

    def button2_click(self):
        print('Dashboard button 2 clicked')


