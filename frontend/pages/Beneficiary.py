import customtkinter as mctk

from frontend.Components.Beneficiary.BeneficiaryItem import BeneficiaryItem

class Beneficiary(mctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.lower(parent.sidebar)
        self.place(relx=0.015, rely=0.05, relwidth=0.97, relheight=0.90)
        self.label1 = mctk.CTkLabel(self, text='Hello Account', font=("Arial", 11))
        self.label1.place(relx=1, rely=1, relwidth=1, relheight=1)
        #self.place(relx=0.015, rely=0.125, relwidth=0.97, relheight=0.85)

        self.beneficiary_actions = mctk.CTkFrame(self, height=250,)
        self.beneficiary_actions.place(relx=0, rely=0, relwidth=1)

        self.button1 = mctk.CTkButton(self.beneficiary_actions, text="Add", corner_radius=0)
        self.button1.pack(pady=5, ipady=5, padx=0)

        self.beneficiary_list = mctk.CTkFrame(self, height=250)
        self.beneficiary_list.place(relx=0, rely=0.2, relwidth=1)

        #self.beneficiary_item = BeneficiaryItem(self.beneficiary_list)

        self.label = mctk.CTkLabel(self.beneficiary_list, text="John Doe", text_color='white', height=250, font=("Arial", 17))
        self.label.place(relx=0, rely=0)

        self.label = mctk.CTkLabel(self.beneficiary_list, text="16564561561556", text_color='white', font=("Arial", 11))
        self.label.place(relx=1, rely=0)

        self.button1 = mctk.CTkButton(self.beneficiary_list, text="Transfert", corner_radius=0)
        self.button1.place(relx=0.5, rely=0)

        self.button1 = mctk.CTkButton(self.beneficiary_list, text="Update", corner_radius=0)
        self.button1.place(relx=0.5, rely=0.5)





