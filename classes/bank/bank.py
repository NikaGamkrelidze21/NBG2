from classes.bank.year import Year
import json

class Bank:
    def __init__(self, name):
        self.name = name
        self.year_list = []
        # print("Created Bank:", self.name)

    # def __str__(self):
    #     return json.dumps(self.year_list, indent=4)
    #     return f"Bank: {self.name} Years: {self.year_list}\n"

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_year_list(self, year_list):
        self.year_list = year_list

    def get_year_list(self):
        return self.year_list

    def add_year(self, year):
        self.year_list.append(year)


