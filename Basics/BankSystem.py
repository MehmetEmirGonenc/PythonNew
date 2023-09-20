import BankAccount
import sys

def main():
    if sys.argv[1] == "-admin":
        ###Enter admin mode
        #Admin Panel loop

        while (True):
            #Admin UI
            print ("-------------- Admin Panel---------------")
            print ("|1 - Create Account                     |")
            print ("|2 - Delete Account                     |")
            print ("|3 - Check Account                      |")
            print ("|0 - Exit                               |")
            print ("-----------------------------------------")
            adminchoice = ensure_numeric(input("--> "))

            if adminchoice == 0:
                exit()
            elif adminchoice == 1:
                #Get variables
                name = input("Name : ")
                accId = input("Account Id (6 digit) : ")
                if len(accId) != 6:
                    print("Digit error")
                    continue
                ensure_numeric(accId) #Control later for keep variable string
                pin = input("PIN (4 digits) : ")
                if len(pin) != 4:
                    print("Digit error")
                    continue
                ensure_numeric(pin) #Control later for keep variable string
                balance = 0.0
                #Import to file
                data_import(accId, name, pin, balance)
            elif adminchoice == 2:
                print()
            ###
    else:

        #Create account object

        #Login
        #Ensure input is numberic
        accId = ensure_numeric(input("Please enter your account id : "))

        #Ensure input is numberic
        pin = ensure_numeric(input("Please enter your pin : "))
        
        
        #Ensureing
        print(data_search(str(accId),2))
        if data_search(accId,1) == False:
            print ("Id or pin wrong!")
            return
        print ("Succesfully logged in!\n")

        accDetails = data_search(accId,2)            
        acc = BankAccount.Account(accId, "Mehmet", 0000, 2000.0)
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
            choice = ensure_numeric(input("--> "))

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



def data_import(accId, name, pin, balance):
    # Write variables to file
    with open("accounts.txt", "a") as file:
        file.write(f"accId:   {accId}, ")
        file.write(f"Name:    {name}, ")
        file.write(f"pin:     {pin}, ")
        file.write(f"balance: {balance}\n")



def data_search(accId, mode):
    #mode 1 = if exist ; 2 = get information
    file = open("accounts.txt", "r")# Open file
    lines = file.readlines()    #Read all lines
    file.close()
    #Line my line analyse
    for line in lines:  
        parts = line.split(", ") #Seperate dictionary values
        key = False              #Key for break loop after find wanted value
        for part in parts:       #analyse each part 
            part = part[9:]
            if part == accId:
                list(accId) 
                key = True
            if mode == 1 and key == True:
                return True
            elif mode == 2 and key == True:
                list.append(part)
        if key == True: 
            return list
    return False


main()






