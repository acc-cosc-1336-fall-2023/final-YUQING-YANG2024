#write functions here, don't add input('') statements here!

def test_config():
    return True


def create_multiplication_table(num1, num2):
    list = []
    for i in range(1, num2+1):
        for j in range(1, num1+1):
            list.append(i * j)
    return list

def display_multiplication_table(list, num):
    #num1 = 10
    #num2 = 5
    #list = create_multiplication_table(num1, num2)
    #num = num1
    for x in range(len(list)):
        if x != 0 and x%num == 0:
            print(' ')
        print(list[x], end='\t')
    print(' ')

#display_multiplication_table(list)