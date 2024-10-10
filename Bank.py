class Account:
    def __init__(self, account_number, account_holder, initial_balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = initial_balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
            return False
        self.balance -= amount
        self.transactions.append(f"Withdrew: {amount}")
        return True

    def get_balance(self):
        return self.balance

    def get_account_details(self):
        return {
            "Account Number": self.account_number,
            "Account Holder": self.account_holder,
            "Balance": self.balance
        }

    def print_transactions(self):
        for transaction in self.transactions:
            print(transaction)


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder, initial_balance=0):
        if account_number in self.accounts:
            print("Account already exists.")
            return
        new_account = Account(account_number, account_holder, initial_balance)
        self.accounts[account_number] = new_account
        print("Account created successfully.")

    def view_account_details(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            details = account.get_account_details()
            for key, value in details.items():
                print(f"{key}: {value}")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        account = self.accounts.get(account_number)
        if account:
            if account.withdraw(amount):
                print("Withdrawal successful.")
            else:
                print("Withdrawal failed.")
        else:
            print("Account not found.")

    def fund_transfer(self, from_account_number, to_account_number, amount):
        from_account = self.accounts.get(from_account_number)
        to_account = self.accounts.get(to_account_number)
        if from_account and to_account:
            if from_account.withdraw(amount):
                to_account.deposit(amount)
                print("Transfer successful.")
            else:
                print("Transfer failed due to insufficient funds.")
        else:
            print("One or both accounts not found.")

    def print_transactions(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            account.print_transactions()
        else:
            print("Account not found.")


def main():
    bank = Bank()
    while True:
        print("\n1. Create Account")
        print("2. View Account Details by Account Number")
        print("3. Withdraw")
        print("4. Fund Transfer")
        print("5. Print Transactions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            account_number = input("Enter account number: ")
            account_holder = input("Enter account holder name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, account_holder, initial_balance)

        elif choice == '2':
            account_number = input("Enter account number: ")
            bank.view_account_details(account_number)

        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)

        elif choice == '4':
            from_account = input("Enter your account number: ")
            to_account = input("Enter recipient account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.fund_transfer(from_account, to_account, amount)

        elif choice == '5':
            account_number = input("Enter account number: ")
            bank.print_transactions(account_number)

        elif choice == '6':
            print("Exiting the bank application.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
