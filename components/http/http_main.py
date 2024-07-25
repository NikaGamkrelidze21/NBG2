from pprint import pprint

import requests
from bs4 import BeautifulSoup

from classes.bank.bank import Bank
from classes.bank.year import Year
from components.helpers.fix_name import fix_name


def http_main(URL):
    bank_link_dict = {}

    response = requests.get(URL)
    sup = BeautifulSoup(response.text, 'html.parser')
    table_soup = sup.find('div',
                          class_="jsx-2864173099 md:mt-3-0 mt-4-0 relative border border-grey-400 rounded-base select-none print:w-full")
    all_bank_soup = table_soup.find("div", class_="text-subtitle3 font-normal font-lt leading-subtitle3")
    list_bank_soup = all_bank_soup.find_all("div", class_="jsx-2864173099 tb-row flex")

    for bank in list_bank_soup:
        bank_name = fix_name(bank.find("a").text)

    pprint(bank_link_dict)


if __name__ == "__main__":
    http_main()
