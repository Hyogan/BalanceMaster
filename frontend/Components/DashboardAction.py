import customtkinter as mctk


class DashboardAction(mctk.CTkButton):
    def __init__(self, parent, action_text, action, name='account'):
        mctk.CTkButton.__init__(self, parent)
        self.parent = parent
        self.name = name
        self.action = action
        self.text = action_text
        self.configure(text=self.text, font=('', 15, "bold"), corner_radius=0,
                       command=self.on_click_to_switch)
        self.pack(pady=5, ipady=5, padx=0, fill='x')

    def on_click_to_switch(self):
        print('hello world')
        self.action(self.name)
