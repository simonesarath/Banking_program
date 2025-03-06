# Banking Programme

def show_balance(balance):

    print("*******************************")
    print(f"Your Balance Is ₹{balance:.2f}")
    print("*******************************")

def deposit():

    print("********************************")
    amount = float(input("Enter An Amount To Be Deposited: "))
    print("********************************")

    if amount < 0:

        print("***************************")
        print("That's Not A Valid Amount: ")
        print("***************************")

        return 0
    else:
        return amount

def withdraw(balance):

    print("*************************")
    amount = float(input("Enter Amount To Be Withdraw: "))
    print("*************************")

    if amount > balance:

        print("********************")
        print("Insufficient Funds: ")
        print("********************")

        return 0
    elif amount < 0:

        print("*************************")
        print("Amount Must Be Greater Than 0")
        print("*************************")
        
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:

        print("*************************")
        print("    Banking Program::    ")
        print("*************************")

        print("1.Show Balance:")
        print("2.Deposit:")
        print("3.Withdraw:")
        print("4.Exit::")

        print("*************************")

        choice = input("Enter Your Chioce(1,4):: ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("***************************")
            print("That Is Not A Valid Choice:")
            print("***************************")

    print("**************************")       
    print("Thank You Have A Nice Day:")
    print("**************************")

if __name__ == "__main__":
    main()