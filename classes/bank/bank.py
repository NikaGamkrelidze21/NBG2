from classes.bank.year import Year


class Bank:
    def __init__(self, name):
        self.name = name
        self.year_list = []

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name



