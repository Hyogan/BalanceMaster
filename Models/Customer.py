class Customer:
    def __init__(self, id=0, email=None, username=None, password=None):
        self.id = id
        self.email = email
        self.username = username
        self.password = password

    def getId(self):
        return self.id

    def getEmail(self):
        return self.email

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def setId(self, id):
        self.id = id

    def setEmail(self, n_email):
        self.email = n_email

    def setUsername(self, n_username):
        self.username = n_username

    def setPassword(self, n_password):
        self.password = n_password

    def __str__(self) -> str:
        return (f"{self.id},{self.email},{self.username},{self.password}")
