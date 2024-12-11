#add import
import question_a

def menu():
    print("-----MENU-----\n1-create multiplication table\n2-exit")

def get_the_list():
    global num1
    num1 = int(input("please enter the number for row: "))
    num2 = int(input("please enter the number for column: "))
    list = question_a.create_multiplication_table(num1, num2)
    return list

def run_menu():

    option = 0
    flag = 0

    while option != 2 and flag == 0:
        menu()
        option = int(input("PLEASE MAKE YOUR SELECTION: "))
        list = []

        if option == 1:
            list = get_the_list()
            question_a.display_multiplication_table(list, num1)

            answer = input("Do you want to continue? y/n ").upper()
            if not answer == "Y":
                flag = 1

        elif option == 2:
            exit()
            
        else:
            print("invalid selection")

run_menu()