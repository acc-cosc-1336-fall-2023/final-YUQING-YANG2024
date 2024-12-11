#write functions here, don't add input('') statements here!

class stock:

    def __init__(self, company_name, symbol):
        self.__company_name = company_name
        self.__symbol = symbol

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name

def get_stock_list():
    stock_list = []
    comp_1 = stock("Apple Inc", "AAPL")
    comp_2 = stock("Caterpillar", "CAT")
    comp_3 = stock("Eastman Kodak", "EK")
    comp_4 = stock("Google", "GOOG")
    comp_5 = stock("Microsoft", "MSFT")

    stock_list.append(comp_1)
    stock_list.append(comp_2)
    stock_list.append(comp_3)
    stock_list.append(comp_4)
    stock_list.append(comp_5)
    
    return stock_list
