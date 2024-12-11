#add import
import question_c

def menu():
    print("-----MENU-----\n1-Display stock purchase history\n2-Exit")

def main():
    option = 0

    while option != 2:
        menu()
        option = int(input("PLEASE MAKE YOUR SELECTION: "))

        if option == 1:
            stock_list = question_c.get_stock_list()

            for item in stock_list:
                print(item.get_symbol() + "\t" + item.get_company_name())

        elif option == 2:
            exit()
            
        else:
            print("invalid selection")

main()