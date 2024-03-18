import customtkinter as mctk

from Controllers.DashboardController import DashboardController
from frontend.pages.Beneficiary import Beneficiary


class DashboardInstance(mctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.place(relx=0.01, rely=0.0019, relwidth=0.98, relheight=1)
        self.header = mctk.CTkFrame(self)
        # #c6ced8
        # self.label = mctk.CTkLabel(self, text="GESTION DES BENEFICIAIRES", text_color='white', font=("Arial", 17,'bold'))
        # self.label.pack(pady=10, ipadx=15, ipady=5, padx=0)
        # self.header.place(relx=0, rely=0.005, relwidth=1, relheight=0.1)

        # self.dashboard_content = Beneficiary(self)

