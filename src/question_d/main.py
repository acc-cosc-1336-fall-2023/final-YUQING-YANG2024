#add import
import question_d

def menu():
    print("-----MENU-----\n1-Display stock purchase history\n2-Exit")

def main():
    option = 0

    while option != 2:
        menu()
        option = int(input("PLEASE MAKE YOUR SELECTION: "))

        if option == 1:
            question_d.stock_purchase_history()

        elif option == 2:
            exit()
            
        else:
            print("invalid selection")

main()