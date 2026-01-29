print("[Welcome to OwlBanking]")

choice = 0
balance = 0
history = ""
while choice != 'Q':
    print("Select an Option:")
    print("1 - Deposit")
    print("2 - Withdraw")
    print("3 - Check Balance")
    print("4 - Check Transaction History")
    print("Q - Quit")

    choice = input("").upper()
    if choice == '1':
        print("")
        transaction = float(input("How much do you want to deposit: $"))
        original_balance = balance
        balance += transaction
        history += f"${transaction:.2f} was deposited, balance went from ${original_balance:.2f} to ${balance:.2f}\n"
    elif choice == '2':
        if balance == 0:
            print("")
            print("Error: Cannot Withdraw with balance of zero")
        else:
            transaction = float(input("How much do you want to withdraw: $"))
            if transaction > balance:
                print("")
                print("Insufficient funds. Withdrawal would drop balance below $0.”")
            else:
                original_balance = balance
                balance -= transaction
                history += f"${transaction:.2f} was withdrawn, balance went from ${original_balance:.2f} to ${balance:.2f}\n"
    elif choice == '3':
        print("")
        print(f"Balance: ${balance:.2f}")
    elif choice == '4':
        print("")
        print(history)
