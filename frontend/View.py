from frontend.pages import Account, Beneficiary, Category, Deposit, Transfer, Withdrawal


class View:
    def __init__(self, parent):
        self.parent = parent
        self.frames = {}
        self.frame_classes = {
            "account": Account,
            "beneficiary": Beneficiary,
            "category": Category,
            "deposit": Deposit,
            "transfer": Transfer,
            "withdrawal": Withdrawal
        }
        self.current_frame = None

    def _add_frame(self, frame, name):
        self.frames[name] = frame(self.parent)
        self.frames[name].grid(row=0, column=0, sticky="nsew")

    def switch(self, name):
        new_frame = self.frame_classes[name](self.parent)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.grid(row=0, column=0, sticky="nsew")
        #frame = self.frames[name]
        #frame.tkraise()

    def start_mainloop(self):
        self.parent.mainLoop()
