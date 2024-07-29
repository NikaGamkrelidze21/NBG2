from classes.bank.quarter import Quarter


class Year:
    def __init__(self, year):
        self.year = year
        self.quarters = {"Q1": None, "Q2": None, "Q3": None, "Q4": None}
        # print("Created Year:", self.year, self.quarters)

    def __str__(self):
        q_s = self.quarters
        return f"Year: {self.year} Quarters: {q_s}\n"

    def set_quarter(self, q_num, quarter: Quarter):
        if isinstance(quarter, Quarter):
            if isinstance(q_num, str):
                self.quarters[q_num] = quarter

            elif isinstance(q_num, int):
                self.quarters[list(self.quarters)[q_num]] = quarter

            else:
                raise ValueError("Quarter must be of type str or int")
        else:
            raise TypeError("Quarter must be of type Quarter")

    def get_quarters(self):
        return self.quarters

    def get_year(self):
        return self.year

    def get_quarter(self,  quarter_name):
        if isinstance(quarter_name, str):
            quarter_name = quarter_name.upper()
            return self.quarters.get(quarter_name)

        elif isinstance(quarter_name, int):
            return self.quarters[list(self.quarters)[quarter_name]]

        else:
            raise ValueError("Quarter name must be str or int")