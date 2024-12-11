#add import
import question_b

def menu():
    print("-----MENU-----\n1-get_most_likely_ancestor_consensus\n2-exit")

def get_dna_string():
    while True:
        dna_string = input("please enter the DNA string: ").upper()
        if len(dna_string) > 8 and len(dna_string) <= 16:
            return dna_string
        
        else:
            print("invalid string, please enter again")

def get_dna_substring():
    while True:
        dna_substring = input("please enter the DNA substring: ").upper()
        if len(dna_substring) == 4:
            return dna_substring
        
        else:
            print("invalid string, please enter again")

def run_menu():
    option = 0

    while option != 2:
        menu()
        option = int(input("PLEASE MAKE YOUR SELECTION: "))

        if option == 1:
            dna_string1 = get_dna_string()
            dna_string2 = get_dna_substring()
            print(question_b.get_most_likely_ancestor_consensus(dna_string1, dna_string2))

        elif option == 2:
            exit()
            
        else:
            print("invalid selection")

run_menu()