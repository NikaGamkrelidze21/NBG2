class Quarter:
    def __init__(self, quarter):
        if isinstance(quarter, str):
            if len(quarter) == 2 and quarter[0].isalpha() and quarter[1].isnumeric():
                self.quarter = quarter.upper()

            else:
                raise ValueError("Quarter must be a string and like 'Q1' or 'Q2'")

        elif isinstance(quarter, int):
            if 4 >= quarter >= 1:
                self.quarter = f"Q{quarter}"

            else:
                raise ValueError("Quarter must be between 1 and 4")

        else:
            raise ValueError("Quarter must be an integer (between 1 and 4) or string (like 'Q1')")

        self.link = ''

