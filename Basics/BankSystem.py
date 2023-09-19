import BankAccount

def main():
    #Create account object
    acc = BankAccount.Account('0000', "Mehmet", 0000, 2000.0)

    #Login
    #Ensure input is numberic
    accId = ensure_numeric(input("Please enter your account id : "))

    #Ensure input is numberic
    pin = ensure_numeric(input("Please enter your pin : "))
    
    
    #Ensureing
    if (pin != acc.pin or accId != int(acc.accId) ):
        print ("Id or pin wrong!")
        return
    print ("Succesfully logged in!\n")
    
    #Main loop
    while (True):
        #UI
        print ("------------------------------- Welcome to Bank System-----------------------------")
        print ("| Account id : {}                                   Balance : ${:.2f}             |".format(acc.accId, acc.balance))
        print ("| 1 - Deposit                                                                     |")
        print ("| 2 - Withdraw                                                                    |")
        print ("| 3 - Account                                                                     |")
        print ("| 0 - Exit                                                                        |")
        print ("-----------------------------------------------------------------------------------")
        #Get choice
        choice = ensure_numeric(input("- > "))

        if choice == 0 :
            return
        
        elif choice == 1:
            amount = ensure_float(input("Deposit amount :"))
            acc.deposit(amount)
        
        elif choice == 2:
            amount = ensure_float(input("Withdraw amount :"))
            acc.withdrow(amount)
        
        elif choice == 3:
            print(f"Name    : {acc.name}")
            print(f"Id      : {acc.accId}")
            print(f"Balance : {acc.balance}")
        
        else:
            print ("Undefined choice!")
            continue


        
def ensure_numeric(input):
    if input.isnumeric() == 0:
        print ("Unexpected error occured!")
        exit()
    return int(input)



def ensure_float(input):
    try:
        return float(input)
    except:
        print ("Unexpected error occured!")
        exit()
main()






