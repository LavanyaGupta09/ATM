accounts = {
    10001: {
        "name": "Ria",
        "balance": 5000.00
    },
    10002: {
        "name": "Rahul",
        "balance": 3000.00
    },
    10003: {
        "name": "Amit",
        "balance": 7000.00
    }
}
while True:
    print("Welcome to the ATM!")
    print("1. Create Account")
    print("2. withdraw Money")
    print("3. Transfer Money")
    print("4. Deposit Money")
    print("5. Check Balance")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    if choice == "1":
        create_account = input("Do you want to create a new account? (yes/no): ").strip().lower()
        if create_account == "yes":
            account_number = int(input("Enter your account number:"))
            if account_number in accounts:
                print("Account already exists.")
            else:
                name = input("Enter your name:")
                balance = float(input("Enter your initial balance:"))
                accounts[account_number] = {
                    "name": name,
                    "balance": balance
                }
                print("Account created successfully.")
    elif choice == "2":
        account_number = int(input("Enter your account number:"))
        if account_number in accounts:
            withdraw_amount = float(input("Enter the amount to withdraw:"))
            if withdraw_amount <= accounts[account_number]["balance"]:
                accounts[account_number]["balance"] -= withdraw_amount
                print(f"Withdrawal successful. New balance: {accounts[account_number]['balance']}")
            else:
                print("Insufficient balance.")
    elif choice == "3":
        account_number = int(input("Enter your account number:"))
        if account_number in accounts:
            print(f"Transaction history for account {account_number}:")
            print(f"Account Holder: {accounts[account_number]['name']}")
            print(f"Current Balance: {accounts[account_number]['balance']}")
            transfer_account = int(input("Enter the account number to transfer money to:"))
            if transfer_account in accounts:
                if account_number == transfer_account:
                    print("You cannot transfer money to the same account.")
                else:
                    transfer_amount = float(input("Enter the amount to transfer:"))
                    if transfer_amount <= accounts[account_number]['balance']:
                        accounts[account_number]['balance'] -= transfer_amount
                        accounts[transfer_account]['balance'] += transfer_amount
                        print(f"Transfer successful. New balance: {accounts[account_number]['balance']}")
                    else:
                        print("Insufficient balance.")
            else:
                print("Recipient account not found.")
        else:
            print("Account not found.")
    elif choice == "4":
        account_number = int(input("Enter your account number:"))
        if account_number in accounts:
            deposit_amount = float(input("Enter the amount to deposit:"))
            if deposit_amount > 0:
                accounts[account_number]["balance"] += deposit_amount
                print("Deposit Successful")
            else:
                print("Invalid Amount")
    elif choice == "5":
        account_number = int(input("Enter your account number:"))
        if account_number in accounts:
                print(f"Current balance: {accounts[account_number]['balance']}")
        else:
            print("Account not found.")
    elif choice == "6":
        print("Thank you for using our services.")
        break 
