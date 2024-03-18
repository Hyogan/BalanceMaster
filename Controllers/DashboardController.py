from frontend.pages.Account import Account
from frontend.pages.Beneficiary import Beneficiary
from frontend.pages.Category import Category
from frontend.pages.Deposit import Deposit
from frontend.pages.Transfer import Transfer
from frontend.pages.Withdrawal import Withdrawal

user = {
    'username': 'john',
    'password': 'hello'
}


class DashboardController:
    def __init__(self, parent):
        self.parent = parent
        self.frame_classes = {
            "account": Account,
            "beneficiary": Beneficiary,
            "category": Category,
            "deposit": Deposit,
            "transfer": Transfer,
            "withdrawal": Withdrawal
        }
        self.current_frame = None

    def switch_page(self, name):
        new_frame = self.frame_classes[name](self.parent)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        print(f"The actual frame is  : {name}")

    def logout(self):
        print('Logged out')

    def update_view(self):
        current_user = user
        if current_user:
            print(current_user['username'])
        else:
            print("None")

    def _bind(self):
        # self.frame.signout_button.config(command=self.logout)
        print('binding')
