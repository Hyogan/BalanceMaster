import customtkinter as mctk


class BeneficiaryItem(mctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = mctk.CTkLabel(self, text="John Doe", text_color='white', height=250, font=("Arial", 17))
        self.label.place(relx=0, rely=0)

        self.label = mctk.CTkLabel(self, text="16564561561556", text_color='white', font=("Arial", 11))
        self.label.place(relx=1, rely=0)

        self.button1 = mctk.CTkButton(self, text="Transfert", corner_radius=0)
        self.button1.place(relx=0.5, rely=0)

        self.button1 = mctk.CTkButton(self, text="Update", corner_radius=0)
        self.button1.place(relx=0.5, rely=0.5)





