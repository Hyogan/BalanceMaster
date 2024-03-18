import customtkinter as mctk
from frontend.Components.DashboardAction import DashboardAction

class Sidebar(mctk.CTkFrame):
    def __init__(self, parent, on_logout,a_frame, switch_page):
        mctk.CTkFrame.__init__(self, parent)
        self.current_frame = a_frame
        self.parent = parent
        self.on_logout = on_logout
        self.on_switch = switch_page
        self.user_information = mctk.CTkFrame(self, bg_color='transparent')
        self.user_information.place(relx=0, rely=0.1, relwidth=1, relheight=0.15, bordermode='inside')
        self.user_information.configure(corner_radius=0)
        uni_name = mctk.CTkLabel(self.user_information, text='JOHN DOE', font=('', 17, "bold"))
        uni_name.place(x=55, y=27, anchor="w")
        uni_name = mctk.CTkLabel(self.user_information, text='Personal Account', font=('', 15, "bold"))
        uni_name.place(x=55, y=60, anchor="w")

        # self.user_actions = mctk.CTkFrame(self, bg_color='transparent', fg_color='skyblue')
        self.user_actions = mctk.CTkFrame(self, bg_color='transparent')
        self.user_actions.place(relx=0.01, rely=0.30, relwidth=0.985, bordermode='outside')
        self.user_actions.configure(corner_radius=0)

        self.user_action = DashboardAction(self.user_actions, 'Depot', self.on_switch, name='deposit')
        self.user_action = DashboardAction(self.user_actions, 'Retrait', self.on_switch, name='withdrawal')
        self.user_action = DashboardAction(self.user_actions, 'Transfert', self.on_switch, name='category')
        self.user_action = DashboardAction(self.user_actions, 'Gestion de beneficiaires', self.on_switch, name='beneficiary')
        self.user_action = DashboardAction(self.user_actions, 'Categories', self.on_switch, name='category')
        self.user_action = DashboardAction(self.user_actions, 'Releves', self.on_switch, name='account')
        self.user_action = DashboardAction(self.user_actions, 'Mon compte', self.on_switch, name='account')
        self.user_action = DashboardAction(self.user_actions, 'Logout', self.on_switch, name='deposit')

        # Create and configure the widgets for the sidebar
        # self.configure(fg_color='#c6ced8')
        # self.place(x=-160, y=0, relheight=1)
        self.place(relx=0, rely=0, relwidth=0.2, relheight=1)

        # self.bind("<Enter>", self.extend_sidebar)
        # self.bind("<Leave>", self.retract_sidebar)
    def extend_sidebar(self, event):
        self.place(x=0, y=0)
        self.lift(self.parent)

    def retract_sidebar(self, event):
        self.place(x=-100, y=0)

    def toggle_sidebar(self):
        #print(self.winfo_x())
        hidden_position = -(self.winfo_width())
        if self.winfo_x() == 0:
            self.place(x=hidden_position)
        elif self.winfo_x() == hidden_position:
            self.place(x=0)

    def button1_click(self):
        # Perform some action when Button 1 is clicked
        print("Button 1 clicked!")

    def button2_click(self):
        # Perform some action when Button 2 is clicked
        print("Button 2 clicked!")




