from datetime import datetime
from pprint import pprint
from json import dumps
import requests
from bs4 import BeautifulSoup

from classes.bank.bank import Bank
from classes.bank.quarter import Quarter
from classes.bank.year import Year
from components.helpers.fix_name import fix_name


def http_main(URL):
    bank_link_dict = {}
    bank_list = []
    response = requests.get(URL)
    sup = BeautifulSoup(response.text, 'html.parser')
    table_soup = sup.find('div',
                          class_="jsx-2864173099 md:mt-3-0 mt-4-0 relative border border-grey-400 rounded-base select-none print:w-full")
    all_bank_soup = table_soup.find("div", class_="text-subtitle3 font-normal font-lt leading-subtitle3")
    list_bank_soup = all_bank_soup.find_all("div", class_="jsx-2864173099 tb-row flex")

    for bank in list_bank_soup:
        bank_name = fix_name(bank.find("a").text)
        years = bank.find("div", class_="jsx-2864173099 grid flex-1 grid-cols-6").find_all("ul")

        bank_obj = Bank(bank_name)

        for year, content in enumerate(years):
            quarters = content.find_all("li")

            year_obj = Year(datetime.today().year - year)
            for index, quarter in enumerate(quarters):
                quarter_name = index + 1
                link = quarter.find("a").attrs["href"] if quarter.find("a") is not None else None
                quarter_obj = Quarter(quarter_name)
                quarter_obj.set_link(link)
                year_obj.set_quarter(quarter_name-1, quarter_obj)
            bank_obj.add_year(year_obj)

        bank_list.append(bank_obj)

    # for i in bank_list:
    #     print(i.get_name(), bank_obj.get_year_list()[0].get_quarters()['Q1'].get_link())


if __name__ == "__main__":
    http_main()
