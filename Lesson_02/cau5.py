print("Get 'y' or 'Y' to start program : ", end = '')
keep_going = input()

if keep_going != 'y' and keep_going != 'Y':
    print("FALSE !")
else:
    while keep_going == 'Y' or keep_going == 'y':
        print("Get the amount of sales: ", end = '')
        sales = int(input())
        print("Get the commission rate ",end = '')
        comm_rate = int(input())
        commission = sales * comm_rate
        print("The commission: ", commission)

        print("Do you want to calculate another commission?")
        print("Get 'Y' OR 'y' to continue: ", end = '')
        keep_going = input()