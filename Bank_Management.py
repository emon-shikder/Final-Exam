import uuid

class Account:
    def __init__(self, name, email, address, account_type, password):
        self.account_number = uuid.uuid4().int
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.transaction_history = []
        self.loan_count = 0
        self.loan_amount = 0
        self.password = password

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Withdrawal amount exceeded")
            return
        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount}")

    def check_balance(self):
        return self.balance

    def check_transaction_history(self):
        return self.transaction_history

    def take_loan(self, amount):
        if self.loan_count >= 2:
            print("You have already taken two loans")
            return
        self.balance += amount
        self.loan_count += 1
        self.loan_amount += amount
        self.transaction_history.append(f"Took loan of {amount}")

    def transfer(self, amount, recipient_account_number):
        if amount > self.balance:
            print("Insufficient balance")
            return
        recipient_account = bank.get_account(recipient_account_number)
        if recipient_account:
            self.balance -= amount
            recipient_account.deposit(amount)
            self.transaction_history.append(f"Transferred {amount} to {recipient_account_number}")
        else:
            print("Account does not exist")

class Bank:
    def __init__(self):
        self.accounts = {}
        self.loan_feature_enabled = True

    def create_account(self, name, email, address, account_type, password):
        account = Account(name, email, address, account_type, password)
        self.accounts[account.account_number] = account
        return account.account_number

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
        else:
            print("Account does not exist")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def get_account_by_email(self, email):
        for account in self.accounts.values():
            if account.email == email:
                return account
        return None

    def get_all_accounts(self):
        return list(self.accounts.values())

    def get_total_balance(self):
        return sum(account.balance for account in self.accounts.values())

    def get_total_loan_amount(self):
        return sum(account.loan_amount for account in self.accounts.values())

    def loan_feature(self):
        self.loan_feature_enabled = not self.loan_feature_enabled

    def is_loan_feature_enabled(self):
        return self.loan_feature_enabled

def create_account(name, email, address, account_type, password):
    account_number = bank.create_account(name, email, address, account_type, password)
    print("Account created with account number:", account_number)

def login(email, password):
    account = bank.get_account_by_email(email)
    if account and account.password == password :
        user_menu(account.account_number)
    else:
        print("Invalid email or password")

bank = Bank()

def user_menu(account_number):
    while True:
        print("--------- User -------------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Check Transaction History")
        print("5. Take Loan")
        print("6. Transfer")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            amount = int(input("Enter amount to deposit: "))
            bank.get_account(account_number).deposit(amount)
        elif choice == "2":
            amount = int(input("Enter amount to withdraw: "))
            bank.get_account(account_number).withdraw(amount)
        elif choice == "3":
            print("Your balance is:", bank.get_account(account_number).check_balance())
        elif choice == "4":
            print("Your transaction history is:", bank.get_account(account_number).check_transaction_history())
        elif choice == "5":
            if bank.is_loan_feature_enabled():
                amount = int(input("Enter loan amount: "))
                bank.get_account(account_number).take_loan(amount)
            else:
                print("Loan feature is currently disabled")
        elif choice == "6":
            amount = int(input("Enter amount to transfer: "))
            recipient_account_number = int(input("Enter recipient account number: "))
            bank.get_account(account_number).transfer(amount, recipient_account_number)
        elif choice == "7":
            break
        else:
            print("Invalid choice")
        print("\n")

def admin_menu():
    while True:
        print("--------- Admin -------------")
        print("1. Create Account")
        print("2. Delete Account")
        print("3. See All Accounts")
        print("4. Check Total Balance")
        print("5. Check Total Loan Amount")
        print("6. Loan Feature")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            password = input("Enter password: ")
            create_account(name, email, address, account_type, password)
        elif choice == "2":
            account_number = int(input("Enter account number to delete: "))
            bank.delete_account(account_number)
        elif choice == "3":
            for account in bank.get_all_accounts():
                print("----------------------")
                print("Account Number:", account.account_number)
                print("Name:", account.name)
                print("Email:", account.email)
                print("Address:", account.address)
                print("Account Type:", account.account_type)
                print("Balance:", account.check_balance())
                print("Transaction History:", account.check_transaction_history())
                print("Loan Amount:", account.loan_count * 1000)
                print("Loan Status:", "Yes" if account.loan_count > 0 else "No")
                print("----------------------")
        elif choice == "4":
            print("Total Balance:", bank.get_total_balance())
        elif choice == "5":
            print("Total Loan Amount:", bank.get_total_loan_amount())
        elif choice == "6":
            bank.loan_feature()
            print("Loan feature is now", "Enabled" if bank.is_loan_feature_enabled() else "Disabled")
        elif choice == "7":
            break
        else:
            print("Invalid choice")
        print("\n")

while True:
    print("1. User")
    print("2. Admin")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        Y_N = input("Do you have any Account Y\\N: ")
        
        if Y_N == 'Y':
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            login(email, password)
        elif Y_N == 'N':
            name = input("Enter name: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            account_type = input("Enter account type (Savings/Current): ")
            password = input("Enter password: ")
            create_account(name, email, address, account_type, password)
        else:
            print("Invalid choice")
    elif choice == "2":
        user = input("Enter your username: ")
        password = int(input("Enter your password: "))
        if user== "admin" and password == 123:
            admin_menu()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
    print("\n")