from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from model.transaction import Transaction


class TransactionHelper:
    def __init__(self, app):
        self.app = app

    def get(self):
        wd = self.app.wd
        web_el_transaction = wd.find_element_by_css_selector("div#app tbody tr")
        td = web_el_transaction.find_elements_by_css_selector("td")
        id = td[0].text
        trade_time = td[1].text
        price = td[2].text
        quantity = td[3].text
        who = td[4].text
        return Transaction(trade_id=id, trade_time=trade_time,
                                       price=price, quantity=quantity, who=who)

        # for p in w_prices:
        #     price = p.find_element_by_css_selector("td:nth-of-type(3)").text
        #     transactions.append(Transaction(price=price))
        # print(transactions)
        # return transactions

    # def get_prices(self):
    #     wd = self.app.wd
    #     transactions = []
    #     w_prices = wd.find_elements_by_css_selector("div#app tbody tr")
    #     for p in w_prices:
    #         price = p.find_element_by_css_selector("td:nth-of-type(3)").text
    #         transactions.append(Transaction(price=price))
    #         print()
    #     print(transactions)


    # def get_prices(self):
    #     wd = self.app.wd
    #     dates = []
    #     date_elements = WebDriverWait(wd, 10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div#app tbody tr")))
    #     for date_element in date_elements:
    #         dates.append(date_element.text)
    #     print(dates)
    #     transactions = []
        # w_prices = WebDriverWait(wd, 10).until(expected_conditions.visibility_of_all_elements_located("div#app tbody tr"))
        # #w_prices = wd.find_elements_by_css_selector("div#app tbody tr")
        # for p in w_prices:
        #     price = p.find_element_by_css_selector("td:nth-of-type(3)").text
        #     transactions.append(Transaction(price=price))
        #     print()
        # print(transactions)
