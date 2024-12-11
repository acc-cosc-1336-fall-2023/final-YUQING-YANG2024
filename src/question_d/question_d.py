#write functions here, don't add input('') statements here!

class stock:

    def __init__(self, company_name, symbol):
        self.__company_name = company_name
        self.__symbol = symbol

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    stock_purchase_history = {}
    comp_1 = stock("Apple Inc", "AAPL")
    comp_2 = stock("Caterpillar", "CAT")
    comp_3 = stock("Eastman Kodak", "EK")
    comp_4 = stock("Google", "GOOG")
    comp_5 = stock("Microsoft", "MSFT")

    stock_purchase_history.update({"1" : comp_1})
    stock_purchase_history.update({"2" : comp_2})
    stock_purchase_history.update({"3" : comp_3})
    stock_purchase_history.update({"4" : comp_4})
    stock_purchase_history.update({"5" : comp_5})

    for value in stock_purchase_history.values():
        print(value.get_symbol() + "\t" + value.get_company_name())

#stock_purchase_history()