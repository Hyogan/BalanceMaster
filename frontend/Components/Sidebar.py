import customtkinter as mctk


class Sidebar(mctk.CTkFrame):
    def __init__(self, parent, button_click_callback):
        mctk.CTkFrame.__init__(self, parent)

        self.button_click_callback = button_click_callback

        # Create and configure the widgets for the sidebar
        self.label = mctk.CTkLabel(self, text="Sidebar", font=("Arial", 14))
        self.label.pack(pady=10)

        self.button1 = mctk.CTkButton(self, text="Button 1", command=self.button1_click)
        self.button1.pack(pady=5)

        self.button2 = mctk.CTkButton(self, text="Button 2", command=self.button2_click)
        self.button2.pack(pady=5)

    def button1_click(self):
        # Perform some action when Button 1 is clicked
        self.button_click_callback("Button 1 clicked!")

    def button2_click(self):
        # Perform some action when Button 2 is clicked
        self.button_click_callback("Button 2 clicked!")

